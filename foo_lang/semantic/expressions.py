# expressions.py
# author: Christophe VG

# Implementations of functions and expressions

from foo_lang.semantic.model import base

class Exp(base):
  def __init__(self):
    raise RuntimeError("Exp is an abstract base class")

# TODO: phase out in favor of typed literals
class LiteralExp(Exp):
  def __init__(self, value):
    self.value = value

  def to_string(self, level):
    return "  " * level + self.value

# NOTE: this does already more than possible ;-)
class BooleanLiteralExp(Exp):
  def __init__(self, value):
    if isinstance(value, bool):
      self.value = value
    elif isinstance(value, str) or isinstance(value, unicode):
      self.value = value == "true"
    elif isinstance(value, int):
      self.value = value != 0
    else:
      raise RuntimeError("Can't convert value to boolean:" + str(value))

  def to_string(self, level):
    return "  " * level + "true" if self.value else "false"

class IntegerLiteralExp(Exp):
  def __init__(self, value):
    self.value = int(value)

  def to_string(self, level):
    return str(self.value)

class FloatLiteralExp(Exp):
  def __init__(self, value):
    self.value = float(value)

  def to_string(self, level):
    return str(self.value)

class AtomLiteralExp(Exp):
  def __init__(self, name):
    self.name = name

  def to_string(self, level):
    return "  " * level + "#" + self.name

class TypeExp(Exp):
  def __init__(self, type):
    self.type = type

  def to_string(self, level):
    return "  " * level + str(self.type)

class ManyTypeExp(TypeExp):
  def __init__(self, type):
    assert isinstance(type, TypeExp)
    self.type = type

  def to_string(self, level):
    return "  " * level + str(self.type) + "*"

class TupleTypeExp(TypeExp):
  def __init__(self, types):
    isinstance(types, TypeExp)
    self.types = types

  def to_string(self, level):
    return "  " * level + \
           "[" + ",".join([str(type) for type in self.types]) + "]"

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

