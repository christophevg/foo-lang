# visitor.py
# author: Christophe VG

# Visitors related to the Semantic Model
# - AstVisitor for converting an AST into a Semantic Model
# - SemanticVisitor is a base class for visitors that work on the Semantic Model
# - SemanticChecker is a base class for visitors that perform checks

import sys
import inspect

from util.check               import isidentifier, isstring
from util.visitor             import Visitable
from util.environment         import Environment

from foo_lang.semantic.model  import *     # too many to import explicitly
from foo_lang.semantic.dumper import Dumper

# AST VISITOR
#
# Accepts a model and imports a foo-based AST.
# Note: trying to create a tree grammar to do this seemed harder in the end

class AstVisitor():
  def __init__(self, model):
    self.model = model

    # local scoping helper
    self.current_module = None

    # mapping top-node's text to handler (aka poor man's visitor pattern)
    self.dispatch = {
      "ROOT"            : self.handle_root,
      "MODULE"          : self.handle_module,
      "CONST"           : self.handle_constant,
      "IMPORT"          : self.handle_import,
      "EXTEND"          : self.handle_extend,
      "ANNOTATED"       : self.handle_annotated,
      "DOMAIN"          : self.handle_domain,

      "ANON_FUNC_DECL"  : self.handle_anon_func_decl,
      "FUNC_DECL"       : self.handle_func_decl,
      "ON"              : self.handle_event_handler_decl,
      
      "BLOCK"           : self.handle_block_stmt,
      "IF"              : self.handle_if_stmt,
      "CASES"           : self.handle_cases_stmt,

      "INC"             : self.handle_inc_stmt,
      "DEC"             : self.handle_dec_stmt,

      "="               : lambda t: self.handle_bin_stmt("=",  AssignStmt, t),
      "+="              : lambda t: self.handle_bin_stmt("+=", AddStmt,    t),
      "-="              : lambda t: self.handle_bin_stmt("-=", SubStmt,    t),

      "RETURN"          : self.handle_return_stmt,

      "OBJECT_REF"      : self.handle_object_ref,
      "FUNC_REF"        : self.handle_function_ref,

      "PROPERTY_EXP"    : self.handle_property_exp,
      "MATCH_EXP"       : self.handle_match_exp,
      "VAR_EXP"         : self.handle_variable_exp,
      "TYPE_EXP"        : self.handle_type_exp,
      "UNKNOWN_TYPE"    : self.handle_unknown_type,
      "MANY_TYPE_EXP"   : self.handle_many_type_exp,
      "TUPLE_TYPE_EXP"  : self.handle_tuple_type_exp,

      ">"               : lambda t: self.handle_bin_exp(">",   GTExp,        t),
      ">="              : lambda t: self.handle_bin_exp(">=",  GTEQExp,      t),
      "<"               : lambda t: self.handle_bin_exp("<",   LTExp,        t),
      "<="              : lambda t: self.handle_bin_exp("<=",  LTEQExp,      t),
      "+"               : lambda t: self.handle_bin_exp("+",   PlusExp,      t),
      "-"               : lambda t: self.handle_bin_exp("-",   MinusExp,     t),
      "and"             : lambda t: self.handle_bin_exp("and", AndExp,       t),
      "or"              : lambda t: self.handle_bin_exp("or",  OrExp,        t),
      "=="              : lambda t: self.handle_bin_exp("==",  EqualsExp,    t),
      "!="              : lambda t: self.handle_bin_exp("!=",  NotEqualsExp, t),
      "*"               : lambda t: self.handle_bin_exp("*",   MultExp,      t),
      "/"               : lambda t: self.handle_bin_exp("/",   DivExp,       t),
      "%"               : lambda t: self.handle_bin_exp("%",   ModuloExp,    t),
      "!"               : self.handle_not_exp,
      
      # TODO: merge these into handle_call ?
      "FUNC_CALL"       : self.handle_function_call,
      "METHOD_CALL"     : self.handle_method_call,
      
      "BOOLEAN_LITERAL" : lambda t: self.handle_literal("BOOLEAN_LITERAL", \
                                                        BooleanLiteralExp, t),
      "INTEGER_LITERAL" : lambda t: self.handle_literal("INTEGER_LITERAL", \
                                                        IntegerLiteralExp, t),
      "FLOAT_LITERAL"   : lambda t: self.handle_literal("FLOAT_LITERAL", \
                                                        FloatLiteralExp, t),
      "ATOM_LITERAL"    : self.handle_atom_literal,
      "LIST_LITERAL"    : self.handle_list_literal,
      "IDENTIFIER"      : self.handle_identifier
  }

  # visiting an unknown tree, using the dispatch to get to specialized handler
  def visit(self, tree):
    try:
      return self.dispatch[tree.text](tree)
    except KeyError as e:
      print "foo-ast-visitor: missing handler for", e

  # HANDLERS

  def handle_identifier(self, tree):
    assert tree.text == "IDENTIFIER"
    name = tree.getChildren()[0].text
    assert isidentifier(name), "bad identifier name " + name
    return Identifier(name)

  def handle_root(self, tree):
    assert tree.text == "ROOT"
    for child in tree.getChildren():
      self.visit(child)

  def handle_module(self, tree):
    assert tree.text == "MODULE"
    children = tree.getChildren()
    name     = self.visit(children[0])
    module   = Module(name)
    self.model.modules[name.name] = module
    self.current_module           = module
    for index in range(1,len(children)):
      self.visit(children[index])
    return module

  def handle_constant(self, tree):
    assert tree.text == "CONST"
    children = tree.getChildren()
    name     = self.visit(children[0])
    type   = self.visit(children[1])
    value  = self.visit(children[2])
    constant = Constant(name, value, type)
    self.current_module.constants.append(constant)
    return constant

  def handle_extend(self, tree):
    assert tree.text == "EXTEND"
    children  = tree.getChildren()
    domain    = self.handle_domain(children[0])
    obj       = self.handle_object_literal(children[1])
    extension = Extension(domain, obj)
    self.current_module.extensions.append(extension)
    return extension
  
  def handle_import(self, tree):
    assert tree.text == "IMPORT"
    children = tree.getChildren()
    module   = self.visit(children[0])
    function = self.visit(children[1])
    self.current_module.externals[function.name] = module.name
  
  def handle_annotated(self, tree):
    assert tree.text == "ANNOTATED"
    children   = tree.getChildren()
    [annotation, arguments] = self.handle_annotation(children[0])
    [scope, function]       = self.handle_annotated_execution(children[1])

    self.add_execution(annotation, scope, function, arguments)

  def handle_annotation(self, tree):
    assert tree.text == "ANNOTATION"
    children = tree.getChildren()
    return {
      'every': ['Every', [self.handle_variable_exp(children[1].getChildren()[0])]]
    }[children[0].getChildren()[0].text]  # FIXME: ugly with ID in between

  # two executions are supported currently:
  # 1. application of function to scope
  # 2. (simple) function in global scope (NOT IMPLEMENTED YET)
  # TODO: implement simple function support
  def handle_annotated_execution(self, tree):
    return {
      'APPLY': self.handle_application(tree)  # returns [scope, function]
    }[tree.text]
  
  def handle_application(self, tree):
    assert tree.text == "APPLY"
    children = tree.getChildren()
    scope    = self.as_scope(self.visit(children[0]))
    function = self.visit(children[1])
    return [scope, function]

  def handle_domain(self, tree):
    assert tree.text == "DOMAIN"
    domain = self.visit(tree.getChildren()[0])
    return self.model.domains[domain.name]

  def handle_anon_func_decl(self, tree):
    assert tree.text == "ANON_FUNC_DECL"
    children   = tree.getChildren()
    parameters = self.handle_parameters(children[0])
    body       = self.visit(children[1])
    function   = FunctionDecl(body, parameters=parameters)
    self.current_module.functions.append(function)
    return function

  def handle_func_decl(self, tree):
    assert tree.text == "FUNC_DECL"
    children   = tree.getChildren()
    name       = self.visit(children[0])
    if len(children) > 2:
      parameters = self.handle_parameters(children[1])
      body       = self.visit(children[2])
    else:
      parameters = []
      body       = self.visit(children[1])
    function   = FunctionDecl(body, identifier=name, parameters=parameters)
    self.current_module.functions.append(function)
    return function

  def handle_parameters(self, tree):
    assert tree.text == "PARAMS"
    parameters = tree.getChildren()
    return [Parameter(self.visit(parameter)) for parameter in parameters]

  def handle_event_handler_decl(self, tree):
    assert tree.text == "ON"
    children = tree.getChildren()
    timing   = children[0].text
    scope    = self.as_scope(self.visit(children[1]))
    event    = self.visit(children[2])
    function = self.visit(children[3])
    
    return self.add_execution("When", scope, function, [timing, event])

  def add_execution(self, class_name, scope, function, arguments):
    module   = sys.modules["foo_lang.semantic.model"]
    clazz    = getattr(module, class_name)
    strategy = clazz(scope, function, *arguments)
    self.current_module.executions.append(strategy)
    return strategy

  # STATEMENTS

  def handle_block_stmt(self, tree):
    assert tree.text == "BLOCK"
    statements = tree.getChildren()
    return BlockStmt([self.visit(statement) for statement in statements])

  def handle_if_stmt(self, tree):
    assert tree.text == "IF"
    children  = tree.getChildren()
    condition = self.visit(children[0])
    true      = self.visit(children[1])
    if len(children) > 2:
      false   = self.visit(children[2])
    else:
      false   = None
    return IfStmt(condition, true, false)

  def handle_cases_stmt(self, tree):
    assert tree.text == "CASES"
    children     = tree.getChildren()
    expression   = self.visit(children[0])
    cases        = []
    for index in range(1,len(children)):
      cases.append(self.handle_case(children[index]))
    [cases, consequences] = zip(*cases)
    return CaseStmt(expression, cases, consequences)

  def handle_case(self, tree):
    assert tree.text == "CASE"
    children       = tree.getChildren()
    function_name  = self.visit(children[0])
    if len(children) > 2:
      arguments = self.handle_arguments(children[1])
      function  = FunctionCallExp(FunctionExp(function_name), arguments)
      body      = self.visit(children[2])
    else:
      function = FunctionCallExp(function_name)
      body     = self.visit(children[1])
    return [function, body]

  def handle_inc_stmt(self, tree):
    assert tree.text == "INC"
    target = self.visit(tree.getChildren()[0])
    return IncStmt(target)

  def handle_dec_stmt(self, tree):
    assert tree.text == "DEC"
    target = self.visit(tree.getChildren()[0])
    return DecStmt(target)

  def handle_bin_stmt(self, text, constructor, tree):
    assert tree.text == text
    children = tree.getChildren()
    left     = self.visit(children[0])
    right    = self.visit(children[1])
    return constructor(left, right)

  def handle_return_stmt(self, tree):
    assert tree.text == "RETURN"
    return ReturnStmt()

  # ??? :-)

  def handle_object_ref(self, tree):
    assert tree.text == "OBJECT_REF"
    return ObjectExp(self.visit(tree.getChildren()[0]))

  def handle_function_ref(self, tree):
    assert tree.text == "FUNC_REF"
    return FunctionExp(self.visit(tree.getChildren()[0]))

  # EXPRESSIONS

  def handle_property_exp(self, tree):
    assert tree.text == "PROPERTY_EXP"
    children = tree.getChildren()
    obj      = self.visit(children[0])
    prop     = self.visit(children[1])
    # TODO: make more generic
    if isinstance(obj, Domain):
      return obj.get_property(prop.name)
    else:
      return PropertyExp(obj, prop)

  def handle_match_exp(self, tree):
    assert tree.text == "MATCH_EXP"
    children = tree.getChildren()
    if children[0].text == "ANYTHING":
      return MatchExp(AnythingExp())
    else:
      # first child is a string representation of the comparator-operator
      # second child is an expression: the right operand of the comparator
      return MatchExp(children[0].text, self.visit(children[1]))

  def handle_variable_exp(self, tree):
    assert tree.text == "VAR_EXP"
    return VariableExp(self.visit(tree.getChildren()[0]))

  def handle_type_exp(self, tree):
    assert tree.text == "TYPE_EXP"
    child      = tree.getChildren()[0]
    identifier = self.visit(child)
    assert isinstance(identifier, Identifier)
    try:
      return {
        "boolean"   : BooleanType,
        "int"       : IntegerType,
        "integer"   : IntegerType,
        "byte"      : ByteType,
        "float"     : FloatType,
        "timestamp" : TimestampType,
      }[identifier.name.lower()]()
    except KeyError:
      print "Failed to resolve simple type based on identifier", identifier.name
    return UnknownType()

  def handle_unknown_type(self, tree):
    assert tree.text == "UNKNOWN_TYPE"
    return UnknownType()

  def handle_many_type_exp(self, tree):
    assert tree.text == "MANY_TYPE_EXP"
    type = self.visit(tree.getChildren()[0])
    return ManyType(type)

  def handle_tuple_type_exp(self, tree):
    assert tree.text == "TUPLE_TYPE_EXP"
    types = [self.visit(type) for type in tree.getChildren()]
    return TupleType(types)

  def handle_not_exp(self, tree):
    assert tree.text == "!"
    return NotExp(self.visit(tree.getChildren()[0]))

  # GENERIC FUNCTION FOR BINARY EXPRESSIONS

  def handle_bin_exp(self, text, constructor, tree):
    assert tree.text == text
    children = tree.getChildren()
    left     = self.visit(children[0])
    right    = self.visit(children[1])
    return constructor(left, right)

  # CALLING
  
  def handle_function_call(self, tree):
    assert tree.text == "FUNC_CALL"
    children  = tree.getChildren()
    function  = self.visit(children[0])
    if len(children) > 1:
      arguments = self.handle_arguments(children[1])
      return FunctionCallExp(FunctionExp(function), arguments)
    else:
      return FunctionCallExp(FunctionExp(function))

  def handle_method_call(self, tree):
    assert tree.text == "METHOD_CALL"
    children = tree.getChildren()
    obj      = self.visit(children[0])
    method   = self.visit(children[1])
    if len(children) > 2:
      arguments = self.handle_arguments(children[2])
      return MethodCallExp(obj, method, arguments)
    else:
      return MethodCallExp(obj, method)

  def handle_arguments(self, tree):
    assert tree.text == "ARGS"
    arguments = tree.getChildren()
    return [self.visit(argument) for argument in arguments]

  # TYPES

  def handle_literal(self, text, constructor, tree):
    assert tree.text == text
    return constructor(tree.getChildren()[0].text)

  def handle_atom_literal(self, tree):
    assert tree.text == "ATOM_LITERAL"
    return AtomLiteralExp(self.visit(tree.getChildren()[0]))

  def handle_list_literal(self, tree):
    assert tree.text == "LIST_LITERAL"
    children = tree.getChildren()
    return ListLiteralExp([self.visit(child) for child in children])

  def handle_object_literal(self, tree):
    assert tree.text == "OBJECT_LITERAL"
    obj = ObjectLiteralExp()
    for child in tree.getChildren():
      obj.properties.append(self.handle_property_literal(child))
    return obj

  def handle_property_literal(self, tree):
    assert tree.text == "PROPERTY_LITERAL"
    children = tree.getChildren()
    name     = self.visit(children[0])
    type   = self.visit(children[1])
    value  = self.visit(children[2])
    return Property(name, value, type)

  # HELPERS

  # makes sure that the argument is a scope
  def as_scope(self, obj):
    if isinstance(obj, Scope):
      return obj
    elif isinstance(obj, Domain):
      return obj.get_scope()
    else:
      raise RuntimeError("Un-scopable object:", obj)

