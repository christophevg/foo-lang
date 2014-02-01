# model.py
# author: Christophe VG

# The semantic model container

import os, sys, inspect

# use this if you want to include modules from a subforder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"domains")))
if cmd_subfolder not in sys.path:
  sys.path.insert(0, cmd_subfolder)

from nodes import Nodes

class Model():
  def __init__(self):
    self.constants = []
    self.externals = {} # function => module (unique function names)

    # set up the functional domain
    self.domain = Nodes()

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
    string += str(self.domain) + "\n"

    return string
