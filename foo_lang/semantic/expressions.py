# expressions.py
# author: Christophe VG

# Implementations of functions and expressions

from foo_lang.semantic.model import base

class Expression(base):
  def __init__(self):
    raise RuntimeError("Expression is an abstract base class")

class LiteralExpression(Expression):
  def __init__(self, value):
    self.value = value

  def to_string(self, level):
    return "  " * level + self.value

class ListLiteral(Expression):
  def __init__(self, expressions):
    self.expressions = expressions

  def to_string(self, level):
    return "  " * level + \
           "[" + ",".join([str(exp) for exp in self.expressions]) + "]"

class VariableExpression(Expression):
  def __init__(self, name):
    self.name = name

  def to_string(self, level):
    return "  " * level + self.name

class PropertyExpression(Expression):
  def __init__(self, object, property):
    self.object   = object
    self.property = property

  def to_string(self, level):
    return "  " * level + str(self.object) + "." + str(self.property)

class AtomExpression(Expression):
  def __init__(self, name):
    self.name = name

  def to_string(self, level):
    return "  " * level + "#" + self.name

class UnaryExpression(Expression):
  def __init__(self, operand):
    self.operand = operand

  def operator(self):
    raise RuntimeError("WARNING: need to implement operator(self))")

  def to_string(self, level):
    return "  " * level + self.operator() + " " + str(self.operand)

class BinaryExpression(Expression):
  def __init__(self, left, right):
    self.left  = left
    self.right = right

  def operator(self):
    raise RuntimeError("WARNING: need to implement operator(self))")

  def to_string(self, level):
    return "  " * level + \
           " ".join([ "(", str(self.left), self.operator(), str(self.right), ")"])

class AndExpression(BinaryExpression):
  def operator(self): return "and"

class OrExpression(BinaryExpression):
  def operator(self): return "or"

class EqualsExpression(BinaryExpression):
  def operator(self): return "=="

class NotEqualsExpression(BinaryExpression):
  def operator(self): return "!="

class LTExpression(BinaryExpression):
  def operator(self): return "<"

class LTEQExpression(BinaryExpression):
  def operator(self): return "<="

class GTExpression(BinaryExpression):
  def operator(self): return ">"

class GTEQExpression(BinaryExpression):
  def operator(self): return ">="

class PlusExpression(BinaryExpression):
  def operator(self): return "+"

class MinusExpression(BinaryExpression):
  def operator(self): return "-"

class MultExpression(BinaryExpression):
  def operator(self): return "*"

class DivExpression(BinaryExpression):
  def operator(self): return "/"

class ModuloExpression(BinaryExpression):
  def operator(self): return "%"

class NotExpression(UnaryExpression):
  def operator(self): return "!"

class FunctionCallExpression(Expression):
  def __init__(self, function, arguments=[]):
    self.function  = function
    self.arguments = arguments
  
  def to_string(self, level):
    return "  " * level + \
           str(self.function) + "(" + ", ".join([str(arg) for arg in self.arguments]) + ")"

class MethodCallExpression(Expression):
  def __init__(self, object, method, arguments):
    self.object    = object
    self.method    = method
    self.arguments = arguments
  
  def to_string(self, level):
    return "  " * level + \
           str(self.object) + "." + str(self.method) + \
           "(" + ", ".join([str(arg) for arg in self.arguments]) + ")"

