# transformer.py
# visitor to transform Semantic Model elements into Code Model elements
# author: Christophe VG

from foo_lang.semantic.visitor import SemanticChecker

import codecanvas.instructions as code

class Transformer(SemanticChecker):
  def __init__(self):
    super(Transformer, self).__init__(None, True)

  def transform(self, tree):
    self.model = tree
    
    # we use a stack to populate it with transformed elements and then reduce
    # it again constructing higher level constructs after lowerl level 
    # constructs are handled
    self.code = []

    self.verbose = False
    self.check()

    # the final answer should be on the stack and it should be the only thing
    assert len(self.code) <= 1, "Bad codestack length : " + str(len(self.code))
    try: code = self.code.pop()
    except IndexError: code = None
    
    # assert not code is None, "Got no result from transformation."
    return code

  # general
  
  def after_visit_Identifier(self, id):
    self.code.append(code.Identifier(id.name))

  # types
  
  def after_visit_VoidType(self, type):
    self.code.append(code.VoidType())

  def after_visit_IntegerType(self, type):
    self.code.append(code.IntegerType())

  def after_visit_FloatType(self, type):
    self.code.append(code.FloatType())

  def after_visit_LongType(self, type):
    self.code.append(code.LongType())

  def after_visit_BooleanType(self, type):
    self.code.append(code.BooleanType())

  def after_visit_ByteType(self, type):
    self.code.append(code.ByteType())
    
  def before_visit_TimestampType(self, type):
    self.code.append(code.NamedType("timestamp"))

  def after_visit_ManyType(self, type):
    subtype = self.code.pop()
    self.code.append(code.ManyType(subtype))

  def after_visit_TupleType(self, type):
    types = []
    for i in range(len(type.types)):
      types.append(self.code.pop())
    self.code.append(code.TupleType(list(reversed(types))))

  # literals

  def after_visit_BooleanLiteralExp(self, literal):
    self.code.append(code.BooleanLiteral(literal.value))

  def after_visit_IntegerLiteralExp(self, literal):
    self.code.append(code.IntegerLiteral(literal.value))

  def after_visit_FloatLiteralExp(self, literal):
    self.code.append(code.FloatLiteral(literal.value))

  # expressions

  def after_visit_VariableExp(self, var):
    # FIXME? non-consistent behaviour, not visiting Identifier
    # id = self.code.pop()
    self.code.append(code.SimpleVariable(var.name))

  # statements

  def after_visit_AssignStmt(self, stmt):
    # MIND that the visitor first visits the value, and only then the variable!!
    operand    = self.code.pop()
    expression = self.code.pop()
    self.code.append(code.Assign(operand, expression))
  
  def after_visit_BlockStmt(self, stmt): pass
    # blockstmt's are no relevant, the parent should handle it's children
    # previously contained in the blockstmt

  # declarations
  
  def before_visit_FunctionDecl(self, function):
    # TODO: we should be able to remove this ;-)
    # add the function as a placeholder on the code stack
    self.code.append(function)
  
  def after_visit_FunctionDecl(self, function):
    body = []
    
    stmt = self.code.pop()

    # first pop stmts
    while isinstance(stmt, code.Statement):
      body.append(stmt)
      stmt = self.code.pop()
    # next pop parameters
    params = []
    while isinstance(stmt, code.Parameter):
      params.append(stmt)
      stmt = self.code.pop()
    type = stmt
    stmt = self.code.pop()
    assert stmt is function
    # construct
    f = code.Function(function.name, type=type, params=list(reversed(params)))
    for stmt in list(reversed(body)):
      f.append(stmt)
    self.code.append(f)

  def after_visit_Parameter(self, parameter):
    # TODO: grmbl: identifier is not handled consistently again ;-(
    type = self.code.pop()
    self.code.append(code.Parameter(parameter.name, type))
  
"""
  def before_visit_ObjectType(self, type):
    if self.current is None: return
    self.current.type = NamedType(type.name)
"""
