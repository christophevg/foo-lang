# types.py
# author: Christophe VG

# Implementations of types

from foo_lang.semantic.model import base

class Object(base):
  def __init__(self):
    self.properties = []

  def to_string(self, level):
    string = "  " * level + "{";
    if self.properties != []: string += "\n"
    for property in self.properties:
      string += "  " * (level+1) + str(property) + "\n"
    string += "  " * level + "}"
    return string

class Property(base):
  def __init__(self, name, type, value):
    self.name  = name
    self.type  = type
    self.value = value
  
  def to_string(self, level):
    return "  " * level + \
           self.name + " : " + self.type + " = " + self.value
