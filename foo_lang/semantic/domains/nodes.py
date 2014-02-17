# nodes.py
# author: Christophe VG

# Nodes domain implementation

from foo_lang.semantic.model import *

class Nodes(Domain):
  def __init__(self):
    self.scoping = {
      "*"    : AllNodes(self),
      "self" : OwnNode(self)
    }
  def get_function(self, name=None):
    raise RuntimeException("This shouldn't happen ;-)")

class NodesScope(Scope):
  def get_function(self, name=None):
    try:
      # print "NODES: looking for function ", str(name)
      # without a name, we can only return a function that is implemented on
      # one argument: node, something is performed in scope of each single node
      if name is None: return { "type": VoidType(),
                                "params": [ ObjectType(Identifier("node"))]}
      return {
        "receive"  : { "type": VoidType(),
                       "params": [ ObjectType(Identifier("node")),
                                   ObjectType(Identifier("node")),
                                   ManyType(ManyType(ByteType())) ] },
        "transmit" : { "type": VoidType,
                       "params": [ ObjectType(Identifier("node")),
                                   ObjectType(Identifier("node")),
                                   ObjectType(Identifier("node")),
                                   ManyType(ManyType(ByteType())) ] }
      }[name]
    except KeyError:
      print "WARNING: requested unknown function : node::" + str(name)
      pass
    return None

class AllNodes(NodesScope):
  def __init__(self, domain):
    Scope.__init__(self, domain)
    self.scope = "nodes"

  def get_method(self, name):
    try:
      return {
        "broadcast" : { "type": VoidType(),
                        "params": [ ManyType(ManyType(ByteType())) ] }

      }[name]
    except KeyError:
      print "WARNING: requested unknown method : nodes::" + name
      pass
    return None
  
class OwnNode(NodesScope):
  def __init__(self, domain):
    Scope.__init__(self, domain)
    self.scope = "nodes.self"
