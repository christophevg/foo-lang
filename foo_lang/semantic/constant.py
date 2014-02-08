# constant.py
# author: Christophe VG

# Part of the semantic model

from foo_lang.semantic.model import base

class Constant(base):
  def __init__(self, name, type, value):
    self.name  = name
    self.type  = type
    self.value = value

  def to_string(self, indent):
    return "  " * indent + \
           "const " + str(self.name) \
           + ((" : " + str(self.type)) if self.type != None else "") \
           + " = " + str(self.value)
