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

    def test_parse_args(self):
        args = ['--flag', '--params=10', 'arg']
        parsed_args = CommandLineArgs.parse_args(args)
        self.assertDictEqual(parsed_args, {
            'flags': {'flag': True},
            'params': {'params': 10},
            'arguments': ['arg']
        })

    def test_get_flag(self):
        fake_arguments = ['--aFlag', '--param=20', '--paramFlag=false']

        args = CommandLineArgs()

        options = args.parse_args(fake_arguments)

        args.flags = options['flags']
        args.params = options['params']
        args.arguments = options['arguments']

        self.assertIs(args.get_flag('aFlag'), True)
        self.assertIs(args.get_flag('paramFlag'), False)
        self.assertIs(args.get_flag('doesNotExists'), False)
        self.assertNotIn('param', args.flags)

    def test_get_param(self):
        fake_arguments = ['--aFlag', '--param=20', '--paramFlag=false', '--stringParam=string', '--empty=']

        args = CommandLineArgs()

        options = args.parse_args(fake_arguments)

        args.flags = options['flags']
        args.params = options['params']
        args.arguments = options['arguments']

        self.assertEqual(args.get_param('param'), 20)
        self.assertEqual(args.get_param('stringParam'), 'string')
        self.assertEqual(args.get_param('empty'), '')
        self.assertIs(args.get_param('notDefined'), None)
        self.assertNotIn('aFlag', args.params)
        self.assertNotIn('paramFlag', args.params)

    def test_get_args(self):
        fake_arguments = ['--flag', 'arg1', '--param=20', 'arg2', 'arg3', '10']

        args = CommandLineArgs()

        options = args.parse_args(fake_arguments)

        args.flags = options['flags']
        args.params = options['params']
        args.arguments = options['arguments']

        self.assertEqual(args.get_argument(0), 'arg1')
        self.assertEqual(args.get_argument(1), 'arg2')
        self.assertEqual(args.get_argument(2), 'arg3')
        self.assertEqual(args.get_argument(3), 10)
        self.assertIs(args.get_argument(4), None)
        self.assertNotIn('flag', args.arguments)
        self.assertNotIn('param', args.arguments)


if __name__ == '__main__':
    unittest.main()
