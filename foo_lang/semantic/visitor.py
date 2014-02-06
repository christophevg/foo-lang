# visitor.py
# author: Christophe VG

# Visitor for converting a tree into model
# Note: trying to create a tree grammar to do this seemed harder in the end

from foo_lang.semantic.constant import Constant
from foo_lang.semantic.types    import Object, Property
from foo_lang.semantic.model    import Module, Extension

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
      "ANNOTATED" : self.handle_annotated
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
    annotation = self.visit(children[0])
    annotated  = self.visit(children[1])
    # WIP
    return None
  
  # TODO
  def handle_application(self, tree):
    assert tree.text == "APPLY"
    
    return None
  
  # HELPERS

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
