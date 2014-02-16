# handler.py
# SemanticVisitor implementation separating the visiting from the handling
# author: Christophe VG

import inspect

from util.visitor import Visitable
from util.check   import isstring

from foo_lang.semantic.model  import SemanticVisitor
from foo_lang.semantic.dumper import Dumper

def stacked(method):
  """
  Decorator for methods to keep track of their execution using a stack.
  """
  obj_name = method.__name__[7:]
  def wrapped(self, obj):
    self.start_handling(obj_name, obj)
    method(self, obj)
    self.stop_handling(obj_name, obj)
  return wrapped

class SemanticHandler(SemanticVisitor):
  def __init__(self, top_down=None, bottom_up=None):
    self.prefix    = None
    self._stack    = []
    if top_down == bottom_up == None:
      top_down = True
      bottom_up = False
    assert top_down != bottom_up, "Can't move in both/no direction ;-)"
    self.top_down  = top_down
    self.bottom_up = bottom_up

  def start_handling(self, part_name, part):
    self._stack.append(part)
    if self.top_down: self.perform_handling(part_name, part)

  def stop_handling(self, part_name, part):
    if self.bottom_up: self.perform_handling(part_name, part)
    self._stack.pop()

  def perform_handling(self, part_name, part):
    if self.prefix != None and self.prefix != "handle_":
      try:
        method = getattr(self, self.prefix + part_name)
        method(part)
      except AttributeError:
        # possibly there is no handler
        # print "not handling", part_name
        pass
  
  def get_stack(self): return self._stack
  stack = property(get_stack)

  # HANDLERS IMPLEMENTING VISITOR and adding a handle call

  @stacked
  def handle_Model(self, model):
    for module in model.modules.values():
      module.accept(self)

  @stacked
  def handle_Domain(self, domain): pass
    
  @stacked
  def handle_Scope(self, scope): pass

  @stacked
  def handle_Module(self, module):
    for constant in module.constants:
      constant.accept(self)
    
    for extension in module.extensions:
      extension.accept(self)
    
    for execution in module.executions:
      execution.accept(self)

    for function in module.functions:
      # we only want to handle non-anonymous function declarations here
      # because anonymous declarations are declared in their specific scope
      # TODO: do this in a cleaner way (AnonFunctionDecl?)
      if function.name[0:9] != "anonymous":
        function.accept(self)

  @stacked
  def handle_Constant(self, constant): pass

  @stacked
  def handle_Extension(self, extension):
    extension.domain.accept(self)
    extension.extension.accept(self)

  @stacked
  def handle_Every(self, execution):
    execution.interval.accept(self)
    execution.scope.accept(self)
    execution.executed.accept(self)

  @stacked
  def handle_When(self, execution):
    execution.scope.accept(self)
    execution.event.accept(self)
    execution.executed.accept(self)

  @stacked
  def handle_FunctionDecl(self, function):
    for param in function.parameters:
      param.accept(self)
    function.body.accept(self)

  @stacked
  def handle_Parameter(self, parameter): pass

  # STATEMENTS

  @stacked
  def handle_BlockStmt(self, block):
    for statement in block.statements:
      statement.accept(self)

  @stacked
  def handle_AssignStmt(self, stmt):
    stmt.variable.accept(self)
    stmt.value.accept(self)

  @stacked
  def handle_AddStmt(self, stmt):
    stmt.variable.accept(self)
    stmt.value.accept(self)
  
  @stacked
  def handle_SubStmt(self, stmt):
    stmt.variable.accept(self)
    stmt.value.accept(self)

  @stacked
  def handle_IncStmt(self, stmt):
    stmt.variable.accept(self)

  @stacked
  def handle_DecStmt(self, stmt):
    stmt.variable.accept(self)

  @stacked
  def handle_IfStmt(self, stmt):
    stmt.condition.accept(self)
    stmt.true.accept(self)
    if stmt.false != None:
      stmt.false.accept(self)

  @stacked
  def handle_CaseStmt(self, stmt):
    stmt.expression.accept(self)
    for case, consequence in zip(stmt.cases, stmt.consequences):
      case.accept(self)
      consequence.accept(self)

  @stacked
  def handle_ReturnStmt(self, stmt):
    if stmt.expression != None:
      stmt.expression.accept(self)
    
  # EXPRESSIONS
  
  @stacked
  def handle_BooleanLiteralExp(self, exp): pass
    
  @stacked
  def handle_IntegerLiteralExp(self, exp): pass

  @stacked
  def handle_FloatLiteralExp(self, exp): pass

  @stacked
  def handle_AtomLiteralExp(self, atom): pass

  @stacked
  def handle_ListLiteralExp(self, lst):
    for exp in lst.expressions:
      exp.accept(self) 

  @stacked
  def handle_ObjectLiteralExp(self, obj):
    for prop in obj.properties:
      prop.accept(self)

  @stacked
  def handle_Property(self, prop):
    if prop.type != None:
      prop.type.accept(self)
    prop.value.accept(self)

  @stacked
  def handle_BooleanType(self, type): pass

  @stacked
  def handle_ByteType(self, type): pass

  @stacked
  def handle_IntegerType(self, type): pass

  @stacked
  def handle_FloatType(self, type): pass

  @stacked
  def handle_TimestampType(self, type): pass

  @stacked
  def handle_ManyType(self, many):
    many.subtype.accept(self)
    
  @stacked
  def handle_TupleType(self, tuple):
    for type in tuple.types:
      type.accept(self)

  @stacked
  def handle_VariableExp(self, var): pass
  
  @stacked
  def handle_PropertyExp(self, prop):
    prop.obj.accept(self)

  @stacked
  def handle_UnaryExp(self, exp):
    exp.operand.accept(self)

  @stacked
  def handle_BinaryExp(self, exp):
    exp.left.accept(self)
    exp.right.accept(self)

  @stacked
  def handle_FunctionCallExp(self, exp):
    exp.function.accept(self)
    for arg in exp.arguments:
      arg.accept(self)

  @stacked
  def handle_FunctionExp(self, exp): pass

  @stacked
  def handle_ObjectExp(self, exp): pass

  @stacked
  def handle_MethodCallExp(self, exp):
    exp.object.accept(self)
    for arg in exp.arguments:
      arg.accept(self)

  @stacked
  def handle_AnythingExp(self, exp): pass

  @stacked
  def handle_MatchExp(self, exp):
    if not isstring(exp.operator):
      exp.operator.accept(self)
    if exp.operand != None:
      exp.operand.accept(self)

