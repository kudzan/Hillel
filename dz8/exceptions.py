class exceptions:

    def evaluate_exceptions(node):

        try:
                    return op_map[type(op)](left, right)
                except KeyError:
                    raise ValueError(
                        "Operator %s not supported" % op.__class__.__name__)

            elif isinstance(node, ast.Call):
                func_name = node.func.id
                args = [evaluate(arg) for arg in node.args]

                try:
                    return func_map[func_name](*args)
                except KeyError:
                    raise ValueError("Function %s not supported" % func_name)

            elif isinstance(node, ast.Num):
                return node.n

            elif isinstance(node, ast.Name):
                try:
                    return const_map[node.id]
                except KeyError:
                    raise ValueError("Constant %s not supported" % node.id)

            raise TypeError("Unsupported operation: %s" % node.__class__.__name__)
