# nodes.py
# author: Christophe VG

# Nodes domain implementation

from foo_lang.generator.domain import Domain

import foo_lang.code.builders as build

class Nodes(Domain):
  def sections(self, module):
    return [ "header", "body", "footer" ]
  
  def transform(self, module, name):
    {
      "main": self.transform_main
    }[name](module)

  def transform_main(self, module):
    module.instructions.prepend(build.Function("import_nodes"))
    module.event_loop.body.append(build.Call("nodes_process"))

  def create(self, module, model):
    return build.Module().code()
