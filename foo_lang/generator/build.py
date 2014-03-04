# build.py
# module for constructing a generator
# author: Christophe VG

import os

from codecanvas.structure import Unit, Module, Section

import codecanvas.instructions as code
import codecanvas.languages.C  as C

import foo_lang.code.builders  as build

class Generator():
  def __init__(self, args):
    self.verbose  = args.verbose

    assert args.language == "c", "Only C language is currently implemented."
    self.output   = args.output
    self.language = C.Emitter().output_to(self.output)
    self.unit     = Unit()
    self.platform = self.get_platform(args.platform)

    self.domain_generators = {}
    
  def __str__(self):
    return "generating to " + self.output + " using " + str(self.language) + \
                     " on " + str(self.platform)

  def generate(self, model):
    self.transform(model)
    self.language.emit(self.unit)

  def transform(self, model):
    """
    Transforms a model in snippets of CodeModels on the CodeCanvas
    """
    self.create_modules(model)
    self.create_main_module(model)

  def create_modules(self, model):
    """
    Creates a module for each domain/module pair.
    """
    for module_name, module in model.modules.items():
      for domain_name, domain in module.domains.items():
        domain_generator = self.generator_for_domain(domain_name)
        name = domain_name + "-" + module_name
        if self.verbose: print "creating " + name
        # construct section
        domain_generator.populate(self.unit.append(Module(name)), module)

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

    # construct an event_loop builder and hook it into the main function
    event_loop = code.WhileDo(code.BooleanLiteral(True))
    main.append(event_loop).tag("event_loop") \
        .append(code.Comment("your application gets its share"),
                code.FunctionCall("application_step"))

    # allow each domain generator to alter the main section
    for mod in model.modules.values():
      for domain_name, domain in mod.domains.items():
        self.generator_for_domain(domain_name).transform(module)

    main.append(code.FunctionCall("init"))

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
    return clazz(self)

  def get_class(self, module_name, class_name):
    module = __import__( module_name, fromlist=[class_name])
    return getattr(module, class_name)
