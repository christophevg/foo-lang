# dumper.py
# a plain text foo syntax-based dumper, based on SemanticVisitor
# author: Christophe VG

import inspect

from util.support            import print_stderr
from util.check              import isstring
from util.dot                import DotBuilder

from foo_lang.semantic.model import SemanticVisitorBase, UnknownType, TypeExp

# Helper decorator for indenting foo-syntax
def indent(method):
  def wrapped(self, obj):
    return "  " * self.indent_level + method(self, obj)
  return wrapped

class Dumper(SemanticVisitorBase):
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
      
    for function in module.functions:
      # we only want to handle non-anonymous function declarations here
      # because anonymous declarations are declared in their specific scope
      # TODO: do this in a cleaner way (AnonFunctionDecl?)
      if function.name[0:9] != "anonymous":
        string += function.accept(self)

    return string

  @indent
  def handle_Constant(self, constant):
    return "const " + constant.identifier.accept(self) \
           + ((" : " + constant.type.accept(self)) \
             if not isinstance(constant.type, UnknownType) else "") \
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
           ((" : " + prop.type.accept(self)) \
             if not isinstance(prop.type, UnknownType) else "") + \
           " = " + prop.value.accept(self)

  def handle_UnknownType(self, type): return "__unknown__"

  def handle_VoidType   (self, type): return ""
  def handle_BooleanType(self, type): return "boolean"
  def handle_ByteType   (self, type): return "byte"
  def handle_IntegerType(self, type): return "integer"
  def handle_FloatType  (self, type): return "float"
  def handle_ObjectType (self, type): return type.name

  def handle_TimestampType (self, type): return "timestamp"
  
  def handle_ManyType(self, many):
    return many.subtype.accept(self) + "*"
    
  def handle_TupleType(self, tuple):
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

# DOT DUMPER
#
# Generic Dumper using the internal __dict__ of objects to traverse attributes
# - loops are detected and presented as lightblue nodes
# - Model classes are given a green color
# - UnknownType nodes are shown orange (after inference there shouldn't be any)
# - _type in Types is suppressed as it is always UnknownType

class DotDumper(object):
  def __init__(self):
    self.dot = DotBuilder()
    self.stack = []

  def dump(self, obj):
    self.process(obj)
    return str(self.dot)

  def process(self, obj):
    # CLASSES
    if inspect.isclass(obj):
      options = {"color":"springgreen"} if "semantic.model" in obj.__module__ else {}
      node = self.dot.node(obj.__name__, options)
      return node

    # A SIMPLE TYPE
    if isstring(obj) or isinstance(obj, int) or isinstance(obj, float) or \
       isinstance(obj, bool):
      return self.dot.node(str(obj))

    # UNKNOWN TYPE
    if isinstance(obj, UnknownType): 
      return self.dot.node(obj.__class__.__name__, {"color":"orange"})

    # TYPES
    if isinstance(obj, TypeExp): 
      return self.dot.node(obj.__class__.__name__, {"color":"limegreen"})

    # RECURSION & LOOP DETECTION
    if obj.__repr__ in self.stack:
      # print_stderr("LOOP DETECTED: " + str(obj) + str(self.stack) + "\n")
      return self.dot.node(str(obj), {"color":"lightblue"})

    self.stack.append(obj.__repr__)

    # ITERATABLES

    # SIMPLE DICT
    if isinstance(obj, dict):
      node = self.dot.node(obj.__class__.__name__)
      for key, value in obj.items():
        if not value is None:
          self.dot.vertex(node, self.process(value), {"label":key})
    # SIMPLE LIST
    elif isinstance(obj, list):
      node = self.dot.node(obj.__class__.__name__)
      for value in obj:
        if not value is None:
          self.dot.vertex(node, self.process(value))
    # OBJECT
    else:
      options = {"color":"green"} if "semantic.model" in obj.__module__ else {}
      node = self.dot.node(obj.__class__.__name__, options)
      for key, value in obj.__dict__.items():
        if not value is None:
          self.dot.vertex(node, self.process(value), {"label":key})

    self.stack.pop()
    return node
