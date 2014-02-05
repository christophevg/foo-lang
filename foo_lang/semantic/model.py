# model.py
# author: Christophe VG

# The semantic model container

import os, sys, inspect

from foo_lang.semantic.domains.nodes import Nodes

class Model():
  def __init__(self):
    self.constants  = []
    self.externals  = {}     # function => module (unique function names)

    self.executions = []

    # set up the functional domain, all of them and the current one ;-)
    self.domains = { 'nodes' : Nodes() }
    self.domain = self.domains['nodes']

  # entry point of request for conversion to string
  def __repr__(self):
    string = ""

    # constants
    for const in self.constants:
      string += str(const) + "\n"
    
    # imports
    for function in self.externals:
      string += "from " + self.externals[function] + " import " + function + "\n"

    # domain with extensions
    domain = str(self.domain)
    if domain != "": string += str(self.domain) + "\n"

    # functions & event handlers (optionally with annotations)
    

    return string
