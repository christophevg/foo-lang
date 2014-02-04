lexer grammar foo_lang;
options {
  language=Python;

}

@members {                 
def reportError(self, e):
  raise e
}

T__64 : '@' ;
T__65 : 'with' ;
T__66 : 'do' ;
T__67 : 'const' ;
T__68 : 'before' ;
T__69 : 'after' ;
T__70 : 'function' ;
T__71 : 'return' ;
T__72 : '++' ;
T__73 : 'if' ;
T__74 : 'else' ;
T__75 : 'case' ;
T__76 : 'from' ;
T__77 : 'import' ;
T__78 : 'extend' ;
T__79 : 'true' ;
T__80 : 'false' ;
T__81 : '#' ;
T__82 : 'byte' ;
T__83 : 'integer' ;
T__84 : 'float' ;
T__85 : 'boolean' ;
T__86 : 'timestamp' ;
T__87 : 'use' ;

// $ANTLR src "foo_lang/parser/foo_lang.g" 279
INTEGER: '0' | ('1'..'9') ('0'..'9')*;
// $ANTLR src "foo_lang/parser/foo_lang.g" 280
FLOAT: ('0'..'9')+ '.' ('0'..'9')*;

// $ANTLR src "foo_lang/parser/foo_lang.g" 282
UNDERSCORE : '_';
// $ANTLR src "foo_lang/parser/foo_lang.g" 283
PLUS : '+';
// $ANTLR src "foo_lang/parser/foo_lang.g" 284
MINUS : '-';
// $ANTLR src "foo_lang/parser/foo_lang.g" 285
LBRACE : '{';
// $ANTLR src "foo_lang/parser/foo_lang.g" 286
RBRACE : '}';
// $ANTLR src "foo_lang/parser/foo_lang.g" 287
LPAREN 	: '(';
// $ANTLR src "foo_lang/parser/foo_lang.g" 288
RPAREN 	: ')';
// $ANTLR src "foo_lang/parser/foo_lang.g" 289
LBRACKET : '[';
// $ANTLR src "foo_lang/parser/foo_lang.g" 290
RBRACKET : ']';
// $ANTLR src "foo_lang/parser/foo_lang.g" 291
COLON: ':';
// $ANTLR src "foo_lang/parser/foo_lang.g" 292
EQUALS: '==';
// $ANTLR src "foo_lang/parser/foo_lang.g" 293
NOTEQUALS: '!=';
// $ANTLR src "foo_lang/parser/foo_lang.g" 294
COMMA: ',';
// $ANTLR src "foo_lang/parser/foo_lang.g" 295
DOT: '.';
// $ANTLR src "foo_lang/parser/foo_lang.g" 296
ASSIGN: '=';
// $ANTLR src "foo_lang/parser/foo_lang.g" 297
ADD: '+=';
// $ANTLR src "foo_lang/parser/foo_lang.g" 298
SUB: '-=';

// $ANTLR src "foo_lang/parser/foo_lang.g" 300
AND: 'and';
// $ANTLR src "foo_lang/parser/foo_lang.g" 301
OR: 'or';
// $ANTLR src "foo_lang/parser/foo_lang.g" 302
NOT: '!';
// $ANTLR src "foo_lang/parser/foo_lang.g" 303
GT: '>';
// $ANTLR src "foo_lang/parser/foo_lang.g" 304
GTEQ: '>=';
// $ANTLR src "foo_lang/parser/foo_lang.g" 305
LT: '<';
// $ANTLR src "foo_lang/parser/foo_lang.g" 306
LTEQ: '<=';
// $ANTLR src "foo_lang/parser/foo_lang.g" 307
MULT: '*';
// $ANTLR src "foo_lang/parser/foo_lang.g" 308
DIV: '/';
// $ANTLR src "foo_lang/parser/foo_lang.g" 309
MOD: '%';

// all that remains can be an identifier
// $ANTLR src "foo_lang/parser/foo_lang.g" 312
IDENTIFIER : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')*;

// WHITESPACE and COMMENTS

// $ANTLR src "foo_lang/parser/foo_lang.g" 316
COMMENT
 :   '//' ~('\n'|'\r')* '\r'? '\n' {$channel=HIDDEN;}
    |   '/*' ( options {greedy=false;} : . )* '*/' {$channel=HIDDEN;}
    ;

// $ANTLR src "foo_lang/parser/foo_lang.g" 321
WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) {$channel=HIDDEN;};
