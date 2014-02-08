# visitor.py
# author: Christophe VG

# Visitor for converting a tree into model
# Note: trying to create a tree grammar to do this seemed harder in the end

import sys

from foo_lang.semantic.constant    import Constant
from foo_lang.semantic.types       import Object, Property
from foo_lang.semantic.model       import Module, Extension, Function
from foo_lang.semantic.domain      import Domain, Scope
from foo_lang.semantic.execution   import Every
from foo_lang.semantic.expressions import *   # too many to import explicitly
from foo_lang.semantic.statements  import *

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
      "PROPERTY"        : self.handle_property,
      "ANON_FUNC_DECL"  : self.handle_anon_func_decl,

      "BLOCK"           : self.handle_block_stmt,
      "IF"              : self.handle_if_stmt,
      "INC"             : self.handle_inc_stmt,
      "DEC"             : self.handle_dec_stmt,
      "="               : self.handle_assign_stmt,

      "OBJECT_REF"      : self.handle_object_ref,

      "VAR"             : self.handle_variable_exp,

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
      
      "FUNC_CALL"       : self.handle_function_call,
      
      "BOOLEAN_LITERAL" : self.handle_boolean_literal
    }

  # visiting an unknown tree, using the dispatch to get to specialized handler
  def visit(self, tree):
    try:
      return self.dispatch[tree.text](tree)
    except KeyError as e:
      print "TODO: handle", e
      pass

  # HANDLERS

  def handle_root(self, tree):
    assert tree.text == "ROOT"
    for child in tree.getChildren():
      self.visit(child)
    return None

  def handle_module(self, tree):
    assert tree.text == "MODULE"
    children = tree.getChildren()
    name     = children[0].text
    module   = Module(name)
    self.model.modules[name] = module
    self.current_module      = module
    for index in range(1,len(children)):
      self.visit(children[index])
    return module

  def handle_constant(self, tree):
    assert tree.text == "CONST"
    [name, type, value] = self.tree2ntv(tree.getChildren()[0])
    constant            = Constant(name,type,value)
    self.current_module.constants[constant.name] = constant
    return constant

  def handle_extend(self, tree):
    assert tree.text == "EXTEND"
    children  = tree.getChildren()
    domain    = children[0].text
    # TODO: change to handle_object_literal
    obj       = self.tree2object(children[1])
    extension = Extension(domain, obj)
    self.current_module.extensions.append(extension)
    return extension
  
  def handle_import(self, tree):
    assert tree.text == "IMPORT"
    children = tree.getChildren()
    module   = children[0].text
    function = children[1].text
    self.current_module.externals[function] = module
    return None
  
  def handle_annotated(self, tree):
    assert tree.text == "ANNOTATED"
    children   = tree.getChildren()
    [annotation, arguments] = self.handle_annotation(children[0])
    [scope, function]       = self.handle_annotated_execution(children[1])

    module   = sys.modules["foo_lang.semantic.execution"]
    clazz    = getattr(module, annotation)
    strategy = clazz(scope, function, arguments)

    self.current_module.executions.append(strategy)
    return None

  def handle_annotation(self, tree):
    assert tree.text == "ANNOTATION"
    children = tree.getChildren()
    return {
      'every': ['Every', self.handle_variable_exp(children[1].getChildren()[0])]
    }[children[0].text]

  def handle_variable_exp(self, tree):
    assert tree.text == "VAR"
    return VariableExp(tree.getChildren()[0].text)

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
    return self.model.domains[tree.getChildren()[0].text]

  def handle_property(self, tree):
    assert tree.text == "PROPERTY"
    children = tree.getChildren()
    obj      = self.visit(children[0])
    prop     = children[1].text
    # TODO: make more generic
    if isinstance(obj, Domain):
      return obj.get_property(prop)
    else:
      return PropertyExp(obj, prop)

  # TODO: make generic to handle also named function decl
  def handle_anon_func_decl(self, tree):
    assert tree.text == "ANON_FUNC_DECL"
    children  = tree.getChildren()
    arguments = [arg.text for arg in children[0].getChildren()]
    body      = self.visit(children[1])
    function  = Function(body, arguments=arguments)
    self.current_module.functions[function.name] = function
    return function

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

  def handle_inc_stmt(self, tree):
    assert tree.text == "INC"
    target = self.visit(tree.getChildren()[0])
    return IncStmt(target)

  def handle_dec_stmt(self, tree):
    assert tree.text == "INC"
    target = self.visit(tree.getChildren()[0])
    return DecStmt(target)

  def handle_assign_stmt(self, tree):
    assert tree.text == "="
    children = tree.getChildren()
    left     = self.visit(children[0])
    right    = self.visit(children[1])
    return AssignStmt(left, right)

  # ??? :-)

  def handle_object_ref(self, tree):
    assert tree.text == "OBJECT_REF"
    # TODO: use something more specific?!
    return VariableExp(tree.getChildren()[0].text)

  # GENERIC FUNCTION FOR BINARY EXPRESSIONS

  def handle_bin_exp(self, text, constructor, tree):
    assert tree.text == text
    children = tree.getChildren()
    left     = self.visit(children[0])
    right    = self.visit(children[1])
    return constructor(left, right)

  # FUNCTIONS
  
  def handle_function_call(self, tree):
    assert tree.text == "FUNC_CALL"
    children  = tree.getChildren()
    function  = children[0].text
    if len(children) > 1:
      arguments = self.as_list(self.handle_list(children[1]))
      return FunctionCallExp(function, arguments)
    else:
      return FunctionCallExp(function)

  # TYPES

  def handle_boolean_literal(self, tree):
    assert tree.text == "BOOLEAN_LITERAL"
    return BooleanLiteralExp(tree.getChildren()[0].text)

  def handle_list(self, tree):
    assert tree.text == "LIST"
    children = tree.getChildren()
    return ListLiteral([self.visit(child) for child in children])

  # HELPERS

  def as_list(self, list_exp):
    assert instanceof(list_exp, ListLiteral)
    return list_exp.expressions

  # makes sure that the argument is a scope
  def as_scope(self, obj):
    if isinstance(obj, Scope):
      return obj
    elif isinstance(obj, Domain):
      return obj.get_scope()
    else:
      raise RuntimeError("Un-scopable object:", obj)

  # extract a name-type-value tuple
  # TODO: should become handle_named_typed_value
  def tree2ntv(self, tree):
    assert tree.text == "VALUE"
    children = tree.getChildren()
    assert children[1].text == "TYPE"
    # TODO convert value to actual number, ...
    return [children[0].text, 
            children[1].getChildren()[0].text,
            children[2].text]

  # extract an object
  # TODO: should become handle_object_literal
  def tree2object(self, tree):
    assert tree.text == "OBJECT"
    obj = Object()
    children = tree.getChildren()
    for child in children:
      assert child.text == "PROPERTY"
      [name, type, value] = self.tree2ntv(child.getChildren()[0])
      obj.properties.append(Property(name, type, value))
    return obj
