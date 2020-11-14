import unittest
from current_cmd_a import CurrentCMD_A
from io import StringIO
import sys


class TestCurrentCmdA(unittest.TestCase):
    def setUp(self):
        self.test_cmd = CurrentCMD_A("Runner Message")

    def test_create_uml_sets_command(self):
        self.test_cmd.do_create_uml("args")
        assert self.test_cmd.current_command == "do_create_uml"

    def test_create_uml_returns_true(self):
        assert self.test_cmd.do_create_uml("args") is True

    def test_help_create_uml(self):
        test_str = 'Generate UML 2 Class Diagrams from JavaScript file(s)'
        stdout = sys.stdout
        s = StringIO()
        sys.stdout = s
        self.test_cmd.help_create_uml()
        sys.stdout = stdout
        s.seek(0)
        assert test_str in s.read()

    def test_deserialize_sets_command(self):
        self.test_cmd.do_deserialize("args")
        assert self.test_cmd.current_command == "do_deserialize"

    def test_deserialize_returns_true(self):
        assert self.test_cmd.do_deserialize("args") is True

    def test_info_prints(self):
        test_str = "JS2UML: Generate UML 2 Class Diagrams"
        stdout = sys.stdout
        s = StringIO()
        sys.stdout = s
        self.test_cmd.do_info(" ")
        sys.stdout = stdout
        s.seek(0)
        assert test_str in s.read()

    def test_quit_prints_to_terminal(self):
        test_str = "Thank you for using JS2UML"
        stdout = sys.stdout
        s = StringIO()
        sys.stdout = s
        self.test_cmd.do_quit(" ")
        sys.stdout = stdout
        s.seek(0)
        assert test_str in s.read()

    def test_quit_sets_command(self):
        self.test_cmd.do_quit("args")
        assert self.test_cmd.current_command == "do_quit"

    def test_quit_returns_true(self):
        assert self.test_cmd.do_quit("args") is True

    def test_switch_cmd_prints_to_terminal(self):
        test_str = "Swapping to Ethan's Command Line"
        stdout = sys.stdout
        s = StringIO()
        sys.stdout = s
        self.test_cmd.do_switch_cmd(" ")
        sys.stdout = stdout
        s.seek(0)
        assert test_str in s.read()

    def test_switch_cmd_sets_command(self):
        self.test_cmd.do_switch_cmd("args")
        assert self.test_cmd.current_command == "do_switch_cmd"

    def test_switch_cmd_returns_true(self):
        assert self.test_cmd.do_switch_cmd("args") is True

    def test_help_prints_to_terminal(self):
        test_str = "JavaScript file / dirs"
        stdout = sys.stdout
        s = StringIO()
        sys.stdout = s
        self.test_cmd.do_help(" ")
        sys.stdout = stdout
        s.seek(0)
        assert test_str in s.read()


if __name__ == '__main__':
    unittest.main(verbosity=2)
