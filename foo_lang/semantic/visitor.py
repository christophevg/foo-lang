# visitor.py
# author: Christophe VG

# Visitor for converting a tree into model
# Note: trying to create a tree grammar to do this seemed harder in the end

import sys

from foo_lang.semantic.constant    import Constant
from foo_lang.semantic.types       import Object, Property
from foo_lang.semantic.model       import Module, Extension
from foo_lang.semantic.domain      import Domain, Scope
from foo_lang.semantic.execution   import Every
from foo_lang.semantic.expressions import VariableExp

class Visitor():
  def __init__(self, model):
    self.model = model

    # local scoping helper
    self.current_module = None

    # mapping top-node's text to handler (aka poor man's visitor pattern)
    self.dispatch = {
      "ROOT"      : self.handle_root,
      "MODULE"    : self.handle_module,
      "CONST"     : self.handle_constant,
      "IMPORT"    : self.handle_import,
      "EXTEND"    : self.handle_extend,
      "ANNOTATED" : self.handle_annotated,
      "DOMAIN"    : self.handle_domain,
      "PROPERTY"  : self.handle_property
      # "APPLY"     : self.handle_application
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
      'every': ['Every', self.handle_variable(children[1].getChildren()[0])]
    }[children[0].text]

  def handle_variable(self, tree):
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
    return obj.get_property(prop)

  # HELPERS

  # makes sure that the argument is a scope
  def as_scope(self, obj):
    if isinstance(obj, Scope):
      return obj
    elif isinstance(obj, Domain):
      return obj.get_scope()
    else:
      raise RuntimeError("Un-scopable object:", obj)

  # extract a name-type-value tuple
  def tree2ntv(self, tree):
    assert tree.text == "VALUE"
    children = tree.getChildren()
    assert children[1].text == "TYPE"
    # TODO convert value to actual number, ...
    return [children[0].text, 
            children[1].getChildren()[0].text,
            children[2].text]

  # extract an object
  def tree2object(self, tree):
    assert tree.text == "OBJECT"
    obj = Object()
    children = tree.getChildren()
    for child in children:
      assert child.text == "PROPERTY"
      [name, type, value] = self.tree2ntv(child.getChildren()[0])
      obj.properties.append(Property(name, type, value))
    return obj
