# nodes.py
# author: Christophe VG

# Nodes domain implementation

from foo_lang.generator.domain import Domain

import foo_lang.code.builders     as build
import foo_lang.code.instructions as code

from foo_lang.code.transform import Transformer

from foo_lang.code.canvas import Section, Part, Snippet

class Nodes(Domain):
  def prepare(self):
    # prepare content for nodes.h
    node_type = build.StructuredType("node")
    # TODO: add default more information (e.g. address, ...)
    node_type.append(code.Comment("domain properties"))
    node_type.append(code.PropertyDecl(code.Identifier("address"), code.LongType()))
    self.generator.canvas.tag("node_type_def", node_type)
    self.generator.canvas.append(Section("nodes")) \
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
    if section.tag("nodes_main"): return
    # prepare top-level actions in event_loop
    section.tagged("event_loop").body.append(code.Comment("nodes logic execution hooks"))
    for f in ["all", "outgoing"]:
      section.part("dec").append(Snippet(content=build.Function("nodes_process_" + f, "void")))
      section.tagged("event_loop").body.append(build.Call("nodes_process_" + f))
    # wire processing of incoming frames to our nodes handler
    receive_handler = build.Function("nodes_process_" + f, "void")
    section.part("dec").append(Snippet(content=receive_handler))
    self.generator.platform.add_handler("receive",
      function=receive_handler,
      location=section.tagged("main_function").body
    )


  def populate(self, section, module):
    self.add_import_nodes(section)

    # add extensions to node_t definition
    section.tagged("node_type_def") \
      .append(code.Comment("extended properties for " + module.name))
    for ext in module.domains["nodes"].extensions:
      section.tagged("node_type_def").apply(ext.extension)

    # create all functions
    for function in module.functions:
      section.part("dec").append(Snippet(content=Transformer(function).transform()))

  def add_import_nodes(self, section):
    # add import of nodes' domain functionality
    if section.tag("nodes_imported"): return
    section.part("def").append(Snippet(content=code.Import("nodes")))
