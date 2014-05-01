# build.py
# module for constructing a generator
# author: Christophe VG

import os

from codecanvas.structure import Unit, Module, Section

import codecanvas.instructions as code
import codecanvas.languages.C  as C

from foo_lang.code.translate import Translator

from foo_lang.semantic.domains.nodes import AllNodes

class Generator():
  def __init__(self, args):
    try:    self.verbose = args.verbose
    except: self.verbose = False

    # small limitation for now ;-)
    assert args.language == "c", "Only C language is currently implemented."

    try:    self.output = args.output
    except: self.output = None
    self.platform   = self.get_platform(args.platform)

    # create top-level compilation unit
    self.unit       = Unit()

    # SM->CM translator
    self.translator = Translator()

    # prepare code emitter
    self.language   = C.Emitter(platform=self.platform).output_to(self.output)

    self.domain_generators = {}
    
  def __str__(self):
    return "generating to " + self.output + " using " + str(self.language) + \
                     " on " + str(self.platform)

  def log(self, msg):
    if self.verbose: print "--- " + msg

  def generate(self, model):
    self.construct_code_model(model)
    return self.emit_source()

  def construct_code_model(self, model):
    # construct basic model
    self.construct(model)

    # appy domain transformations to entire unit
    for domain_generator in self.domain_generators.values():
      domain_generator.transform(self.unit)

    return self.unit

  def emit_source(self, unit=None):
    if unit is None: unit = self.unit
    # emit to language
    self.log("starting language emission")
    return self.language.emit(unit)

  def translate(self, part):
    return self.translator.translate(part)

  def construct(self, model):
    """
    Constructs a CodeModel given a SemanticModel.
    """
    self.log("constructing basic code model from semantic model")
    self.create_main_module(model)
    # basic setup is ready, allow platform to add stuff
    self.platform.setup(self.unit)
    
    self.create_constants(model)
    self.create_modules(model)
    self.create_executions(model)

  def create_constants(self, model):
    defines = None
    for module in model.modules.values():
      for constant in module.constants:
        if defines is None:
          defines = self.unit.append(Module("constants")).select("def")
        defines.append(code.Constant(constant.name,
                                     self.translate(constant.value),
                                     self.translate(constant.type)))

  def create_modules(self, model):
    """
    Creates a module for each domain/module pair.
    """
    for module_name, module in model.modules.items():
      for domain_name, domain in module.domains.items():
        domain_generator = self.generator_for_domain(domain_name)
        name = domain_name + "-" + module_name
        self.log("creating " + name)
        # construct section
        domain_generator.construct(self.unit.append(Module(name)), module)

  def create_main_module(self, model):
    """
    Creates the top-level main and includes modules.
    """
    module = self.unit.append(Module("includes"))
    module.select("def").tag("includes")
    # add basic set of includes that apply to all generations, without causing
    # compilation problems
    module.select("def").append(code.Import("<stdint.h>"))

    for mod in model.modules.values():
      if len(mod.constants.items()) > 0:
        module.select("def").append(code.Import("constants"))
        break

    module.select("def").append(code.Import("foo-lib/crypto")).tag("foo-lib-start")
    module.select("def").append(code.Import("foo-lib/time"))
    
    module.select("def").append(code.Import("../lib/network"))

    # MAIN module
    module = self.unit.append(Module("main"))
    module.select("def").append(code.Import("includes"))
    module.select("dec").append(code.Import("main"))

    for domain_module_name, domain_module in model.modules.items():
      for domain_name, domain in domain_module.domains.items():
        name = domain_name + "-" + domain_module_name
        module.select("def").append(code.Import(name))

    # init
    init = code.Function("init").tag("init") \
               .contains(code.Comment("add framework init here"))

    # app
    app = code.Function("application_step") \
              .contains(code.Comment("add application specific code here"))

    # main
    main = code.Function("main", code.NamedType("int")).tag("main_function")
    main.append(code.FunctionCall("init").stick_top())
    main.append(code.Return(code.IntegerLiteral(1))).stick_bottom()

    module.select("dec").append(code.Comment("""init and application_step
can be implemented using application specific needs."""),
                                init,
                                app,
                                code.Comment("""starting point
please don't change anything beyond this point."""),
                                main)

    # construct an event_loop builder and hook it into the main function
    event_loop = code.WhileDo(code.BooleanLiteral(True))
    main.append(event_loop).tag("event_loop") \
        .append(code.Comment("your application gets its share"),
                code.FunctionCall("application_step"))

    # allow each domain generator to extend the main section
    for mod in model.modules.values():
      for domain_name, domain in mod.domains.items():
        self.generator_for_domain(domain_name).extend(module)

  def create_executions(self, model):
    # executions
    for module_name, module in model.modules.items():
      for execution in module.executions:
        self.generator_for_domain("nodes").link_execution(execution)

  def generator_for_domain(self, domain_name):
    """
    Lazy-Dynamic-Loading of Domain Generators, based on the Semantic Domain name
    """
    if domain_name not in self.domain_generators:
      clazz = self.get_class("foo_lang.generator.domains." + domain_name, 
                             domain_name.capitalize())
      self.domain_generators[domain_name] = clazz(self)
      
    return self.domain_generators[domain_name]

  def get_platform(self, platform_name):
    clazz = self.get_class("foo_lang.generator.platforms." + platform_name, 
                           platform_name.capitalize())
    return clazz()

  def get_class(self, module_name, class_name):
    module = __import__( module_name, fromlist=[class_name])
    return getattr(module, class_name)
