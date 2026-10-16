"""The standalone kit: host paths/IO, console, keys, and bring-your-own AI.

Every test here forces the STANDALONE branch by mapping the navig module it would delegate to
onto ``None`` in ``sys.modules`` (which makes ``import`` raise ImportError) through
monkeypatch, so it is undone after each test. The tree running these tests usually has navig
installed; without this, every assertion below would be exercising navig, not the fallback.
"""

from __future__ import annotations

import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import pytest

from navig_sdk import ai, host, keys
from navig_sdk import console as ch

_AI_ENV = (
    "NAVIG_AI_BASE_URL", "NAVIG_AI_API_KEY", "NAVIG_AI_MODEL", "NAVIG_AI_PROVIDER",
    "NAVIG_OLLAMA_URL", "OLLAMA_HOST",
    *{n for names in keys.PROVIDER_ENV_VARS.values() for n in names},
    *(f"{p.upper()}_API_KEY" for p in keys.PROVIDER_ENV_VARS),
)


@pytest.fixture
def no_navig(monkeypatch: pytest.MonkeyPatch) -> None:
    for mod in (
        "navig", "navig.llm", "navig.llm.generate", "navig.agent", "navig.agent.ai_client", "navig.console_helper",
        "navig.platform", "navig.platform.paths", "navig.core.yaml_io",
        "navig.core.json_io", "navig.core.proc_text", "navig_vault", "navig_vault.core",
    ):
        monkeypatch.setitem(sys.modules, mod, None)
    # Prove the block took: otherwise every test below silently tests navig.
    assert not host.navig_available()


@pytest.fixture
def clean_ai_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in _AI_ENV:
        monkeypatch.delenv(name, raising=False)
    # Point Ollama discovery at a closed port so a real local Ollama cannot answer.
    monkeypatch.setenv("OLLAMA_HOST", "http://127.0.0.1:9")


class _FakeOpenAI(BaseHTTPRequestHandler):
    seen: list[dict] = []

    def do_POST(self) -> None:  # noqa: N802
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        _FakeOpenAI.seen.append({"path": self.path, "auth": self.headers.get("Authorization"), "body": body})
        if body["model"] == "thinker":
            reply = {"choices": [{"message": {"content": ""}, "finish_reason": "length"}]}
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(reply).encode())
            return
        if body["model"] == "broken":
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b'{"error":"bad key"}')
            return
        reply = {"choices": [{"message": {"content": f"echo:{body['messages'][-1]['content']}"}}]}
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(reply).encode())

    def do_GET(self) -> None:  # noqa: N802 - Ollama's /api/tags
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({"models": [{"name": "llama3.2:1b"}]}).encode())

    def log_message(self, *args: object) -> None:
        pass


@pytest.fixture
def fake_server():
    _FakeOpenAI.seen = []
    srv = HTTPServer(("127.0.0.1", 0), _FakeOpenAI)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        yield f"http://127.0.0.1:{srv.server_address[1]}"
    finally:
        srv.shutdown()
        srv.server_close()


# ── AI ───────────────────────────────────────────────────────────────────────


def test_nothing_configured_says_how_to_fix_it(no_navig, clean_ai_env) -> None:
    assert ai.resolve() is None
    with pytest.raises(ai.AINotConfigured) as exc:
        ai.generate("hi")
    assert "OPENAI_API_KEY" in str(exc.value) and "Ollama" in str(exc.value)


def test_custom_openai_compatible_server(no_navig, clean_ai_env, fake_server, monkeypatch) -> None:
    monkeypatch.setenv("NAVIG_AI_BASE_URL", f"{fake_server}/v1/")
    monkeypatch.setenv("NAVIG_AI_MODEL", "my-model")
    monkeypatch.setenv("NAVIG_AI_API_KEY", "sk-secret-123")
    out = ai.generate("ping", system="be brief", max_tokens=5)
    assert out == "echo:ping"
    call = _FakeOpenAI.seen[-1]
    assert call["path"] == "/v1/chat/completions"
    assert call["auth"] == "Bearer sk-secret-123"
    assert call["body"]["model"] == "my-model"
    assert call["body"]["messages"][0] == {"role": "system", "content": "be brief"}
    assert call["body"]["max_tokens"] == 5


