# visitor.py
# author: Christophe VG

# Visitors related to the Semantic Model
# - AstVisitor for converting an AST into a Semantic Model
# - SemanticVisitor is a base class for visitors that work on the Semantic Model
# - SemanticChecker is a base class for visitors that perform checks

import sys
import inspect

from util.support             import print_stderr
from util.check               import isidentifier, isstring
from util.visitor             import Visitable, stacked, with_handling
from util.environment         import Environment

from foo_lang.semantic.model  import *     # too many to import explicitly
from foo_lang.semantic.dumper import Dumper

from foo_lang.semantic.domains.nodes import Nodes

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
      "ROOT"            : self.visit_root,
      "MODULE"          : self.visit_module,
      "CONST"           : self.visit_constant,
      "IMPORT"          : self.visit_import,
      "EXTEND"          : self.visit_extend,
      "ANNOTATED"       : self.visit_annotated,
      "DOMAIN"          : self.visit_domain,

      "ANON_FUNC_DECL"  : self.visit_anon_func_decl,
      "FUNC_DECL"       : self.visit_func_decl,
      "FUNC_PROTO"      : self.visit_func_proto,
      "ON"              : self.visit_event_handler_decl,
      
      "BLOCK"           : self.visit_block_stmt,
      "IF"              : self.visit_if_stmt,
      "CASES"           : self.visit_cases_stmt,

      "INC"             : self.visit_inc_stmt,
      "DEC"             : self.visit_dec_stmt,

      "="               : lambda t: self.visit_bin_stmt("=",  AssignStmt, t),
      "+="              : lambda t: self.visit_bin_stmt("+=", AddStmt,    t),
      "-="              : lambda t: self.visit_bin_stmt("-=", SubStmt,    t),

      "RETURN"          : self.visit_return_stmt,

      "OBJECT_REF"      : self.visit_object_ref,
      "FUNC_REF"        : self.visit_function_ref,

      "PROPERTY_EXP"    : self.visit_property_exp,
      "MATCH_EXP"       : self.visit_match_exp,
      "VAR_EXP"         : self.visit_variable_exp,
      "TYPE_EXP"        : self.visit_type_exp,
      "UNKNOWN_TYPE"    : self.visit_unknown_type,
      "MANY_TYPE_EXP"   : self.visit_many_type_exp,
      "AMOUNT_TYPE_EXP" : self.visit_amount_type_exp,
      "TUPLE_TYPE_EXP"  : self.visit_tuple_type_exp,

      ">"               : lambda t: self.visit_bin_exp(">",   GTExp,        t),
      ">="              : lambda t: self.visit_bin_exp(">=",  GTEQExp,      t),
      "<"               : lambda t: self.visit_bin_exp("<",   LTExp,        t),
      "<="              : lambda t: self.visit_bin_exp("<=",  LTEQExp,      t),
      "+"               : lambda t: self.visit_bin_exp("+",   PlusExp,      t),
      "-"               : lambda t: self.visit_bin_exp("-",   MinusExp,     t),
      "and"             : lambda t: self.visit_bin_exp("and", AndExp,       t),
      "or"              : lambda t: self.visit_bin_exp("or",  OrExp,        t),
      "=="              : lambda t: self.visit_bin_exp("==",  EqualsExp,    t),
      "!="              : lambda t: self.visit_bin_exp("!=",  NotEqualsExp, t),
      "*"               : lambda t: self.visit_bin_exp("*",   MultExp,      t),
      "/"               : lambda t: self.visit_bin_exp("/",   DivExp,       t),
      "%"               : lambda t: self.visit_bin_exp("%",   ModuloExp,    t),
      "!"               : self.visit_not_exp,
      
      # TODO: merge these into visit_call ?
      "FUNC_CALL"       : self.visit_function_call,
      "METHOD_CALL"     : self.visit_method_call,
      
      "BOOLEAN_LITERAL" : lambda t: self.visit_literal("BOOLEAN_LITERAL", \
                                                        BooleanLiteralExp, t),
      "INTEGER_LITERAL" : lambda t: self.visit_literal("INTEGER_LITERAL", \
                                                        IntegerLiteralExp, t),
      "FLOAT_LITERAL"   : lambda t: self.visit_literal("FLOAT_LITERAL", \
                                                        FloatLiteralExp, t),
      "ATOM_LITERAL"    : self.visit_atom_literal,
      "LIST_LITERAL"    : self.visit_list_literal,
      "IDENTIFIER"      : self.visit_identifier
  }

  # visiting an unknown tree, using the dispatch to get to specialized handler
  def visit(self, tree):
    try:
      return self.dispatch[tree.text](tree)
    except KeyError as e:
      print "foo-ast-visitor: missing handler for", e

  # HANDLERS

  def visit_identifier(self, tree):
    assert tree.text == "IDENTIFIER"
    name = tree.getChildren()[0].text
    assert isidentifier(name), "bad identifier name " + name
    return Identifier(name)

  def visit_root(self, tree):
    assert tree.text == "ROOT"
    for child in tree.getChildren():
      self.visit(child)

  def visit_module(self, tree):
    assert tree.text == "MODULE"
    children = tree.getChildren()
    id       = self.visit(children[0])
    module   = Module(id)
    
    # by default a module contains the Nodes domain
    # more generic this could be triggered by a USE <domain> instruction
    module.domains['nodes'] = Nodes()
    
    self.model.modules[id.name] = module
    self.current_module         = module

    if len(children) > 1:
      for index in range(1,len(children)):
        self.visit(children[index])
    return module

  def visit_constant(self, tree):
    assert tree.text == "CONST"
    children = tree.getChildren()
    name     = self.visit(children[0])
    type   = self.visit(children[1])
    value  = self.visit(children[2])
    constant = Constant(name, value, type)
    self.current_module.constants.append(constant)
    return constant

  def visit_extend(self, tree):
    assert tree.text == "EXTEND"
    children  = tree.getChildren()
    domain    = self.visit_domain(children[0])
    obj       = self.visit_object_literal(children[1])
    extension = Extension(domain, obj)
    self.current_module.domains[domain.name].extend(extension)
    return extension
  
  def visit_import(self, tree):
    assert tree.text == "IMPORT"
    children = tree.getChildren()
    module   = self.visit(children[0])
    function = self.visit(children[1])
    self.current_module.externals[function.name] = function
  
  def visit_annotated(self, tree):
    assert tree.text == "ANNOTATED"
    children   = tree.getChildren()
    [annotation, arguments] = self.visit_annotation(children[0])
    [scope, function]       = self.visit_annotated_execution(children[1])

    self.add_execution(annotation, scope, function, arguments)

  def visit_annotation(self, tree):
    assert tree.text == "ANNOTATION"
    children = tree.getChildren()
    return {
      'every': ['Every', [self.visit_variable_exp(children[1].getChildren()[0])]]
    }[children[0].getChildren()[0].text]  # FIXME: ugly with ID in between

  # two executions are supported currently:
  # 1. application of function to scope
  # 2. (simple) function in global scope (NOT IMPLEMENTED YET)
  # TODO: implement simple function support
  def visit_annotated_execution(self, tree):
    return {
      'APPLY': self.visit_application(tree)  # returns [scope, function]
    }[tree.text]
  
  def visit_application(self, tree):
    assert tree.text == "APPLY"
    children = tree.getChildren()
    scope    = self.as_scope(self.visit(children[0]))
    function = self.visit(children[1])
    return [scope, function]

  def visit_domain(self, tree):
    assert tree.text == "DOMAIN"
    domain = self.visit(tree.getChildren()[0])
    return self.current_module.domains[domain.name]

  def visit_anon_func_decl(self, tree):
    assert tree.text == "ANON_FUNC_DECL"
    children   = tree.getChildren()
    parameters = self.visit_parameters(children[0])
    body       = self.visit(children[1])
    function   = FunctionDecl(body, parameters=parameters)
    self.current_module.functions.append(function)
    return function

  def visit_func_decl(self, tree):
    assert tree.text == "FUNC_DECL"
    children   = tree.getChildren()
    name       = self.visit(children[0])
    if len(children) > 2:
      parameters = self.visit_parameters(children[1])
      body       = self.visit(children[2])
    else:
      parameters = []
      body       = self.visit(children[1])
    function   = FunctionDecl(body, identifier=name, parameters=parameters)
    self.current_module.functions.append(function)
    return function

  def visit_func_proto(self, tree):
    assert tree.text == "FUNC_PROTO"
    children   = tree.getChildren()
    name       = self.visit(children[0])
    type       = self.visit(children[1])
    if len(children) > 2:
      parameter_types = self.visit_parameter_types(children[2])
    else:
      parameter_types = []
    prototype = FunctionDecl(BlockStmt(), identifier=name, parameters=parameter_types)
    prototype.type = type
    return prototype

  def visit_parameters(self, tree):
    assert tree.text == "PARAMS"
    parameters = tree.getChildren()
    return [Parameter(self.visit(parameter)) for parameter in parameters]

  def visit_parameter_types(self, tree):
    assert tree.text == "PARAMS"
    parameter_types = tree.getChildren()
    return [Parameter(Identifier("name"+str(index)), type=self.visit(parameter_type)) \
              for index, parameter_type in enumerate(parameter_types)]

  def visit_event_handler_decl(self, tree):
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

  def visit_block_stmt(self, tree):
    assert tree.text == "BLOCK"
    statements = tree.getChildren()
    return BlockStmt([self.visit(statement) for statement in statements])

  def visit_if_stmt(self, tree):
    assert tree.text == "IF"
    children  = tree.getChildren()
    condition = self.visit(children[0])
    true      = self.visit(children[1])
    if len(children) > 2:
      false   = self.visit(children[2])
    else:
      false   = None
    return IfStmt(condition, true, false)

  def visit_cases_stmt(self, tree):
    assert tree.text == "CASES"
    children     = tree.getChildren()
    expression   = self.visit(children[0])
    cases        = []
    case_else    = None
    for index in range(1,len(children)):
      if children[index].getChildren()[0].text == "else":
        case_else = self.visit_case_else(children[index])
      else:
        cases.append(self.visit_case(children[index]))
    [cases, consequences] = zip(*cases)
    return CaseStmt(expression, cases, consequences, case_else)

  def visit_case(self, tree):
    assert tree.text == "CASE"
    children       = tree.getChildren()
    function_name  = self.visit(children[0])
    if len(children) > 2:
      arguments = self.visit_arguments(children[1])
      function  = FunctionCallExp(FunctionExp(function_name), arguments)
      body      = self.visit(children[2])
    else:
      function = FunctionCallExp(function_name)
      body     = self.visit(children[1])
    return [function, body]

  def visit_case_else(self, tree):
    assert tree.text == "CASE"
    children = tree.getChildren()
    body     = self.visit(children[1])
    return body

  def visit_inc_stmt(self, tree):
    assert tree.text == "INC"
    target = self.visit(tree.getChildren()[0])
    return IncStmt(target)

  def visit_dec_stmt(self, tree):
    assert tree.text == "DEC"
    target = self.visit(tree.getChildren()[0])
    return DecStmt(target)

  def visit_bin_stmt(self, text, constructor, tree):
    assert tree.text == text
    children = tree.getChildren()
    left     = self.visit(children[0])
    right    = self.visit(children[1])
    return constructor(left, right)

  def visit_return_stmt(self, tree):
    assert tree.text == "RETURN"
    return ReturnStmt()

  # references -> expressions

  def visit_object_ref(self, tree):
    assert tree.text == "OBJECT_REF"
    children = tree.getChildren()
    obj = ObjectExp(self.visit(children[0]))
    if len(children) > 1:
      for prop in children[1:]:
        obj = PropertyExp(obj, self.visit(prop))
    return obj

  def visit_function_ref(self, tree):
    assert tree.text == "FUNC_REF"
    return FunctionExp(self.visit(tree.getChildren()[0]))

  # EXPRESSIONS

  def visit_property_exp(self, tree):
    assert tree.text == "PROPERTY_EXP"
    children = tree.getChildren()
    obj      = self.visit(children[0])
    prop     = self.visit(children[1])
    # TODO: make more generic
    if isinstance(obj, Domain):
      return obj.get_property(prop.name)
    else:
      return PropertyExp(obj, prop)

  def visit_match_exp(self, tree):
    assert tree.text == "MATCH_EXP"
    children = tree.getChildren()
    if children[0].text == "ANYTHING":
      return MatchExp(AnythingExp())
    else:
      # first child is a string representation of the comparator-operator
      # second child is an expression: the right operand of the comparator
      return MatchExp(Comparator(children[0].text), self.visit(children[1]))

  def visit_variable_exp(self, tree):
    assert tree.text == "VAR_EXP"
    children = tree.getChildren()
    name = self.visit(tree.getChildren()[0])
    if len(children) > 1:
      type = self.visit(tree.getChildren()[1])
      return VariableExp(name, type)
    return VariableExp(name)

  def visit_type_exp(self, tree):
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
    except KeyError: pass
    return ObjectType(identifier)

  def visit_unknown_type(self, tree):
    assert tree.text == "UNKNOWN_TYPE"
    return UnknownType()

  def visit_many_type_exp(self, tree):
    assert tree.text == "MANY_TYPE_EXP"
    type = self.visit(tree.getChildren()[0])
    return ManyType(type)

  def visit_amount_type_exp(self, tree):
    assert tree.text == "AMOUNT_TYPE_EXP"
    type = self.visit(tree.getChildren()[0])
    size = int(tree.getChildren()[1].text)
    return AmountType(type, size)

  def visit_tuple_type_exp(self, tree):
    assert tree.text == "TUPLE_TYPE_EXP"
    types = [self.visit(type) for type in tree.getChildren()]
    return TupleType(types)

  def visit_not_exp(self, tree):
    assert tree.text == "!"
    return NotExp(self.visit(tree.getChildren()[0]))

  # GENERIC FUNCTION FOR BINARY EXPRESSIONS

  def visit_bin_exp(self, text, constructor, tree):
    assert tree.text == text
    children = tree.getChildren()
    left     = self.visit(children[0])
    right    = self.visit(children[1])
    return constructor(left, right)

  # CALLING
  
  def visit_function_call(self, tree):
    assert tree.text == "FUNC_CALL"
    children  = tree.getChildren()
    function  = self.visit(children[0])
    if len(children) > 1:
      arguments = self.visit_arguments(children[1])
      return FunctionCallExp(FunctionExp(function), arguments)
    else:
      return FunctionCallExp(FunctionExp(function))

  def visit_method_call(self, tree):
    assert tree.text == "METHOD_CALL"
    children = tree.getChildren()
    obj      = self.visit(children[0])
    method   = self.visit(children[1])
    if len(children) > 2:
      arguments = self.visit_arguments(children[2])
      return MethodCallExp(obj, method, arguments)
    else:
      return MethodCallExp(obj, method)

  def visit_arguments(self, tree):
    assert tree.text == "ARGS"
    arguments = tree.getChildren()
    return [self.visit(argument) for argument in arguments]

  # TYPES

  def visit_literal(self, text, constructor, tree):
    assert tree.text == text
    return constructor(tree.getChildren()[0].text)

  def visit_atom_literal(self, tree):
    assert tree.text == "ATOM_LITERAL"
    return AtomLiteralExp(self.visit(tree.getChildren()[0]))

  def visit_list_literal(self, tree):
    assert tree.text == "LIST_LITERAL"
    children = tree.getChildren()
    return ListLiteralExp([self.visit(child) for child in children])

  def visit_object_literal(self, tree):
    assert tree.text == "OBJECT_LITERAL"
    obj = ObjectLiteralExp()
    for child in tree.getChildren():
      obj.properties.append(self.visit_property_literal(child))
    return obj

  def visit_property_literal(self, tree):
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

