# build.py
# module for constructing a generator
# author: Christophe VG

import os

from foo_lang.code.canvas import CodeCanvas, Section, Part, Snippet

import foo_lang.code.instructions as code
import foo_lang.code.builders     as build
import foo_lang.code.emitters.C   as C


class Generator():
  def __init__(self, args):
    self.verbose  = args.verbose

    assert args.language == "c", "Only C language is currently implemented."
    self.language = C.Emitter(self)

    self.output   = args.output

    self.canvas   = CodeCanvas()

    # reserved for future use
    self.platform = self.get_platform(args.platform)

    self.domain_generators = {}
    
  def __str__(self):
    return "generating to " + self.output + " using " + self.language + \
                     " on " + self.platform

  def generate(self, model):
    self.transform(model)
    self.persist()

  def persist(self):
    if not os.path.exists(self.output): os.makedirs(self.output)
    for name, module in self.canvas.items():
      for style, content in module.items():
        file_name = os.path.join(self.output, name + "." + self.language.ext(style))
        if self.verbose: print "foo-gen: creating", file_name
        file = open(file_name, 'w+')
        for code in content:
          try: file.write(code.content.accept(self.language) + "\n")
          except: pass
        file.close()

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
        section = self.canvas.append(Section(name))
        section.append(Part("dec"))
        section.append(Part("def"))

        domain_generator.populate(section, module)

  def create_main_module(self, model):
    """
    Creates the top-level main module.
    """
    section      = self.canvas.append(Section("main"))
    declarations = section.append(Part("dec"))
    definitions  = section.append(Part("def"))

    # init
    init = build.Function("init", "void")
    init.body.append(code.Comment("add framework init here"))
    declarations.append(Snippet("init", init))

    # app
    app = build.Function("application_step", "void")
    app.body.append(code.Comment("add application specific code here"))
    declarations.append(Snippet("app", app))

    # main
    main = build.Function("main", "int")
    self.canvas.tag("main_function", main)
    declarations.append(Snippet(content=code.Comment("starting point")))
    declarations.append(Snippet("main", content=main))

    # construct a builder and hook it into the main function
    event_loop = build.EventLoop()
    main.body.append(event_loop)
    # tagged for access by domain generators
    self.canvas.tag("event_loop", event_loop)
    
    # add the app specific hook to the event loop
    event_loop.body.append(code.Comment("your application gets its share"))
    event_loop.body.append(build.Call("app"))

    # allow each domain generator to alter the main section
    for mod in model.modules.values():
      for domain_name, domain in mod.domains.items():
        domain_generator = self.generator_for_domain(domain_name)
        domain_generator.transform(section)

    main.body.prepend(build.Call("init"))

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