def test_base_url_without_model_is_an_error(no_navig, clean_ai_env, monkeypatch) -> None:
    monkeypatch.setenv("NAVIG_AI_BASE_URL", "http://127.0.0.1:9/v1")
    with pytest.raises(ai.AIError, match="NAVIG_AI_MODEL"):
        ai.resolve()


def test_first_provider_key_wins_in_table_order(no_navig, clean_ai_env, monkeypatch) -> None:
    monkeypatch.setenv("GROQ_API_KEY", "gsk-x")
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-x")
    ep = ai.resolve()
    assert ep is not None and ep.name == "openrouter"  # openrouter precedes groq
    monkeypatch.setenv("NAVIG_AI_PROVIDER", "groq")
    assert ai.resolve().name == "groq"
    monkeypatch.setenv("NAVIG_AI_MODEL", "llama-custom")
    assert ai.resolve().model == "llama-custom"


def test_alternate_env_name_is_honoured(no_navig, clean_ai_env, monkeypatch) -> None:
    monkeypatch.setenv("CLAUDE_API_KEY", "sk-ant-x")
    assert ai.resolve().name == "anthropic"


def test_unknown_or_unkeyed_explicit_provider_is_an_error(no_navig, clean_ai_env, monkeypatch) -> None:
    monkeypatch.setenv("NAVIG_AI_PROVIDER", "nope")
    with pytest.raises(ai.AIError, match="not one of"):
        ai.resolve()
    monkeypatch.setenv("NAVIG_AI_PROVIDER", "mistral")
    with pytest.raises(ai.AIError, match="no mistral key"):
        ai.resolve()


def test_local_ollama_is_used_when_nothing_else_is(no_navig, clean_ai_env, fake_server, monkeypatch) -> None:
    monkeypatch.setenv("OLLAMA_HOST", fake_server)
    ep = ai.resolve()
    assert ep is not None and ep.name == "ollama" and ep.model == "llama3.2:1b" and ep.key is None
    assert ai.generate("hi") == "echo:hi"
    assert _FakeOpenAI.seen[-1]["auth"] is None


def test_http_error_names_provider_never_the_key(no_navig, clean_ai_env, fake_server, monkeypatch) -> None:
    monkeypatch.setenv("NAVIG_AI_BASE_URL", f"{fake_server}/v1")
    monkeypatch.setenv("NAVIG_AI_MODEL", "broken")
    monkeypatch.setenv("NAVIG_AI_API_KEY", "sk-must-not-leak")
    with pytest.raises(ai.AIError) as exc:
        ai.generate("hi")
    assert "HTTP 401" in str(exc.value)
    assert "sk-must-not-leak" not in str(exc.value)
    assert "sk-must-not-leak" not in repr(ai.resolve())


def test_navig_answers_when_installed(clean_ai_env, monkeypatch) -> None:
    import types

    captured = {}

    def fake_llm_generate(messages, **kw):
        captured.update(kw, messages=messages)
        return "from navig"

    mod = types.ModuleType("navig.llm.generate")
    mod.llm_generate = fake_llm_generate
    monkeypatch.setitem(sys.modules, "navig.llm.generate", mod)
    assert ai.generate("hi", mode="summarize", timeout=7) == "from navig"
    assert captured["mode"] == "summarize" and captured["timeout"] == 7
    assert captured["messages"] == [{"role": "user", "content": "hi"}]


# ── keys ─────────────────────────────────────────────────────────────────────


