// foo_lang.g
// author: Christophe VG

// ANTLR3 grammar for foo-lang, a Function Organization Optimizing DSL

grammar foo_lang;

options {
  output=AST;
  language=Python;
  backtrack=true;
}

// a few virtual tokens, used as identifying node
tokens {  // must be declared here/before use, not with other real tokens below
  ANNOTATED; ANNOTATION; ANON_FUNC_DECL; ANYTHING; APPLY; ARGS; ATOM_LITERAL;
  BLOCK; BOOLEAN_LITERAL; CASE; CASES; CONST; DEC; DOMAIN; EXTEND; EXTERNAL;
  FLOAT_LITERAL; FUNC_CALL; FUNC_DECL; FUNC_PROTO; FUNC_REF; IDENTIFIER; IF;
  IMPORT; INC; INTEGER_LITERAL; LIST_LITERAL; MANY_TYPE_EXP; MATCH_EXP;
  METHOD_CALL; MODULE; OBJECT_LITERAL; OBJECT_REF; ON; PARAMS; PROPERTY_EXP;
  PROPERTY_LITERAL; RETURN; ROOT; TUPLE_TYPE_EXP; TYPE_EXP; UNKNOWN_TYPE;
  VALUE; VAR_EXP;
}

// to have our parser raise its exceptions we need to override some methods in
// the lexer
// trick found at:
// http://www.dalkescientific.com/writings/diary/archive/2007/11/03/

@lexer::members {
def reportError(self, e):
  raise e
}

@parser::members {
def getMissingSymbol(self, input, e, expectedTokenType, follow):
#  print "Expected:", self.tokenNames[expectedTokenType], \
#        "after", self.getCurrentInputSymbol(input)
  raise RecognitionException(input)
}

@rulecatch {
except RecognitionException, e:
  raise
}

// PARSING RULES

start : modules? EOF -> ^(ROOT modules?);

modules : (module)*;
module : 'module' identifier instructions? -> ^(MODULE identifier instructions?);

instructions : (instruction)*;
instruction
  : declaration
  | directive
  | extension
  ;

// DECLARATIONS

declaration
  : annotated_declaration
  | constant_declaration
  | event_handler_declaration
  | function_declaration
  ;

annotated_declaration
  : annotation apply_declaration    -> ^(ANNOTATED annotation apply_declaration)
  | annotation function_declaration -> ^(ANNOTATED annotation function_declaration)
  ;

annotation
  : '@' function_call_expression -> ^(ANNOTATION function_call_expression)
  ;

apply_declaration
  : 'with' scoping 'do' function_expression -> ^(APPLY scoping function_expression)
  ;
  
constant_declaration: 'const' name_type_value -> ^(CONST name_type_value);

event_handler_declaration
  : event_timing scoping function_expression 'do' function_expression
    -> ^(ON event_timing scoping function_expression function_expression)
  ;

scoping
  : domain DOT identifier -> ^(PROPERTY_EXP domain identifier)
  | domain
  ;

domain: identifier -> ^(DOMAIN identifier);

event_timing: 'before' | 'after';

function_prototype
  : identifier LPAREN (function_param_type_list)? RPAREN COLON type
  -> ^(FUNC_PROTO identifier type function_param_type_list?)
  ;

function_param_type_list: t+=type (COMMA t+=type)* -> ^(PARAMS $t+);

function_declaration
  : 'function' identifier LPAREN (function_param_list)? RPAREN function_body
     -> ^(FUNC_DECL identifier function_param_list? function_body)
  ;
function_expression
  : 'function' identifier? LPAREN (function_param_list)? RPAREN function_body
     -> ^(ANON_FUNC_DECL identifier? function_param_list? function_body)
  | identifier -> ^(FUNC_REF identifier)
  ;
function_param_list: p+=identifier (COMMA p+=identifier)* -> ^(PARAMS $p+);
function_body: block_statement;

statements: (statement)*;
statement
  : block_statement
  | assignment_statement
  | increment_statement
  | decrement_statement
  | if_statement
  | case_statement
  | call_expression
  | 'return' -> ^(RETURN)
  ;

block_statement
  : LBRACE RBRACE            -> ^(BLOCK)
  | LBRACE statement+ RBRACE -> ^(BLOCK statement+)
  ;

assignment_statement
  : variable (ASSIGN|ADD|SUB)^ expression
  ;

increment_statement
  : variable '++' -> ^(INC variable)
  ;

decrement_statement
  : variable '--' -> ^(DEC variable)
  ;

if_statement
  : 'if' LPAREN expression RPAREN statement 'else' statement
    -> ^(IF expression statement statement)
  | 'if' LPAREN expression RPAREN statement
    -> ^(IF expression statement)
  ;

case_statement
  : 'case' expression LBRACE case_clauses? else_clause? RBRACE
    -> ^(CASES expression case_clauses?)
  ;

case_clauses: case_clause*;
case_clause
  : function_call_expression block_statement
    -> ^(CASE function_call_expression block_statement)
  ;
else_clause: 'else' statement -> ^(CASE 'else' statement);

expression: logical_expression;

// expressions with presedence, inspired by
// www.codeproject.com/Articles/18880/State-of-the-Art-Expression-Evaluation

logical_expression: or_expression;

or_expression
  : and_expression (OR^ and_expression)*
  ;

and_expression
  : equality_expression (AND^ equality_expression)*
  ;

equality_expression
  : order_expression ((EQUALS | NOTEQUALS)^ order_expression)*
  ;

order_expression
  : left=additive_expression
    ((LT | LTEQ | GT | GTEQ)^ additive_expression)*
  ;

additive_expression
  : left=multiplicative_expression
    ((PLUS | MINUS)^ multiplicative_expression)*
  ;

