# model.py
# classes to construct the Semantic Model
# author: Christophe VG

from collections import OrderedDict

from util.visitor import Visitable, visitor_for, nohandling
from util.check   import isidentifier

class Identifier(Visitable):
  def __init__(self, name):
    assert isidentifier(name), "bad identifier name " + str(name)
    self.name = name

class Model(Visitable):
  """
  Top-level model container.
  """
  def __init__(self):
    self.modules = {}
    self.domains = {}

@nohandling
class Domain(Visitable):
  def get_scope(self, sub="*"):
    return self.scoping[sub]

  def get_property(self, property):
    return self.get_scope(property)
  
  def handler(self):
    return "Domain"

  def get_function(self, function_name):
    return None

@nohandling
class Scope(Visitable):
  def __init__(self, domain):
    assert isinstance(domain, Domain)
    self.domain = domain
    self.scope  = None    # implemented by concrete Scope implementation

  def handler(self):
    return "Scope"

class Module(Visitable):
  """
  Modules match input files. Each module contains all related functions and
  configuration regarding an aspect of the implementation.
  """
  def __init__(self, identifier):
    assert isinstance(identifier, Identifier)

    self.identifier = identifier
    self.constants  = NamedTypedOrderedDict(Constant)
    self.externals  = OrderedDict()     # { function : library }
    self.extensions = TypedList(Extension)
    self.executions = TypedList(ExecutionStrategy)

    # functions are part of a module, but are linked from ExecutionStrategies
    self.functions  = NamedTypedOrderedDict(FunctionDecl)
  def get_name(self): return self.identifier.name
  name = property(get_name)

@nohandling
class NamedTypedOrderedDict(Visitable):
  def __init__(self, type):
    self.objects = OrderedDict()
    self.type    = type
  def __iter__(self):
    return iter(self.objects.values())
  def __contains__(self, key):
    return key in self.objects
  def append(self, obj):
    assert isinstance(obj, self.type)
    self.objects[obj.name] = obj
    return self

@nohandling
class TypedList(Visitable):
  def __init__(self, type, objects=[]):
    self.objects = []
    self.type    = type
    [self.append(obj) for obj in objects]
  def __iter__(self):
    return iter(self.objects)
  def append(self, obj):
    assert isinstance(obj, self.type), \
           "TypedList's provided obj is a " + + obj.__class__.__name__ + \
           " but got a " + self.type.__name__
    self.objects.append(obj)
    return self
  def __len__(self):
    return len(self.objects)

class Constant(Visitable):
  def __init__(self, identifier, value, type=None):
    if type is None: type = UnknownType()
    assert isinstance(identifier, Identifier), \
           "Constant's identifier (name) should be an identifier"
    assert isinstance(type, TypeExp)
    assert isinstance(value, LiteralExp), \
           "Constant.value is a " + value.__class__.__name__ + \
           " but exptected a LiteralExp"
    self.identifier = identifier
    self.type       = type
    self.value      = value
  def get_name(self): return self.identifier.name
  name = property(get_name)

class Extension(Visitable):
  def __init__(self, domain, extension):
    assert isinstance(domain, Domain), \
           "Extension.domain is a " + domain.__class__.__name__ + \
           " but expected a Domain"
    assert isinstance(extension, ObjectLiteralExp), \
           "Extension.extension is a " + extension.__class__.__name__ + \
           " but expected an ObjectLiteralExp"
    self.domain    = domain
    self.extension = extension

@nohandling
class ExecutionStrategy(Visitable):
  def __init__(self, scope, function):
    assert isinstance(scope, Domain) or isinstance(scope, Scope), \
           "ExecutionStrategy.scope is a " + scope.__class__.__name__ + \
           " but expected a Scope or a Domain"
    assert isinstance(function, FunctionExp) or isinstance(function, FunctionDecl)
    self.scope    = scope
    self.executed = function

class Every(ExecutionStrategy):
  """
  Interval-based execution.
  """
  def __init__(self, scope, function, interval):
    assert isinstance(interval, VariableExp) \
        or isinstance(interval, IntegerLiteralExp), \
           "Every.interval is a " + interval.__class__.__name__ + \
           " but exptected an IntegerLiteralExp or a VariableExp"
    ExecutionStrategy.__init__(self, scope, function)
    self.interval = interval

