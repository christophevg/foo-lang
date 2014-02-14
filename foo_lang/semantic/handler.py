# handler.py
# SemanticVisitor implementation separating the visiting from the handling
# author: Christophe VG

import inspect

from util.visitor import Visitable
from util.check   import isstring

from foo_lang.semantic.model  import SemanticVisitor
from foo_lang.semantic.dumper import Dumper

class SemanticHandler(SemanticVisitor):
  def __init__(self):
    self.prefix = None

  def handle(self, part_name, part):
    if self.prefix != None and self.prefix != "handle_":
      try:
        method = getattr(self, self.prefix + part_name)
        method(part)
      except AttributeError:
        # possibly there is no handler
        # print "not handling", part_name
        pass

  def trace(self):
    """
    Inspects the stack to build a semantic trace to the current point in the
    visiting process.
    """
    config = {
               'FunctionDecl'    : [ 'function',  'name'       ],
               'FunctionCallExp' : [ 'exp',       'function'   ],
               'CaseStmt'        : [ 'stmt',      'expression' ],
               'Every'           : [ 'execution', 'interval'   ],
               'When'            : [ 'execution', 'event'      ],
               'Module'          : [ 'module',    'name'       ],
               'Model'           : False,
               'BlockStmt'       : False
             }
    skip_self = True
    trace = []
    for frame in inspect.stack():
      if frame[3][0:7] == "handle_":
        if skip_self: skip_self = False
        else:
          parent = frame[3][7:]
          # print "parent=", parent
          if parent in config:
            if config[parent]:
              # print "  config=", config[parent][0], config[parent][1]
              local = frame[0].f_locals[config[parent][0]]
              # print "  local=", local
              if config[parent][1] is None:
                attrib = ""
              else:
                attrib = getattr(local, config[parent][1])
              # print "  attrib", attrib
              if isinstance(attrib, Visitable):
                attrib = attrib.accept(Dumper())
              trace.append(parent + "(" + attrib + ")")
          else:
            print "in", parent, frame[0].f_locals
    return trace

  # HANDLERS IMPLEMENTING VISITOR and adding a handle call

  def handle_Model(self, model):
    self.handle('Model', model)
    for module in model.modules.values():
      module.accept(self)

  def handle_Domain(self, domain):
    self.handle('Domain', domain)
    
  def handle_Scope(self, scope):
    self.handle('Scope', scope)

  def handle_Module(self, module):
    self.handle('Module', module)
    for constant in module.constants:
      constant.accept(self)
    
    for extension in module.extensions:
      extension.accept(self)
    
    for execution in module.executions:
      execution.accept(self)

  def handle_Constant(self, constant):
    self.handle('Constant', constant)

  def handle_Extension(self, extension):
    self.handle('Extension', extension)

    extension.domain.accept(self)
    extension.extension.accept(self)

  def handle_Every(self, execution):
    self.handle('Every', execution)
    execution.interval.accept(self)
    execution.scope.accept(self)
    execution.executed.accept(self)

  def handle_When(self, execution):
    self.handle('When', execution)
    execution.scope.accept(self)
    execution.event.accept(self)
    execution.executed.accept(self)

  def handle_FunctionDecl(self, function):
    self.handle('FunctionDecl', function)
    for param in function.parameters:
      param.accept(self)

    function.body.accept(self)

  def handle_Parameter(self, parameter):
    self.handle('Parameter', parameter)

  # STATEMENTS

  def handle_BlockStmt(self, block):
    self.handle('BlockStmt', 'block')
    for statement in block.statements:
      statement.accept(self)

  def handle_AssignStmt(self, stmt):
    self.handle('AssignStmt', stmt)
    stmt.variable.accept(self)
    stmt.value.accept(self)

  def handle_AddStmt(self, stmt):
    self.handle('AddStmt', stmt)
    stmt.variable.accept(self)
    stmt.value.accept(self)
  
  def handle_SubStmt(self, stmt):
    self.handle('SubStmt', stmt)
    stmt.variable.accept(self)
    stmt.value.accept(self)

  def handle_IncStmt(self, stmt):
    self.handle('IncStmt', stmt)
    stmt.variable.accept(self)

  def handle_DecStmt(self, stmt):
    self.handle('DecStmt', stmt)
    stmt.variable.accept(self)

  def handle_IfStmt(self, stmt):
    self.handle('IfStmt', stmt)
    stmt.condition.accept(self)
    stmt.true.accept(self)
    if stmt.false != None:
      stmt.false.accept(self)

  def handle_CaseStmt(self, stmt):
    self.handle('CaseStmt', stmt)
    stmt.expression.accept(self)
    for case, consequence in zip(stmt.cases, stmt.consequences):
      case.accept(self)
      consequence.accept(self)

  def handle_ReturnStmt(self, stmt):
    self.handle('ReturnStmt', stmt)
    if stmt.expression != None:
      stmt.expression.accept(self)
    
  # EXPRESSIONS
  
  def handle_BooleanLiteralExp(self, exp):
    self.handle('BooleanLiteralExp', exp)
    
  def handle_IntegerLiteralExp(self, exp):
    self.handle('IntergerLiteralExp', exp)

  def handle_FloatLiteralExp(self, exp):
    self.handle('FloatLiteralExp', exp)

  def handle_AtomLiteralExp(self, atom):
    self.handle('AtomLiteralExp', atom)

  def handle_ListLiteralExp(self, lst):
    self.handle('ListLiteralExp', lst)
    for exp in lst.expressions:
      exp.accept(self) 

  def handle_ObjectLiteralExp(self, obj):
    self.handle('ObjectLiteralExp', obj)
    for prop in obj.properties:
      prop.accept(self)

  def handle_Property(self, prop):
    self.handle('Property', prop)
    if prop.type != None:
      prop.type.accept(self)
    prop.value.accept(self)

  def handle_TypeExp(self, type):
    self.handle('TypeExp', type)

  def handle_ManyTypeExp(self, many):
    self.handle('ManyTypeExp', many)
    many.subtype.accept(self)
    
  def handle_TupleTypeExp(self, tuple):
    self.handle('TupleTypeExp', tuple)
    for type in tuple.types:
      type.accept(self)

  def handle_VariableExp(self, var):
    self.handle('VariableExp', var)
  
  def handle_PropertyExp(self, prop):
    self.handle('PropertyExp', prop)
    prop.obj.accept(self)

  def handle_UnaryExp(self, exp):
    self.handle('UnaryExp', exp)
    exp.operand.accept(self)

  def handle_BinaryExp(self, exp):
    self.handle('BinaryExp', exp)
    exp.left.accept(self)
    exp.right.accept(self)

  def handle_FunctionCallExp(self, exp):
    self.handle('FunctionCallExp', exp)
    exp.function.accept(self)
    for arg in exp.arguments:
      arg.accept(self)

  def handle_FunctionExp(self, exp):
    self.handle('FunctionExp', exp)

  def handle_ObjectExp(self, exp):
    self.handle('ObjectExp', exp)

  def handle_MethodCallExp(self, exp):
    self.handle('MethodCallExp', exp)
    exp.object.accept(self)
    for arg in exp.arguments:
      arg.accept(self)

  def handle_AnythingExp(self, exp):
    self.handle('AnythingExp', exp)

  def handle_MatchExp(self, exp):
    self.handle('MatchExp', exp)
    if not isstring(exp.operator):
      exp.operator.accept(self)
    if exp.operand != None:
      exp.operand.accept(self)

# CHECKER

class SemanticChecker(SemanticHandler):
  def __init__(self, model):
    self.model = model
    self.prefix = "check_"

  def check(self):
    print "foo-" + self.__class__.__name__.lower() + ": processing model"
    self.start();
    self.model.accept(self)
    self.stop()

  def start(self):
    self.fails = 0

  def stop(self):
    self.report()

  def report(self):
    print "-" * 79
    print "foo-" + self.__class__.__name__.lower() + ": result: " + \
      ( "SUCCESS - model is valid" if self.fails == 0 \
        else "FAILURES:" + str(self.fails) )
    print "-" * 79

  def fail(self, msg, *args):
    self.fails += 1
    print "  failure:", msg, ":", str(*args)
    print "           " + " > ".join(reversed(self.trace()))

  # ASSERTIONS HELPERS
  def assertIsNotNone(self, obj, msg, *info):
    if obj is None:
      self.fail(msg, *info)