# CHECKER

class SemanticChecker(SemanticHandler):
  def __init__(self, model, top_down=None, bottom_up=None):
    super(SemanticChecker, self).__init__(top_down, bottom_up)
    self.model  = model
    self.prefix = "check_"
    self.name   = "foo-" + self.__class__.__name__.lower()

  def check(self):
    print self.name + ": processing model"
    self.start();
    self.model.accept(self)
    self.stop()

  def start(self):
    self.fails = 0
    self.successes = 0

  def stop(self):
    self.report()

  def report(self):
    print "-" * 79

    result = "SUCCESS - model is valid" if self.fails == 0 \
             else "FAILURES : " + str(self.fails)
    info   = "SUCCESSES: " + str(self.successes) if self.successes != 0 \
             else None

    self.log("results of run", result, info)
    print "-" * 79

  def fail(self, msg, *args):
    self.fails += 1
    self.log("failure: " + msg + " : " + str(*args),
             "stack: " + " > ".join([self.show(obj) for obj in self._stack]))

  def show(self, obj):
    name   = obj.__class__.__name__
    attrib = False
    try:
      attrib = {
                 'FunctionDecl'    : 'name',
                 'FunctionExp'     : 'name',
                 'FunctionCallExp' : 'function',
                 'CaseStmt'        : 'expression',
                 'Every'           : 'interval',
                 'When'            : 'event',
                 'Module'          : 'name',
                 'Parameter'       : 'name'
               }[name]
    except KeyError: pass

    if attrib != False:
      attrib = getattr(obj, attrib)
      if isinstance(attrib, Visitable):
        attrib = attrib.accept(Dumper())
      return name + "(" + attrib + ")"
    else:
      return name

  def success(self, msg, *args):
    self.successes += 1
    self.log("success: " + msg + " : " + " ".join([str(arg) for arg in args]))

  def log(self, msg1, *msgs):
    print "foo-" + self.__class__.__name__.lower() + ": " + msg1
    for msg in msgs:
      if not msg is None:
        print " " * len(self.name) + "  " + msg

  # ASSERTIONS HELPERS

  def assertIsNotNone(self, obj, msg, *info):
    if obj is None:
      self.fail(msg, *info)

  def assertNotIsInstance(self, obj, instance, msg, *info):
    if isinstance(obj, instance):
      self.fail(msg, *info)

