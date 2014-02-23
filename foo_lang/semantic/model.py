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
  def __str__(self): return self.__class__.__name__ + "(" + self.name + ")"

class Model(Visitable):
  """
  Top-level model container.
  """
  def __init__(self):
    self.modules = {}
  def __str__(self): return self.__class__.__name__

@nohandling
class Domain(Visitable):
  def extend(self, extension):
    raise NotImplementedError, "Domain.extend not implemented on " + str(self)
  
  def get_scope(self, sub="*"):
    return self.scoping[sub]

  def get_property(self, property):
    return self.get_scope(property)
  
  def handler(self):
    return "Domain"

  def get_function(self, function_name):
    return None
  
  def get_name(self):
    return self.__class__.__name__.lower()
  name = property(get_name)

  def __str__(self): return self.__class__.__name__ + "(" + self.name + ")"

@nohandling
class Scope(Visitable):
  def __init__(self, domain):
    assert isinstance(domain, Domain)
    self.domain = domain
    self.scope  = None    # implemented by concrete Scope implementation

  def handler(self):
    return "Scope"

  def __str__(self): return self.__class__.__name__ + "(" + self.domain.name + ")"

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
    self.domains    = NamedTypedOrderedDict(Domain)
    self.executions = TypedList(ExecutionStrategy)
    
    # functions are part of a module, but are linked from ExecutionStrategies
    self.functions  = NamedTypedOrderedDict(FunctionDecl)
  def get_name(self): return self.identifier.name
  name = property(get_name)
  def __str__(self): return self.__class__.__name__ + "(" + self.name + ")"

@nohandling
class NamedTypedOrderedDict(Visitable):
  def __init__(self, type):
    self.objects = OrderedDict()
    self.type    = type
  def items(self):
    return self.objects.items()
  def __iter__(self):
    return iter(self.objects.values())
  def __contains__(self, key):
    return key in self.objects
  def __getitem__(self, key):
    return self.objects[key]
  def __setitem__(self, key, value):
    self.objects[key] = value
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
  def index(self, obj):
    try: return self.objects.index(obj)
    except: return None
  def __getitem__(self, index):
    try: return self.objects[index]
    except: return None
  def __str__(self):
    return "TypedList(" + self.type.__name__ + ")"

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
  def __str__(self): return self.__class__.__name__ + "(" + self.name + ")"

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
  def __str__(self): return self.__class__.__name__

@nohandling
class ExecutionStrategy(Visitable):
  def __init__(self, scope, function):
    assert isinstance(scope, Domain) or isinstance(scope, Scope), \
           "ExecutionStrategy.scope is a " + scope.__class__.__name__ + \
           " but expected a Scope or a Domain"
    assert isinstance(function, FunctionExp) or isinstance(function, FunctionDecl)
    self.scope    = scope
    self.executed = function
  def __str__(self): return self.__class__.__name__ + "(" + str(self.scope) + ")"

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
  def __str__(self): return self.__class__.__name__ + "(" + self.name + ")"

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
    assert self._type == type or isinstance(self._type, UnknownType)
    self._type = type
  type = property(get_type, set_type)
  def get_name(self): return self.identifier.name
  name = property(get_name)
  def __str__(self): return self.__class__.__name__ + "(" + self.name + ")"

# STATEMENTS

@nohandling
class Stmt(Visitable): pass

class BlockStmt(Stmt):
  def __init__(self, statements=[]):
    self.statements = TypedList(Stmt, statements)
  def __str__(self): return self.__class__.__name__

@nohandling
class VariableValueStmt(Stmt):
  def __init__(self, variable, value):
    assert isinstance(variable, VariableExp) or isinstance(variable, PropertyExp)
    assert isinstance(value, Exp)
    self.variable = variable
    self.value    = value
  def __str__(self): return self.__class__.__name__ + "(" + str(self.variable) + "," + str(self.value) + ")"

class AssignStmt(VariableValueStmt): pass
class AddStmt(VariableValueStmt): pass
class SubStmt(VariableValueStmt): pass

@nohandling
class VariableStmt(Stmt):
  def __init__(self, variable):
    assert isinstance(variable, VariableExp) or isinstance(variable, PropertyExp)
    self.variable = variable
  def __str__(self): return self.__class__.__name__ + "(" + str(self.variable) + ")"

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
  def __str__(self): return self.__class__.__name__ + "(" + str(self.condition) + ")"

