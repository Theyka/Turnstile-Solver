import argparse
import inspect
import sys
import unittest
from unittest.mock import patch

from api_solver import create_app, parse_args, parse_bool, TurnstileAPIServer
from main import TurnstileTester


class ParseBoolTests(unittest.TestCase):
    def test_true_values(self):
        for value in ("1", "true", "TRUE", "yes", "y", "on", True):
            self.assertTrue(parse_bool(value))

    def test_false_values(self):
        for value in ("0", "false", "FALSE", "no", "n", "off", False):
            self.assertFalse(parse_bool(value))

    def test_invalid_value(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_bool("maybe")


class ParseArgsTests(unittest.TestCase):
    def test_headless_false_string_stays_false(self):
        with patch.object(sys, "argv", ["api_solver.py", "--headless", "False", "--debug", "False", "--proxy", "False"]):
            args = parse_args()
        self.assertFalse(args.headless)
        self.assertFalse(args.debug)
        self.assertFalse(args.proxy)

    def test_bare_boolean_flags_enable_options(self):
        with patch.object(sys, "argv", ["api_solver.py", "--headless", "--debug", "--proxy"]):
            args = parse_args()
        self.assertTrue(args.headless)
        self.assertTrue(args.debug)
        self.assertTrue(args.proxy)

    def test_defaults_are_false(self):
        with patch.object(sys, "argv", ["api_solver.py"]):
            args = parse_args()
        self.assertFalse(args.headless)
        self.assertFalse(args.debug)
        self.assertFalse(args.proxy)


class CreateAppTests(unittest.TestCase):
    def test_proxy_support_is_optional(self):
        signature = inspect.signature(create_app)
        self.assertIn("proxy_support", signature.parameters)
        self.assertFalse(signature.parameters["proxy_support"].default)

    def test_main_style_call_without_proxy_support_works(self):
        app = create_app(
            debug=False,
            headless=False,
            useragent=None,
            browser_type="chromium",
            thread=1,
        )
        self.assertIsNotNone(app)

    def test_tester_passes_proxy_support(self):
        source = inspect.getsource(TurnstileTester.run_api_server)
        self.assertIn("proxy_support=proxy_support", source)


class ResultContractTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.server = TurnstileAPIServer(
            headless=False,
            useragent=None,
            debug=False,
            browser_type="chromium",
            thread=1,
            proxy_support=False,
        )

    async def test_pending_result_is_json(self):
        self.server.results["pending-id"] = "CAPTCHA_NOT_READY"
        payload, status = await self._result_payload("pending-id")
        self.assertEqual(status, 200)
        self.assertEqual(payload, {"status": "pending", "value": "CAPTCHA_NOT_READY"})

    async def test_failed_result_returns_422(self):
        self.server.results["fail-id"] = {"value": "CAPTCHA_FAIL", "elapsed_time": 1.23}
        payload, status = await self._result_payload("fail-id")
        self.assertEqual(status, 422)
        self.assertEqual(payload["status"], "error")
        self.assertEqual(payload["value"], "CAPTCHA_FAIL")

    async def test_successful_result_includes_status(self):
        self.server.results["ok-id"] = {"value": "XXXX.DUMMY.TOKEN.XXXX", "elapsed_time": 3.69}
        payload, status = await self._result_payload("ok-id")
        self.assertEqual(status, 200)
        self.assertEqual(payload["status"], "success")
        self.assertEqual(payload["value"], "XXXX.DUMMY.TOKEN.XXXX")

    async def _result_payload(self, task_id):
        async with self.server.app.test_request_context(f"/result?id={task_id}"):
            response, status = await self.server.get_result()
        payload = await response.get_json()
        return payload, status


if __name__ == "__main__":
    unittest.main()
