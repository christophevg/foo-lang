# instructions.py
# instructions to represent abstract (procedural+OO) code - AST anyone? ;-)
# author: Christophe VG

from util.visitor import Visitable, visitor_for, nohandling
from util.check   import isstring, isidentifier

@nohandling
class Fragment(Visitable): pass

class Identifier(Fragment):
  def __init__(self, name):
    assert isstring(name)
    assert isidentifier(name)
    self.name = name

@nohandling
class Instruction(Visitable): pass

class InstructionList(Visitable):
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

@nohandling
class Declaration(Instruction): pass

class FunctionDecl(Declaration):
  def __init__(self, name, parameters=[], body=None, type=None):
    assert isinstance(name, Identifier)
    if body == None:
      body = BlockStmt()
    else:
      assert isinstance(body, Stmt)
    if type == None:
      type = TypeExp(None)
    else:
      assert isinstance(type, TypeExp)
    self.name       = name
    self.parameters = ParameterList(parameters)
    self.body       = body
    self.type       = type

@nohandling
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
  def __init__(self, name, type, default=None):
    assert isinstance(name, Identifier)
    assert isinstance(type, TypeExp)
    assert default == None or isinstance(default, Expression)
    self.name    = name
    self.type    = type
    self.default = default

@nohandling
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

@nohandling
class MutUnOpStmt(Stmt):
  def __init__(self, operand):
    assert isinstance(operand, VariableExp)
    self.operand = operand
  def ends(self):
    return True

class IncStmt(MutUnOpStmt): pass
class DecStmt(MutUnOpStmt): pass

@nohandling
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
  def __repr__(self):
    return self.comment

@nohandling
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

@nohandling
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

@nohandling
class Expression(Stmt): pass

@nohandling
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

@nohandling
class UnOpExp(Expression):
  def __init__(self, operand):
    assert isinstance(operand, Expression)
    self.operand = operand

class NotExp(UnOpExp): pass

@nohandling
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

@nohandling
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

@nohandling
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

class TypeExp(Expression):
  def __init__(self, name=None):
    assert name == None or isinstance(name, Identifier)
    self.name = name

# VISITOR FOR INSTRUCTIONS

@visitor_for([Instruction, Fragment])
class InstructionVisitor(): pass
