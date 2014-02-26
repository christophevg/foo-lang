# nodes.py
# author: Christophe VG

# Nodes domain implementation

from foo_lang.generator.domain import Domain

import foo_lang.code.builders as build

from foo_lang.code.canvas import Snippet

class Nodes(Domain):
  
  def transform(self, section):
    {
      "main": self.transform_main
    }[section.name](section)

  def transform_main(self, section):
    self.add_import_nodes(section)
    section.tagged("event_loop").body.append(build.Call("nodes_process"))

  def populate(self, section, module):
    self.add_import_nodes(section)

    # create all functions
    for function in module.functions:
      section.part("dec").append(Snippet(content=build.Function(function.name)))

  def add_import_nodes(self, section):
    # add import of nodes' domain functionality
    if section.tagged("nodes_imported"): return
    section.tag(True, "nodes_imported")
    section.part("def").append(Snippet(content=build.Import("nodes")))
