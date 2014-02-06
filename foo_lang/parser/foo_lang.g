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
  ROOT; MODULE; CONST; EXTERNAL; OBJECT; FUNC_DECL; ANON_FUNC_DECL; FUNC_CALL;
  METHOD_CALL; LIST; PROPERTY; IMPORT; EXTEND; IF; BLOCK; VAR; ANNOTATION;
  ANNOTATED; INC; DEC; APPLY; ON; ATOM; CASES; CASE; TYPE; MANY; TUPLE; VALUE;
  DOMAIN;
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
module : 'module' identifier instructions -> ^(MODULE identifier instructions);

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
  : annotation apply_declaration -> ^(ANNOTATED annotation apply_declaration)
  ;

annotation
  : '@' function_call_expression -> ^(ANNOTATION function_call_expression)
  ;

apply_declaration
  : 'with' identifier DOT identifier 'do' function_expression
    -> ^(APPLY ^(PROPERTY identifier identifier) function_expression)
  | 'with' identifier 'do' function_expression
    -> ^(APPLY ^(DOMAIN identifier) function_expression)
  ;
  
constant_declaration: 'const' typed_value -> ^(CONST typed_value);

typed_value
  :  identifier COLON type ASSIGN literal
    -> ^(VALUE identifier type literal)
  | identifier ASSIGN FLOAT
    -> ^(VALUE identifier ^(TYPE TYPE['float']) FLOAT)
  | identifier ASSIGN INTEGER
    -> ^(VALUE identifier ^(TYPE TYPE['integer']) INTEGER)
  | identifier ASSIGN boolean_literal
    -> ^(VALUE identifier ^(TYPE TYPE['boolean']) boolean_literal)
  ;

event_handler_declaration
  : event_timing identifier identifier 'do' function_expression
    -> ^(ON event_timing identifier identifier function_expression)
  ;

event_timing: 'before' | 'after';

function_declaration
  : 'function' identifier LPAREN (function_param_list)? RPAREN function_body
     -> ^(FUNC_DECL identifier function_param_list? function_body)
  ;
function_expression
  : 'function' identifier? LPAREN (function_param_list)? RPAREN function_body
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
  | decrement_statement
  | if_statement
  | case_statement
  | call_expression
  | 'return'
  ;

block_statement
  : LBRACE RBRACE            -> ^(BLOCK)
  | LBRACE statement+ RBRACE -> ^(BLOCK statement+);

assignment_statement
  : variable (ASSIGN|ADD|SUB)^ expression
  ;

increment_statement
  : variable '++'            -> ^(INC variable)
  ;

decrement_statement
  : variable '--'            -> ^(DEC variable)
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

// TODO: extract object_expression
method_call_expression : identifier DOT! (identifier DOT!)* function_call_expression;
function_call_expression: identifier LPAREN! (argument_list)? RPAREN!;
argument_list: a+=expression (COMMA a+=expression)* -> ^(LIST $a+);

// functional aliases for identifiers
// TODO: add more
variable
  : property_expression
  | identifier           -> ^(VAR identifier)
  ;

property_expression
  : o+=identifier DOT (o+=identifier DOT)* p=identifier
    -> ^(PROPERTY $o+ $p)
  ;

/*object_expression
  : identifier DOT object_expression -> ^(OBJECT identifier object_expression)
  | identifier                       -> ^(OBJECT identifier)
  ;
*/
// DIRECTIVES

directive : import_directive;

import_directive : 'from' identifier 'import' identifier
                   -> ^(IMPORT identifier identifier);

// EXTENSIONS

extension : 'extend' identifier 'with' literal
            -> ^(EXTEND identifier literal);

// LITERALS

literal: numeric_literal | boolean_literal | object_literal | list_literal;
boolean_literal: 'true' | 'false';
numeric_literal: INTEGER | FLOAT;
object_literal: LBRACE (property_type_value_list)? RBRACE
                -> ^(OBJECT property_type_value_list?);
property_type_value_list: property_type_value (property_type_value)*;
property_type_value: typed_value -> ^(PROPERTY typed_value);

atom : '#' identifier -> ^(ATOM identifier);

matching_expression: dontcare | comparison;
dontcare: UNDERSCORE;
comparison: comparator^ expression;
comparator: LT | LTEQ | GT | GTEQ | EQUALS | NOTEQUALS | NOT;

list_literal 
  : LBRACKET RBRACKET -> ^(LIST)
  | LBRACKET i+=expression (COMMA i+=expression)* RBRACKET -> ^(LIST $i+);

type
  : basic_type '*' -> ^(TYPE ^(MANY basic_type))
  | basic_type     -> ^(TYPE basic_type)
  | tuple_type '*' -> ^(TYPE ^(MANY tuple_type))
  | tuple_type     -> ^(TYPE tuple_type)
  ;
basic_type : 'byte' | 'integer' | 'float' | 'boolean' | 'timestamp';
tuple_type : '[' t+=type (COMMA t+=type)* ']' -> ^(TUPLE $t+);

// to avoid some keywords to be excluded from being an identifier, we add them
// again here.
// TODO: implement error reporting when the source contains a reserved keyword
identifier: IDENTIFIER | 'from' | 'import' | 'with' | 'use' | 'extend';

// ATOMIC FRAGMENTS

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
