# dumper.py
# a plain text foo syntax-based dumper, based on SemanticVisitor
# author: Christophe VG

import inspect

from util.check              import isstring
from util.dot                import DotBuilder

from foo_lang.semantic.model import *

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

  def visit_Identifier(self, id):
    return id.name

  @indent
  def visit_Model(self, model):
    string = ""
    for module in model.modules.values():
      string += module.accept(self)
    return string

  @indent
  def visit_Domain(self, domain):
    return domain.__class__.__name__.lower()

  @indent
  def visit_Scope(self, scope):
    return scope.scope

  @indent
  def visit_Module(self, module):
    string = "module " + module.identifier.accept(self) + "\n";

    for constant in module.constants:
      string += constant.accept(self) + "\n"
    
    for function, library in module.externals.items():
      string += "from " + library + " import " + function + "\n"
    
    for domain in module.domains:
      for extension in domain.extensions:
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
  def visit_Constant(self, constant):
    return "const " + constant.identifier.accept(self) \
           + ((" : " + constant.type.accept(self)) \
             if not isinstance(constant.type, UnknownType) else "") \
           + " = " + constant.value.accept(self)

  @indent
  def visit_Extension(self, extension):
    return "extend " + extension.domain.accept(self) + \
           " with " + extension.extension.accept(self)

  @indent
  def visit_Every(self, execution):
    return "@every(" + execution.interval.accept(self) + ")\n" + \
           "with " + execution.scope.accept(self) + " do " + \
           execution.executed.accept(self).lstrip()

  @indent
  def visit_When(self, execution):
    return execution.timing + " " + execution.scope.accept(self) + " " + \
           execution.event.accept(self) + " do " + \
           execution.executed.accept(self).lstrip()

  @indent
  def visit_FunctionDecl(self, function):
    name = "" if function.name[0:9] == "anonymous" \
              else " " + function.identifier.accept(self)
    string = "function" + name + \
             "(" + ", ".join([ param.accept(self) 
                                   for param in function.parameters]) + ") " + \
               function.body.accept(self).lstrip()
    return string

  def visit_Parameter(self, parameter):
    return parameter.identifier.accept(self)

  # STATEMENTS

  @indent
  def visit_BlockStmt(self, block):
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
  def visit_AssignStmt(self, stmt):
    return stmt.variable.accept(self) + " = " + stmt.value.accept(self)

  @indent
  def visit_AddStmt(self, stmt):
    return stmt.variable.accept(self) + " += " + stmt.value.accept(self)
  
  @indent
  def visit_SubStmt(self, stmt):
    return stmt.variable.accept(self) + " -= " + stmt.value.accept(self)

  @indent
  def visit_IncStmt(self, stmt):
    return stmt.variable.accept(self) + "++"

  @indent
  def visit_DecStmt(self, stmt):
    return stmt.variable.accept(self) + "--"

  @indent
  def visit_IfStmt(self, stmt):
    string =  "if( " + stmt.condition.accept(self) + " ) " + \
              stmt.true.accept(self).lstrip()
    if stmt.false != None:
      string += " else " + stmt.false.accept(self).lstrip()
    return string

  @indent
  def visit_CaseStmt(self, stmt):
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
  def visit_ReturnStmt(self, stmt):
    return "return" + \
         ("" if stmt.expression == None else " " + stmt.expression.accept(self))
    
  # EXPRESSIONS
  
  def visit_BooleanLiteralExp(self, exp):
    return "true" if exp.value else "false"

  def visit_IntegerLiteralExp(self, exp):
    return str(exp.value)

  def visit_FloatLiteralExp(self, exp):
    return str(exp.value)
  
  def visit_AtomLiteralExp(self, atom):
    return "#" + atom.identifier.accept(self)

  def visit_ListLiteralExp(self, lst):
    return "[" + ",".join([exp.accept(self) for exp in lst.expressions]) + "]"

  def visit_ObjectLiteralExp(self, obj):
    string = "{";
    if len(obj.properties) != 0: string += "\n"
    self.inc_indent()
    for prop in obj.properties:
      string += prop.accept(self) + "\n"
    self.dec_indent()
    string += "  " * self.indent_level + "}"
    return string

  @indent
  def visit_Property(self, prop):
    return prop.identifier.accept(self) + \
           ((" : " + prop.type.accept(self)) \
             if not isinstance(prop.type, UnknownType) else "") + \
           " = " + prop.value.accept(self)

  def visit_UnknownType(self, type): return "__unknown__"
  def visit_AnyType(self, type):     return "__any__"
  def visit_MixedType(self, type):   return "__mixed__"
  def visit_AtomType(self, type):    return "__atom__"

  def visit_VoidType   (self, type): return ""
  def visit_BooleanType(self, type): return "boolean"
  def visit_ByteType   (self, type): return "byte"
  def visit_IntegerType(self, type): return "integer"
  def visit_FloatType  (self, type): return "float"
  def visit_ObjectType (self, type): return type.name

  def visit_TimestampType (self, type): return "timestamp"
  
  def visit_ManyType(self, many):
    return many.subtype.accept(self) + "*"
    
  def visit_TupleType(self, tuple):
    return "[" + ",".join([type.accept(self) for type in tuple.types]) + "]"

  def visit_VariableExp(self, var):
    return var.identifier.accept(self)

  def visit_FunctionExp(self, var):
    return var.identifier.accept(self)

  def visit_ObjectExp(self, var):
    return var.identifier.accept(self)
  
  def visit_PropertyExp(self, prop):
    return prop.obj.accept(self) + "." + prop.identifier.accept(self)

  def visit_UnaryExp(self, exp):
    return exp.operator() + " " + exp.operand.accept(self)

  def visit_BinaryExp(self, exp):
    return "( " + exp.left.accept(self) + " "  + exp.operator() + " " + \
                 exp.right.accept(self) + " )"

  def visit_NumericBinaryExp(self, exp):
    return self.visit_BinaryExp(exp)

  @indent
  def visit_FunctionCallExp(self, exp):
    return exp.function.accept(self) + \
           "(" + ", ".join([arg.accept(self) for arg in exp.arguments]) + ")"

  @indent
  def visit_MethodCallExp(self, exp):
    return exp.object.accept(self) + "." + exp.identifier.accept(self) + \
           "(" + ", ".join([arg.accept(self) for arg in exp.arguments]) + ")"

  def visit_AnythingExp(self, exp):
    return "_"

  def visit_MatchExp(self, exp):
    return (exp.operator.accept(self) if isstring(exp.operator) else exp.operator.accept(self)) + \
           ((" " + exp.operand.accept(self)) if exp.operand != None else "")

  def visit_Comparator(self, comp):
    return comp.operator

