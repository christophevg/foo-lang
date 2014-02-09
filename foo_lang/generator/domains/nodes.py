# nodes.py
# author: Christophe VG

# Nodes domain implementation

from foo_lang.generator.domain import Domain, Scope

class Nodes(Domain):
  def __init__(self):
    pass
  
class AllNodes(Scope):
  def __init__(self, domain):
    Scope.__init__(self,domain)
  
class OwnNode(Scope):
  def __init__(self, domain):
    Scope.__init__(self, domain)
