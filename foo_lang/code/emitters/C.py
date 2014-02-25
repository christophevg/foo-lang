# C.py
# a plain C emitter, based on InstructionVisitor
# author: Christophe VG

from util.support import warn

from foo_lang.code.language import Language

class Emitter(Language):
  def __init__(self):
    self.atoms = [] # list with emitted atoms

  def ext(self): return "c"

  def visit_Identifier(self, id):
    return str(id.name)

  def visit_InstructionList(self, program):
    return "\n".join([ instruction.accept(self)
                       for instruction in program.instructions ])

  def visit_FunctionDecl(self, function):
    params = ", ".join([ param.accept(self) for param in function.parameters ])
    if params == "": params = "void"
    return function.type.accept(self) + " " + function.name.accept(self) + \
           "(" + params + ")" + \
           " " + function.body.accept(self)

  def visit_TypeExp(self, type):
    return type.name.accept(self)

  def visit_UnknownType(self, type):
    return "void"

  def visit_EmptyStmt(self, stmt):
    return "{}"

  def visit_ParameterDecl(self, param):
    return param.type.accept(self) + " " + param.name.accept(self)

  def visit_BlockStmt(self, block):
    if block == None: block = [] # Fixme, happens when testing coverage
    return "{\n" + "\n".join([ (statement.accept(self) + \
                                (";" if statement.ends() else ""))
                                 for statement in block ]) + "\n}"

  def visit_SimpleVariableExp(self, var):
    return var.name.accept(self)

  def visit_ObjectExp(self, obj):
    return obj.name.accept(self)

  def visit_PropertyExp(self, exp):
    """
    Emission strategy: Objects are represented by structs and are passed around
    as pointers. So accessing a property is accessing a struct member after
    dereferencing the pointer.
    """
    return exp.obj.accept(self) + "->" + exp.prop.accept(self)

  def visit_Comment(self, comment):
    if "\n" in str(comment):
      return "/* " + str(comment) + " */"
    else:
      return "// " + str(comment)

  def visit_IncStmt(self, stmt):
    return stmt.operand.accept(self) + "++";

  def visit_DecStmt(self, stmt):
    return stmt.operand.accept(self) + "--";

  def visit_AssignStmt(self, stmt):
    return stmt.operand.accept(self) + " = " + stmt.expression.accept(self)

  def visit_AddStmt(self, stmt):
    return stmt.operand.accept(self) + " += " + stmt.expression.accept(self)

  def visit_SubStmt(self, stmt):
    return stmt.operand.accept(self) + " -= " + stmt.expression.accept(self)

  def visit_AndExp(self, exp):
    return exp.left.accept(self) + " and " + exp.right.accept(self)

  def visit_OrExp(self, exp):
    return exp.left.accept(self) + " or " + exp.right.accept(self)

  def visit_EqualsExp(self, exp):
    return exp.left.accept(self) + " == " + exp.right.accept(self)

  def visit_NotEqualsExp(self, exp):
    return exp.left.accept(self) + " != " + exp.right.accept(self)

  def visit_LTExp(self, exp):
    return exp.left.accept(self) + " < " + exp.right.accept(self)

  def visit_LTEQExp(self, exp):
    return exp.left.accept(self) + " <= " + exp.right.accept(self)

  def visit_GTExp(self, exp):
    return exp.left.accept(self) + " > " + exp.right.accept(self)

  def visit_GTEQExp(self, exp):
    return exp.left.accept(self) + " >= " + exp.right.accept(self)

  def visit_PlusExp(self, exp):
    return exp.left.accept(self) + " + " + exp.right.accept(self)

  def visit_MinusExp(self, exp):
    return exp.left.accept(self) + " - " + exp.right.accept(self)

  def visit_MultExp(self, exp):
    return exp.left.accept(self) + " * " + exp.right.accept(self)

  def visit_DivExp(self, exp):
    return exp.left.accept(self) + " / " + exp.right.accept(self)

  def visit_ModuloExp(self, exp):
    return exp.left.accept(self) + " % " + exp.right.accept(self)

  def visit_NotExp(self, exp):
    return "! " + exp.operand.accept(self)

  def visit_FunctionCallExp(self, call):
    return call.function.accept(self) + \
           "(" + ", ".join([arg.accept(self) for arg in call.arguments])+ ")"

  @warn("MethodCalls are badly supported.")
  def visit_MethodCallExp(self, call):
    return call.obj.accept(self) + "->" + call.method.accept(self) + \
           "(" + ", ".join([arg.accept(self) for arg in call.arguments])+ ")"

  def visit_AtomLiteral(self, atom):
    """
    Emission strategy: replace by unique (sequence) number.
    """
    index = self.atoms.index(atom.name)
    if index:
      return str(index)
    else:
      self.atoms.append(atom.name)
      return str(len(self.atoms)-1)

  def visit_BooleanLiteral(self, boolean):
    return "TRUE" if boolean.value else "FALSE"

  def visit_FloatLiteral(self, literal):
    return str(literal.value)

  def visit_IntegerLiteral(self, literal):
    return str(literal.value)

  @warn("ListLiterals are badly supported.")
  def visit_ListLiteral(self, literal):
    return "{" + [exp.accept(self) for exp in literal.expressions ] + "}"

  @warn("TupleLiterals are badly supported.")
  def visit_TupleLiteral(self, literal):
    return "{" + [exp.accept(self) for exp in literal.expressions ] + "}"

  def visit_WhileDoStmt(self, loop):
    return "while(" + loop.condition.accept(self) + ")" + \
           loop.body.accept(self)

  def visit_RepeatUntilStmt(self, loop):
    return "do " + loop.body.accept(self) + \
           "while(!" + loop.condition.accept(self) + ")"

  def visit_ForStmt(self, loop):
    return "for(" + loop.init.accept(self) + ";" + \
                    loop.check.accept(self)+ ";" + \
                    loop.change.accept(self)+ ") " + \
              loop.body.accept(self)

  def visit_IfStmt(self, stmt):
    return "if(" + stmt.expression.accept(self) + ")" + \
           stmt.true_clause.accept(self) + \
           (" else " + stmt.false_clause.accept(self)) \
             if stmt.false_clause != None else ""

  @warn("Exceptions are badly supported.")
  def visit_RaiseStmt(self, stmt):
    return "printf( \"EXCEPTION: " + stmt.expression.accept(self) + "\");\n" + \
           "exit(-1)"

  def visit_PrintStmt(self, stmt):
    return "printf( \"" + stmt.expression.accept(self) + "\")"

  def visit_ReturnStmt(self, stmt):
    return "return" + (" " + stmt.expression.accept(self)) \
                        if stmt.expression != None else ""
