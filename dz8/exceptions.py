import logging
#import operator os op
#from some module import op

class OperatorNotSupported(Exception):
    def __init__(self, op):
        self.message = "Operator %s not supported" % op.__class__.__name__

class FunctionNotSupported(Exception):
    def __init__(self, op):
        self.message = "Function %s not supported" % op.__class__.__name__

class ConstantNotSupported(Exception):
    def __init__(self, op):
        self.message = "Constant %s not supported" % op.__class__.__name__

class UnsupportedOperation(Exception):
    def __init__(self, op):
        self.message = "Unsupported operation: %s" % op.__class__.__name__
