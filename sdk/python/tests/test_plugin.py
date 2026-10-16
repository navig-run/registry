"""Tests for navig_sdk.plugin — covers all correctness bugs fixed 2026-03-17.

Bug coverage:
  BUG-1  navig_config() regex dropped uppercase / mixed-case keys
  BUG-2  navig_config() left surrounding YAML quotes in returned values
  BUG-3  run() coerced empty list params [] to {} via `or {}`
  BUG-4  run() leaked "None" into error message when method key was JSON null
  BUG-5  package had no __init__.py, breaking editable installs
"""
from __future__ import annotations

import io
import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

from navig_sdk.plugin import NavigPlugin, _reply, navig_config


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run_plugin(plugin: NavigPlugin, messages: list[dict]) -> list[dict]:
    """Feed *messages* into plugin.run() via fake stdin; return parsed replies."""
    stdin_text = "\n".join(json.dumps(m) for m in messages) + "\n"
    fake_stdin = io.StringIO(stdin_text)
    fake_stdout = io.StringIO()
    with patch.object(sys, "stdin", fake_stdin), patch.object(sys, "stdout", fake_stdout):
        plugin.run()
    fake_stdout.seek(0)
    return [json.loads(line) for line in fake_stdout if line.strip()]


# ---------------------------------------------------------------------------
# NavigPlugin — basic dispatch
# ---------------------------------------------------------------------------

class TestNavigPluginDispatch:
    def setup_method(self) -> None:
        self.plugin = NavigPlugin(name="test", version="0.1.0")

        @self.plugin.command("add")
        def add(a: int, b: int) -> int:
            return a + b

        @self.plugin.command("echo")
        def echo(*args: str) -> list:
            return list(args)

    def test_keyword_params_dispatch(self) -> None:
        replies = _run_plugin(self.plugin, [{"id": 1, "method": "add", "params": {"a": 3, "b": 4}}])
        assert replies[0] == {"id": 1, "result": 7}

    def test_positional_params_dispatch(self) -> None:
        replies = _run_plugin(self.plugin, [{"id": 2, "method": "echo", "params": ["hello", "world"]}])
        assert replies[0] == {"id": 2, "result": ["hello", "world"]}

    def test_missing_method_gives_unknown_error(self) -> None:
        replies = _run_plugin(self.plugin, [{"id": 5, "method": "no_such_method"}])
        assert "error" in replies[0]
        assert "no_such_method" in replies[0]["error"]

    def test_handler_exception_returned_as_error(self) -> None:
        @self.plugin.command("boom")
        def boom() -> None:
            raise ValueError("intentional error")

        replies = _run_plugin(self.plugin, [{"id": 6, "method": "boom", "params": {}}])
        assert "error" in replies[0]
        assert "intentional error" in replies[0]["error"]

    def test_empty_lines_are_ignored(self) -> None:
        input_text = '\n  \n{"id":7,"method":"add","params":{"a":1,"b":1}}\n'
        fake_stdin = io.StringIO(input_text)
        fake_stdout = io.StringIO()
        with patch.object(sys, "stdin", fake_stdin), patch.object(sys, "stdout", fake_stdout):
            self.plugin.run()
        fake_stdout.seek(0)
        replies = [json.loads(l) for l in fake_stdout if l.strip()]
        assert len(replies) == 1
        assert replies[0]["result"] == 2

    def test_meta_returns_correct_values(self) -> None:
        m = self.plugin.meta()
        assert m["name"] == "test"
        assert m["version"] == "0.1.0"

    def test_name_property(self) -> None:
        assert self.plugin.name == "test"


# ---------------------------------------------------------------------------
# BUG-3 — empty list params must NOT be coerced to dict
# ---------------------------------------------------------------------------

class TestParamsNullHandling:
    def setup_method(self) -> None:
        self.plugin = NavigPlugin(name="p")

        @self.plugin.command("noop")
        def noop() -> str:
            return "ok"

        @self.plugin.command("pos")
        def pos(x: str, y: str) -> str:
            return f"{x}-{y}"

    def test_empty_list_params_calls_handler(self) -> None:
        """params=[] must dispatch to the handler (BUG-3 fix)."""
        replies = _run_plugin(self.plugin, [{"id": 3, "method": "noop", "params": []}])
        assert replies[0].get("result") == "ok", replies[0]
        assert "error" not in replies[0]

    def test_none_params_calls_handler(self) -> None:
        """Absent 'params' key (None) must default to {} and dispatch correctly."""
        replies = _run_plugin(self.plugin, [{"id": 4, "method": "noop"}])
        assert replies[0].get("result") == "ok", replies[0]

    def test_positional_list_params_dispatched_correctly(self) -> None:
        """Non-empty list params must still use positional dispatch."""
        replies = _run_plugin(self.plugin, [{"id": 8, "method": "pos", "params": ["a", "b"]}])
        assert replies[0].get("result") == "a-b", replies[0]

    def test_empty_dict_params_calls_handler(self) -> None:
        """params={} must dispatch via keyword path without error."""
        replies = _run_plugin(self.plugin, [{"id": 9, "method": "noop", "params": {}}])
        assert replies[0].get("result") == "ok", replies[0]


# ---------------------------------------------------------------------------
# BUG-4 — null method must not leak "None" into error message
# ---------------------------------------------------------------------------

