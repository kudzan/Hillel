"""
calcAST
"""

import ast
import operator
import sys

from optparse import OptionParser

import const
import extra_funtions
import exceptions

extra_funtions.interactive

print(const.const_map['pi'])
def evaluate(node):

    op_map = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.LShift: operator.lshift,
        ast.RShift: operator.rshift,
        ast.BitOr: operator.or_,
        ast.BitAnd: operator.and_,
        ast.BitXor: operator.xor,
    }


    if isinstance(node, (list, tuple)):
        return [evaluate(sub_node) for sub_node in node]

    elif isinstance(node, str):
        return evaluate(ast.parse(node))

    elif isinstance(node, ast.Module):
        values = []
        for body in node.body:
            values.append(evaluate(body))
        if len(values) == 1:
            values = values[0]
        return values

    elif isinstance(node, ast.Expr):
        return evaluate(node.value)

    elif isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        op = node.op
        right = evaluate(node.right)

        try:
            return op_map[type(op)](left, right)
        except KeyError:
            logging.error(ValueError(
                "Operator %s not supported" % op.__class__.__name__))

    elif isinstance(node, ast.Call):
        func_name = node.func.id
        args = [evaluate(arg) for arg in node.args]

        try:
            return func_map[func_name](*args)
        except KeyError:
            logging.error(ValueError("Function %s not supported" % func_name))

    elif isinstance(node, ast.Num):
        return node.n

    elif isinstance(node, ast.Name):
        try:
            return const.const_map.ob
        except KeyError:
            logging.error(ValueError("Constant %s not supported" % node.id))

    logging.error(TypeError("Unsupported operation: %s" % node.__class__.__name__))


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
