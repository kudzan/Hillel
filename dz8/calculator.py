import ast
import math
import operator
import sys

from optparse import OptionParser

def evaluate(node):
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