class CaseStmt(Stmt):
  def __init__(self, expression, cases, consequences):
    if len(cases) != len(consequences):
      raise AttributeError, "Cases and consequences don't match."
    assert isinstance(expression, Exp)
    self.expression   = expression
    self.cases        = TypedList(FunctionCallExp, cases)
    self.consequences = TypedList(Stmt, consequences)
  def __str__(self): return self.__class__.__name__ + "(" + str(self.expression) + ")"

class ReturnStmt(Stmt):
  def __init__(self, expression=None):
    assert expression == None or isinstance(expression, Exp)
    self.expression = expression
  def __str__(self): return self.__class__.__name__

# EXPRESSIONS

@nohandling
class Exp(Visitable):
  def __init__(self):
    self._type = UnknownType()
  def get_type(self):
    return self._type
  def set_type(self, type):
    # allow to set only to same type or better than Unknown
    assert self._type.__class__.__name__ == type.__class__.__name__ or \
      isinstance(self._type, UnknownType), \
      "Can't update type from " + self._type.__class__.__name__ + " to " + \
      type.__class__.__name__
    self._type = type
  type = property(get_type, set_type)
  def __str__(self): return self.__class__.__name__

@nohandling
class LiteralExp(Exp): pass

class BooleanLiteralExp(LiteralExp):
  def __init__(self, value):
    self._type = BooleanType()
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
    self._type = IntegerType()

class FloatLiteralExp(LiteralExp):
  def __init__(self, value):
    self.value = float(value)
    self._type = FloatType()

class AtomLiteralExp(LiteralExp):
  def __init__(self, identifier):
    assert isinstance(identifier, Identifier)
    self.identifier = identifier
    self._type = AtomType()
  def get_name(self): return self.identifier.name
  name = property(get_name)

class ListLiteralExp(LiteralExp):
  def __init__(self, expressions=[]):
    self.expressions = TypedList(Exp, expressions)
    self._type = ManyType(UnknownType())

class ObjectLiteralExp(LiteralExp):
  def __init__(self, properties=[]):
    self.properties = TypedList(Property, properties)
    self._type = ObjectType(Identifier("__literal__"))

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
  def __str__(self):
    return "Property(" + self.name + ")"

@nohandling
class TypeExp(Exp):
  def __str__(self): return self.__class__.__name__

class UnknownType(TypeExp):
  def __init__(self):
    self._type = None

class VoidType(TypeExp): pass
class AtomType(TypeExp): pass

@nohandling
class SimpleType(TypeExp): pass

class BooleanType(SimpleType): pass

@nohandling
class NumericType(SimpleType): pass

class ByteType(NumericType): pass
class IntegerType(NumericType): pass
class FloatType(NumericType): pass

@nohandling
class ComplexType(TypeExp): pass

manytype_provides = {
  "contains": FunctionDecl(BlockStmt(), type=BooleanType(),
                           parameters=[Parameter(Identifier("items"),
                                                 type=ByteType())])
}
class ManyType(ComplexType):
  def __init__(self, subtype):
    assert isinstance(subtype, TypeExp)
    self.subtype = subtype
    self.provides = manytype_provides

class TupleType(ComplexType):
  def __init__(self, types=[]):
    self.types = TypedList(TypeExp, types)
    self.provides = { "contains": {} }

class ObjectType(ComplexType):
  def __init__(self, identifier, provides={}):
    assert isinstance(identifier, Identifier)
    self.identifier = identifier
    self.provides   = OrderedDict()
    for key, value in provides.items():
      self.provides[key] = value
  def get_name(self): return self.identifier.name
  name = property(get_name)
  def __str__(self):
    return "ObjectType(" + self.name + ")"

# BUILD-IN object types

class TimestampType(ObjectType):
  def __init__(self):
    super(TimestampType, self).__init__(Identifier("timestamp"))
    self.provides = {}

class VariableExp(Exp):
  def __init__(self, identifier):
    assert isinstance(identifier, Identifier)
    self.identifier = identifier
    self._type      = UnknownType()
  def get_name(self): return self.identifier.name
  name = property(get_name)
  def __str__(self):
    return self.__class__.__name__ + "(" +  self.identifier.name + ")"

class ObjectExp(VariableExp):
  def __init__(self, identifier):
    super(ObjectExp, self).__init__(identifier)

class FunctionExp(VariableExp):
  def __init__(self, identifier):
    super(FunctionExp, self).__init__(identifier)
    self.declaration = FunctionDecl(BlockStmt())
  def get_type(self): return self.declaration.type
  type = property(get_type)
  def get_parameters(self): return self.declaration.parameters
  parameters = property(get_parameters)