def stacked(method):
  """
  Decorator for methods to keep track of their execution using a stack.
  """
  obj_name = method.__name__[7:]
  def wrapped(self, obj):
    self._stack.append(obj)
    if self.bottom_up: method(self, obj)
    if self.prefix != None and self.prefix != "handle_":
      try:
        external_handler = getattr(self, self.prefix + obj_name)
        external_handler(obj)
      except AttributeError:
        # possibly there is no handler
        # print "not handling", part_name
        pass
    if self.top_down: method(self, obj)
    self._stack.pop()
  return wrapped

# SEMANTIC VISITOR
#
# Implements the SemanticVisitorBase with handlers to visit all parts of the
# Semantic Model. This can be done in a top-down or bottom-up approach.
# While doing so, it constructs a stack of visited parts and an environment of
# declared entities (Variables, Objects,...)

class SemanticVisitor(SemanticVisitorBase):
  def __init__(self, top_down=None, bottom_up=None):
    self.prefix    = None
    self._stack    = []
    self.env       = Environment()
    if top_down == bottom_up == None:
      top_down = True
      bottom_up = False
    assert top_down != bottom_up, "Can't move in both/no direction ;-)"
    self.top_down  = top_down
    self.bottom_up = bottom_up

  def get_stack(self): return self._stack
  stack = property(get_stack)

  # HANDLERS IMPLEMENTING VISITOR and adding a handle call

  @stacked
  def handle_Model(self, model):
    for module in model.modules.values():
      module.accept(self)

  @stacked
  def handle_Domain(self, domain):
    self.env[domain.name] = domain
    
  @stacked
  def handle_Scope(self, scope): pass

  @stacked
  def handle_Module(self, module):
    self.env.extend()
    for constant in module.constants:
      constant.accept(self)
    
    for function, library in module.externals.items():
      self.env[function] = library
    
    for extension in module.extensions:
      extension.accept(self)
    
    for function in module.functions:
      # we only want to handle non-anonymous function declarations here
      # because anonymous declarations are declared in their specific scope
      # TODO: do this in a cleaner way (AnonFunctionDecl?)
      if function.name[0:9] != "anonymous":
        function.accept(self)

    for execution in module.executions:
      execution.accept(self)
        
    self.env.reduce()

  @stacked
  def handle_Constant(self, constant):
    self.env[constant.name] = constant

  @stacked
  def handle_Extension(self, extension):
    extension.domain.accept(self)
    extension.extension.accept(self)

  @stacked
  def handle_Every(self, execution):
    execution.interval.accept(self)
    execution.scope.accept(self)
    execution.executed.accept(self)

  @stacked
  def handle_When(self, execution):
    execution.scope.accept(self)
    execution.event.accept(self)
    execution.executed.accept(self)

  @stacked
  def handle_FunctionDecl(self, function):
    self.env[function.name] = function
    self.env.extend()
    for param in function.parameters:
      param.accept(self)
    function.body.accept(self)
    self.env.reduce()

  @stacked
  def handle_Parameter(self, parameter):
    self.env[parameter.name] = parameter

  # STATEMENTS

  @stacked
  def handle_BlockStmt(self, block):
    self.env.extend()
    for statement in block.statements:
      statement.accept(self)
    self.env.reduce()

  @stacked
  def handle_AssignStmt(self, stmt):
    stmt.variable.accept(self)
    stmt.value.accept(self)

  @stacked
  def handle_AddStmt(self, stmt):
    stmt.variable.accept(self)
    stmt.value.accept(self)
  
  @stacked
  def handle_SubStmt(self, stmt):
    stmt.variable.accept(self)
    stmt.value.accept(self)

  @stacked
  def handle_IncStmt(self, stmt):
    stmt.variable.accept(self)

  @stacked
  def handle_DecStmt(self, stmt):
    stmt.variable.accept(self)

  @stacked
  def handle_IfStmt(self, stmt):
    stmt.condition.accept(self)
    stmt.true.accept(self)
    if stmt.false != None:
      stmt.false.accept(self)

  @stacked
  def handle_CaseStmt(self, stmt):
    stmt.expression.accept(self)
    for case, consequence in zip(stmt.cases, stmt.consequences):
      self.env.extend()
      case.accept(self)
      consequence.accept(self)
      self.env.reduce()

  @stacked
  def handle_ReturnStmt(self, stmt):
    if stmt.expression != None:
      stmt.expression.accept(self)
    
  # EXPRESSIONS
  
  @stacked
  def handle_BooleanLiteralExp(self, exp): pass
    
  @stacked
  def handle_IntegerLiteralExp(self, exp): pass

  @stacked
  def handle_FloatLiteralExp(self, exp): pass

  @stacked
  def handle_AtomLiteralExp(self, atom): pass

  @stacked
  def handle_ListLiteralExp(self, lst):
    for exp in lst.expressions:
      exp.accept(self) 

  @stacked
  def handle_ObjectLiteralExp(self, obj):
    for prop in obj.properties:
      prop.accept(self)

  @stacked
  def handle_Property(self, prop):
    if prop.type != None:
      prop.type.accept(self)
    prop.value.accept(self)

  @stacked
  def handle_BooleanType(self, type): pass

  @stacked
  def handle_ByteType(self, type): pass

  @stacked
  def handle_IntegerType(self, type): pass

  @stacked
  def handle_FloatType(self, type): pass

  @stacked
  def handle_TimestampType(self, type): pass

  @stacked
  def handle_ManyType(self, many):
    many.subtype.accept(self)
    
  @stacked
  def handle_TupleType(self, tuple):
    for type in tuple.types:
      type.accept(self)

  @stacked
  def handle_VariableExp(self, var):
    # on first use, a variable is self-instantiating
    try:
      prev = self.env[var.name]
    except KeyError:
      self.env[var.name] = var
  
  @stacked
  def handle_PropertyExp(self, prop):
    prop.obj.accept(self)

  @stacked
  def handle_UnaryExp(self, exp):
    exp.operand.accept(self)

  @stacked
  def handle_BinaryExp(self, exp):
    exp.left.accept(self)
    exp.right.accept(self)

  @stacked
  def handle_FunctionCallExp(self, exp):
    exp.function.accept(self)
    for arg in exp.arguments:
      arg.accept(self)

  @stacked
  def handle_FunctionExp(self, exp): pass

  @stacked
  def handle_ObjectExp(self, exp): pass

  @stacked
  def handle_MethodCallExp(self, exp):
    exp.object.accept(self)
    for arg in exp.arguments:
      arg.accept(self)

  @stacked
  def handle_AnythingExp(self, exp): pass

  @stacked
  def handle_MatchExp(self, exp):
    # TODO remove this dependency on string operator
    if not isstring(exp.operator):
      exp.operator.accept(self)
    if exp.operand != None:
      exp.operand.accept(self)

