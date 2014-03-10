# translator.py
# visitor to translate Semantic Model elements into Code Model elements
# author: Christophe VG

from foo_lang.semantic.visitor import SemanticChecker

import codecanvas.instructions as code
import foo_lang.semantic.model as model

class Translator(SemanticChecker):
  def __init__(self):
    super(Translator, self).__init__(None, True, warn_unhandled=True, visit_internal_types=False)

  def translate(self, tree):
    self.model = tree
    
    # we use a stack to populate it with translated elements and then reduce
    # it again constructing higher level constructs after lowerl level 
    # constructs are handled
    self.code = []

    self.verbose = False
    self.check()

    # the final answer should be on the stack and it should be the only thing
    assert len(self.code) <= 1, "Bad codestack length : " + str(len(self.code))
    try: code = self.code.pop()
    except IndexError: code = None
    
    # assert not code is None, "Got no result from translateation."
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

  def after_visit_AtomLiteralExp(self, literal):
    self.code.append(code.AtomLiteral(literal.name))

  def before_visit_ListLiteralExp(self, placeholder):
    self.code.append(placeholder)

  def after_visit_ListLiteralExp(self, placeholder):
    items = []
    while not self.code[-1] is placeholder:
      items.append(self.code.pop())
    self.code.pop() # placeholder
    l = code.ListLiteral()
    for item in list(reversed(items)):
      l.append(item)
    self.code.append(l)      

  # expressions

  def after_visit_VariableExp(self, var):
    # FIXME? non-consistent behaviour, not visiting Identifier
    # id = self.code.pop()
    self.code.append(code.SimpleVariable(var.name))

  def after_visit_ObjectExp(self, obj):
    # TODO: it seems that ObjectType is also pushed ?!
    self.code.pop()
    self.code.append(code.Object(obj.name))

  def after_visit_PropertyExp(self, prop):
    obj = self.code.pop()
    self.code.append(code.ObjectProperty(obj, code.Identifier(prop.name)))

  # statements

  def after_visit_AssignStmt(self, stmt):
    # MIND that the visitor first visits the value, and only then the variable!!
    operand    = self.code.pop()
    expression = self.code.pop()
    self.code.append(code.Assign(operand, expression))
  
  def before_visit_BlockStmt(self, placeholder):
    self.code.append(placeholder)

  def after_visit_BlockStmt(self, placeholder):
    if not len(self.code): return
    stmts = []
    while not self.code[-1] is placeholder:
      stmts.append(self.code.pop())
    self.code.pop() # placeholder
    # storing/grouping the block statement's children as a list on the stack
    if len(stmts) > 0:
      self.code.append(list(reversed(stmts)))

  # declarations
  
  def after_visit_FunctionDecl(self, function):
    # the body was appended as a block stmt == list on the stack
    body = self.code.pop()

    # next pop parameters
    params = []
    while len(self.code) and isinstance(self.code[-1], code.Parameter):
      params.append(self.code.pop())

    # return type
    if len(self.code): type = self.code.pop()
    else:              type = None

    # construct
    f = code.Function(function.name, type=type, params=list(reversed(params)))
    for stmt in body: f.append(stmt)

    self.code.append(f)

  def after_visit_Parameter(self, parameter):
    # TODO: grmbl: identifier is not handled consistently again ;-(
    type = self.code.pop()
    self.code.append(code.Parameter(parameter.name, type))

  def after_visit_ObjectType(self, obj):
    self.code.append(code.ObjectType(obj.name))

  def after_visit_FunctionExp(self, func):
    self.code.append(code.Identifier(func.name))

  def after_visit_FunctionCallExp(self, call):
    # argument-expressions were pushed onto the code stack after a single
    # function-identifier.
    args = []
    while isinstance(self.code[-1], code.Expression):
      args.append(self.code.pop())
    assert isinstance(self.code[-1], code.Identifier)
    function = self.code.pop()
    self.code.append(code.FunctionCall(function, list(reversed(args))))

  def before_visit_MethodCallExp(self, placeholder):
    self.code.append(placeholder)

  def after_visit_MethodCallExp(self, placeholder):
    args = []
    while not self.code[-2] is placeholder:
      args.append(self.code.pop())
    obj    = self.code.pop()
    self.code.pop()  # placeholder
    method = placeholder.identifier.name
    self.code.append(code.MethodCall(obj, method, list(reversed(args))))

  def after_visit_UnaryExp(self, exp):
    operand = self.code.pop()
    self.code.append(
      {
        "NotExp" : code.Not
      }
    [exp.__class__.__name__](operand))

  def after_visit_BinaryExp(self, exp):
    right = self.code.pop()
    left  = self.code.pop()
    self.code.append(
      {
        "AndExp"       : code.And,
        "OrExp"        : code.Or,
        "EqualsExp"    : code.Equals,
        "NotEqualsExp" : code.NotEquals,
        "LTExp"        : code.LT,
        "LTEQExp"      : code.LTEQ,
        "GTExp"        : code.GT,
        "GTEQExp"      : code.GTEQ,
        "PlusExp"      : code.Plus,
        "MinusExp"     : code.Minus,
        "MultExp"      : code.Mult,
        "DivExp"       : code.Div,
        "ModuleExp"    : code.Modulo
      }[exp.__class__.__name__](left, right))

  def after_visit_IncStmt(self, stmt):
    var = self.code.pop()
    self.code.append(code.Inc(var))

  def after_visit_DecStmt(self, stmt):
    var = self.code.pop()
    self.code.append(code.Dec(var))

  def after_visit_AddStmt(self, stmt):
    value = self.code.pop()
    var   = self.code.pop()
    self.code.append(code.Add(var, value))

  def after_visit_SubStmt(self, stmt):
    value = self.code.pop()
    var   = self.code.pop()
    self.code.append(code.Sub(var, value))

  def after_visit_MatchExp(self, exp):
    if isinstance(self.code[-1], code.Anything):
      expression = None
    else:
      expression = self.code.pop()
    comp = self.code.pop()
    self.code.append(code.Match(comp, expression))
    
  def after_visit_Comparator(self, comp):
    self.code.append(code.Comparator(comp.operator))

  def after_visit_AnythingExp(self, comp):
    self.code.append(code.Anything())

  def before_visit_IfStmt(self, stmt):
    self.code.append(stmt)

  def after_visit_IfStmt(self, placeholder):
    # code stack = condition [true] [false]?
    if self.code[-3] is placeholder:
      false = []
    else:
      false = self.code.pop()
    true      = self.code.pop()
    condition = self.code.pop()
    self.code.pop() # placeholder
    self.code.append(code.IfStatement(condition, true, false))

  def after_visit_ReturnStmt(self, stmt):
    self.code.append(code.Return())

  def before_visit_CaseStmt(self, placeholder):
    self.code.append(placeholder)

  def after_visit_CaseStmt(self, placeholder):
    # code stack = expression [case [consequence]]
    cases        = []
    consequences = []
    while not self.code[-2] is placeholder:
      consequences.append(self.code.pop())
      cases.append(self.code.pop())
    expression = self.code.pop()
    self.code.pop() # placeholder
    self.code.append(code.CaseStatement(expression, cases, consequences))