class When(ExecutionStrategy):
  """
  Event-based execution.
  """
  def __init__(self, scope, function, timing, event):
    ExecutionStrategy.__init__(self, scope, function)
    assert timing == "after" or timing == "before"
    assert isinstance(event, FunctionExp), \
           "When.event is a " + event.__class__.__name__ + \
           " but expected an identifier"
    self.timing = timing
    self.event  = event

class FunctionDecl(Visitable):
  anonymous = 0
  def __init__(self, body, identifier=None, parameters=[], type=None):
    if identifier is None:
      identifier = Identifier("anonymous" + str(FunctionDecl.anonymous))
      FunctionDecl.anonymous += 1
    if type is None: type = UnknownType()
    assert isinstance(identifier, Identifier)
    assert isinstance(body, Stmt)
    assert isinstance(type, TypeExp)
    self.identifier = identifier
    self.parameters = TypedList(Parameter, parameters)
    self.body       = body
    self.type       = type
  def get_name(self): return self.identifier.name
  name = property(get_name)

class Parameter(Visitable):
  def __init__(self, identifier, type=None):
    if type is None: type = UnknownType()
    assert isinstance(identifier, Identifier)
    assert isinstance(type, TypeExp)
    self.identifier = identifier
    self._type      = type
  def get_type(self):
    return self._type
  def set_type(self, type):
    assert self._type == type
    self._type = type
  def del_type(self):
    del self._type
  type = property(get_type, set_type, del_type)
  def get_name(self): return self.identifier.name
  name = property(get_name)

# STATEMENTS

@nohandling
class Stmt(Visitable): pass

class BlockStmt(Stmt):
  def __init__(self, statements=[]):
    self.statements = TypedList(Stmt, statements)

@nohandling
class VariableValueStmt(Stmt):
  def __init__(self, variable, value):
    assert isinstance(variable, VariableExp) or isinstance(variable, PropertyExp)
    assert isinstance(value, Exp)
    self.variable = variable
    self.value    = value

class AssignStmt(VariableValueStmt): pass
class AddStmt(VariableValueStmt): pass
class SubStmt(VariableValueStmt): pass

@nohandling
class VariableStmt(Stmt):
  def __init__(self, variable):
    assert isinstance(variable, VariableExp) or isinstance(variable, PropertyExp)
    self.variable = variable

class IncStmt(VariableStmt): pass
class DecStmt(VariableStmt): pass

class IfStmt(Stmt):
  def __init__(self, condition, true, false=None):
    assert isinstance(condition, Exp)
    assert isinstance(true, Stmt)
    assert false == None or isinstance(false, Stmt)
    self.condition = condition
    self.true      = true
    self.false     = false

class CaseStmt(Stmt):
  def __init__(self, expression, cases, consequences):
    if len(cases) != len(consequences):
      raise AttributeError, "Cases and consequences don't match."
    assert isinstance(expression, Exp)
    self.expression   = expression
    self.cases        = TypedList(FunctionCallExp, cases)
    self.consequences = TypedList(Stmt, consequences)

class ReturnStmt(Stmt):
  def __init__(self, expression=None):
    assert expression == None or isinstance(expression, Exp)
    self.expression = expression

# EXPRESSIONS

@nohandling
class Exp(Visitable): pass

@nohandling
class LiteralExp(Exp): pass

class BooleanLiteralExp(LiteralExp):
  def __init__(self, value):
    if isinstance(value, bool):
      self.value = value
    elif isinstance(value, str) or isinstance(value, unicode):
      self.value = value.lower() == "true"
    elif isinstance(value, int):
      self.value = value != 0
    else:
      raise RuntimeError("Can't convert value to boolean:" + str(value))

class IntegerLiteralExp(LiteralExp):
  def __init__(self, value):
    self.value = int(value)

class FloatLiteralExp(LiteralExp):
  def __init__(self, value):
    self.value = float(value)

class AtomLiteralExp(LiteralExp):
  def __init__(self, identifier):
    assert isinstance(identifier, Identifier)
    self.identifier = identifier
  def get_name(self): return self.identifier.name
  name = property(get_name)

class ListLiteralExp(LiteralExp):
  def __init__(self, expressions=[]):
    self.expressions = TypedList(Exp, expressions)

class ObjectLiteralExp(LiteralExp):
  def __init__(self, properties=[]):
    self.properties = TypedList(Property, properties)