def test_generic_provider_env_name(no_navig, clean_ai_env, monkeypatch) -> None:
    monkeypatch.setenv("REPLICATE_API_KEY", "r8-x")
    assert keys.api_key("replicate") == "r8-x"
    assert keys.api_key("replicate", "REPLICATE_API_TOKEN") == "r8-x"
    assert keys.api_key("nothing-here") is None


# ── host ─────────────────────────────────────────────────────────────────────


def test_paths_standalone(no_navig, monkeypatch, tmp_path) -> None:
    for v in ("NAVIG_CONFIG_DIR", "NAVIG_DATA_DIR", "NAVIG_SYSTEM_SERVICE", "NAVIG_CACHE_DIR"):
        monkeypatch.delenv(v, raising=False)
    monkeypatch.setenv("NAVIG_CONFIG_DIR", str(tmp_path / "cfg"))
    assert host.config_dir() == tmp_path / "cfg"
    assert host.data_dir() == tmp_path / "cfg" / "data"
    monkeypatch.setenv("NAVIG_DATA_DIR", str(tmp_path / "d"))
    assert host.data_dir() == tmp_path / "d"
    monkeypatch.setenv("NAVIG_CACHE_DIR", str(tmp_path / "c"))
    assert host.cache_dir() == tmp_path / "c"


def test_atomic_write_and_json(no_navig, tmp_path) -> None:
    target = tmp_path / "nested" / "f.json"
    host.atomic_write_text(target, '{"a": 1}')
    assert host.safe_json_loads(target.read_text(encoding="utf-8"), {}) == {"a": 1}
    assert host.safe_json_loads("{broken", {"d": 1}) == {"d": 1}
    assert host.safe_json_loads(None, []) == []
    assert not list(target.parent.glob("*.navig~"))


def test_run_text_decodes(no_navig) -> None:
    proc = host.run_text([sys.executable, "-c", "import sys; sys.stdout.buffer.write('é✓'.encode())"])
    assert proc.returncode == 0 and proc.stdout == "é✓"


# ── console ──────────────────────────────────────────────────────────────────


def test_console_standalone_surface(no_navig, capsys) -> None:
    ch.success("saved", "3 files")
    ch.error("failed")
    ch.kv("name", "value")
    ch.emit_json({"b": 1})
    out = capsys.readouterr().out
    assert "saved" in out and "3 files" in out and "failed" in out and "name:" in out
    assert '"b": 1' in out
    table = ch.create_table(columns=[{"name": "A"}])
    table.add_row("x")
    ch.print_table(table)
    assert "x" in capsys.readouterr().out
    with pytest.raises(AttributeError):
        ch.definitely_not_a_function  # noqa: B018


def test_console_delegates_to_navig_when_installed(monkeypatch) -> None:
    import types

    fake = types.ModuleType("navig.console_helper")
    fake.success = lambda *a, **k: "navig"
    fake.format_db_output = object()
    monkeypatch.setitem(sys.modules, "navig.console_helper", fake)
    assert ch.success("x") == "navig"
    assert ch.format_db_output is fake.format_db_output  # full navig surface, not just the subset


def test_no_module_imports_navig_at_import_time() -> None:
    """The kit itself must import with navig absent — checked on the AST, not by hope."""
    import ast

    pkg = Path(host.__file__).parent
    offenders = []
    for f in pkg.glob("*.py"):
        tree = ast.parse(f.read_text(encoding="utf-8"))
        for node in tree.body:  # module level only; function bodies are lazy
            names = []
            if isinstance(node, ast.ImportFrom) and node.module:
                names = [node.module]
            elif isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            offenders += [f"{f.name}:{node.lineno}" for n in names if n == "navig" or n.startswith("navig.")]
    assert not offenders


def test_cut_off_before_any_text_is_an_error_not_an_empty_answer(
    no_navig, clean_ai_env, fake_server, monkeypatch
) -> None:
    monkeypatch.setenv("NAVIG_AI_BASE_URL", f"{fake_server}/v1")
    monkeypatch.setenv("NAVIG_AI_MODEL", "thinker")
    with pytest.raises(ai.AIError, match="token limit"):
        ai.generate("hi", max_tokens=8)


