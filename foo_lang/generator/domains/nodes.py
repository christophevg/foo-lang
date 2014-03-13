# nodes.py
# author: Christophe VG

# Nodes domain implementation

from util.visitor import stacked

from foo_lang.generator.domain import Domain

import codecanvas.instructions as code
import codecanvas.structure    as structure
import codecanvas.language     as language

from foo_lang.semantic.domains.nodes import Nodes as SemanticNodes
from foo_lang.code.translate         import Translator

class Nodes(Domain):
  def prepare(self):
    """
    Prepares the definition of the node type.
    """
    # this is a generator for the Nodes domain, let's get it ;-)
    self.domain = SemanticNodes()
    
    # we need a translator
    self.translator = Translator()

    node_type = code.StructuredType("node").tag("node_type_def")
    # TODO: add default more information (e.g. address, ...)
    node_type.append(code.Comment("domain properties"),
                     code.Property("address", code.LongType()))
    module = self.generator.unit.append(structure.Module("nodes"))
    module.select("def").append( code.Comment("THE node type"), node_type )
  
  def translate(self, tree):
    return self.translator.translate(tree)
  
  def extend(self, module):
    """
    Add domain specific extensions (e.g. includes, functions, ...)
    """
    {
      "main": self.extend_main
    }[module.name](module)

  def extend_main(self, module):
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
      dec.append(code.Function("nodes_process_" + f, code.VoidType()) \
                  .contains(code.Comment("nodes_process_" + f)))
      event_loop.append(code.FunctionCall("nodes_process_" + f))

    # wire processing of incoming frames to our nodes handler
    incoming_handler = dec.append(
      code.Function("nodes_process_incoming", code.VoidType(),
                    [code.Parameter("from", code.ObjectType("node")),
                     code.Parameter("to", code.ObjectType("node")),
                     code.Parameter("payload",
                                    self.translate(self.domain.get_type("payload"))),
                     code.Parameter("length", code.IntegerType())
                    ]).tag("nodes_process_incoming"))

    self.generator.platform.add_handler("receive",
      call     = incoming_handler,
      location = module.find("main_function")
    ).stick_top()

  def construct(self, code_module, module):
    """
    Constructs a code_module from a module.
    """
    self.add_import_nodes(code_module)

    # add extensions to node_t definition
    node_type = self.generator.unit.find("node_type_def")
    node_type.append(code.Comment("extended properties for " + module.name))

    for ext in module.domains["nodes"].extensions:
      for prop in ext.extension.properties:
        node_type.append(code.Property(prop.name,
                                       self.translate(prop.type)))

    # create all functions
    for function in module.functions:
      code_module.select("dec").append(self.translate(function))

  def add_import_nodes(self, module):
    """
    Make sure that nodes functionality is imported (once)
    """
    if not module.find("import_nodes") is None: return
    module.select("def").append(code.Import("nodes")).tag("import_nodes")

  def transform(self, unit):
    unit.accept(Transformer())

class Transformer(language.Visitor):
  """
  Visitor for CodeCanvas-based ASTs to add/remove code automagically.
  """

  def __init__(self):
    # TODO: use a backlink to generator ?
    super(Transformer, self).__init__()
    self.translator = Translator()
    # this is a Transformer for the Nodes domain, let's get it ;-)
    self.domain = SemanticNodes()

  def translate(self, tree):
    return self.translator.translate(tree)

  @stacked
  def visit_MethodCall(self, call):
    """
    Methodcalls to the nodes domain are rewritten to function-calls.
    """
    if isinstance(call.obj, code.Object) and call.obj.name == "nodes":
      # create function-call
      function = code.FunctionCall("nodes_" + call.method.name, call.arguments)
      # replace
      return function

  processors = 0
  @stacked
  def visit_CaseStatement(self, stmt):
    """
    CaseStatements may be used to handle incoming payloads. These should be
    centralized in the processing of incoming payloads. Payload references are
    found in the case.expression.type == semantic.Nodes.payload_t.
    We now support the typical case with a contains() function. For each of
    these we generate a function based on the consequence, accepting a payload,
    positioned where it contains information following the case condition.
    The case condition's literals are added as to-find literals and a reference
    to the handling function is also registered with a general purpose byte-
    stream parser/state machine.
    """
    try:
      # TODO: take into account execution strategy
      # TODO: only supported now: SimpleVariable
      if isinstance(stmt.expression, code.SimpleVariable):
        if stmt.expression.info == SemanticNodes.payload_t:
          # move handling to centralized processing of incoming data
          for case, consequence in zip(stmt.cases, stmt.consequences):
            # create a function that processes matched payload
            handler = code.Function(
              "nodes_process_incoming_case_" + str(Transformer.processors),
              params=[ code.Parameter("from",    code.ObjectType("node")),
                code.Parameter("to",      code.ObjectType("node")),
                code.Parameter("payload", self.translate(self.domain.get_type("payload")))
              ]
            )
            Transformer.processors += 1
            # declare matching local variables from case
            # NOTE: these are inside a ListLiteral
            for arg in case.arguments[0]:
              if isinstance(arg, code.Variable):
                # TODO: TYPE = ObjectType(node)
                handler.append(code.FunctionCall("payload_parser_consume_TODO_Type"))
            # add consequence
            for stmt in consequence: handler.append(stmt)

            self.stack[0].find("nodes_main").select("dec").append(handler)

            # register the handle for the literals in the case
            registration = code.FunctionCall("payload_parser_register")
            self.stack[0].find("nodes_process_incoming").append(registration)

          # remove the case
          self.stack[-2].remove_child(self.child)
    except Exception, e:
      print e