class TestNullMethodHandling:
    def setup_method(self) -> None:
        self.plugin = NavigPlugin(name="q")

    def test_null_method_gives_clean_error(self) -> None:
        """JSON null method must produce 'Unknown method: ' not 'Unknown method: None'."""
        replies = _run_plugin(self.plugin, [{"id": 10, "method": None}])
        assert "error" in replies[0]
        assert "None" not in replies[0]["error"], (
            "Error must not expose Python None repr; got: " + replies[0]["error"]
        )

    def test_null_method_error_message_prefix(self) -> None:
        replies = _run_plugin(self.plugin, [{"id": 11, "method": None}])
        assert replies[0]["error"].startswith("Unknown method:")

    def test_empty_string_method_gives_unknown_error(self) -> None:
        replies = _run_plugin(self.plugin, [{"id": 12, "method": ""}])
        assert "error" in replies[0]


# ---------------------------------------------------------------------------
# BUG-1 + BUG-2 — navig_config() key regex + quote stripping
# ---------------------------------------------------------------------------

SAMPLE_YAML = """\
lowercase_key: plain_value
MixedCase: SomeValue
API_KEY: sk-abc123
quoted_double: "my secret"
quoted_single: 'another secret'
normal_url: https://example.com
"""


def _mock_config(yaml_text: str) -> dict:
    """Run navig_config() with *yaml_text* as the contents of config.yaml."""
    with patch("pathlib.Path.home", return_value=Path("/fake")), \
         patch("pathlib.Path.read_text", return_value=yaml_text):
        return navig_config()


class TestNavigConfigKeyParsing:
    """BUG-1: regex must accept uppercase and mixed-case keys."""

    def test_lowercase_key_is_parsed(self) -> None:
        result = _mock_config(SAMPLE_YAML)
        assert result.get("lowercase_key") == "plain_value"

    def test_mixed_case_key_is_parsed(self) -> None:
        """MixedCase key was silently dropped by [a-z_] regex (BUG-1)."""
        result = _mock_config(SAMPLE_YAML)
        assert "MixedCase" in result, "MixedCase key silently dropped — BUG-1 not fixed"
        assert result["MixedCase"] == "SomeValue"

    def test_all_caps_key_is_parsed(self) -> None:
        """ALL_CAPS key was silently dropped by [a-z_] regex (BUG-1)."""
        result = _mock_config(SAMPLE_YAML)
        assert "API_KEY" in result, "ALL_CAPS key silently dropped — BUG-1 not fixed"
        assert result["API_KEY"] == "sk-abc123"

    def test_value_with_colon_preserved(self) -> None:
        """Values containing colons (e.g. URLs) must be parsed completely."""
        result = _mock_config(SAMPLE_YAML)
        assert result.get("normal_url") == "https://example.com"

    def test_comment_lines_ignored(self) -> None:
        result = _mock_config("# this is a comment\nkey: val\n")
        assert "key" in result
        assert "#" not in result

    def test_empty_yaml_returns_empty_dict(self) -> None:
        assert _mock_config("") == {}

    def test_missing_file_returns_empty_dict(self) -> None:
        with patch("pathlib.Path.home", return_value=Path("/nonexistent_xyz99")):
            result = navig_config()
        assert result == {}


class TestNavigConfigQuoteStripping:
    """BUG-2: values surrounded by matching quotes must have those quotes removed."""

    def test_double_quoted_value_stripped(self) -> None:
        """[BUG-2] double-quoted value must not include quote chars."""
        result = _mock_config(SAMPLE_YAML)
        assert result.get("quoted_double") == "my secret", (
            "Got: " + repr(result.get("quoted_double"))
        )

    def test_single_quoted_value_stripped(self) -> None:
        """[BUG-2] single-quoted value must not include quote chars."""
        result = _mock_config(SAMPLE_YAML)
        assert result.get("quoted_single") == "another secret", (
            "Got: " + repr(result.get("quoted_single"))
        )

    def test_unquoted_value_unchanged(self) -> None:
        result = _mock_config("key: value\n")
        assert result["key"] == "value"

    def test_mismatched_quotes_not_stripped(self) -> None:
        """Outer chars differ — must not strip anything."""
        result = _mock_config("key: 'mismatch\"\n")
        val = result["key"]
        assert val.startswith("'"), "Leading quote must be preserved"

    def test_single_char_value_not_stripped(self) -> None:
        """A single quote char as the entire value must not cause IndexError."""
        result = _mock_config('key: "\n')
        # value is `"` — len<2, so no stripping attempted
        assert result.get("key") == '"'


# ---------------------------------------------------------------------------
# BUG-5 — package __init__.py exists and re-exports NavigPlugin
# ---------------------------------------------------------------------------

def test_navig_sdk_package_importable() -> None:
    """navig_sdk must be importable at the package level (requires __init__.py)."""
    import navig_sdk  # noqa: PLC0415
    assert hasattr(navig_sdk, "NavigPlugin")
    assert navig_sdk.NavigPlugin is NavigPlugin


def test_navig_sdk_has_navig_config_export() -> None:
    import navig_sdk  # noqa: PLC0415
    assert hasattr(navig_sdk, "navig_config")
    assert navig_sdk.navig_config is navig_config


def test_navig_sdk_has_navig_stdio_plugin_alias() -> None:
    """NavigStdioPlugin must be a re-export alias of NavigPlugin."""
    import navig_sdk  # noqa: PLC0415
    assert hasattr(navig_sdk, "NavigStdioPlugin")
    assert navig_sdk.NavigStdioPlugin is NavigPlugin


# ---------------------------------------------------------------------------
# _reply helper
# ---------------------------------------------------------------------------

class TestReplyHelper:
    def test_result_reply(self) -> None:
        assert _reply(1, result=42) == {"id": 1, "result": 42}

    def test_error_reply(self) -> None:
        assert _reply(2, error="oops") == {"id": 2, "error": "oops"}

    def test_no_id_defaults_to_none(self) -> None:
        r = _reply(result="x")
        assert r["id"] is None
        assert r["result"] == "x"