# SEMANTIC VISITOR
#
# Implements the SemanticVisitorBase with handlers to visit all parts of the
# Semantic Model. This can be done in a top-down or bottom-up approach.
# While doing so, it constructs a stack of visited parts and an environment of
# declared entities (Variables, Objects,...)

class SemanticVisitor(SemanticVisitorBase):
  def __init__(self, warn_unhandled=False, visit_internal_types=True):
    self.prefix               = None
    self._stack               = []
    self.env                  = Environment()
    self.warn_unhandled       = warn_unhandled
    self.visit_internal_types = visit_internal_types

  def get_stack(self): return self._stack
  stack = property(get_stack)
  
  def stack_as_string(self):
    return " > ".join([str(obj) for obj in self._stack])

  # HANDLERS IMPLEMENTING VISITOR and adding a handle call

  @stacked
  @with_handling
  def visit_Identifier(self, id): pass

  @stacked
  @with_handling
  def visit_Model(self, model):
    for module in model.modules.values():
      module.accept(self)

  @stacked
  @with_handling
  def visit_Domain(self, domain):
    self.env[domain.name] = domain
    
  @stacked
  @with_handling
  def visit_Scope(self, scope): pass

  @stacked
  @with_handling
  def visit_Module(self, module):
    self.env.extend()
    for constant in module.constants:
      constant.accept(self)
    
    for name, function in module.externals.items():
      self.env[name] = function
    
    for domain in module.domains:
      domain.accept(self)
      for extension in domain.extensions:
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
  @with_handling
  def visit_Constant(self, constant):
    self.env[constant.name] = constant

  @stacked
  @with_handling
  def visit_Extension(self, extension):
    extension.domain.accept(self)
    extension.extension.accept(self)

  @stacked
  @with_handling
  def visit_Every(self, execution):
    execution.interval.accept(self)
    execution.scope.accept(self)
    execution.executed.accept(self)

  @stacked
  @with_handling
  def visit_When(self, execution):
    execution.scope.accept(self)
    execution.event.accept(self)
    execution.executed.accept(self)

  @stacked
  @with_handling
  def visit_FunctionDecl(self, function):
    self.env[function.name] = function
    self.env.extend()
    function.type.accept(self)
    for param in function.parameters:
      param.accept(self)
    function.body.accept(self)
    self.env.reduce()

  @stacked
  @with_handling
  def visit_Parameter(self, parameter):
    self.env[parameter.name] = parameter
    parameter.type.accept(self)

  # STATEMENTS

  @stacked
  @with_handling
  def visit_BlockStmt(self, block):
    self.env.extend()
    for statement in block.statements:
      statement.accept(self)
    self.env.reduce()

  @stacked
  @with_handling
  def visit_AssignStmt(self, stmt):
    stmt.value.accept(self)
    stmt.variable.accept(self)

  @stacked
  @with_handling
  def visit_AddStmt(self, stmt):
    stmt.variable.accept(self)
    stmt.value.accept(self)
  
  @stacked
  @with_handling
  def visit_SubStmt(self, stmt):
    stmt.variable.accept(self)
    stmt.value.accept(self)

  @stacked
  @with_handling
  def visit_IncStmt(self, stmt):
    stmt.variable.accept(self)

  @stacked
  @with_handling
  def visit_DecStmt(self, stmt):
    stmt.variable.accept(self)

  @stacked
  @with_handling
  def visit_IfStmt(self, stmt):
    stmt.condition.accept(self)
    stmt.true.accept(self)
    if stmt.false != None:
      stmt.false.accept(self)

  @stacked
  @with_handling
  def visit_CaseStmt(self, stmt):
    stmt.expression.accept(self)
    for case, consequence in zip(stmt.cases, stmt.consequences):
      self.env.extend()
      case.accept(self)
      consequence.accept(self)
      self.env.reduce()

  @stacked
  @with_handling
  def visit_ReturnStmt(self, stmt):
    if stmt.expression != None:
      stmt.expression.accept(self)
    
  # EXPRESSIONS
  
  @stacked
  @with_handling
  def visit_BooleanLiteralExp(self, exp): pass
    
  @stacked
  @with_handling
  def visit_IntegerLiteralExp(self, exp): pass

  @stacked
  @with_handling
  def visit_FloatLiteralExp(self, exp): pass

  @stacked
  @with_handling
  def visit_AtomLiteralExp(self, atom): pass

  @stacked
  @with_handling
  def visit_UnknownType(self, lst): pass

  def visit_AnyType(self, type): pass
  def visit_MixedType(self, type): pass
  def visit_AtomType(self, type): pass

  @stacked
  @with_handling
  def visit_ListLiteralExp(self, lst):
    if self.visit_internal_types: lst.type.accept(self)
    for exp in lst.expressions:
      exp.accept(self) 

  @stacked
  @with_handling
  def visit_ObjectLiteralExp(self, obj):
    for prop in obj.properties:
      prop.accept(self)

  @stacked
  @with_handling
  def visit_Property(self, prop):
    if prop.type != None:
      prop.type.accept(self)
    prop.value.accept(self)

  # types

  @stacked
  @with_handling
  def visit_VoidType(self, type): pass

  @stacked
  @with_handling
  def visit_BooleanType(self, type): pass

  @stacked
  @with_handling
  def visit_ByteType(self, type): pass

  @stacked
  @with_handling
  def visit_IntegerType(self, type): pass

  @stacked
  @with_handling
  def visit_FloatType(self, type): pass

  @stacked
  @with_handling
  def visit_LongType(self, type): pass

  @stacked
  @with_handling
  def visit_TimestampType(self, type): pass

  @stacked
  @with_handling
  def visit_ManyType(self, many):
    many.subtype.accept(self)

  @stacked
  @with_handling
  def visit_AmountType(self, many):
    many.subtype.accept(self)
    
  @stacked
  @with_handling
  def visit_TupleType(self, tuple):
    for type in tuple.types:
      type.accept(self)

  @stacked
  @with_handling
  def visit_VariableExp(self, var):
    # on first use, a variable is self-instantiating
    try:
      prev = self.env[var.name]
    except KeyError:
      # print "AUTO-DECL", var.name, "Stack=", self.stack_as_string(), "Env=", str(self.env)
      self.env[var.name] = var
    var.identifier.accept(self)
    var.type.accept(self)
  
  @stacked
  @with_handling
  def visit_PropertyExp(self, prop):
    prop.obj.accept(self)
    prop.identifier.accept(self)
    prop.type.accept(self)

  @stacked
  @with_handling
  def visit_UnaryExp(self, exp):
    exp.operand.accept(self)

  @stacked
  @with_handling
  def visit_BinaryExp(self, exp):
    exp.left.accept(self)
    exp.right.accept(self)

  @stacked
  @with_handling
  def visit_NumericBinaryExp(self, exp):
    exp.left.accept(self)
    exp.right.accept(self)

  @stacked
  @with_handling
  def visit_FunctionCallExp(self, exp):
    exp.function.accept(self)
    exp.type.accept(self)
    for arg in exp.arguments:
      arg.accept(self)

  @stacked
  @with_handling
  def visit_FunctionExp(self, exp): pass

  @stacked
  @with_handling
  def visit_ObjectExp(self, exp):
    exp._type.accept(self)

  @stacked
  @with_handling
  def visit_ObjectType(self, obj): pass

  @stacked
  @with_handling
  def visit_MethodCallExp(self, exp):
    exp.object.accept(self)
    exp.type.accept(self)
    for arg in exp.arguments:
      arg.accept(self)

  @stacked
  @with_handling
  def visit_AnythingExp(self, exp): pass

  @stacked
  @with_handling
  def visit_MatchExp(self, exp):
    exp.operator.accept(self)
    if exp.operand != None:
      exp.operand.accept(self)

  @with_handling
  def visit_Comparator(self, comp): pass

  