def test_openai_gets_max_completion_tokens(no_navig, clean_ai_env, fake_server, monkeypatch) -> None:
    ep = ai.Endpoint("openai", f"{fake_server}/v1", "m", "k")
    ai._chat(ep, [{"role": "user", "content": "x"}], max_tokens=9, temperature=None, timeout=5)
    body = _FakeOpenAI.seen[-1]["body"]
    assert body.get("max_completion_tokens") == 9 and "max_tokens" not in body
    ep = ai.Endpoint("groq", f"{fake_server}/v1", "m", "k")
    ai._chat(ep, [{"role": "user", "content": "x"}], max_tokens=9, temperature=None, timeout=5)
    assert _FakeOpenAI.seen[-1]["body"].get("max_tokens") == 9


# ── files ────────────────────────────────────────────────────────────────────

from navig_sdk import files  # noqa: E402


def test_json_update_never_masks_an_unreadable_store(no_navig, tmp_path, monkeypatch) -> None:
    store = tmp_path / "s.json"
    assert files.load_json_for_update(store, default={}) == {}  # absent
    files.atomic_write_json({"a": 1}, store)
    assert files.load_json_for_update(store, default={}) == {"a": 1}

    def locked(*a, **k):
        raise PermissionError("locked by antivirus")

    monkeypatch.setattr(Path, "read_text", locked)
    monkeypatch.setattr(files.time, "sleep", lambda s: None)
    with pytest.raises(files.JsonReadError):
        files.load_json_for_update(store, default={})
    assert files.load_json_safe(store, default={"x": 0}) == {"x": 0}  # a view degrades


def test_corrupt_json_is_kept_beside_the_store(no_navig, tmp_path) -> None:
    store = tmp_path / "s.json"
    store.write_text("{not json", encoding="utf-8")
    assert files.load_json_for_update(store, default={}) == {}
    assert (tmp_path / "s.json.corrupt").read_text(encoding="utf-8") == "{not json"
    store.write_text("[1, 2]", encoding="utf-8")  # wrong shape is corruption too
    assert files.load_json_for_update(store, default={}) == {}


def test_yaml_update_refuses_invalid_or_non_mapping(no_navig, tmp_path) -> None:
    pytest.importorskip("yaml")
    cfg = tmp_path / "c.yaml"
    assert files.load_yaml_for_update(cfg) == {}
    cfg.write_text("# only a comment\n", encoding="utf-8")
    assert files.load_yaml_for_update(cfg) == {}
    files.atomic_write_yaml({"token_source": "vault", "n": 2}, cfg)
    assert files.load_yaml_for_update(cfg) == {"token_source": "vault", "n": 2}
    assert files.safe_load_yaml(cfg) == {"token_source": "vault", "n": 2}
    cfg.write_text("a: [unclosed\n", encoding="utf-8")
    with pytest.raises(files.ConfigReadError):
        files.load_yaml_for_update(cfg)
    assert files.safe_load_yaml(cfg) is None
    cfg.write_text("- a\n- b\n", encoding="utf-8")
    with pytest.raises(files.ConfigReadError, match="mapping"):
        files.load_yaml_for_update(cfg)


def test_error_classes_are_navigs_own_when_navig_is_installed() -> None:
    """An `except files.JsonReadError` must catch what navig's implementation raises."""
    json_io = pytest.importorskip("navig.core.json_io")
    yaml_io = pytest.importorskip("navig.core.yaml_io")
    assert files.JsonReadError is json_io.JsonReadError
    assert files.ConfigReadError is yaml_io.ConfigReadError


# ── net ──────────────────────────────────────────────────────────────────────

from http.server import BaseHTTPRequestHandler as _H  # noqa: E402

