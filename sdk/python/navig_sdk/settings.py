"""A plugin's own settings, stored where navig stores them.

    from navig_sdk import settings
    settings.set("mobile", "leapp_cmd", "/opt/leapp/leapp.py")
    settings.get("mobile", "leapp_cmd")

navig keeps plugin settings in ``<config dir>/config.yaml`` under ``plugins.<plugin>.<key>``.
Inside navig these ARE ``ConfigManager.get_plugin_config`` / ``set_plugin_config``. Without
navig they read and write that same file and layout, so a setting saved on its own is the
setting navig finds after it is installed.

Writing is read-modify-write through :func:`navig_sdk.files.load_yaml_for_update`: a
config.yaml that exists but cannot be read or parsed RAISES instead of being treated as
empty — a failed read must never become a write that erases every other setting in it.
"""

from __future__ import annotations

from typing import Any

from navig_sdk import files
from navig_sdk.host import config_dir

__all__ = ["get", "get_path", "set", "set_path"]


def _manager() -> Any:
    try:
        from navig.config import get_config_manager  # noqa: PLC0415
    except ImportError:
        return None
    return get_config_manager()


def get(plugin: str, key: str, default: Any = None) -> Any:
    """The value of ``plugins.<plugin>.<key>``, or *default*."""
    cm = _manager()
    if cm is not None:
        return cm.get_plugin_config(plugin, key, default)
    data = files.safe_load_yaml(config_dir() / "config.yaml") or {}
    node = data.get("plugins", {}) if isinstance(data, dict) else {}
    node = node.get(plugin, {}) if isinstance(node, dict) else {}
    return node.get(key, default) if isinstance(node, dict) else default


def set(plugin: str, key: str, value: Any) -> None:  # noqa: A001 - mirrors navig's naming
    """Persist ``plugins.<plugin>.<key> = value``. Raises if config.yaml is unreadable."""
    cm = _manager()
    if cm is not None:
        cm.set_plugin_config(plugin, key, value)
        return
    path = config_dir() / "config.yaml"
    data = files.load_yaml_for_update(path)
    plugins = data.setdefault("plugins", {})
    if not isinstance(plugins, dict):
        raise files.ConfigReadError(f"{path}: `plugins` is not a mapping — refusing to overwrite it")
    section = plugins.setdefault(plugin, {})
    if not isinstance(section, dict):
        plugins[plugin] = section = {}
    section[key] = value
    files.atomic_write_yaml(data, path)


def get_path(dotted: str, default: Any = None) -> Any:
    """Any global config value by dotted path (``adapters.social.x.page_id``), or *default*.

    For a plugin whose settings predate ``plugins.<name>``: its data already lives at another
    path in config.yaml, and moving it would lose every user's saved value. Inside navig this
    is ``ConfigManager.get``; without navig it reads the same file.
    """
    cm = _manager()
    if cm is not None:
        return cm.get(dotted, default)
    node: Any = files.safe_load_yaml(config_dir() / "config.yaml") or {}
    for part in dotted.split("."):
        if not isinstance(node, dict) or part not in node:
            return default
        node = node[part]
    return node


def set_path(dotted: str, value: Any) -> None:
    """Persist one global config value by dotted path, leaving every sibling key alone.

    Inside navig this is ``ConfigManager.set_global`` (refresh → deep-set → save). Without navig
    it is the same read-modify-write on config.yaml, raising if the file cannot be read.
    """
    cm = _manager()
    if cm is not None:
        cm.set_global(dotted, value)
        return
    path = config_dir() / "config.yaml"
    data = files.load_yaml_for_update(path)
    node = data
    parts = dotted.split(".")
    for part in parts[:-1]:
        if not isinstance(node.get(part), dict):
            node[part] = {}
        node = node[part]
    node[parts[-1]] = value
    files.atomic_write_yaml(data, path)
