import unittest
from current_cmd_b import CurrentCMD_B
from io import StringIO
import sys


class TestCurrentCmdB(unittest.TestCase):
    def setUp(self):
        self.test_cmd = CurrentCMD_B("Runner Message")

    def test_create_uml_sets_command(self):
        self.test_cmd.do_create_uml("args")
        assert self.test_cmd.current_command == "do_create_uml"

    def test_create_uml_returns_true(self):
        assert self.test_cmd.do_create_uml("args") is True

    def test_deserialize_sets_command(self):
        self.test_cmd.do_deserialize("args")
        assert self.test_cmd.current_command == "do_deserialize"

    def test_deserialize_returns_true(self):
        assert self.test_cmd.do_deserialize("args") is True

    def test_info_prints(self):
        test_str = "by Azez Nassar & Ethan Bray in Python3"
        stdout = sys.stdout
        s = StringIO()
        sys.stdout = s
        self.test_cmd.do_info(" ")
        sys.stdout = stdout
        s.seek(0)
        assert test_str in s.read()

    def test_quit_prints_to_terminal(self):
        test_str = "Leaving System"
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
        test_str = "Swapping to Azez's Command Line"
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
        test_str = "description: Prints deserialized cla"
        stdout = sys.stdout
        s = StringIO()
        sys.stdout = s
        self.test_cmd.do_help(" ")
        sys.stdout = stdout
        s.seek(0)
        assert test_str in s.read()

    def test_unrecognized_command(self):
        test_str = "Sorry, the command: blah was not recognized,"
        stdout = sys.stdout
        s = StringIO()
        sys.stdout = s
        self.test_cmd.default(test_str)
        sys.stdout = stdout
        s.seek(0)
        assert "blah" in s.read()


if __name__ == '__main__':
    unittest.main(verbosity=2)