from navig_sdk import net  # noqa: E402


def test_bind_falls_back_to_a_free_port_when_the_default_is_refused(no_navig) -> None:
    # Simulated refusal rather than a second real bind: on Windows ThreadingHTTPServer sets
    # SO_REUSEADDR, which lets a second server bind a port already in use, so "busy" cannot
    # be staged portably. The case the helper exists for (a port inside a reserved range,
    # WinError 10013) is a refusal, which is what this stages.
    refused = 8099
    calls = []

    class _Srv:
        def __init__(self, addr, handler):
            calls.append(addr[1])
            if addr[1] == refused:
                raise OSError(10013, "An attempt was made to access a socket in a way forbidden")
            self.server_address = (addr[0], addr[1] or 50123)

    srv, port = net.bind_http_server(_H, preferred=refused, server_cls=_Srv)
    assert calls == [refused, 0] and port == 50123
    with pytest.raises(net.PortBindError, match="--port 8100"):
        net.bind_http_server(_H, refused, server_cls=_Srv)  # an explicit port is never swapped


def test_port_bind_error_is_navigs_class_when_installed() -> None:
    http_bind = pytest.importorskip("navig.http_bind")
    assert net.PortBindError is http_bind.PortBindError


# ── cli (the standalone front door) ─────────────────────────────────────────

from navig_sdk import cli as sdk_cli  # noqa: E402


def test_front_door_turns_a_navig_only_feature_into_one_line(capsys) -> None:
    def app(prog_name: str) -> None:
        raise ModuleNotFoundError("No module named 'navig.browser'", name="navig.browser")

    with pytest.raises(SystemExit) as exc:
        sdk_cli.run(app, "navig-download")
    assert exc.value.code == 1
    err = capsys.readouterr().err
    assert "navig-download: this feature is part of navig" in err and "pip install navig" in err
    assert "Traceback" not in err


def test_front_door_leaves_other_missing_modules_alone() -> None:
    def app(prog_name: str) -> None:
        raise ModuleNotFoundError("No module named 'yt_dlp'", name="yt_dlp")

    with pytest.raises(ModuleNotFoundError, match="yt_dlp"):
        sdk_cli.run(app, "navig-download")


def test_front_door_passes_the_program_name() -> None:
    seen = {}
    sdk_cli.run(lambda prog_name: seen.setdefault("prog", prog_name), "navig-github")
    assert seen["prog"] == "navig-github"


def test_owner_only_permissions_standalone(no_navig, tmp_path) -> None:
    secret = tmp_path / "cookies.txt"
    secret.write_text("x", encoding="utf-8")
    host.set_owner_only_file_permissions(secret)  # must never raise
    if sys.platform != "win32":
        assert (secret.stat().st_mode & 0o777) == 0o600


# ── ai.status / ai.acomplete ─────────────────────────────────────────────────


def test_status_standalone(no_navig, clean_ai_env, fake_server, monkeypatch) -> None:
    st = ai.status()
    assert st["ready"] is False and st["via"] == "standalone" and "OPENAI_API_KEY" in st["error"]
    monkeypatch.setenv("NAVIG_AI_BASE_URL", f"{fake_server}/v1")
    monkeypatch.setenv("NAVIG_AI_MODEL", "m1")
    st = ai.status()
    assert st == {"ready": True, "provider": "custom", "model": "m1", "via": "standalone", "error": None}


def test_acomplete_standalone(no_navig, clean_ai_env, fake_server, monkeypatch) -> None:
    import asyncio

    monkeypatch.setenv("NAVIG_AI_BASE_URL", f"{fake_server}/v1")
    monkeypatch.setenv("NAVIG_AI_MODEL", "m1")
    assert asyncio.run(ai.acomplete("hello", system="s")) == "echo:hello"
    assert _FakeOpenAI.seen[-1]["body"]["messages"][0] == {"role": "system", "content": "s"}