multiplicative_expression
  : unary_expression (( MULT | DIV | MOD )^ unary_expression)*
  ;

unary_expression
  : NOT^? primary_expression
  ;

primary_expression
  : LPAREN! logical_expression RPAREN!
  | literal
  | call_expression
  | variable
  | atom
  | matching_expression
  ;

call_expression
  : method_call_expression   -> ^(METHOD_CALL method_call_expression)
  | function_call_expression -> ^(FUNC_CALL function_call_expression)
  ;

method_call_expression : object_expression DOT! function_call_expression;
function_call_expression: identifier LPAREN! (argument_list)? RPAREN!;
argument_list: a+=expression (COMMA a+=expression)* -> ^(ARGS $a+);

// functional aliases for identifiers
// TODO: add more
variable
  : property_expression
  | identifier           -> ^(VAR_EXP identifier)
  ;

property_expression
  : object_expression DOT identifier
    -> ^(PROPERTY_EXP object_expression identifier)
  ;

object_expression
  : identifier DOT identifier -> ^(OBJECT_REF identifier identifier)
  | identifier                -> ^(OBJECT_REF identifier)
  | object_literal
  ;

// DIRECTIVES

directive : import_directive;

import_directive : 'from' identifier 'import' function_prototype
                   -> ^(IMPORT identifier function_prototype);

// EXTENSIONS

extension : 'extend' domain 'with' object_literal
            -> ^(EXTEND domain object_literal);

// LITERALS

literal: numeric_literal | boolean_literal | object_literal | list_literal;
boolean_literal
  : value='true'  -> ^(BOOLEAN_LITERAL $value)
  | value='false' -> ^(BOOLEAN_LITERAL $value)
  ;
numeric_literal
  : value=INTEGER -> ^(INTEGER_LITERAL $value)
  | value=FLOAT   -> ^(FLOAT_LITERAL $value)
  ;
object_literal: LBRACE (property_literal_list)? RBRACE
                -> ^(OBJECT_LITERAL property_literal_list?);
property_literal_list: property_literal (property_literal)*;
property_literal: name_type_value -> ^(PROPERTY_LITERAL name_type_value);

name_type_value: identifier optional_type ASSIGN! literal;

optional_type
  : COLON type -> type
  |            -> ^(UNKNOWN_TYPE)
  ;

atom : '#' identifier -> ^(ATOM_LITERAL identifier);

matching_expression
  : dontcare   -> ^(MATCH_EXP dontcare)
  | comparison -> ^(MATCH_EXP comparison)
  ;
dontcare: UNDERSCORE -> ANYTHING;
comparison: comparator expression;
comparator: LT | LTEQ | GT | GTEQ | EQUALS | NOTEQUALS | NOT;

list_literal 
  : LBRACKET RBRACKET -> ^(LIST_LITERAL)
  | LBRACKET i+=expression (COMMA i+=expression)* RBRACKET -> ^(LIST_LITERAL $i+)
  ;

type
  : many_type '*'  -> ^(MANY_TYPE_EXP many_type)    // support for type**
  | many_type      -> many_type
  | basic_type     -> basic_type
  | tuple_type '*' -> ^(MANY_TYPE_EXP tuple_type)
  | tuple_type     -> tuple_type
  ;

many_type
  : basic_type '*' -> ^(MANY_TYPE_EXP basic_type)
  ;

basic_type: type_identifier -> ^(TYPE_EXP type_identifier);
type_identifier
  : t='byte'      -> ^(IDENTIFIER $t)
  | t='integer'   -> ^(IDENTIFIER $t)
  | t='float'     -> ^(IDENTIFIER $t)
  | t='boolean'   -> ^(IDENTIFIER $t)
  | t='timestamp' -> ^(IDENTIFIER $t)
  ;
tuple_type : '[' t+=type (COMMA t+=type)* ']' -> ^(TUPLE_TYPE_EXP $t+);

// to avoid some keywords to be excluded from being an identifier, we add them
// again here.
// TODO: implement error reporting when the source contains a reserved keyword
identifier
  : id=ID       -> ^(IDENTIFIER $id)
  | id='from'   -> ^(IDENTIFIER $id)
  | id='import' -> ^(IDENTIFIER $id)
  | id='with'   -> ^(IDENTIFIER $id)
  | id='use'    -> ^(IDENTIFIER $id)
  | id='extend' -> ^(IDENTIFIER $id)
  ;

// ATOMIC FRAGMENTS aka TOKENS ;-)

INTEGER: '0' | ('1'..'9') ('0'..'9')*;
FLOAT: ('0'..'9')+ '.' ('0'..'9')*;

UNDERSCORE : '_';
PLUS : '+';
MINUS : '-';
LBRACE : '{';
RBRACE : '}';
LPAREN 	: '(';
RPAREN 	: ')';
LBRACKET : '[';
RBRACKET : ']';
COLON: ':';
EQUALS: '==';
NOTEQUALS: '!=';
COMMA: ',';
DOT: '.';
ASSIGN: '=';
ADD: '+=';
SUB: '-=';

AND: 'and';
OR: 'or';
NOT: '!';
GT: '>';
GTEQ: '>=';
LT: '<';
LTEQ: '<=';
MULT: '*';
DIV: '/';
MOD: '%';

// all that remains can be an identifier
ID : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')*;

// WHITESPACE and COMMENTS

COMMENT
 :   '//' ~('\n'|'\r')* '\r'? '\n' {$channel=HIDDEN;}
    |   '/*' ( options {greedy=false;} : . )* '*/' {$channel=HIDDEN;}
    ;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) {$channel=HIDDEN;};
