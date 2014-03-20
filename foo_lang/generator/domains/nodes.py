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

    node_type = code.StructuredType("nodes").tag("node_type_def")
    # TODO: add default more information (e.g. address, ...)
    node_type.append(code.Comment("domain properties"),
                     code.Property("id", code.ByteType()),
                     code.Property("address", code.LongType())
                    )
    module = self.generator.unit.append(structure.Module("nodes"))
    module.select("def").append( code.Comment("THE node type"), node_type )
    
    payload_type = code.StructuredType("payload").tag("payload_type_def")
    payload_type.append(
      code.Property("bytes", code.ManyType(code.ByteType())),
      code.Property("size",  code.IntegerType())
    )
    module.select("def").append( code.Comment("THE payload type"), payload_type)
  
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
      event_loop.append(code.FunctionCall("nodes_process_" + f))

    # prepare the payload parser with callbacks for parsing
    parser_init = dec.append(
      code.Function("nodes_parser_init", code.VoidType())
    ).tag("nodes_parser_init")
    module.find("main_function").append(
      code.FunctionCall(parser_init.name).stick_top()
    )

    # wire the receiving of packets to the underlying platform
    self.generator.platform.add_handler("receive",
      call     = "payload_parser_parse",
      module   = module,
      location = "main_function"
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
      # FIXME: this is a bit too local, would nicer at C-level, based on the 
      # definition of the parameters of these functions. not for now ;-)

      # these function call take vararg bytes. we need to convert each non-byte
      # argument to a ListLiteral of corresponding bytes.
      # create function-call
      
      # strategy:
      # AtomLiteral     will be expanded later, so we skip them here
      # ObjectProperty  check/convert property type
      # SimpleVariable  
      # FunctionCall    extract from arguments, assign to variable, convert

      assert isinstance(call.arguments[0], code.ListLiteral)

      # TODO: mark this somehow and move logic to emitter
      #       the UnionType solution is to C-specific - no more time to do it
      #       right :-(

      # rebuild the arguments
      args  = code.ListLiteral()
      temp = 0;
      for index, arg in enumerate(call.arguments[0]):
        # TODO: generalize a bit more - this only support our minimal needs

        if isinstance(arg, code.FunctionCall):
          code.Assign(code.VariableDecl("temp" + str(temp), arg.type), arg) \
              .insert_before(call)
          if isinstance(arg.type, code.AmountType) and \
             isinstance(arg.type.type, code.ByteType):
            for i in range(arg.type.size):
              args.append(code.ListVariable("temp" +str(temp), i))
          temp += 1

        elif isinstance(arg, code.SimpleVariable):
          if str(arg.info) == "TimestampType":
            code.VariableDecl(
              "temp" + str(temp),
              code.UnionType("temp" + str(temp)) \
                  .contains( code.Property("value", code.NamedType("timestamp")),
                             code.Property(
                               "b", code.AmountType(code.ByteType(), 4) # platf?
                             )
                           )
            ).insert_before(call)

            code.Assign(code.StructProperty("temp" + str(temp), "value"), arg) \
              .insert_before(call)

            for i in range(4):
              args.append(
                code.ListVariable(
                  code.StructProperty("temp" + str(temp), "b"),
                  i
                )
              )
            temp += 1
          elif str(arg.info) == "ObjectType(nodes)":
            args.append(code.ObjectProperty(arg.name, "id"))

        elif isinstance(arg, code.ObjectProperty):

          if isinstance(arg.type, code.ByteType):
            args.append(arg)

          elif isinstance(arg.type, code.FloatType):
            code.VariableDecl(
              "temp" + str(temp),
              code.UnionType("temp" + str(temp)) \
                  .contains( code.Property("value", code.FloatType() ),
                             code.Property(
                               "b", code.AmountType(code.ByteType(), 4)
                             )
                           )
            ).insert_before(call)

            code.Assign(code.StructProperty("temp" + str(temp), "value"), arg) \
              .insert_before(call)

            for i in range(4):
              args.append(
                code.ListVariable(
                  code.StructProperty("temp" + str(temp), "b"),
                  i
                )
              )
            temp += 1

        else: args.append(arg)

      # replace by functioncall
      return code.FunctionCall("nodes_" + call.method.name, [args])

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

            handler.append(code.Comment("extract variables from payload"))
            # declare matching local variables from case
            # NOTE: these are inside a ListLiteral
            for arg in case.arguments[0]:
              if isinstance(arg, code.Variable):
                code_type = self.translate(arg.info)
                # TODO: generalize this more
                code_type_name = {
                  "NamedType {'name': 'timestamp'}": lambda: code_type.name,
                  "ByteType"                       : lambda: "byte",
                  # TODO: amount has type, should be recursively extracted
                  # TODO:            size
                  "AmountType {}"                  : lambda: "bytes",
                  "ObjectType {'name': 'nodes'}"   : lambda: code_type.name[:-1],
                  "FloatType"                      : lambda: "float"
                }[str(code_type)]()
                # TODO: size should be generalized
                args = [code.IntegerLiteral(code_type.size)] \
                          if code_type_name == "bytes" else []
                handler.append(
                  code.Assign(
                    code.VariableDecl(arg.name, code_type),
                    code.FunctionCall("payload_parser_consume_" + code_type_name,
                      type=code_type, arguments=args)
                  )
                )

            # add consequence
            handler.append(code.Comment("perform handling actions"))
            for stmt in consequence:
              handler.append(stmt)

            self.stack[0].find("nodes_main").select("dec").append(handler)

            # register the handle for the literals in the case
            arguments = code.ListLiteral()
            for arg in case.arguments[0]:
              if isinstance(arg, code.Literal):
                arguments.append(arg)
            registration = code.FunctionCall("payload_parser_register",
              [ code.SimpleVariable(handler.name), arguments ]
            )
            self.stack[0].find("nodes_parser_init").append(registration)

          # remove the case
          self.stack[-2].remove_child(self.child)
    except Exception, e:
      print e
