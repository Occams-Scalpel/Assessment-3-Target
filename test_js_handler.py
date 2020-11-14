import unittest
from unittest.mock import patch
from javascript_handler import JavascriptHandler


class TestJSHandler(unittest.TestCase):
    def setUp(self):
        with open("test.js") as test_file:
            test_code = test_file.read()
        self.js_handler_a = JavascriptHandler(test_code, "a")
        self.js_handler_b = JavascriptHandler(test_code, "b")

    def test_js_handler_a(self):
        before_code = self.js_handler_a.js_code
        assert isinstance(before_code, str) is True
        self.js_handler_a.extract_javascript_a()
        after_result = self.js_handler_a.js_code
        assert isinstance(after_result, list) is True

    def test_js_handler_b(self):
        before_code = self.js_handler_b.js_code
        assert isinstance(before_code, str) is True
        self.js_handler_b.extract_javascript_b()
        after_result = self.js_handler_b.js_code
        assert isinstance(after_result, list) is True

    @patch('dot_formatter.DotFormatter.convert_to_dot_a')
    def test_dot_converter_a(self, test_method):
        self.js_handler_a.create_puml()
        self.assertTrue(test_method.called)

    @patch('dot_formatter.DotFormatter.convert_to_dot_b')
    def test_dot_converter_b(self, test_method):
        self.js_handler_b.create_puml()
        self.assertTrue(test_method.called)


if __name__ == '__main__':
    unittest.main(verbosity=2)