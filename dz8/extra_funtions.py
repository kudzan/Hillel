class extra:

    def evaluate_func(node):

        func_map = {
            "log": math.log,
            "exp": math.exp,
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
        }

        def interactive():
        """
        Evaluates expressions given by user in interactive fashion
        """

        print "Please specify expressions to evaluate"
        print "To exit please enter: empty line or word 'quit'"
        print ""

        while True:
            expression = raw_input(">>> ")
            if expression in ["", "quit"]:
                print "Bye"
                break

            try:
                print evaluate(expression)
            except StandardError, err:
                print "Your expression could not be evaluated:", err


    def from_file(filename):
        """
        Runs expressions found in given file
        """

        input_file = file(filename, "r")

        for line in input_file:
            expression = line.strip()
            try:
                print "%s = %s" % (expression, evaluate(expression))
            except StandardError, err:
                print "%s could not be evaluated: %s" % (expression, err)


    def main(argv):
        description = "Program evaluates mathematical expressions."
        epilog = "By default user will be prompted to input expression."
        usage = "usage: %prog [expression | options]"
        parser = OptionParser(description=description,
                              epilog=epilog,
                              usage=usage)

        parser.add_option("-f", "--file", dest="filename",
                          help="Load expressions from file")

        (options, args) = parser.parse_args(argv)

        if len(args) == 2:
            # Evaluate expression from argument
            try:
                print evaluate(args[1])
            except StandardError, err:
                print "Your expression could not be evaluated:", err
                sys.exit(1)

        elif options.filename:
            # Evaluate expressions in batch mode
            try:
                from_file(options.filename)
            except IOError, err:
                print "There was a problem with your file:", err
                sys.exit(1)

        else:
            # Evaluate expressions entered by user
            interactive()

        sys.exit(0)

    if __name__ == "__main__":
        main(sys.argv)
