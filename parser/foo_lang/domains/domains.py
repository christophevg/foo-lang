# domains.py
# author: Christophe VG

# Base classes for domains

class Domain():
  def __init__(self):
    pass
  
  def extend_with(self, extension):
    raise NotImplementedError("extend_with")

class Scope():
  def __init__(self, domain):
    self.domain = domain
