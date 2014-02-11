# C.py
# a plain C emitter, based on InstructionVisitor
# author: Christophe VG

from foo_lang.code.instructions import InstructionVisitor

class Emitter(InstructionVisitor):
  
  def handle_Program(self, program):
    return "\n".join([ instruction.accept(self)
                       for instruction in program.instructions ])

  def handle_FunctionDecl(self, function):
    return function.type.accept(self) + " " + function.name + \
           "(" + ", ".join([ param.accept(self)
                             for param in function.parameters ]) + ")" + \
           " " + function.body.accept(self)
  
  def handle_TypeExp(self, type):
    return "void" if type.name == None else type.name

  def handle_EmptyStmt(self, stmt):
    return "{}"

  def handle_ParameterDecl(self, param):
    return param.type.accept(self) + " " + str(param.name)

  def handle_BlockStmt(self, block):
    return "{" + "\n".join([ (statement.accept(self) + ";")
                             for statement in block.statements ]) + "}"

  def handle_IncStmt(self, stmt):
    return stmt.operand.accept(self) + "++";

  def handle_SimpleVariableExp(self, var):
    return str(var.name)

  def handle_Comment(self, comment):
    if "\n" in str(comment):
      return "/* " + str(comment) + " */"
