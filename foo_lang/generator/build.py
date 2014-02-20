# build.py
# author: Christophe VG

# module for constructing a generator

import os
import sys
import pprint

import foo_lang.code.emitters.C as C
import foo_lang.code.builders   as build

from foo_lang.code.instructions import *

class Generator():
  def __init__(self, args):
    self.verbose  = args.verbose

    assert args.language == "c"
    self.language = C.Emitter()

    self.output   = args.output

    # reserved for future use
    self.platform = args.platform

    self.domain_generators = {}

  def __str__(self):
    return "generating to " + self.output + " using " + self.language + \
                     " on " + self.platform

  def generate(self, model):
    if not os.path.exists(self.output): os.makedirs(self.output)
    files = self.transform(model)
    for name, code in files.items():
      file_name = os.path.join(self.output, name + "." + self.language.ext())
      if self.verbose: print "foo-gen: creating", file_name
      file = open(file_name, 'w+')
      file.write(code.accept(self.language) + "\n")
      file.close()

  def transform(self, model):
    """
    Transforms a model in a collection of modules consisting of code
    """
    modules         = self.create_modules(model)
    modules['main'] = self.create_main_module(model)
    return modules

  def create_modules(self, model):
    """
    Creates a module for each domain/module pair.
    """
    modules = {}
    
    for domain_name, domain in model.domains.items():
      domain_generator = self.generator_for_domain(domain_name)
      for module_name, module in model.modules.items():
        code = domain_generator.create(module, model)
        name = domain_name + "-" + module_name
        if self.verbose: print "creating " + name
        modules[name] = code

    return modules

  def create_main_module(self, model):
    """
    Creates the top-level main module.
    """
    module = build.Module(builders=["event_loop"])

    # init
    init = build.Function("init", "void")
    module.instructions.append(init)
    init.body.append(Comment("add framework init here"))

    # main
    main = build.Function("main", "int")
    module.instructions.append(Comment("starting point"))
    module.instructions.append(main)
    main.body.append(build.Call("init"));

    module.event_loop = build.EventLoop()
    
    # allow each domain generator to alter the main module
    for domain_name, domain in model.domains.items():
      domain_generator = self.generator_for_domain(domain_name)
      domain_generator.transform(module, name="main")

    # insert event loop
    main.body.append(module.event_loop.code())

    return module.code()

  def generator_for_domain(self, domain_name):
    """
    Lazy-Dynamic-Loading of Domain Generators, based on the Semantic Domain name
    """
    if domain_name not in self.domain_generators:
      class_name = domain_name.capitalize()
      module = __import__( "foo_lang.generator.domains." + domain_name, 
                           fromlist=[class_name])
      clazz = getattr(module, class_name)
      self.domain_generators[domain_name] = clazz()

    return self.domain_generators[domain_name]
