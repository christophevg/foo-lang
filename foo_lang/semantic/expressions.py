# expressions.py
# author: Christophe VG

# Implementations of functions and expressions

from foo_lang.semantic.model import base

class Exp(base):
  def __init__(self):
    raise RuntimeError("Exp is an abstract base class")

class LiteralExp(Exp):
  def __init__(self, value):
    self.value = value

  def to_string(self, level):
    return "  " * level + self.value

class ListLiteral(Exp):
  def __init__(self, expressions):
    self.expressions = expressions

  def to_string(self, level):
    return "  " * level + \
           "[" + ",".join([str(exp) for exp in self.expressions]) + "]"

class VariableExp(Exp):
  def __init__(self, name):
    self.name = name

  def to_string(self, level):
    return "  " * level + self.name

class PropertyExp(Exp):
  def __init__(self, object, property):
    self.object   = object
    self.property = property

  def to_string(self, level):
    return "  " * level + str(self.object) + "." + str(self.property)

class AtomExp(Exp):
  def __init__(self, name):
    self.name = name

  def to_string(self, level):
    return "  " * level + "#" + self.name

class UnaryExp(Exp):
  def __init__(self, operand):
    self.operand = operand

  def operator(self):
    raise RuntimeError("WARNING: need to implement operator(self))")

  def to_string(self, level):
    return "  " * level + self.operator() + " " + str(self.operand)

class BinaryExp(Exp):
  def __init__(self, left, right):
    self.left  = left
    self.right = right

  def operator(self):
    raise RuntimeError("WARNING: need to implement operator(self))")

  def to_string(self, level):
    return "  " * level + \
           " ".join([ "(", str(self.left), self.operator(), str(self.right), ")"])

class AndExp(BinaryExp):
  def operator(self): return "and"

class OrExp(BinaryExp):
  def operator(self): return "or"

class EqualsExp(BinaryExp):
  def operator(self): return "=="

class NotEqualsExp(BinaryExp):
  def operator(self): return "!="

class LTExp(BinaryExp):
  def operator(self): return "<"

class LTEQExp(BinaryExp):
  def operator(self): return "<="

class GTExp(BinaryExp):
  def operator(self): return ">"

class GTEQExp(BinaryExp):
  def operator(self): return ">="

class PlusExp(BinaryExp):
  def operator(self): return "+"

class MinusExp(BinaryExp):
  def operator(self): return "-"

class MultExp(BinaryExp):
  def operator(self): return "*"

class DivExp(BinaryExp):
  def operator(self): return "/"

class ModuloExp(BinaryExp):
  def operator(self): return "%"

class NotExp(UnaryExp):
  def operator(self): return "!"

class FunctionCallExp(Exp):
  def __init__(self, function, arguments=[]):
    self.function  = function
    self.arguments = arguments
  
  def to_string(self, level):
    return "  " * level + \
           str(self.function) + "(" + ", ".join([str(arg) for arg in self.arguments]) + ")"

class MethodCallExp(Exp):
  def __init__(self, object, method, arguments):
    self.object    = object
    self.method    = method
    self.arguments = arguments
  
  def to_string(self, level):
    return "  " * level + \
           str(self.object) + "." + str(self.method) + \
           "(" + ", ".join([str(arg) for arg in self.arguments]) + ")"
