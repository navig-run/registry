"""
hello-app/commands/__init__.py — command registry for hello-app pack.
"""
from .hello import handle as hello_handle
from .echo import handle as echo_handle

COMMANDS = {
    "hello": hello_handle,
    "echo": echo_handle,
}
