# build.py
# module for constructing a generator
# author: Christophe VG

import os

from codecanvas.structure import Unit, Module, Section

import codecanvas.instructions as code
import codecanvas.languages.C  as C

from foo_lang.code.translate import Translator

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
    self.create_constants(model)
    self.create_modules(model)
    self.create_main_module(model)

  def create_constants(self, model):
    module  = self.unit.append(Module("constants"))
    defines = module.select("def")
    for module in model.modules.values():
      for constant in module.constants:
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
    Creates the top-level main module.
    """
    module = self.unit.append(Module("main"))

    # init
    init = code.Function("init", code.VoidType()) \
             .contains(code.Comment("add framework init here"))

    # app
    app = code.Function("application_step", code.VoidType()) \
            .contains(code.Comment("add application specific code here"))

    # main
    main = code.Function("main", code.IntegerType()).tag("main_function")
    module.select("dec").append(init,
                                app,
                                code.Comment("starting point"),
                                main)

    main.append(code.FunctionCall("init")).stick_top()

    # construct an event_loop builder and hook it into the main function
    event_loop = code.WhileDo(code.BooleanLiteral(True))
    main.append(event_loop).tag("event_loop") \
        .append(code.Comment("your application gets its share"),
                code.FunctionCall("application_step"))

    # allow each domain generator to extend the main section
    for mod in model.modules.values():
      for domain_name, domain in mod.domains.items():
        self.generator_for_domain(domain_name).extend(module)

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
