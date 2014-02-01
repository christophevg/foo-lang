# base.py
# author: Christophe VG

# Base class for all domain classes

class base():
  def __init__(self):
    pass

  def extend_with(self, extension):
    raise NotImplementedError("extend_with")
