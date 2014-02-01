# visitor.py
# author: Christophe VG

# Visitor for converting tree into model

from constant import Constant
from types import Object, Property

class Visitor():
  def __init__(self, model):
    self.model = model
    self.dispatch = {
      "ROOT"      : self.handle_root,
      "CONST"     : self.handle_constant,
      "EXTEND"    : self.handle_extend,
      "IMPORT"    : self.handle_import,
      "ANNOTATED" : self.handle_annotated,
      "APPLY"     : self.handle_application
    }

  # visiting an unknown tree, using the dispatch to get to specialized handler
  def visit(self, tree):
    try:
      return self.dispatch[tree.text](tree)
    except KeyError as e:
      print "TODO: handle", e
      pass

  # handle the root
  def handle_root(self, tree):
    for child in tree.getChildren():
      self.visit(child)
    return None

  # handle a constant definition
  def handle_constant(self, tree):
    [name, type, value] = self.tree2ntv(tree.getChildren()[0])
    constant = Constant(name,type,value)
    self.model.constants.append(constant)
    return Constant

  # apply extensions to domains
  def handle_extend(self, tree):
    children = tree.getChildren()
    domain_name = children[0].text
    extension = self.tree2object(children[1])
    self.model.domain.extensions.append(extension)
    return None
  
  # keep track of imports
  def handle_import(self, tree):
    children = tree.getChildren()
    module   = children[0].text
    function = children[1].text
    self.model.externals[function] = module
    return None
  
  # record an annotation for a subtree
  def handle_annotated(self, tree):
    assert tree.text == "ANNOTATED"
    children = tree.getChildren()
    annotated = self.visit(children[1])
    return None
  
  #
  def handle_application(self, tree):
    assert tree.text == "APPLY"
    
    return None
  
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
    obj = Object()
    children = tree.getChildren()
    for child in children:
      assert child.text == "PROPERTY"
      [name, type, value] = self.tree2ntv(child.getChildren()[0])
      obj.properties.append(Property(name, type, value))
    return obj