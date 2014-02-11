# instructions.py
# instructions to represent abstract (procedural+OO) code - AST anyone? ;-)
# author: Christophe VG

from util.visitor import Visitable, visitor_for

class Program(Visitable):
  def __init__(self, instructions):
    assert islistof(instructions, Instruction)
    self.instructions = instructions

class Instruction(Visitable): pass

class Declaration(Instruction): pass

class FunctionDecl(Declaration):
  def __init__(self, name, parameters, body, type=None):
    assert isidentifier(name)
    assert islistof(parameters, ParameterDecl)
    assert isinstance(body,    Stmt)
    assert type == None or isinstance(type, TypeExp)
    if type == None:
      type = TypeExp(None)
    self.name       = name
    self.parameters = parameters
    self.body       = body
    self.type       = type

class ParameterDecl(Declaration):
  def __init__(self, name, type, default=None):
    assert isidentifier(name)
    assert isinstance(type, TypeExp)
    assert default == None or isinstance(default, Expression)
    self.name    = name
    self.type    = type
    self.default = default

class Stmt(Instruction): pass

class EmptyStmt(Stmt): pass

class BlockStmt(Stmt):
  def __init__(self, statements):
    assert islistof(statements, Stmt)
    self.statements = statements

class IfStmt(Stmt):
  def __init__(self, expression, true_clause, false_clause):
    assert isinstance(expression, Expression)
    assert isinstance(true_clause, Stmt)
    assert isinstance(false_clause, Stmt)
    self.expression   = expression
    self.true_clause  = true_clause
    self.false_clause = false_clause

class MutUnOpStmt(Stmt):
  def __init__(self, operand):
    assert isinstance(operand, VariableExp)
    self.operand = operand

class IncStmt(MutUnOpStmt): pass
class DecStmt(MutUnOpStmt): pass

class ImmutUnOpStmt(Stmt):
  def __init__(self, expression):
    assert isinstance(expression, Expression)

class PrintStmt(ImmutUnOpStmt): pass
class RaiseStmt(ImmutUnOpStmt): pass

class Comment(Stmt):
  def __init__(self, comment):
    assert isstring(comment)
    self.comment = comment
  def __repr__(self):
    return self.comment

class BinOpStmt(Stmt):
  def __init__(self, operand, expression):
    assert isinstance(operand, VariableExp)
    assert isinstance(expression, Expression)
    self.operand    = operand
    self.expression = expression

class AssignStmt(BinOpStmt): pass
class AddStmt(BinOpStmt): pass
class SubStmt(BinOpStmt): pass

class ReturnStmt(Stmt):
  def __init__(self, expression=None):
    assert expression == None or isinstance(expression, Expression)
    self.expression = expression

class CondLoopStmt(Stmt):
  def __init__(self, condition, body):
    assert isinstance(condition, Expression)
    assert isinstance(body, Stmt)
    self.condition = condition
    self.body      = body

class WhileDoStmt(CondLoopStmt): pass
class RepeatUntilStmt(CondLoopStmt): pass

class ForStmt(Stmt):
  def __init__(self, init, check, change, body):
    assert isinstance(init,   Stmt) and not isinstance(init,   BlockStmt)
    assert isinstance(check,  Expression)
    assert isinstance(change, Stmt) and not isinstance(change, BlockStmt)
    assert isinstance(body,   Stmt)
    self.init   = init
    self.check  = check
    self.change = change
    self.body   = body

class Expression(Instruction): pass

class VariableExp(Expression): pass

class SimpleVariableExp(VariableExp):
  def __init__(self, name):
    assert isidentifier(name)
    self.name = name

class PropertyExp(VariableExp):
  def __init__(self, obj, property):
    assert isinstance(obj, ObjectExp)
    assert isidentifier(property)
    self.obj  = obj
    self.prop = prop

class UnOpExp(Expression):
  def __init__(self, operand):
    assert isinstance(operand, Expression)
    self.operand = operand

class NotExp(UnOpExp): pass

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
  def __init__(self, function, arguments):
    assert isidentifier(function)
    assert islistof(arguments, Expression)
    self.function  = function
    self.arguments = arguments

class MethodCallExp(Expression):
  def __init__(self, obj, method, arguments):
    assert isinstance(obj, ObjectExp)
    assert isidentifier(method)
    assert islistof(arguments, Expression)
    self.obj       = obj
    self.method    = method
    self.arguments = arguments
    
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
  def __init__(self, expressions):
    assert islistof(expressions, Expression)
    self.expressions = expressions

class TupleLiteral(LiteralExp):
  def __init__(self, expressions):
    assert islistof(expressions, Expression)
    self.expressions = expressions

class AtomLiteral(LiteralExp):
  def __init__(self, name):
    assert isidentifier(name)
    self.name = name

class TypeExp(Expression):
  def __init__(self, name=None):
    assert name == None or isidentifier(name)
    self.name = name

# VISITOR FOR INSTRUCTIONS

@visitor_for(Instruction)
class InstructionVisitor(): pass

# HELPERS

# TODO: move centrally ? or better Python way

def islistof(var, type):
  assert isinstance(var, list)
  for item in var:
    assert isinstance(item, type)
  return True

def isstring(var):
  assert isinstance(var, str) or isinstance(var, unicode)
  return True

import re
identifier = re.compile(r"^[^\d\W]\w*\Z")

def isidentifier(var):
  assert isstring(var)
  assert re.match(identifier, var) is not None
  return True
