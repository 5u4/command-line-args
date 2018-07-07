import unittest
from context import CommandLineArgs


class CommandLineArgsTest(unittest.TestCase):
    def test_auto_convert_int(self):
        result = CommandLineArgs.auto_convert("10")
        self.assertIs(type(result), int)

        result = CommandLineArgs.auto_convert("0")
        self.assertIs(type(result), int)

        result = CommandLineArgs.auto_convert("-10")
        self.assertIs(type(result), int)

    def test_auto_convert_float(self):
        result = CommandLineArgs.auto_convert("10.15")
        self.assertIs(type(result), float)

        result = CommandLineArgs.auto_convert("-10.15")
        self.assertIs(type(result), float)

        result = CommandLineArgs.auto_convert("0.00")
        self.assertIs(type(result), float)

        result = CommandLineArgs.auto_convert("0.15")
        self.assertIs(type(result), float)

    def test_auto_convert_bool(self):
        result = CommandLineArgs.auto_convert("true")
        self.assertIs(type(result), bool)

        result = CommandLineArgs.auto_convert("True")
        self.assertIs(type(result), bool)

        result = CommandLineArgs.auto_convert("false")
        self.assertIs(type(result), bool)

        result = CommandLineArgs.auto_convert("False")
        self.assertIs(type(result), bool)

    def test_auto_convert_string(self):
        result = CommandLineArgs.auto_convert("Some random string")
        self.assertIs(type(result), str)

        result = CommandLineArgs.auto_convert("str100")
        self.assertIs(type(result), str)

        result = CommandLineArgs.auto_convert("10a")
        self.assertIs(type(result), str)

        result = CommandLineArgs.auto_convert("10f")
        self.assertIs(type(result), str)


if __name__ == '__main__':
    unittest.main()
