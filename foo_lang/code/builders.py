# builders.py
# small builders of code instructions, offering an OO interface to tweak them
# and can be accesses as final a code instructions tree
# author: Christophe VG

from foo_lang.code.instructions import *

class Builder():
  def code(self):
    raise RuntimeError("WARNING: need to implement as_code(self)")

class MainProgram():
  def __init__(self, arguments=None):
    self.function = FunctionDecl(Identifier("main"))
  def code(self):
    return InstructionList([Comment("starting point"), self.function])

def Variable(name):
  return SimpleVariableExp(Identifier(name))
