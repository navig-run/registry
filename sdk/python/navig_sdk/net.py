"""Bind a local HTTP server without tripping over OS-reserved port ranges.

Windows (Hyper-V / WSL / Docker) reserves whole blocks of TCP ports at boot, and binding one
fails with ``WinError 10013`` — which reads like a firewall problem but means "that number is
spoken for". The blocks move between reboots, so a hard-coded default port is a coin flip.

So: try the familiar default, and if the OS refuses it, let the OS pick a free port. A port
the *user* asked for is never silently swapped (that would send them to the wrong place); it
raises :class:`PortBindError` instead.

Inside navig this is navig's own ``navig.http_bind`` and :class:`PortBindError` IS navig's
class, so an ``except`` written against this module catches what navig raises.
"""

from __future__ import annotations

from http.server import ThreadingHTTPServer
from typing import Any

__all__ = ["PortBindError", "bind_http_server"]

try:
    from navig.http_bind import PortBindError  # noqa: PLC0415
except ImportError:

    class PortBindError(RuntimeError):  # type: ignore[no-redef]
        """An explicitly requested port could not be bound (in use, reserved, or denied)."""


def bind_http_server(
    handler: Any,
    port: int | None = None,
    *,
    preferred: int = 8099,
    host: str = "127.0.0.1",
    server_cls: type | None = None,
) -> tuple[Any, int]:
    """Return ``(server, bound_port)``: *preferred* or an OS-picked port, or exactly *port*."""
    try:
        from navig.http_bind import bind_http_server as _impl  # noqa: PLC0415
    except ImportError:
        return _bind_fallback(handler, port, preferred=preferred, host=host, server_cls=server_cls)
    return _impl(handler, port, preferred=preferred, host=host, server_cls=server_cls)


def _bind_fallback(
    handler: Any,
    port: int | None,
    *,
    preferred: int,
    host: str,
    server_cls: type | None,
) -> tuple[Any, int]:
    server_cls = server_cls or ThreadingHTTPServer
    candidates = [port] if port is not None else [preferred, 0]
    last: OSError | None = None
    for candidate in candidates:
        try:
            srv = server_cls((host, candidate), handler)
        except OSError as exc:  # busy, or inside a reserved range (Windows 10013)
            last = exc
            continue
        return srv, srv.server_address[1]
    reason = getattr(last, "strerror", None) or last
    raise PortBindError(
        f"cannot bind {host}:{port} ({reason}). The port is in use or reserved by the "
        f"OS — try another, e.g. --port {(port or 0) + 1}, or omit --port to auto-pick."
    ) from last
