# instructions.py
# instructions to represent abstract (procedural+OO) code - AST anyone? ;-)
# author: Christophe VG

from util.types   import TypedList
from util.visitor import Visitable, visits, novisiting
from util.check   import isstring, isidentifier

@novisiting
class Fragment(Visitable): pass

class Identifier(Fragment):
  def __init__(self, name):
    assert isidentifier(name), "Not an Identifier: " + name
    self.name = name

@novisiting
class Instruction(Fragment): pass

class InstructionList(Instruction):
  def __init__(self, instructions=[]):
    self.instructions = []
    [self.append(instruction) for instruction in instructions]
  def __iter__(self):
    return iter(self.instructions)
  def prepend(self, instruction):
    assert isinstance(instruction, Instruction)
    self.instructions.insert(0, instruction)
    return self
  def append(self, instruction):
    assert isinstance(instruction, Instruction)
    self.instructions.append(instruction)
    return self

class Import(Instruction):
  def __init__(self, name):
    self.name = name

@novisiting
class Declaration(Instruction): pass

class FunctionDecl(Declaration):
  def __init__(self, name, parameters=[], body=None, type=None):
    if body is None: body = BlockStmt()
    if type is None: type = VoidType()
    assert isinstance(name, Identifier)
    assert isinstance(body, Stmt)
    assert isinstance(type, TypeExp)
    self.name       = name
    self.parameters = ParameterList(parameters)
    self.body       = body
    self.type       = type

@novisiting
class ParameterList(Fragment):
  def __init__(self, parameters):
    self.parameters = []
    [self.append(parameter) for parameter in parameters]
  def __iter__(self):
    return iter(self.parameters)
  def prepend(self, parameter):
    assert isinstance(parameter, ParameterDecl)
    self.parameters.insert(0, parameter)
    return self
  def append(self, parameter):
    assert isinstance(parameter, ParameterDecl)
    self.parameters.append(parameter)
    return self

class ParameterDecl(Declaration):
  def __init__(self, name, type=None, default=None):
    if type is None: type = UnknownType()
    assert isinstance(name, Identifier)
    assert isinstance(type, TypeExp)
    assert default == None or isinstance(default, Expression)
    self.name    = name
    self.type    = type
    self.default = default

@novisiting
class Stmt(Instruction):
  def ends(self):
    return False

class EmptyStmt(Stmt): pass

class BlockStmt(Stmt):
  def __init__(self, statements=[]):
    self.statements = []
    [self.append(statement) for statement in statements]
  def __iter__(self):
    return iter(self.statements)
  def prepend(self, statement):
    assert isinstance(statement, Stmt)
    self.statements.insert(0, statement)
    return self
  def append(self, statement):
    assert isinstance(statement, Stmt), "Not a Stmt:" + str(statement)
    self.statements.append(statement)
    return self

class IfStmt(Stmt):
  def __init__(self, expression, true_clause, false_clause=None):
    assert isinstance(expression, Expression)
    assert isinstance(true_clause, Stmt)
    assert false_clause == None or isinstance(false_clause, Stmt)
    self.expression   = expression
    self.true_clause  = true_clause
    self.false_clause = false_clause

@novisiting
class MutUnOpStmt(Stmt):
  def __init__(self, operand):
    assert isinstance(operand, VariableExp)
    self.operand = operand
  def ends(self):
    return True

class IncStmt(MutUnOpStmt): pass
class DecStmt(MutUnOpStmt): pass

@novisiting
class ImmutUnOpStmt(Stmt):
  def __init__(self, expression):
    assert isinstance(expression, Expression)
    self.expression = expression
  def ends(self):
    return True

class PrintStmt(ImmutUnOpStmt): pass
class RaiseStmt(ImmutUnOpStmt): pass

class Comment(Stmt):
  def __init__(self, comment):
    assert isstring(comment)
    self.comment = comment
  def __str__(self):
    return self.comment

@novisiting
class BinOpStmt(Stmt):
  def __init__(self, operand, expression):
    assert isinstance(operand, VariableExp)
    assert isinstance(expression, Expression)
    self.operand    = operand
    self.expression = expression
  def ends(self):
    return True

class AssignStmt(BinOpStmt): pass
class AddStmt(BinOpStmt): pass
class SubStmt(BinOpStmt): pass

class ReturnStmt(Stmt):
  def __init__(self, expression=None):
    assert expression == None or isinstance(expression, Expression)
    self.expression = expression
  def ends(self):
    return True

@novisiting
class CondLoopStmt(Stmt):
  def __init__(self, condition, body):
    assert isinstance(condition, Expression)
    assert isinstance(body, Stmt)
    self.condition = condition
    self.body      = body

class WhileDoStmt(CondLoopStmt): pass
class RepeatUntilStmt(CondLoopStmt): pass

