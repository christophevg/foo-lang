# types.py
# author: Christophe VG

# Implementations of types

class Object():
  def __init__(self):
    self.properties = []

  def __repr__(self):
    return "{\n" + \
            "\n".join([ str(property) for property in self.properties]) + \
            "\n}"

class Property():
  def __init__(self, name, type, value):
    self.name  = name
    self.type  = type
    self.value = value
  
  def __repr__(self):
    return self.name + " : " + self.type + " = " + self.value
