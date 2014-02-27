# nodes.py
# author: Christophe VG

# Nodes domain implementation

from foo_lang.generator.domain import Domain

import foo_lang.code.builders     as build
import foo_lang.code.instructions as code

from foo_lang.code.transform import Transformer

from foo_lang.code.canvas import Section, Part, Snippet

class Nodes(Domain):
  def __init__(self, canvas):
    # prepare content for nodes.h
    node_type = build.StructuredType("node")
    # TODO: add default more information (e.g. address, ...)
    node_type.append(code.Identifier("address"), code.LongType())
    canvas.tag("node_type_def", node_type)
    canvas.append(Section("nodes")) \
          .append(Part("def")) \
          .append([ Snippet(content=code.Comment("node_t across modules")),
                    Snippet("node_type", node_type)
                  ])
  
  def transform(self, section):
    {
      "main": self.transform_main
    }[section.name](section)

  def transform_main(self, section):
    self.add_import_nodes(section)
    if section.tag("nodes_process_call"): return
    section.tagged("event_loop").body.append(build.Call("nodes_process"))

  def populate(self, section, module):
    self.add_import_nodes(section)

    # add extensions to node_t definition
    for ext in module.domains["nodes"].extensions:
      section.tagged("node_type_def").apply(ext.extension)

    # create all functions
    for function in module.functions:
      section.part("dec").append(Snippet(content=Transformer(function).transform()))

  def add_import_nodes(self, section):
    # add import of nodes' domain functionality
    if section.tag("nodes_imported"): return
    section.part("def").append(Snippet(content=code.Import("nodes")))
