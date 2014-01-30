# visitor.py
# author: Christophe VG

# Visitor for converting tree into model

from constant import Constant

import os, sys, inspect

# use this if you want to include modules from a subforder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"domains")))
if cmd_subfolder not in sys.path:
  print cmd_subfolder
  sys.path.insert(0, cmd_subfolder)

from nodes import nodes

class Visitor():
  def __init__(self, model):
    self.model = model
    self.dispatch = {
      "ROOT"  : self.handle_root,
      "CONST" : self.handle_constant,
      "USE"   : self.handle_use
    }

  # visiting an unknown tree, using the dispatch to get to specialized handler
  def visit(self, tree):
    try:
      self.dispatch[tree.text](tree)
    except KeyError as e:
      print "TODO: handle", e
      pass

  # handle the root
  def handle_root(self, tree):
    for child in tree.getChildren():
      self.visit(child)

  # handle a constant definition
  def handle_constant(self, tree):
    children = tree.getChildren()
    if len(children) == 2:
      name  = children[0].text
      type  = None
      value = children[1].text
    elif len(children) == 3:
      name  = children[0].text
      type  = children[1].getChildren()[0].text
      value = children[2].text
    else:
      raise RuntimeError("const has incorrect childnodes")
    
    self.model.constants.append(Constant(name,type,value))

  def handle_use(self, tree):
    domain_name   = tree.getChildren()[0].text
    domain_module = __import__(domain_name)
    domain_class  = getattr(domain_module, domain_name)
    domain        = domain_class()

    self.model.domains.append(domain)
