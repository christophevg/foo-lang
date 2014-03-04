# transformer.py
# visitor to transform Semantic Model elements into Code Model elements
# author: Christophe VG

from foo_lang.semantic.visitor import SemanticChecker

from codecanvas.instructions import *

class Transformer(SemanticChecker):

  def transform(self):
    # print "transforming:", self.model
    self.verbose = False
    self.code    = None
    # TODO: probably turn this into stack for larger/deeper structures
    self.current = None
    self.check()
    assert not self.code is None
    return self.code

  def before_visit_FunctionDecl(self, function):
    self.code = Function(function.name)

  def before_visit_Parameter(self, parameter):
    self.current = Parameter(parameter.name)
    self.code.params.append(self.current)
  
  def after_visit_Parameter(self, parameter):
    self.current = None
    
  def before_visit_ObjectType(self, type):
    if self.current is None: return
    self.current.type = NamedType(type.name)

  def after_visit_ManyType(self, many):
    if self.current is None:
      # self.fail("parent transformation not yet implemented for ManyType")
      return
    self.current.type = ManyType(self.current.type)
  
  def before_visit_ByteType(self, byte):
    if self.current is None: self.code         = ByteType()
    else:                    self.current.type = ByteType()

  def before_visit_BooleanType(self, byte):
    if self.current is None: self.code         = BooleanType()
    else:                    self.current.type = BooleanType()

  def before_visit_FloatType(self, byte):
    if self.current is None: self.code         = FloatType()
    else:                    self.current.type = FloatType()

  def before_visit_TimestampType(self, stamp):
    self.code = NamedType("timestamp")

  def visit_Identifier(self, id):
    self.code = Identifier(id.name)
