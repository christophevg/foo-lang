# nodes.py
# author: Christophe VG

# Nodes domain implementation

from foo_lang.semantic.model import *

class Nodes(Domain):

  # statically defined for reference - another quick hack ;-
  payload_t = ObjectType(Identifier("payload"))
  payload_t.provides["contains"] = \
    FunctionDecl(BlockStmt(), identifier=Identifier("contains"), type=BooleanType(),
                 parameters=[Parameter(Identifier("pattern"), ManyType(ByteType()))])

  def __init__(self):
    self.scoping = {
      "*"    : AllNodes(self),
      "self" : OwnNode(self)
    }
    self.extensions = []

    # instantiated because different extensions exist in each module
    self.node_t = ObjectType(Identifier("nodes"))

    self.type = self.node_t
    
    # default property (don't expose id!!!)
    self.node_t.provides["address"] = \
      VariableExp(Identifier("address"), type=self.node_t)

    # methods
    self.node_t.provides["foreach_node"] = \
      FunctionDecl(BlockStmt(), identifier=Identifier("foreach_node"), type=VoidType(),
                   parameters=[Parameter(Identifier("node"), self.node_t)])

    self.node_t.provides["broadcast"] = \
      FunctionDecl(BlockStmt(), identifier=Identifier("broadcast"), type=VoidType(),
                   parameters=[Parameter(Identifier("payload"), Nodes.payload_t)])

    self.node_t.provides["transmit"] = \
      FunctionDecl(BlockStmt(), identifier=Identifier("transmit"),  type=VoidType(),
                   parameters=[Parameter(Identifier("from"),    self.node_t),
                               Parameter(Identifier("hop"),     self.node_t),
                               Parameter(Identifier("to"),      self.node_t),
                               Parameter(Identifier("payload"), Nodes.payload_t)
                              ])
    self.node_t.provides["send"] = \
      FunctionDecl(BlockStmt(), identifier=Identifier("transmit"),  type=VoidType(),
                   parameters=[Parameter(Identifier("payload"), Nodes.payload_t)])
    self.node_t.provides["receive"] = \
      FunctionDecl(BlockStmt(), identifier=Identifier("receive"),   type=VoidType(),
                   parameters=[Parameter(Identifier("node"),    self.node_t),
                               Parameter(Identifier("sender"),  self.node_t),
                               Parameter(Identifier("from"),    self.node_t),
                               Parameter(Identifier("hop"),     self.node_t),
                               Parameter(Identifier("to"),      self.node_t),
                               Parameter(Identifier("payload"), Nodes.payload_t)
                              ])

  def get_scope(self, name="*"):
    return self.scoping[name]

  def extend(self, extension):
    assert isinstance(extension, Extension)
    self.extensions.append(extension)
    for prop in extension.extension.properties:
      if prop.identifier.name in self.node_t.provides:
        raise KeyError, "node_type already has definition for " + prop.identifier.name
      self.node_t.provides[prop.identifier.name] = prop

  def get_type(self, name):
    try:
      return {
               "node":    self.node_t,
               "payload": Nodes.payload_t
             }[name]
    except KeyError:
      "Nodes domain only supports the 'node' and 'payload' types."      

class AllNodes(Scope):
  def __init__(self, domain):
    super(AllNodes, self).__init__(domain)
    self.scope = "nodes"

  def get_property(self, name):
    prop = self.domain.node_t[name]
    assert isinstance(prop, Property), "Not a property " + name

  def get_function(self, name="foreach_node"):
    return self.domain.node_t.provides[name]

  def get_type(self):
    return self.domain.get_type("node")
  type = property(get_type)
  
class OwnNode(Scope):
  def __init__(self, domain):
    super(OwnNode, self).__init__(domain)
    self.scope = "nodes.self"

  def get_property(self, name):
    prop = self.domain.node_t[name]
    assert isinstance(prop, Property), "Not a property " + name

  def get_function(self, name="foreach_node"):
    assert name in ["foreach_node", "transmit", "receive"], "OwnNodes doesn't support function " + name
    return self.domain.node_t.provides[name]

  def get_type(self):
    return self.domain.get_type("node")
  type = property(get_type)