# SEMANTIC CHECKER
#
# wraps the SemanticVisitor adding:
#
# - assertion methods
# - tracking of failures and successes
# - visualisation of the stack
# - overrides handle_ prefix with check_

class SemanticChecker(SemanticVisitor):
  def __init__(self, model, top_down=None, bottom_up=None):
    super(SemanticChecker, self).__init__(top_down, bottom_up)
    self.model  = model
    self.prefix = "check_"
    self.name   = "foo-" + self.__class__.__name__.lower()

  def check(self):
    print self.name + ": processing model"
    self.start();
    self.model.accept(self)
    self.stop()

  def start(self):
    self.fails = 0
    self.successes = 0

  def stop(self):
    self.report()

  def report(self):
    print "-" * 79

    result = "SUCCESS - model is valid" if self.fails == 0 \
             else "FAILURES : " + str(self.fails)
    info   = "SUCCESSES: " + str(self.successes) if self.successes != 0 \
             else None

    self.log("results of run", result, info)
    print "-" * 79

  def fail(self, msg, *args):
    self.fails += 1
    self.log("failure: " + msg + " : " + str(*args),
             "stack: " + " > ".join([self.show(obj) for obj in self._stack]))

  def show(self, obj):
    name   = obj.__class__.__name__
    attrib = False
    try:
      attrib = {
                 'FunctionDecl'    : 'name',
                 'FunctionExp'     : 'name',
                 'FunctionCallExp' : 'function',
                 'CaseStmt'        : 'expression',
                 'Every'           : 'interval',
                 'When'            : 'event',
                 'Module'          : 'name',
                 'Parameter'       : 'name'
               }[name]
    except KeyError: pass

    if attrib != False:
      attrib = getattr(obj, attrib)
      if isinstance(attrib, Visitable):
        attrib = attrib.accept(Dumper())
      return name + "(" + attrib + ")"
    else:
      return name

  def success(self, msg, *args):
    self.successes += 1
    self.log("success: " + msg + " : " + " ".join([str(arg) for arg in args]))

  def log(self, msg1, *msgs):
    print "foo-" + self.__class__.__name__.lower() + ": " + msg1
    for msg in msgs:
      if not msg is None:
        print " " * len(self.name) + "  " + msg

  # ASSERTIONS HELPERS

  def assertIsNotNone(self, obj, msg, *info):
    if obj is None:
      self.fail(msg, *info)

  def assertNotIsInstance(self, obj, instance, msg, *info):
    if isinstance(obj, instance):
      self.fail(msg, *info)

