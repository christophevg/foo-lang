# C.py
# a plain C emitter, based on InstructionVisitor
# author: Christophe VG

from foo_lang.code.instructions import InstructionVisitor

class Emitter(InstructionVisitor):
  
  def handle_FunctionDecl(self, function):
    return function.type.accept(self) + " " + function.name + \
           "(" + ", ".join([param.accept(self) for param in function.parameters]) + ")" + \
           " " + function.body.accept(self)
  
  def handle_TypeExp(self, type):
    return "void" if type.name == None else type.name
  
  def handle_EmptyStmt(self, stmt):
    return "{}"
