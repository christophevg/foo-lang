# dumper.py
# a plain text foo syntax-based dumper, based on SemanticVisitor
# author: Christophe VG

from util.check              import isstring
from foo_lang.semantic.model import SemanticVisitor

# Helper decorator for indenting foo-syntax
def indent(method):
  def wrapped(self, obj):
    return "  " * self.indent_level + method(self, obj)
  return wrapped

class Dumper(SemanticVisitor):
  def __init__(self):
    self.indent_level = 0

  def inc_indent(self):
    self.indent_level += 1

  def dec_indent(self):
    self.indent_level -= 1

  def handle_Identifier(self, id):
    return id.name

  @indent
  def handle_Model(self, model):
    string = ""
    for module in model.modules.values():
      string += module.accept(self)
    return string

  @indent
  def handle_Domain(self, domain):
    return domain.__class__.__name__.lower()

  @indent
  def handle_Scope(self, scope):
    return scope.scope

  @indent
  def handle_Module(self, module):
    string = "module " + module.identifier.accept(self) + "\n";

    for constant in module.constants:
      string += constant.accept(self) + "\n"
    
    for function, library in module.externals.items():
      string += "from " + library + " import " + function + "\n"
    
    for extension in module.extensions:
      string += extension.accept(self) + "\n"
    
    for execution in module.executions:
      string += execution.accept(self) + "\n"

    return string

  @indent
  def handle_Constant(self, constant):
    return "const " + constant.identifier.accept(self) \
           + ((" : " + constant.type.accept(self)) if constant.type != None else "") \
           + " = " + constant.value.accept(self)

  @indent
  def handle_Extension(self, extension):
    return "extend " + extension.domain.accept(self) + \
           " with " + extension.extension.accept(self)

  @indent
  def handle_Every(self, execution):
    return "@every(" + execution.interval.accept(self) + ")\n" + \
           "with " + execution.scope.accept(self) + " do " + \
           execution.executed.accept(self).lstrip()

  @indent
  def handle_When(self, execution):
    return execution.timing + " " + execution.scope.accept(self) + " " + \
           execution.event.accept(self) + " do " + \
           execution.executed.accept(self).lstrip()

  @indent
  def handle_FunctionDecl(self, function):
    name = "" if function.name[0:9] == "anonymous" \
              else " " + function.identifier.accept(self)
    string = "function" + name + \
             "(" + ", ".join([ param.accept(self) 
                                   for param in function.parameters]) + ") " + \
               function.body.accept(self).lstrip()
    return string

  def handle_Parameter(self, parameter):
    return parameter.identifier.accept(self)

  # STATEMENTS

  @indent
  def handle_BlockStmt(self, block):
      string = "{";
      if len(block.statements) == 0:
        string += " }"
      else:
        string += "\n"
        self.inc_indent()
        for statement in block.statements:
          string += statement.accept(self) + "\n"
        self.dec_indent()
        string += "  " * self.indent_level + "}"
      return string

  @indent
  def handle_AssignStmt(self, stmt):
    return stmt.variable.accept(self) + " = " + stmt.value.accept(self)

  @indent
  def handle_AddStmt(self, stmt):
    return stmt.variable.accept(self) + " += " + stmt.value.accept(self)
  
  @indent
  def handle_SubStmt(self, stmt):
    return stmt.variable.accept(self) + " -= " + stmt.value.accept(self)

  @indent
  def handle_IncStmt(self, stmt):
    return stmt.variable.accept(self) + "++"

  @indent
  def handle_DecStmt(self, stmt):
    return stmt.variable.accept(self) + "--"

  @indent
  def handle_IfStmt(self, stmt):
    string =  "if( " + stmt.condition.accept(self) + " ) " + \
              stmt.true.accept(self).lstrip()
    if stmt.false != None:
      string += " else " + stmt.false.accept(self).lstrip()
    return string

  @indent
  def handle_CaseStmt(self, stmt):
    string = "case " + stmt.expression.accept(self) + " {\n"
    # a case is a FunctionCallExp
    # a consequences is a Statement
    self.inc_indent();
    for case, consequence in zip(stmt.cases, stmt.consequences):
      string += case.accept(self) + " " + consequence.accept(self).lstrip() + "\n"
    self.dec_indent();
    string += "  " * self.indent_level + "}"
    return string

  @indent
  def handle_ReturnStmt(self, stmt):
    return "return" + \
         ("" if stmt.expression == None else " " + stmt.expression.accept(self))
    
  # EXPRESSIONS
  
  def handle_BooleanLiteralExp(self, exp):
    return "true" if exp.value else "false"

  def handle_IntegerLiteralExp(self, exp):
    return str(exp.value)

  def handle_FloatLiteralExp(self, exp):
    return str(exp.value)
  
  def handle_AtomLiteralExp(self, atom):
    return "#" + atom.identifier.accept(self)

  def handle_ListLiteralExp(self, lst):
    return "[" + ",".join([exp.accept(self) for exp in lst.expressions]) + "]"

  def handle_ObjectLiteralExp(self, obj):
    string = "{";
    if len(obj.properties) != 0: string += "\n"
    self.inc_indent()
    for prop in obj.properties:
      string += prop.accept(self) + "\n"
    self.dec_indent()
    string += "  " * self.indent_level + "}"
    return string

  @indent
  def handle_Property(self, prop):
    return prop.identifier.accept(self) + \
           ((" : " + prop.type.accept(self)) if prop.type != None else "") + \
           " = " + prop.value.accept(self)

  def handle_TypeExp(self, type):
    return type.identifier.accept(self)

  def handle_ManyTypeExp(self, many):
    return many.subtype.accept(self) + "*"
    
  def handle_TupleTypeExp(self, tuple):
    return "[" + ",".join([type.accept(self) for type in tuple.types]) + "]"

  def handle_VariableExp(self, var):
    return var.identifier.accept(self)

  def handle_FunctionExp(self, var):
    return var.identifier.accept(self)

  def handle_ObjectExp(self, var):
    return var.identifier.accept(self)
  
  def handle_PropertyExp(self, prop):
    return prop.obj.accept(self) + "." + prop.identifier.accept(self)

  def handle_UnaryExp(self, exp):
    return exp.operator() + " " + exp.operand.accept(self)

  def handle_BinaryExp(self, exp):
    return "( " + exp.left.accept(self) + " "  + exp.operator() + " " + \
                 exp.right.accept(self) + " )"

  @indent
  def handle_FunctionCallExp(self, exp):
    return exp.function.accept(self) + \
           "(" + ", ".join([arg.accept(self) for arg in exp.arguments]) + ")"

  @indent
  def handle_MethodCallExp(self, exp):
    return exp.object.accept(self) + "." + exp.identifier.accept(self) + \
           "(" + ", ".join([arg.accept(self) for arg in exp.arguments]) + ")"

  def handle_AnythingExp(self, exp):
    return "_"

  def handle_MatchExp(self, exp):
    return (exp.operator if isstring(exp.operator) else exp.operator.accept(self)) + \
           ((" " + exp.operand.accept(self)) if exp.operand != None else "")