class Property(Visitable):
  def __init__(self, identifier, value, type):
    assert isinstance(identifier, Identifier)
    assert isinstance(value, LiteralExp), "Property.value is a " + value.__class__.__name__ + " but expected a LiteralExp" 
    assert isinstance(type, TypeExp)
    self.identifier = identifier
    self.value      = value
    self.type       = type
  def get_name(self): return self.identifier.name
  name = property(get_name)

class TypeExp(Exp):
  def __init__(self, identifier):
    assert isinstance(identifier, Identifier), \
      "TypeExp's identifier (type) should be an identifier"
    self.identifier = identifier
  def get_type(self): return self.identifier.name
  type = property(get_type)

class UnknownType(TypeExp):
  def __init__(self): pass
  def get_type(self): assert False, "Don't get type from UnknownType"

class ManyTypeExp(TypeExp):
  def __init__(self, subtype):
    assert isinstance(subtype, TypeExp)
    self.subtype = subtype

class TupleTypeExp(TypeExp):
  def __init__(self, types=[]):
    self.types = TypedList(TypeExp, types)

class VariableExp(Exp):
  def __init__(self, identifier):
    assert isinstance(identifier, Identifier)
    self.identifier = identifier
  def get_name(self): return self.identifier.name
  name = property(get_name)

class ObjectExp(VariableExp): pass
class FunctionExp(VariableExp): pass

class PropertyExp(Exp):
  def __init__(self, obj, identifier):
    assert isinstance(obj, ObjectExp) or isinstance(obj, Scope)
    assert isinstance(identifier, Identifier)
    self.obj        = obj
    self.identifier = identifier
  def get_name(self): return self.identifier.name
  name = property(get_name)

@nohandling
class UnaryExp(Exp):
  def __init__(self, operand):
    assert isinstance(operand, Exp)
    self.operand = operand
  def operator(self):
    raise NotimplementedError, "Missing implementation for operator(self))" + \
                               " on " + self.__class__.__name__
  def handler(self):
    return "UnaryExp"

@nohandling
class BinaryExp(Exp):
  def __init__(self, left, right):
    assert isinstance(left,  Exp)
    assert isinstance(right, Exp)
    self.left  = left
    self.right = right
  def operator(self):
    raise NotimplementedError, "Missing implementation for operator(self))" + \
                               " on " + self.__class__.__name__
  def handler(self):
    return "BinaryExp"

class AndExp(BinaryExp):
  def operator(self): return "and"

class OrExp(BinaryExp):
  def operator(self): return "or"

class EqualsExp(BinaryExp):
  def operator(self): return "=="

class NotEqualsExp(BinaryExp):
  def operator(self): return "!="

class LTExp(BinaryExp):
  def operator(self): return "<"

class LTEQExp(BinaryExp):
  def operator(self): return "<="

class GTExp(BinaryExp):
  def operator(self): return ">"

class GTEQExp(BinaryExp):
  def operator(self): return ">="

class PlusExp(BinaryExp):
  def operator(self): return "+"

class MinusExp(BinaryExp):
  def operator(self): return "-"

class MultExp(BinaryExp):
  def operator(self): return "*"

class DivExp(BinaryExp):
  def operator(self): return "/"

class ModuloExp(BinaryExp):
  def operator(self): return "%"

class NotExp(UnaryExp):
  def operator(self): return "!"

class FunctionCallExp(Exp, Stmt):
  def __init__(self, function, arguments=[]):
    assert isinstance(function, FunctionExp)
    self.function  = function
    self.arguments = TypedList(Exp, arguments)

class MethodCallExp(Exp, Stmt):
  def __init__(self, obj, identifier, arguments=[]):
    assert isinstance(obj, ObjectExp)
    assert isinstance(identifier, Identifier)
    self.object     = obj
    self.identifier = identifier
    self.arguments  = TypedList(Exp, arguments)
  def get_name(self): return self.identifier.name
  name = property(get_name)

class AnythingExp(Exp): pass

class MatchExp(Exp):
  def __init__(self, operator, operand=None):
    assert isinstance(operator, AnythingExp) \
       or operator in [ "<", "<=", ">", ">=", "==", "!=", "!" ], \
         "MatchExp.operator got " + operator
    assert operand == None or isinstance(operand, Exp)
    self.operator = operator
    self.operand  = operand

# VISITOR

@visitor_for([Visitable])
class SemanticVisitor(): pass
