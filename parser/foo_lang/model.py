# model.py
# author: Christophe VG

# The semantic model container

class Model():
  def __init__(self):
    self.constants = []

  # entry point of request for conversion to string
  def __repr__(self):
    string = ""

    for const in self.constants:
      string += str(const) + "\n"

    return string
