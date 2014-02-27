# builders.py
# small builders of code instructions, offering an OO interface to tweak them
# and can be accesses as final a code instructions tree
# author: Christophe VG

from util.visitor import Visitable

import foo_lang.semantic.model as model
import foo_lang.code.instructions as code

from foo_lang.code.transform import Transformer

class Builder(Visitable):
  """
  Base class for Builders. A Builder can be used as a replacement for
  Instructions. Make sure to add the correct InstructionClass to the Builders'
  definition.
  """
  def visited(self): return "Builder"
  def code(self): raise RuntimeError("WARNING: need to implement as_code(self)")

class EventLoop(Builder, code.Stmt):
  def __init__(self):
    self.body = code.BlockStmt()

  def code(self):
    return code.WhileDoStmt(code.BooleanLiteral(True), self.body)

class StructuredType(Builder, code.Stmt):
  def __init__(self, name):
    self.name       = name
    self.properties = []

  def append(self, name, type):
    if not isinstance(name, code.Identifier):
      name = Transformer(name).transform()
    if not isinstance(type, code.TypeExp):
      type = Transformer(type).transform()
    self.properties.append(code.PropertyDecl(name, type))

  def apply(self, obj):
    for prop in obj.properties:
      self.append(prop.identifier, prop.type)

  def code(self):
    return code.StructuredType(code.Identifier(self.name), self.properties)

# basic instruction builder functions

def Function(name, type=None, params={}, body=None):
  type = code.UnknownType() if type == None else code.TypeExp(code.Identifier(type))
  parameters = [ code.ParameterDecl(code.Identifier(name), 
                                    code.TypeExp(code.Identifier(type)))
                   for name, type in params.items() ]
  return code.FunctionDecl( code.Identifier(name), type=type, parameters=parameters,
                            body=body)

def Call(name, args=[]):
  arguments = [ Expression(arg) for arg in args]
  return code.FunctionCallExp(code.Identifier(name), arguments)

# def Variable(name):
#   return code.SimpleVariableExp(Identifier(name))
