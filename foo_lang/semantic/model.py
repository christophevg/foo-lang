# model.py
# author: Christophe VG

# Technical base class for all semantic model classes
class base():
  # entry point of request for conversion to string
  def __repr__(self):
    return self.to_string(0)

  def to_string(self, level):
    raise RuntimeError("WARNING: need to implement to_string(self, indent)")


# The semantic model container
class Model(base):
  def __init__(self):
    self.modules    = {}

    # set up the functional domain, all of them and the current one ;-)
    self.domains = {}

    # self.executions = []

  # entry point of request for conversion to string
  def to_string(self, level):
    string = ""
    for module in self.modules:
      string += self.modules[module].to_string(level)
    return string

# Modules represent input files, a model manages multiple
class Module(base):
  def __init__(self, name):
    self.name       = name
    self.constants  = {}
    self.extensions = []
    self.externals  = {}   # function : library
    self.functions  = {}
  
  def to_string(self, level):
    string = "module " + self.name + "\n";
    
    for constant in self.constants:
      string += self.constants[constant].to_string(level) + "\n"

    for extension in self.extensions:
      string += extension.to_string(level) + "\n"
    
    for function in self.externals:
      string += "from " + self.externals[function] + " import " + function + "\n"

    for function in self.functions:
      string += self.functions[function].to_string(level)

    return string

class Extension(base):
  def __init__(self, domain, extension=None):
    self.domain    = domain
    self.extension = extension

  def to_string(self, level):
    if self.extension != None:
      return "extend " + str(self.domain) + \
             " with " + self.extension.to_string(level)
    else:
      return ""

class Function(base):
  anonymous = 0
  def __init__(self, name, arguments, body):
    if name == None:
      name = "anonymous" + str(Function.anonymous)
      Function.anonymous += 1
    self.name      = name
    self.arguments = arguments
    self.body      = body

  def to_string(self, level):
    string = "function"
    if self.name != None:
      string += " " + str(self.name)
    string +=  "(" + ", ".join([str(arg) for arg in self.arguments]) + ") " + \
               self.body.to_string(level).lstrip()
    return string
