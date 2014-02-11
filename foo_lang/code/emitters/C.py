# C.py
# a plain C emitter, based on InstructionVisitor
# author: Christophe VG

from util.support import warn

from foo_lang.code.instructions import InstructionVisitor

class Emitter(InstructionVisitor):
  def __init__(self):
    self.atoms = [] # list with emitted atoms

  def handle_Identifier(self, id):
    return str(id.name)

  def handle_Program(self, program):
    return "\n".join([ instruction.accept(self)
                       for instruction in program.instructions ])

  def handle_FunctionDecl(self, function):
    return function.type.accept(self) + " " + function.name.accept(self) + \
           "(" + ", ".join([ param.accept(self)
                             for param in function.parameters ]) + ")" + \
           " " + function.body.accept(self)

  def handle_TypeExp(self, type):
    return "void" if type.name == None else type.name.accept(self)

  def handle_EmptyStmt(self, stmt):
    return "{}"

  def handle_ParameterDecl(self, param):
    return param.type.accept(self) + " " + param.name.accept(self)

  def handle_BlockStmt(self, block):
    return "{" + "\n".join([ (statement.accept(self) + ";")
                             for statement in block.statements ]) + "}"

  def handle_SimpleVariableExp(self, var):
    return var.name.accept(self)

  def handle_ObjectExp(self, obj):
    return obj.name.accept(self)

  def handle_PropertyExp(self, exp):
    """
    Emission strategy: Objects are represented by structs and are passed around
    as pointers. So accessing a property is accessing a struct member after
    dereferencing the pointer.
    """
    return exp.obj.accept(self) + "->" + exp.prop.accept(self)

  def handle_Comment(self, comment):
    if "\n" in str(comment):
      return "/* " + str(comment) + " */"
    else:
      return "// " + str(comment)

  def handle_IncStmt(self, stmt):
    return stmt.operand.accept(self) + "++";

  def handle_DecStmt(self, stmt):
    return stmt.operand.accept(self) + "--";

  def handle_AssignStmt(self, stmt):
    return stmt.operand.accept(self) + " = " + stmt.expression.accept(self)

  def handle_AddStmt(self, stmt):
    return stmt.operand.accept(self) + " += " + stmt.expression.accept(self)

  def handle_SubStmt(self, stmt):
    return stmt.operand.accept(self) + " -= " + stmt.expression.accept(self)

  def handle_AndExp(self, exp):
    return exp.left.accept(self) + " and " + exp.right.accept(self)

  def handle_OrExp(self, exp):
    return exp.left.accept(self) + " or " + exp.right.accept(self)

  def handle_EqualsExp(self, exp):
    return exp.left.accept(self) + " == " + exp.right.accept(self)

  def handle_NotEqualsExp(self, exp):
    return exp.left.accept(self) + " != " + exp.right.accept(self)

  def handle_LTExp(self, exp):
    return exp.left.accept(self) + " < " + exp.right.accept(self)

  def handle_LTEQExp(self, exp):
    return exp.left.accept(self) + " <= " + exp.right.accept(self)

  def handle_GTExp(self, exp):
    return exp.left.accept(self) + " > " + exp.right.accept(self)

  def handle_GTEQExp(self, exp):
    return exp.left.accept(self) + " >= " + exp.right.accept(self)

  def handle_PlusExp(self, exp):
    return exp.left.accept(self) + " + " + exp.right.accept(self)

  def handle_MinusExp(self, exp):
    return exp.left.accept(self) + " - " + exp.right.accept(self)

  def handle_MultExp(self, exp):
    return exp.left.accept(self) + " * " + exp.right.accept(self)

  def handle_DivExp(self, exp):
    return exp.left.accept(self) + " / " + exp.right.accept(self)

  def handle_ModuloExp(self, exp):
    return exp.left.accept(self) + " % " + exp.right.accept(self)

  def handle_NotExp(self, exp):
    return "! " + exp.operand.accept(self)

  def handle_FunctionCallExp(self, call):
    return call.function.accept(self) + \
           "(" + ", ".join([arg.accept(self) for arg in call.arguments])+ ")"

  @warn("MethodCalls are badly supported.")
  def handle_MethodCallExp(self, call):
    return call.obj.accept(self) + "->" + call.method.accept(self) + \
           "(" + ", ".join([arg.accept(self) for arg in call.arguments])+ ")"

  def handle_AtomLiteral(self, atom):
    """
    Emission strategy: replace by unique (sequence) number.
    """
    index = self.atoms.index(atom.name)
    if index:
      return str(index)
    else:
      self.atoms.append(atom.name)
      return str(len(self.atoms)-1)

  def handle_BooleanLiteral(self, boolean):
    return "TRUE" if boolean.value else "FALSE"

  def handle_FloatLiteral(self, literal):
    return str(literal.value)

  def handle_IntegerLiteral(self, literal):
    return str(literal.value)

  @warn("ListLiterals are badly supported.")
  def handle_ListLiteral(self, literal):
    return "{" + [exp.accept(self) for exp in literal.expressions ] + "}"

  @warn("TupleLiterals are badly supported.")
  def handle_TupleLiteral(self, literal):
    return "{" + [exp.accept(self) for exp in literal.expressions ] + "}"

  def handle_WhileDoStmt(self, loop):
    return "while(" + loop.condition.accept(self) + ")" + \
           loop.body.accept(self)

  def handle_RepeatUntilStmt(self, loop):
    return "do " + loop.body.accept(self) + \
           "while(!" + loop.condition.accept(self) + ")"

  def handle_ForStmt(self, loop):
    return "for(" + loop.init.accept(self) + ";" + \
                    loop.check.accept(self)+ ";" + \
                    loop.change.accept(self)+ ") " + \
              loop.body.accept(self)

  def handle_IfStmt(self, stmt):
    return "if(" + stmt.expression.accept(self) + ")" + \
           stmt.true_clause.accept(self) + \
           (" else " + stmt.false_clause.accept(self)) \
             if stmt.false_clause != None else ""

  @warn("Exceptions are badly supported.")
  def handle_RaiseStmt(self, stmt):
    return "printf( \"EXCEPTION: " + stmt.expression.accept(self) + "\");\n" + \
           "exit(-1)"

  def handle_PrintStmt(self, stmt):
    return "printf( \"" + stmt.expression.accept(self) + "\")"

  def handle_ReturnStmt(self, stmt):
    return "return" + (" " + stmt.expression.accept(self)) \
                        if stmt.expression != None else ""
