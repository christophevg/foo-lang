# builders.py
# small builders of code instructions, offering an OO interface to tweak them
# and can be accesses as final a code instructions tree
# author: Christophe VG

import foo_lang.semantic.model as model
import foo_lang.code.instructions as code

class Builder():
  def code(self):
    raise RuntimeError("WARNING: need to implement as_code(self)")

class EventLoop(Builder):
  def __init__(self):
    self.body = code.BlockStmt([])
  def code(self):
    return code.WhileDoStmt(code.BooleanLiteral(True), self.body)

def Function(name, type=None, params={}, body=None):
  type = code.UnknownType() if type == None else code.TypeExp(code.Identifier(type))
  parameters = [ code.ParameterDecl(code.Identifier(name), 
                                    code.TypeExp(code.Identifier(type)))
                   for name, type in params.items() ]
  return code.FunctionDecl( code.Identifier(name), type=type, parameters=parameters,
                            body=body)

def Import(name):
  return code.Import(name)

def Call(name, args=[]):
  arguments = [ Expression(arg) for arg in args]
  return code.FunctionCallExp(code.Identifier(name), arguments)

def Variable(name):
  return code.SimpleVariableExp(Identifier(name))