# DOT DUMPER
#
# Generic Dumper using the internal __dict__ of objects to traverse attributes
# - loops are detected and presented as lightblue nodes
# - Model classes are given a green color
# - UnknownType nodes are shown orange (after inference there shouldn't be any)
# - details of Types is suppressed as its _type always UnknownType
# - Identifiers are simple nodes with their name and a blueish color

class DotDumper(object):
  def __init__(self):
    self.dot = DotBuilder()
    self.processed = []

  def dump(self, obj):
    self.process(obj)
    return str(self.dot)

  def process(self, obj):
    # IDENTIFIERS
    if isinstance(obj, Identifier):
      return self.dot.node(obj.name, {"color":"seagreen"})

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
      return self.dot.node(obj.__class__.__name__, {"color":"coral"})

    # ANY TYPE
    if isinstance(obj, AnyType):
      return self.dot.node(obj.__class__.__name__, {"color":"limegreen"})

    # ANYTHING EXP
    if isinstance(obj, AnythingExp):
      return self.dot.node(obj.__class__.__name__, {"color":"green"})

    # TYPES
    if isinstance(obj, TypeExp) and not isinstance(obj, ComplexType):
      return self.dot.node(obj.__class__.__name__, {"color":"limegreen"})

    # RECURSION & LOOP DETECTION
    if str(obj.__repr__) in self.processed:
      return self.dot.node("dict" if isinstance(obj, dict) else str(obj),
                           {"color":"lightblue"})

    self.processed.append(str(obj.__repr__))

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
      options = {"color":"limegreen"} if isinstance(obj, ComplexType) else \
      {"color":"green"} if "foo_lang.semantic" in obj.__module__ else {}
      node = self.dot.node(obj.__class__.__name__, options)

      # if the obj supports the .type property, add it as such
      if hasattr(obj, "type") and not isinstance(obj, TimestampType):
        subnode = self.process(obj.type)
        self.dot.vertex(node, subnode, {"label": "type"})

      # manual exception to allow modules to be processed in such a way that 
      # domains are processed sooner than functions, to make sure that types
      # defined in domains are added in detail and all other instances are shown
      # as references
      if isinstance(obj, Module):
        items = [ ["identifier", obj.identifier],
                  ["constants",  obj.constants],
                  ["externals",  obj.externals],
                  ["domains",    obj.domains],
                  ["functions",  obj.functions],
                  ["executions", obj.executions]
                ]
      elif isinstance(obj, Domain):
        items = [
                  ["extensions", obj.extensions],
                  ["node_t",     obj.node_t],
                  ["payload_t",  obj.payload_t]
                ]
      else:
        items = obj.__dict__.items()
      for key, value in items:
        if key not in ["_type", "type"] and not value is None:
          # SCOPE
          if isinstance(value, Scope):
            subnode = self.dot.node(value.__class__.__name__, {"color":"lightblue"})
          else:
            subnode = self.process(value)
          self.dot.vertex(node, subnode, {"label":key})

    return node
