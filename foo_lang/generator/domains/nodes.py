# nodes.py
# author: Christophe VG

# Nodes domain implementation

from foo_lang.generator.domain import Domain

import codecanvas.instructions as code
import codecanvas.structure    as structure

from foo_lang.semantic.domains.nodes import Nodes as SemanticNodes
from foo_lang.code.transform         import Transformer

class Nodes(Domain):
  def prepare(self):
    """
    Prepares the definition of the node type.
    """
    # this is a generator for the Nodes domain, let's get it ;-)
    self.domain = SemanticNodes()
    
    # we need a transformer
    self.transformer = Transformer()

    node_type = code.StructuredType("node").tag("node_type_def")
    # TODO: add default more information (e.g. address, ...)
    node_type.append(code.Comment("domain properties"),
                     code.Property("address", code.LongType()))
    module = self.generator.unit.append(structure.Module("nodes"))
    module.select("def").append( code.Comment("THE node type"), node_type )
  
  # TODO: naming is yuch ;-)
  def convert(self, tree):
    return self.transformer.transform(tree)
  
  def transform(self, module):
    {
      "main": self.transform_main
    }[module.name](module)

  def transform_main(self, module):
    """
    Transforms the main module by adding nodes functionality to the event_loop.
    """
    self.add_import_nodes(module)
    if not module.find("nodes_main") is None: return
    module.tag("nodes_main")
    
    # get pointers into the code
    dec        = module.select("dec")
    event_loop = module.find("event_loop")

    # prepare top-level actions in event_loop
    event_loop.append(code.Comment("nodes logic execution hooks"))
    for f in ["all", "outgoing"]:
      dec.append(code.Function("nodes_process_" + f, code.VoidType()))
      event_loop.append(code.FunctionCall("nodes_process_" + f))

    # wire processing of incoming frames to our nodes handler
    incoming_handler = dec.append(
      code.Function("nodes_process_incoming", code.VoidType(),
                    [code.Parameter("payload",
                                    self.convert(self.domain.get_type("payload")))
                    ]))

    self.generator.platform.add_handler("receive",
      call     = incoming_handler,
      location = module.find("main_function")
    ).stick_top()

  def populate(self, code_module, module):
    self.add_import_nodes(code_module)

    # add extensions to node_t definition
    node_type = self.generator.unit.find("node_type_def")
    node_type.append(code.Comment("extended properties for " + module.name))

    for ext in module.domains["nodes"].extensions:
      for prop in ext.extension.properties:
        node_type.append(code.Property(prop.name,
                                       self.convert(prop.type)))

    # create all functions
    for function in module.functions:
      code_module.select("dec").append(self.convert(function))

  def add_import_nodes(self, module):
    """
    Make sure that nodes functionality is imported (once)
    """
    if not module.find("import_nodes") is None: return
    module.select("def").append(code.Import("nodes")).tag("import_nodes")
