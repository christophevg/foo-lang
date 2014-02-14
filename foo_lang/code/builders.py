# builders.py
# small builders of code instructions, offering an OO interface to tweak them
# and can be accesses as final a code instructions tree
# author: Christophe VG

import foo_lang.semantic.model as model
from foo_lang.code.instructions import *

class Builder():
  def code(self):
    raise RuntimeError("WARNING: need to implement as_code(self)")

class Module(Builder):
  def __init__(self, sections=["instructions"], builders=[]):

    self.sections = sections
    for section in sections:
      self.__dict__[section] = InstructionList()

    self.builders = builders
    for builder in builders:
      self.__dict__[builder] = None

  def code(self):
    # merge sections into single InstructionList
    code = InstructionList()
    for section in self.sections:
      for instruction in self.__dict__[section]:
        code.append(instruction)
    return code

class EventLoop(Builder):
  def __init__(self):
    self.body = BlockStmt([])
  def code(self):
    return WhileDoStmt(BooleanLiteral(True), self.body)

def Function(name, type=None, params={}, body=None):
  type = UnknownType() if type == None else TypeExp(Identifier(type))
  parameters = [ ParameterDecl(Identifier(name),TypeExp(Identifier(type)))
                   for name, type in params.items() ]
  return FunctionDecl( Identifier(name), type=type, parameters=parameters,
                       body=body)

def Call(name, args=[]):
  arguments = [ Expression(arg) for arg in args]
  return FunctionCallExp(Identifier(name), arguments)

def Variable(name):
  return SimpleVariableExp(Identifier(name))
