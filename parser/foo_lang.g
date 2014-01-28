// foo_lang.g
// author: Christophe VG

// ANTLR3 grammar for foo_lang-lang, a Function Organisation Optimizing DSL

grammar foo_lang;

options {
  output=AST;
  language=Python;
  backtrack=true;
}

// a few virtual tokens, used as identifying node
tokens {  // must be declared here/before use, not with other real tokens below
  ROOT;  CONST;  EXTERNAL;  OBJECT;  FUNC_DECL;  ANON_FUNC_DECL;  FUNC_CALL;
  METHOD_CALL;  LIST;  PROPERTY;  USE;  IMPORT;  EXTEND;  IF;  BLOCK;  VAR;
  ANNOTATION;  ANNOTATED;  INC;  ASSIGN;  APPLY;  ON;  ATOM;  CASES;  CASE;
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
  # TODO: raise better exception -> RecognitionException?
  raise RuntimeError("expecting different input...")
}

@rulecatch {
except RecognitionException, e:
  raise
}

@header {
  from foo_lang import *
}

// PARSING RULES

start : instructions? EOF -> ^(ROOT instructions?);
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
  : annotation apply_declaration -> ^(ANNOTATED apply_declaration)
  ;

annotation
  : '@' function_call_expression -> ^(ANNOTATION function_call_expression)
  ;

apply_declaration
  : 'with' variable 'do' function_expression
    -> ^(APPLY variable function_expression)
  ;

constant_declaration : 'const' identifier IS literal
                       -> ^(CONST identifier literal);

event_handler_declaration
  : event_timing identifier identifier 'do' function_expression
    -> ^(ON event_timing identifier identifier function_expression)
  ;

fragment event_timing: 'before' | 'after';

function_declaration : 'function' identifier
                       LPAREN (function_param_list)? RPAREN
                       function_body
                       -> ^(FUNC_DECL identifier function_param_list? function_body);
function_expression
  : 'function' identifier? LPAREN (function_param_list)? RPAREN
     function_body
     -> ^(ANON_FUNC_DECL identifier? function_param_list? function_body)
  | identifier
  ;
function_param_list: p+=identifier (COMMA p+=identifier)* -> ^(LIST $p+);
function_body: block_statement;

statements: (statement)*;
statement
  : block_statement
  | assignment_statement
  | increment_statement
  | if_statement
  | case_statement
  | call_expression
  ;

block_statement
  : LBRACE RBRACE            -> ^(BLOCK)
  | LBRACE statement+ RBRACE -> ^(BLOCK statement+);

assignment_statement
  : property_expression '=' expression  -> ^(ASSIGN property_expression expression)
  | variable '=' expression             -> ^(ASSIGN variable expression)
  ;

increment_statement
  : property_expression '++' -> ^(INC property_expression)
  | variable '++'            -> ^(INC variable)
  ;

if_statement
  : 'if' LPAREN expression RPAREN statement 'else' statement
    -> ^(IF expression statement statement)
  | 'if' LPAREN expression RPAREN statement
    -> ^(IF expression statement)
  ;

case_statement
  : 'case' expression LBRACE case_clauses? RBRACE
    -> ^(CASES expression case_clauses?)
  ;

case_clauses  : case_clause*;
case_clause
  : function_call_expression block_statement
    -> ^(CASE function_call_expression block_statement)
  ;

expression: logical_expression;

// expressions with presedence, inspired by
// www.codeproject.com/Articles/18880/State-of-the-Art-Expression-Evaluation

logical_expression: or_expression;

or_expression
  : and_expression (OR and_expression)*
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
  : NOT^? primary_expression { if $NOT != None: print "primary as unary" }
  ;

primary_expression
  : LPAREN! logical_expression RPAREN!
  | literal
  | call_expression
  | property_expression
  | variable
  | atom
  ;

call_expression
  : method_call_expression   -> ^(METHOD_CALL method_call_expression)
  | function_call_expression -> ^(FUNC_CALL function_call_expression)
  ;

method_call_expression : identifier DOT! function_call_expression;

function_call_expression: identifier LPAREN! (argument_list)? RPAREN!;
fragment argument_list: a+=expression (COMMA a+=expression)* -> ^(LIST $a+);

property_expression: identifier DOT identifier -> ^(PROPERTY identifier identifier);

// functional aliases for identifiers
// TODO: add more
variable
  : identifier -> ^(VAR identifier)
  | property_expression;

// DIRECTIVES

directive : usage_directive | import_directive;

usage_directive : 'use' identifier -> ^(USE identifier);

import_directive : 'from' identifier 'import' identifier
                   -> ^(IMPORT identifier identifier);

// EXTENSIONS

extension : 'extend' identifier 'with' literal
            -> ^(EXTEND identifier literal);

// LITERALS

literal : numeric_literal | boolean_literal | object_literal | list_literal;
boolean_literal : 'true' | 'false';
numeric_literal : INTEGER;
object_literal: LBRACE (property_type_value_list)? RBRACE
                -> ^(OBJECT property_type_value_list?);
fragment property_type_value_list: property_type_value (property_type_value)*;
fragment property_type_value : identifier^ COLON! identifier IS! literal;

atom : '#' identifier -> ^(ATOM identifier);

list_literal 
  : LBRACKET RBRACKET -> ^(LIST)
  | LBRACKET i+=expression (COMMA i+=expression)* RBRACKET -> ^(LIST $i+);

// to avoid some keywords to be excluded from being an identifier, we add them
// again here.
// TODO: implement error reporting when the source contains a reserved keyword
identifier: IDENTIFIER | 'from' | 'import' | 'with' | 'use' | 'extend';

// ATOMIC FRAGMENTS

INTEGER: '0' | ('1'..'9') ('0'..'9')*;

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
IS: '=';
EQUALS: '==';
NOTEQUALS: '!=';
COMMA: ',';
DOT: '.';

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
IDENTIFIER : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')*;

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
