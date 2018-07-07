import sys


class CommandLineArgs:
    # store user input data
    flags = {}
    params = {}
    arguments = []

    # store command related data
    commands = {}
    method_args = {}

    def __init__(self):
        """
        get and set command line options
        """

        options = self.parse_args(sys.argv[1:])

        self.flags = options['flags']
        self.params = options['params']
        self.arguments = options['arguments']

    def __str__(self):
        """
        transfer data to string

        Return:
            str: transferred information
        """

        return str({
            'flags': self.flags,
            'params': self.params,
            'arguments': self.arguments,
        })

    def handle(self):
        """
        handle command line input and execute the corresponding command
        """

        # get identifier
        identifier = self.get_argument(0)

        # execute if identifier is been called
        if identifier in self.commands:
            return self.commands[identifier](*self.method_args[identifier], command=self)

        return None

    def add_command(self, identifier, method, args=None):
        """
        add a command

        Args:
            identifier  (str)   : the identifier of the command; execute command when args has the identifier
            method      (method): the method when trigger the command; it has a default argument command which is the
                                  current CommandLineArgs object
            args        (list)  : other arguments for the method; these arguments are fixed after specifying the command
        """

        # check if has extra args
        if args is None:
            args = []

        # set command method
        self.commands[identifier] = method

        # set command extra args
        self.method_args[identifier] = args

    def get_flag(self, flag):
        """
        get flag from current object

        Args:
            flag (str): the flag that is going to be retrieved

        Returns:
            bool: the flag value; if flag not exists, return false
        """

        if flag in self.flags:
            return self.flags[flag]
        else:
            return False

    def get_param(self, param):
        """
        get parameter from current object

        Args:
            param (str): the param that is going to be retrieved

        Returns:
            Union[int, str]: the param value; if param not exists, return none
        """

        if param in self.params:
            return self.params[param]
        else:
            return None

    def get_argument(self, index):
        """
        get argument from current object

        Args:
            index (int): the index of argument that is going to be retrieved

        Returns:
            Union[int, str]: the argument value; if argument not exists, return none
        """

        try:
            return self.arguments[index]
        except IndexError:
            return None

    @staticmethod
    def parse_args(args):
        """
        parse a list of arguments and set them into corresponding category

        Args:
            args (list): argument list

        Returns:
            dict: a dict of options having keys
                - flags     (dict): the flag and its value
                - params    (dict): the parameter and its value
                - arguments (list): ordered arguments
        """

        # init options dict
        options = {
            'flags': {},
            'params': {},
            'arguments': [],
        }

        # loop through arguments
        for arg in args:
            # if is option
            if arg[:2] == '--':
                # get separator position
                separator = arg.find('=')

                # get value of the command
                value = CommandLineArgs.auto_convert(arg[separator + 1:])

                # if is flag usage | e.g. --some_true_val
                if separator == -1:
                    options['flags'][arg[2:]] = True

                elif type(value) is bool:
                    options['flags'][arg[2:separator]] = value

                # if is params usage | e.g. --some_param=20
                else:
                    options['params'][arg[2:separator]] = value

            # if is ordered argument | e.g. some
            else:
                options['arguments'].append(CommandLineArgs.auto_convert(arg))

        return options

    @staticmethod
    def boolify(string):
        """
        convert string to boolean type

        Args:
            string (str): the value needs to be check if is boolean type

        Returns:
            bool: if the input is boolean type string, return the value otherwise raise error
        """

        if string == 'True' or string == 'true':
            return True

        if string == 'False' or string == 'false':
            return False

        raise ValueError("wrong type")

    @staticmethod
    def auto_convert(string):
        """
        convert string to corresponding type (bool, int, float, string)

        Args:
            string (str): the string that needs to be check the type

        Returns:
            bool
            int
            float
            str
        """

        for fn in (CommandLineArgs.boolify, int, float):
            try:
                return fn(string)
            except ValueError:
                pass

        return string
