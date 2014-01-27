// foo_lang.g
// author: Christophe VG

// ANTLR3 grammar for foo_lang-lang, a Function Organisation Optimizing DSL

grammar foo_lang;

options {
  language=Python;
  backtrack=true;
}

// to have our parser raise its exceptions we need to override some methods in
// the lexer
// trick found at:
// http://www.dalkescientific.com/writings/diary/archive/2007/11/03/

@lexer::members {
def reportError(self, e):
   raise e
}

@rulecatch {
except RecognitionException, e:
    raise
}

@header {
  from foo_lang import *
}

// PARSING RULES

compilation_unit : statements?;
statements : (statement)+;
statement
  : declaration
  | directive
  | extension
  ;

declaration : constant_declaration;

directive : usage_directive | import_directive;

constant_declaration : 'const' IDENTIFIER literal;

usage_directive : 'use' IDENTIFIER;

import_directive : 'import' IDENTIFIER 'from' IDENTIFIER;

extension : 'extend' IDENTIFIER 'with' object_literal;

// LITERALS

literal : numeric_literal | boolean_literal;

boolean_literal : TRUE | FALSE;

numeric_literal : integer_literal;
  
integer_literal
  : ZERO
  | NON_ZERO_DIGIT digit*
  ;

object_literal: LBRACE (property_type_value_list)? RBRACE;
fragment property_type_value_list: property_type_value (property_type_value_list_tail)*;
fragment property_type_value : IDENTIFIER COLON IDENTIFIER EQUAL literal;
fragment property_type_value_list_tail : IDENTIFIER COLON IDENTIFIER EQUAL literal;

// ATOMIC FRAGMENTS

digit : ZERO | NON_ZERO_DIGIT;

ZERO : '0';
NON_ZERO_DIGIT : ('1'..'9');

TRUE : 'true';
FALSE : 'false';

UNDERSCORE : '_';
PLUS : '+';
MINUS : '-';
LBRACE : '{';
RBRACE : '}';
COLON: ':';
EQUAL: '=';

IDENTIFIER : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')*;

// WHITESPACE and COMMENTS

WS      : (' '|'\r'|'\t'|'\u000C'|'\n') { $channel=HIDDEN };
COMMENT : '%' ~('\n'|'\r')* '\r'? '\n'  { $channel=HIDDEN };

/*
compilation_unit returns [list] @init { list = [] }
                 : statements? { list = $statements.list }
                 ;

statements returns [list] @init { list = [] }
           : (statement { list.append($statement.instance) })+
           ;

statement returns [instance]
          : assignment { instance = $assignment.instance }
          ;

assignment returns [instance]
          : IDENTIFIER EQUALS expression {
            instance = assignment($IDENTIFIER.getText(), $expression.instance)
          }
          ;

expression returns [instance]
           : literal { instance = $literal.instance }
           ;

literal returns [ instance ]
        : boolean_literal { $instance = $boolean_literal.instance }
        | float_literal   { $instance = $float_literal.instance   }
        | integer_literal { $instance = $integer_literal.instance }
        ;

boolean_literal returns [instance]
                : BOOLEAN {
                  value = True if $BOOLEAN.getText() == "true" else False
                  $instance = boolean(value)
                }
                ;

float_literal returns [instance]
              : FLOAT { instance = floating( float($FLOAT.getText())) }
              ;

integer_literal returns [instance]
                : INTEGER { instance = integer( int($INTEGER.getText())) }
                ;
*/
