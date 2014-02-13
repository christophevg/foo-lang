# nodes.py
# author: Christophe VG

# Nodes domain implementation

from foo_lang.semantic.model import Domain, Scope

class Nodes(Domain):
  def __init__(self):
    self.scoping = {
      "*"    : AllNodes(self),
      "self" : OwnNode(self)
    }
  
class AllNodes(Scope):
  def __init__(self, domain):
    Scope.__init__(self, domain)
    self.scope = "nodes"
  
class OwnNode(Scope):
  def __init__(self, domain):
    Scope.__init__(self, domain)
    self.scope = "nodes.self"
