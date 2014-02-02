# nodes.py
# author: Christophe VG

# Nodes domain implementation

from domains import Domain, Scope

class Nodes(Domain):
  def __init__(self):
    Domain.__init__(self)
    self.extensions   = []
    
    self.scope = {
                   'nodes'      : AllNodes(self),
                   'nodes.self' : OwnNode(self)
                 }

  def __repr__(self):
    return "\n".join( [ "extend nodes with " + str(ext) \
                        for ext in self.extensions ] )

class AllNodes(Scope):
  def __repr__(self):
    return "nodes"
  
class OwnNode(Scope):
  def __repr__(self):
    return "nodes.self"
