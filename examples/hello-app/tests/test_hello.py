"""
tests/test_hello.py — hello-app pack unit tests.
"""
import unittest
import sys
import pathlib

# Allow importing the pack without installing
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from commands.hello import handle as hello
from commands.echo import handle as echo


class TestHelloCommand(unittest.TestCase):
    def test_default_greeting(self):
        result = hello({})
        self.assertEqual(result["status"], "ok")
        self.assertIn("World", result["data"]["message"])

    def test_named_greeting(self):
        result = hello({"name": "Alice"})
        self.assertEqual(result["status"], "ok")
        self.assertIn("Alice", result["data"]["message"])

    def test_custom_greeting_via_ctx(self):
        ctx = {"config": {"greeting": "Hi"}}
        result = hello({"name": "Bob"}, ctx=ctx)
        self.assertEqual(result["data"]["message"], "Hi, Bob!")


class TestEchoCommand(unittest.TestCase):
    def test_echo_text(self):
        result = echo({"text": "ping"})
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["data"]["echo"], "ping")

    def test_echo_missing_text(self):
        result = echo({})
        self.assertEqual(result["status"], "error")

    def test_echo_empty_string(self):
        result = echo({"text": ""})
        self.assertEqual(result["status"], "error")


if __name__ == "__main__":
    unittest.main()