def test_acomplete_and_status_use_navigs_ai_client_when_installed(monkeypatch) -> None:
    import asyncio
    import types

    class _Client:
        provider, model = "openrouter", "google/gemini-2.5-flash"

        def is_available(self):
            return True

        async def complete(self, prompt, system_prompt=None):
            return f"navig:{prompt}:{system_prompt}"

    mod = types.ModuleType("navig.agent.ai_client")
    mod.get_ai_client = lambda: _Client()
    monkeypatch.setitem(sys.modules, "navig.agent.ai_client", mod)
    assert asyncio.run(ai.acomplete("p", system="s")) == "navig:p:s"
    assert ai.status() == {"ready": True, "provider": "openrouter", "model": "google/gemini-2.5-flash", "via": "navig", "error": None}


# ── store / settings / decode ────────────────────────────────────────────────

import importlib  # noqa: E402


def _standalone_store_module(monkeypatch):
    """navig_sdk.store as it is WITHOUT navig: re-executed with navig.store hidden."""
    monkeypatch.setitem(sys.modules, "navig.store", None)
    monkeypatch.setitem(sys.modules, "navig.store.base", None)
    spec = importlib.util.spec_from_file_location("_sdk_store_standalone", Path(host.__file__).with_name("store.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.BaseStore.__module__ == "_sdk_store_standalone"  # really the standalone twin
    return mod


def _notes_store(base):
    class Notes(base):
        SCHEMA_VERSION = 2

        def _create_schema(self, conn):
            conn.executescript("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, body TEXT)")

        def add(self, body):
            self._write("INSERT INTO notes (body) VALUES (?)", (body,))

        def bodies(self):
            return [r["body"] for r in self._read_all("SELECT body FROM notes ORDER BY id")]

    return Notes


def test_standalone_store_roundtrip_and_schema(monkeypatch, tmp_path) -> None:
    mod = _standalone_store_module(monkeypatch)
    Notes = _notes_store(mod.BaseStore)
    s = Notes(tmp_path / "n.db")
    s.add("one")
    s._write_many("INSERT INTO notes (body) VALUES (?)", [("two",), ("three",)])
    assert s.bodies() == ["one", "two", "three"]
    assert s.get_schema_version() == 2
    backup = s.backup(tmp_path / "bak" / "n.db")
    s.close()
    assert Notes(backup).bodies() == ["one", "two", "three"]


def test_a_standalone_database_opens_in_navig_and_back(monkeypatch, tmp_path) -> None:
    """The data-safety promise: one file, readable from either side."""
    navig_base = pytest.importorskip("navig.store.base").BaseStore
    mod = _standalone_store_module(monkeypatch)
    db = tmp_path / "shared.db"
    alone = _notes_store(mod.BaseStore)(db)
    alone.add("written standalone")
    alone.close()
    in_navig = _notes_store(navig_base)(db)
    assert in_navig.bodies() == ["written standalone"]
    assert in_navig.get_schema_version() == 2
    in_navig.add("written by navig")
    in_navig.close()
    again = _notes_store(mod.BaseStore)(db)
    assert again.bodies() == ["written standalone", "written by navig"]
    again.close()


def test_settings_standalone_share_navigs_layout(no_navig, monkeypatch, tmp_path) -> None:
    pytest.importorskip("yaml")
    from navig_sdk import files, settings

    monkeypatch.setitem(sys.modules, "navig.config", None)
    monkeypatch.setenv("NAVIG_CONFIG_DIR", str(tmp_path))
    (tmp_path / "config.yaml").write_text("ai:\n  model: keep-me\n", encoding="utf-8")
    settings.set("mobile", "leapp_cmd", "/opt/leapp")
    assert settings.get("mobile", "leapp_cmd") == "/opt/leapp"
    assert settings.get("mobile", "nope", "dflt") == "dflt"
    data = files.safe_load_yaml(tmp_path / "config.yaml")
    assert data == {"ai": {"model": "keep-me"}, "plugins": {"mobile": {"leapp_cmd": "/opt/leapp"}}}
    (tmp_path / "config.yaml").write_text("ai: [broken\n", encoding="utf-8")
    with pytest.raises(files.ConfigReadError):
        settings.set("mobile", "x", 1)  # never overwrite a config it could not read
    assert (tmp_path / "config.yaml").read_text(encoding="utf-8") == "ai: [broken\n"


def test_decode_console_result_standalone(no_navig) -> None:
    import types

    r = host.decode_console_result(types.SimpleNamespace(returncode=3, stdout="é✓".encode(), stderr=b""))
    assert (r.returncode, r.stdout, r.stderr, r.args) == (3, "é✓", "", None)
    assert host.decode_console_result(types.SimpleNamespace(stdout="already text")).stdout == "already text"


# ── ssrf / pim ───────────────────────────────────────────────────────────────

from navig_sdk import ssrf  # noqa: E402


def test_ssrf_blocks_private_addresses_standalone(no_navig, monkeypatch, tmp_path) -> None:
    monkeypatch.setitem(sys.modules, "navig.config", None)
    monkeypatch.setenv("NAVIG_CONFIG_DIR", str(tmp_path))  # no config.yaml: the secure default
    policy = ssrf.policy_from_config()
    for url in ("http://127.0.0.1/cal.ics", "http://169.254.169.254/latest/meta-data/",
                "http://[::1]/x", "http://10.1.2.3/x"):
        with pytest.raises(ssrf.SsrfBlockedError):
            ssrf.check_url(url, policy)
    with pytest.raises(ValueError, match="http/https"):  # not a web URL at all
        ssrf.check_url("file:///etc/passwd", policy)


def test_ssrf_allow_private_is_read_from_config_standalone(no_navig, monkeypatch, tmp_path) -> None:
    pytest.importorskip("yaml")
    monkeypatch.setitem(sys.modules, "navig.config", None)
    monkeypatch.setenv("NAVIG_CONFIG_DIR", str(tmp_path))
    (tmp_path / "config.yaml").write_text("net:\n  ssrf:\n    allow_private_network: 'false'\n", encoding="utf-8")
    assert ssrf.policy_from_config().allow_private_network is False  # the STRING "false" stays off
    (tmp_path / "config.yaml").write_text("net:\n  ssrf:\n    allow_private_network: true\n", encoding="utf-8")
    ssrf.check_url("http://127.0.0.1/cal.ics", ssrf.policy_from_config())  # a home server, allowed
    (tmp_path / "config.yaml").write_text("net: [broken\n", encoding="utf-8")
    with pytest.raises(ssrf.SsrfBlockedError):  # an unreadable config never LOOSENS the guard
        ssrf.check_url("http://127.0.0.1/cal.ics", ssrf.policy_from_config())



def test_missing_config_needs_no_yaml(no_navig, monkeypatch, tmp_path) -> None:
    """Measured: a standalone plugin with no config.yaml crashed importing PyYAML it never needed."""
    from navig_sdk import files

    monkeypatch.setitem(sys.modules, "yaml", None)  # PyYAML not installed
    assert files.safe_load_yaml(tmp_path / "absent.yaml") is None
    assert files.load_yaml_for_update(tmp_path / "absent.yaml") == {}


def test_settings_by_dotted_path_keep_every_sibling(no_navig, monkeypatch, tmp_path) -> None:
    """navig-social keeps page ids at ``adapters.social.<provider>.<key>`` — not under
    ``plugins.`` — so it needs a dotted path, and a write must not clobber a sibling."""
    pytest.importorskip("yaml")
    from navig_sdk import files, settings

    monkeypatch.setitem(sys.modules, "navig.config", None)
    monkeypatch.setenv("NAVIG_CONFIG_DIR", str(tmp_path))
    (tmp_path / "config.yaml").write_text(
        "adapters:\n  social:\n    reddit:\n      subreddit: keep\n", encoding="utf-8"
    )
    settings.set_path("adapters.social.facebook.page_id", "123")
    assert settings.get_path("adapters.social.facebook.page_id") == "123"
    assert settings.get_path("adapters.social.reddit.subreddit") == "keep"
    assert settings.get_path("adapters.social.nope.x", "dflt") == "dflt"
    assert settings.get_path("adapters.social.reddit.subreddit.deeper", "dflt") == "dflt"
    (tmp_path / "config.yaml").write_text("adapters: [broken\n", encoding="utf-8")
    with pytest.raises(files.ConfigReadError):
        settings.set_path("adapters.social.x.y", 1)
    assert (tmp_path / "config.yaml").read_text(encoding="utf-8") == "adapters: [broken\n"


def test_front_door_names_a_missing_first_party_package(capsys) -> None:
    """A feature behind an optional extra (TikTok login → navig-browser) names the package."""
    def app(prog_name: str) -> None:
        raise ModuleNotFoundError("No module named 'navig_browser'", name="navig_browser.stealth")

    with pytest.raises(SystemExit) as exc:
        sdk_cli.run(app, "navig-download")
    assert exc.value.code == 1
    err = capsys.readouterr().err
    assert "needs the navig-browser package" in err and "pip install navig-browser" in err


# ── provider / model pins (a plugin's --provider / --model) ─────────────────


def test_explicit_pins_win_over_the_environment(no_navig, clean_ai_env, monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "sk-a")
    monkeypatch.setenv("GROQ_API_KEY", "gsk-b")
    monkeypatch.setenv("NAVIG_AI_PROVIDER", "openai")
    monkeypatch.setenv("NAVIG_AI_MODEL", "from-env")
    ep = ai.resolve(provider="groq", model="pinned-model")
    assert ep is not None and ep.name == "groq" and ep.model == "pinned-model"
    # Nothing pinned: the environment still decides, exactly as before.
    ep = ai.resolve()
    assert ep is not None and ep.name == "openai" and ep.model == "from-env"


def test_custom_pin_needs_a_base_url(no_navig, clean_ai_env, monkeypatch) -> None:
    with pytest.raises(ai.AIError, match="NAVIG_AI_BASE_URL"):
        ai.resolve(provider="custom", model="m")
    monkeypatch.setenv("NAVIG_AI_BASE_URL", "http://127.0.0.1:9/v1")
    ep = ai.resolve(provider="custom", model="m")
    assert ep is not None and ep.name == "custom" and ep.model == "m"


def test_a_named_pin_skips_the_custom_base_url(no_navig, clean_ai_env, monkeypatch) -> None:
    monkeypatch.setenv("NAVIG_AI_BASE_URL", "http://127.0.0.1:9/v1")
    monkeypatch.setenv("NAVIG_AI_MODEL", "x")
    monkeypatch.setenv("MISTRAL_API_KEY", "m-key")
    ep = ai.resolve(provider="mistral")
    assert ep is not None and ep.name == "mistral"


def test_pins_reach_navig_as_overrides(clean_ai_env, monkeypatch) -> None:
    import types

    captured: dict = {}

    def fake_llm_generate(messages, **kw):
        captured.update(kw)
        return "ok"

    mod = types.ModuleType("navig.llm.generate")
    mod.llm_generate = fake_llm_generate
    monkeypatch.setitem(sys.modules, "navig.llm.generate", mod)
    assert ai.generate("hi", provider="ollama", model="llama3") == "ok"
    assert captured["provider_override"] == "ollama" and captured["model_override"] == "llama3"
    captured.clear()
    ai.generate("hi")
    # Unpinned calls pass no override keys, so an older navig's llm_generate still answers.
    assert "provider_override" not in captured and "model_override" not in captured
