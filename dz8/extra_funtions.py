def interactive():

    print ("Please specify expressions to evaluate")
    print ("To exit please enter: empty line or word 'quit'")
    print ("")

    while True:
        expression = input(">>> ")
        if expression in ["", "quit"]:
            print ("Bye")
            break

        try:
            print (evaluate(expression))
        except SyntaxError as err:
            print ("Your expression could not be evaluated:", err)


def from_file(filename):
    """
    Runs expressions found in given file
    """

    input_file = file(filename, "r")

    for line in input_file:
        expression = line.strip()
        try:
            print ("%s = %s" % (expression, evaluate(expression)))
        except StandardError as err:
            print ("%s could not be evaluated: %s" % (expression, err))


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
        try:
            print (evaluate(args[1]))
        except StandardError as err:
            logging.error(print ("Your expression could not be evaluated:", err))
            sys.exit(1)

    elif options.filename:
        try:
            from_file(options.filename)
        except IOError as err:
            logging.error(print ("There was a problem with your file:", err))
            sys.exit(1)

    else:
        interactive()

    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)
