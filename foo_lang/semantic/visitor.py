# visitor.py
# author: Christophe VG

# Visitor for converting a tree into model
# Note: trying to create a tree grammar to do this seemed harder in the end

import sys
import traceback

from util.check              import isidentifier
from foo_lang.semantic.model import *     # too many to import explicitly

class Visitor():
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
    parameters = self.handle_parameters(children[1])
    body       = self.visit(children[2])
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
    child = tree.getChildren()[0]
    return TypeExp(self.visit(child))

  def handle_unknown_type(self, tree):
    assert tree.text == "UNKNOWN_TYPE"
    return UnknownType()

  def handle_many_type_exp(self, tree):
    assert tree.text == "MANY_TYPE_EXP"
    type = self.visit(tree.getChildren()[0])
    return ManyTypeExp(type)

  def handle_tuple_type_exp(self, tree):
    assert tree.text == "TUPLE_TYPE_EXP"
    types = [self.visit(type) for type in tree.getChildren()]
    return TupleTypeExp(types)

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