class ForStmt(Stmt):
  def __init__(self, init, check, change, body=None):
    assert isinstance(init,   Stmt) and not isinstance(init,   BlockStmt)
    assert isinstance(check,  Expression)
    assert isinstance(change, Stmt) and not isinstance(change, BlockStmt)
    if body == None:
      body = BlockStmt()
    else:
      assert isinstance(body, BlockStmt)
    self.init   = init
    self.check  = check
    self.change = change
    self.body   = body

@novisiting
class Expression(Stmt): pass

@novisiting
class VariableExp(Expression): pass

class SimpleVariableExp(VariableExp):
  def __init__(self, name):
    assert isinstance(name, Identifier)
    self.name = name

class ObjectExp(SimpleVariableExp): pass

class PropertyExp(ObjectExp):
  def __init__(self, obj, property):
    assert isinstance(obj, ObjectExp)
    assert isinstance(property, Identifier)
    self.obj  = obj
    self.prop = prop

@novisiting
class UnOpExp(Expression):
  def __init__(self, operand):
    assert isinstance(operand, Expression)
    self.operand = operand

class NotExp(UnOpExp): pass

@novisiting
class BinOpExp(Expression):
  def __init__(self, left, right):
    assert isinstance(left, Expression)
    assert isinstance(right, Expression)
    self.left  = left
    self.right = right

class AndExp(BinOpExp): pass
class OrExp(BinOpExp): pass
class EqualsExp(BinOpExp): pass
class NotEqualsExp(BinOpExp): pass
class LTExp(BinOpExp): pass
class LTEQExp(BinOpExp): pass
class GTExp(BinOpExp): pass
class GTEQExp(BinOpExp): pass
class PlusExp(BinOpExp): pass
class MinusExp(BinOpExp): pass
class MultExp(BinOpExp): pass
class DivExp(BinOpExp): pass
class ModuloExp(BinOpExp): pass

class FunctionCallExp(Expression):
  def __init__(self, function, arguments=[]):
    assert isinstance(function, Identifier)
    self.function  = function
    self.arguments = ExpressionList(arguments)
  def ends(self):
    return True

class MethodCallExp(Expression):
  def __init__(self, obj, method, arguments=[]):
    assert isinstance(obj, ObjectExp)
    assert isinstance(method, Identifier)
    self.obj       = obj
    self.method    = method
    self.arguments = ExpressionList(arguments)

@novisiting
class ExpressionList(Fragment):
  def __init__(self, expressions):
    self.expressions = []
    [self.append(expression) for expression in expressions]
  def __iter__(self):
    return iter(self.expressions)
  def prepend(self, expression):
    assert isinstance(expression, Expression)
    self.expressions.insert(0, expression)
    return self
  def append(self, expression):
    assert isinstance(expression, Expression)
    self.expressions.append(expression)
    return self

@novisiting
class LiteralExp(Expression): pass

class BooleanLiteral(LiteralExp):
  def __init__(self, value):
    assert isinstance(value, bool)
    self.value = value

class IntegerLiteral(LiteralExp):
  def __init__(self, value):
    assert isinstance(value, int)
    self.value = value
  
class FloatLiteral(LiteralExp):
  def __init__(self, value):
    assert isinstance(value, float)
    self.value = value

class ListLiteral(LiteralExp):
  def __init__(self, expressions=[]):
    self.expressions = ExpressionList(expressions)

class TupleLiteral(LiteralExp):
  def __init__(self, expressions=[]):
    self.expressions = ExpressionList(expressions)

class AtomLiteral(LiteralExp):
  def __init__(self, name):
    assert isinstance(name, Identifier)
    self.name = name

# TYPES

class TypeExp(Expression):
  def __init__(self, name):
    assert isinstance(name, Identifier)
    self.name = name

class UnknownType(TypeExp):
  def __init__(self): pass

class VoidType(TypeExp):
  def __init__(self): pass

class ManyType(TypeExp):
  def __init__(self, type):
    assert isinstance(type, TypeExp)
    self.subtype = type

class ObjectType(TypeExp): pass

class ByteType(TypeExp):
  def __init__(self): pass

class BooleanType(TypeExp):
  def __init__(self): pass

class FloatType(TypeExp):
  def __init__(self): pass

class LongType(TypeExp):
  def __init__(self): pass

class StructuredType(Declaration):
  def __init__(self, name, properties=[]):
    assert isinstance(name, Identifier)
    self.name       = name
    self.properties = TypedList(PropertyDecl, properties)

class PropertyDecl(Declaration):
  def __init__(self, name, type):
    assert isinstance(name, Identifier)
    assert isinstance(type, TypeExp), "expected TypeExp but got " + type.__class__.__name__
    self.name = name
    self.type = type

# VISITOR FOR INSTRUCTIONS

@visits([Fragment])
class InstructionVisitor(): pass