# SEMANTIC CHECKER
#
# wraps the SemanticVisitor adding:
#
# - assertion methods
# - tracking of failures and successes
# - visualisation of the stack

class SemanticChecker(SemanticVisitor):
  def __init__(self, model, verbose=True, warn_unhandled=False, visit_internal_types=True):
    super(SemanticChecker, self).__init__(warn_unhandled=warn_unhandled,
                                          visit_internal_types=visit_internal_types)
    self.model   = model
    self.name    = "foo-" + self.__class__.__name__.lower()
    self.verbose = verbose

  def check(self):
    if self.verbose: print self.name + ": processing model"
    self.start();
    self.model.accept(self)
    self.stop()
    return { "successes": self.successes, "failures": self.fails }

  def start(self):
    self.fails = 0
    self.successes = 0

  def stop(self):
    self.report()

  def report(self):
    if not self.verbose: return
    print_stderr( "-" * 79 )

    result = "SUCCESS - model is valid" if self.fails == 0 \
             else "FAILURES : " + str(self.fails)
    info   = "SUCCESSES: " + str(self.successes) if self.successes != 0 \
             else None

    self.log("results of run", result, info)
    print_stderr( "-" * 79 )

  def fail(self, msg, *args):
    self.fails += 1
    self.log("failure: " + msg + " : " + " ".join([str(arg) for arg in args]),
             "stack:\n" + self.stack_as_string(),
             "env:\n" + str(self.env))

  def success(self, msg, *args):
    self.successes += 1
    if self.verbose:
      self.log("success: " + msg + " : " + " ".join([str(arg) for arg in args]))

  def log(self, msg1, *msgs):
    print_stderr(self.name + ": " + msg1.replace("\n", "\n      "))
    for msg in msgs:
      if not msg is None:
        print_stderr( "    " + msg.replace("\n", "\n      "))

  # ASSERTIONS HELPERS

  def assertIsNotNone(self, obj, msg, *info):
    if obj is None:
      self.fail(msg, *info)

  def assertNotIsInstance(self, obj, instance, msg, *info):
    if isinstance(obj, instance):
      self.fail(msg, *info)

  def assertIsInstance(self, obj, instance, msg, *info):
    if not isinstance(obj, instance):
      self.fail(msg, *info)

  def assertEqual(self, left, right, msg, *info):
    if left != right:
      self.fail(msg, *info)
