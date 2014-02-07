# nodes.py
# author: Christophe VG

# Nodes domain implementation

from foo_lang.semantic.domain import Domain, Scope

class Nodes(Domain):
  def __init__(self):
    Domain.__init__(self)
    self.extensions   = []
    
    self.scope = {
                   "nodes"      : AllNodes(self),
                   "nodes.self" : OwnNode(self)
                 }

  def to_string(self, level):
    return "  " * level + "nodes"
  
class AllNodes(Scope):
  def __init__(self, domain):
    Scope.__init__(self,domain)
    self.scope = "nodes"
  
class OwnNode(Scope):
  def __init__(self, domain):
    Scope.__init__(self, domain)
    self.scope = "nodes.self"
