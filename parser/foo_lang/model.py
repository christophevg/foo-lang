# model.py
# author: Christophe VG

# The semantic model container

class Model():
  def __init__(self):
    self.constants = []
    self.domains   = []

  # entry point of request for conversion to string
  def __repr__(self):
    string = ""

    # constants
    for const in self.constants:
      string += str(const) + "\n"

    # domains
    for domain in self.domains:
      string += str(domain) + "\n"

    return string
