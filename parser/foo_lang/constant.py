# constant.py
# author: Christophe VG

# Part of the semantic model

from base import base

class Constant(base):
  def __init__(self, name, type, value):
    self.name  = name
    self.type  = type
    self.value = value

  def __repr__(self):
    return "const " + self.name \
           + ((" : " + self.type) if self.type != None else "") \
           + " = " + self.value