class PropertyExp(VariableExp):
  def __init__(self, obj, identifier):
    assert isinstance(obj, ObjectExp) or isinstance(obj, Scope)
    assert isinstance(identifier, Identifier)
    self.obj        = obj
    self.identifier = identifier
    self._type      = UnknownType()
  def get_name(self): return self.identifier.name
  name = property(get_name)

@nohandling
class UnaryExp(Exp):
  def __init__(self, operand):
    assert isinstance(operand, Exp)
    self.operand = operand
    self._type   = UnknownType()
  def operator(self):
    raise NotimplementedError, "Missing implementation for operator(self))" + \
                               " on " + self.__class__.__name__
  def handler(self):
    return "UnaryExp"

@nohandling
class BooleanUnaryExp(UnaryExp):
  def __init__(self, operand):
    super(BooleanUnaryExp, self).__init__(operand)
    self._type = BooleanType()

@nohandling
class BinaryExp(Exp):
  def __init__(self, left, right):
    assert isinstance(left,  Exp)
    assert isinstance(right, Exp)
    self.left  = left
    self.right = right
    self._type = UnknownType()
  def operator(self):
    raise NotimplementedError, "Missing implementation for operator(self))" + \
                               " on " + self.__class__.__name__
  def handler(self):
    return "BinaryExp"

@nohandling
class BooleanBinaryExp(BinaryExp):
  def __init__(self, left, right):
    super(BooleanBinaryExp, self).__init__(left, right)
    self._type = BooleanType()

@nohandling
class NumericBinaryExp(BinaryExp):
  def __init__(self, left, right):
    super(NumericBinaryExp, self).__init__(left, right)
    self._type = NumericType()

class AndExp(BooleanBinaryExp):
  def operator(self): return "and"

class OrExp(BooleanBinaryExp):
  def operator(self): return "or"

class EqualsExp(BooleanBinaryExp):
  def operator(self): return "=="

class NotEqualsExp(BooleanBinaryExp):
  def operator(self): return "!="

class LTExp(BooleanBinaryExp):
  def operator(self): return "<"

class LTEQExp(BooleanBinaryExp):
  def operator(self): return "<="

class GTExp(BooleanBinaryExp):
  def operator(self): return ">"

class GTEQExp(BooleanBinaryExp):
  def operator(self): return ">="

class NotExp(BooleanUnaryExp):
  def operator(self): return "!"

class PlusExp(NumericBinaryExp):
  def operator(self): return "+"

class MinusExp(NumericBinaryExp):
  def operator(self): return "-"

class MultExp(NumericBinaryExp):
  def operator(self): return "*"

class DivExp(NumericBinaryExp):
  def operator(self): return "/"

class ModuloExp(NumericBinaryExp):
  def operator(self): return "%"

@nohandling
class CallExp(Exp, Stmt):
  def __init__(self, arguments=[]):
    self.arguments = TypedList(Exp, arguments)

class FunctionCallExp(CallExp):
  def __init__(self, function, arguments=[]):
    super(FunctionCallExp, self).__init__(arguments)
    assert isinstance(function, FunctionExp)
    self.function  = function
  def get_name(self): return self.function.name
  name=property(get_name)
  def get_type(self): return self.function.type
  type=property(get_type)

class MethodCallExp(CallExp):
  def __init__(self, obj, identifier, arguments=[]):
    super(MethodCallExp, self).__init__(arguments)
    assert isinstance(obj, ObjectExp) or isinstance(obj, PropertyExp)
    # and isinstance(obj.type, ObjectType)
    assert isinstance(identifier, Identifier)
    self.object     = obj
    self.identifier = identifier
  def get_name(self): return self.object.name + "." + self.identifier.name
  name = property(get_name)
  def get_type(self):
    try: return self.object.type.provides[self.identifier.name].type
    except: pass
    return UnknownType()
  type = property(get_type)

class AnythingExp(Exp): pass

class MatchExp(Exp):
  def __init__(self, operator, operand=None):
    assert isinstance(operator, AnythingExp) \
       or operator in [ "<", "<=", ">", ">=", "==", "!=", "!" ], \
         "MatchExp.operator got " + operator
    assert operand == None or isinstance(operand, Exp)
    self.operator = operator
    self.operand  = operand
    self._type    = BooleanType()

# VISITOR

@visitor_for([Visitable])
class SemanticVisitorBase(): pass
