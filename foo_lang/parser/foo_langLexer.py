# $ANTLR 3.1 foo_lang/parser/foo_lang.g 2014-02-05 11:56:58

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__68=68
T__69=69
EXTERNAL=6
APPLY=22
T__66=66
T__67=67
LT=48
T__64=64
T__65=65
MOD=56
ANNOTATION=19
CONST=5
LBRACE=40
CASE=26
LTEQ=49
CASES=25
ANON_FUNC_DECL=9
SUB=43
EQUALS=46
FLOAT=35
NOT=57
ATOM=24
AND=45
EOF=-1
LPAREN=37
TYPE=27
FUNC_CALL=10
IF=16
LBRACKET=59
RPAREN=38
TUPLE=29
INC=21
EXTEND=15
IMPORT=14
OBJECT=7
COMMA=39
IDENTIFIER=61
ANNOTATED=20
PLUS=52
VAR=18
RBRACKET=60
DOT=32
COMMENT=62
ADD=42
INTEGER=36
T__80=80
T__81=81
T__82=82
RBRACE=41
T__83=83
ON=23
NOTEQUALS=47
UNDERSCORE=58
VALUE=30
GTEQ=51
MINUS=53
MULT=54
T__85=85
LIST=12
T__84=84
METHOD_CALL=11
ROOT=4
T__87=87
T__86=86
MANY=28
DOMAIN=31
FUNC_DECL=8
COLON=33
T__71=71
WS=63
T__72=72
T__70=70
PROPERTY=13
BLOCK=17
OR=44
ASSIGN=34
GT=50
DIV=55
T__76=76
T__75=75
T__74=74
T__73=73
T__79=79
T__78=78
T__77=77


class foo_langLexer(Lexer):

    grammarFileName = "foo_lang/parser/foo_lang.g"
    antlr_version = version_str_to_tuple("3.1")
    antlr_version_str = "3.1"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )




                               
    def reportError(self, e):
      raise e



    # $ANTLR start "T__64"
    def mT__64(self, ):

        try:
            _type = T__64
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:12:7: ( '@' )
            # foo_lang/parser/foo_lang.g:12:9: '@'
            pass 
            self.match(64)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__64"



    # $ANTLR start "T__65"
    def mT__65(self, ):

        try:
            _type = T__65
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:13:7: ( 'with' )
            # foo_lang/parser/foo_lang.g:13:9: 'with'
            pass 
            self.match("with")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__65"



    # $ANTLR start "T__66"
    def mT__66(self, ):

        try:
            _type = T__66
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:14:7: ( 'do' )
            # foo_lang/parser/foo_lang.g:14:9: 'do'
            pass 
            self.match("do")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__66"



    # $ANTLR start "T__67"
    def mT__67(self, ):

        try:
            _type = T__67
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:15:7: ( 'const' )
            # foo_lang/parser/foo_lang.g:15:9: 'const'
            pass 
            self.match("const")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__67"



    # $ANTLR start "T__68"
    def mT__68(self, ):

        try:
            _type = T__68
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:16:7: ( 'before' )
            # foo_lang/parser/foo_lang.g:16:9: 'before'
            pass 
            self.match("before")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__68"



    # $ANTLR start "T__69"
    def mT__69(self, ):

        try:
            _type = T__69
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:17:7: ( 'after' )
            # foo_lang/parser/foo_lang.g:17:9: 'after'
            pass 
            self.match("after")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__69"



    # $ANTLR start "T__70"
    def mT__70(self, ):

        try:
            _type = T__70
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:18:7: ( 'function' )
            # foo_lang/parser/foo_lang.g:18:9: 'function'
            pass 
            self.match("function")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__70"



    # $ANTLR start "T__71"
    def mT__71(self, ):

        try:
            _type = T__71
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:19:7: ( 'return' )
            # foo_lang/parser/foo_lang.g:19:9: 'return'
            pass 
            self.match("return")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__71"



    # $ANTLR start "T__72"
    def mT__72(self, ):

        try:
            _type = T__72
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:20:7: ( '++' )
            # foo_lang/parser/foo_lang.g:20:9: '++'
            pass 
            self.match("++")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__72"



    # $ANTLR start "T__73"
    def mT__73(self, ):

        try:
            _type = T__73
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:21:7: ( 'if' )
            # foo_lang/parser/foo_lang.g:21:9: 'if'
            pass 
            self.match("if")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__73"



    # $ANTLR start "T__74"
    def mT__74(self, ):

        try:
            _type = T__74
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:22:7: ( 'else' )
            # foo_lang/parser/foo_lang.g:22:9: 'else'
            pass 
            self.match("else")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__74"



    # $ANTLR start "T__75"
    def mT__75(self, ):

        try:
            _type = T__75
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:23:7: ( 'case' )
            # foo_lang/parser/foo_lang.g:23:9: 'case'
            pass 
            self.match("case")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__75"



    # $ANTLR start "T__76"
    def mT__76(self, ):

        try:
            _type = T__76
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:24:7: ( 'from' )
            # foo_lang/parser/foo_lang.g:24:9: 'from'
            pass 
            self.match("from")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__76"



    # $ANTLR start "T__77"
    def mT__77(self, ):

        try:
            _type = T__77
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:25:7: ( 'import' )
            # foo_lang/parser/foo_lang.g:25:9: 'import'
            pass 
            self.match("import")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__77"



    # $ANTLR start "T__78"
    def mT__78(self, ):

        try:
            _type = T__78
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:26:7: ( 'extend' )
            # foo_lang/parser/foo_lang.g:26:9: 'extend'
            pass 
            self.match("extend")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__78"



    # $ANTLR start "T__79"
    def mT__79(self, ):

        try:
            _type = T__79
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:27:7: ( 'true' )
            # foo_lang/parser/foo_lang.g:27:9: 'true'
            pass 
            self.match("true")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__79"



    # $ANTLR start "T__80"
    def mT__80(self, ):

        try:
            _type = T__80
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:28:7: ( 'false' )
            # foo_lang/parser/foo_lang.g:28:9: 'false'
            pass 
            self.match("false")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__80"



    # $ANTLR start "T__81"
    def mT__81(self, ):

        try:
            _type = T__81
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:29:7: ( '#' )
            # foo_lang/parser/foo_lang.g:29:9: '#'
            pass 
            self.match(35)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__81"



    # $ANTLR start "T__82"
    def mT__82(self, ):

        try:
            _type = T__82
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:30:7: ( 'byte' )
            # foo_lang/parser/foo_lang.g:30:9: 'byte'
            pass 
            self.match("byte")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__82"



    # $ANTLR start "T__83"
    def mT__83(self, ):

        try:
            _type = T__83
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:31:7: ( 'integer' )
            # foo_lang/parser/foo_lang.g:31:9: 'integer'
            pass 
            self.match("integer")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__83"



    # $ANTLR start "T__84"
    def mT__84(self, ):

        try:
            _type = T__84
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:32:7: ( 'float' )
            # foo_lang/parser/foo_lang.g:32:9: 'float'
            pass 
            self.match("float")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__84"



    # $ANTLR start "T__85"
    def mT__85(self, ):

        try:
            _type = T__85
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:33:7: ( 'boolean' )
            # foo_lang/parser/foo_lang.g:33:9: 'boolean'
            pass 
            self.match("boolean")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__85"



    # $ANTLR start "T__86"
    def mT__86(self, ):

        try:
            _type = T__86
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:34:7: ( 'timestamp' )
            # foo_lang/parser/foo_lang.g:34:9: 'timestamp'
            pass 
            self.match("timestamp")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__86"



    # $ANTLR start "T__87"
    def mT__87(self, ):

        try:
            _type = T__87
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:35:7: ( 'use' )
            # foo_lang/parser/foo_lang.g:35:9: 'use'
            pass 
            self.match("use")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__87"



    # $ANTLR start "INTEGER"
    def mINTEGER(self, ):

        try:
            _type = INTEGER
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:279:8: ( '0' | ( '1' .. '9' ) ( '0' .. '9' )* )
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 48) :
                alt2 = 1
            elif ((49 <= LA2_0 <= 57)) :
                alt2 = 2
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae

            if alt2 == 1:
                # foo_lang/parser/foo_lang.g:279:10: '0'
                pass 
                self.match(48)


            elif alt2 == 2:
                # foo_lang/parser/foo_lang.g:279:16: ( '1' .. '9' ) ( '0' .. '9' )*
                pass 
                # foo_lang/parser/foo_lang.g:279:16: ( '1' .. '9' )
                # foo_lang/parser/foo_lang.g:279:17: '1' .. '9'
                pass 
                self.matchRange(49, 57)



                # foo_lang/parser/foo_lang.g:279:27: ( '0' .. '9' )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((48 <= LA1_0 <= 57)) :
                        alt1 = 1


                    if alt1 == 1:
                        # foo_lang/parser/foo_lang.g:279:28: '0' .. '9'
                        pass 
                        self.matchRange(48, 57)


                    else:
                        break #loop1




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTEGER"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):

        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:280:6: ( ( '0' .. '9' )+ '.' ( '0' .. '9' )* )
            # foo_lang/parser/foo_lang.g:280:8: ( '0' .. '9' )+ '.' ( '0' .. '9' )*
            pass 
            # foo_lang/parser/foo_lang.g:280:8: ( '0' .. '9' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((48 <= LA3_0 <= 57)) :
                    alt3 = 1


                if alt3 == 1:
                    # foo_lang/parser/foo_lang.g:280:9: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1


            self.match(46)
            # foo_lang/parser/foo_lang.g:280:24: ( '0' .. '9' )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((48 <= LA4_0 <= 57)) :
                    alt4 = 1


                if alt4 == 1:
                    # foo_lang/parser/foo_lang.g:280:25: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    break #loop4





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "UNDERSCORE"
    def mUNDERSCORE(self, ):

        try:
            _type = UNDERSCORE
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:282:12: ( '_' )
            # foo_lang/parser/foo_lang.g:282:14: '_'
            pass 
            self.match(95)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNDERSCORE"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:283:6: ( '+' )
            # foo_lang/parser/foo_lang.g:283:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:284:7: ( '-' )
            # foo_lang/parser/foo_lang.g:284:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "LBRACE"
    def mLBRACE(self, ):

        try:
            _type = LBRACE
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:285:8: ( '{' )
            # foo_lang/parser/foo_lang.g:285:10: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LBRACE"



    # $ANTLR start "RBRACE"
    def mRBRACE(self, ):

        try:
            _type = RBRACE
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:286:8: ( '}' )
            # foo_lang/parser/foo_lang.g:286:10: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RBRACE"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):

        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:287:9: ( '(' )
            # foo_lang/parser/foo_lang.g:287:11: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):

        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:288:9: ( ')' )
            # foo_lang/parser/foo_lang.g:288:11: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "LBRACKET"
    def mLBRACKET(self, ):

        try:
            _type = LBRACKET
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:289:10: ( '[' )
            # foo_lang/parser/foo_lang.g:289:12: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LBRACKET"



    # $ANTLR start "RBRACKET"
    def mRBRACKET(self, ):

        try:
            _type = RBRACKET
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:290:10: ( ']' )
            # foo_lang/parser/foo_lang.g:290:12: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RBRACKET"



    # $ANTLR start "COLON"
    def mCOLON(self, ):

        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:291:6: ( ':' )
            # foo_lang/parser/foo_lang.g:291:8: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "EQUALS"
    def mEQUALS(self, ):

        try:
            _type = EQUALS
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:292:7: ( '==' )
            # foo_lang/parser/foo_lang.g:292:9: '=='
            pass 
            self.match("==")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUALS"



    # $ANTLR start "NOTEQUALS"
    def mNOTEQUALS(self, ):

        try:
            _type = NOTEQUALS
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:293:10: ( '!=' )
            # foo_lang/parser/foo_lang.g:293:12: '!='
            pass 
            self.match("!=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOTEQUALS"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:294:6: ( ',' )
            # foo_lang/parser/foo_lang.g:294:8: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:295:4: ( '.' )
            # foo_lang/parser/foo_lang.g:295:6: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "ASSIGN"
    def mASSIGN(self, ):

        try:
            _type = ASSIGN
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:296:7: ( '=' )
            # foo_lang/parser/foo_lang.g:296:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSIGN"



    # $ANTLR start "ADD"
    def mADD(self, ):

        try:
            _type = ADD
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:297:4: ( '+=' )
            # foo_lang/parser/foo_lang.g:297:6: '+='
            pass 
            self.match("+=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ADD"



    # $ANTLR start "SUB"
    def mSUB(self, ):

        try:
            _type = SUB
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:298:4: ( '-=' )
            # foo_lang/parser/foo_lang.g:298:6: '-='
            pass 
            self.match("-=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SUB"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:300:4: ( 'and' )
            # foo_lang/parser/foo_lang.g:300:6: 'and'
            pass 
            self.match("and")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:301:3: ( 'or' )
            # foo_lang/parser/foo_lang.g:301:5: 'or'
            pass 
            self.match("or")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:302:4: ( '!' )
            # foo_lang/parser/foo_lang.g:302:6: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "GT"
    def mGT(self, ):

        try:
            _type = GT
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:303:3: ( '>' )
            # foo_lang/parser/foo_lang.g:303:5: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GT"



    # $ANTLR start "GTEQ"
    def mGTEQ(self, ):

        try:
            _type = GTEQ
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:304:5: ( '>=' )
            # foo_lang/parser/foo_lang.g:304:7: '>='
            pass 
            self.match(">=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GTEQ"



    # $ANTLR start "LT"
    def mLT(self, ):

        try:
            _type = LT
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:305:3: ( '<' )
            # foo_lang/parser/foo_lang.g:305:5: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LT"



    # $ANTLR start "LTEQ"
    def mLTEQ(self, ):

        try:
            _type = LTEQ
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:306:5: ( '<=' )
            # foo_lang/parser/foo_lang.g:306:7: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LTEQ"



    # $ANTLR start "MULT"
    def mMULT(self, ):

        try:
            _type = MULT
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:307:5: ( '*' )
            # foo_lang/parser/foo_lang.g:307:7: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MULT"



    # $ANTLR start "DIV"
    def mDIV(self, ):

        try:
            _type = DIV
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:308:4: ( '/' )
            # foo_lang/parser/foo_lang.g:308:6: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIV"



    # $ANTLR start "MOD"
    def mMOD(self, ):

        try:
            _type = MOD
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:309:4: ( '%' )
            # foo_lang/parser/foo_lang.g:309:6: '%'
            pass 
            self.match(37)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MOD"



    # $ANTLR start "IDENTIFIER"
    def mIDENTIFIER(self, ):

        try:
            _type = IDENTIFIER
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:312:12: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )* )
            # foo_lang/parser/foo_lang.g:312:14: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # foo_lang/parser/foo_lang.g:312:38: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or (65 <= LA5_0 <= 90) or LA5_0 == 95 or (97 <= LA5_0 <= 122)) :
                    alt5 = 1


                if alt5 == 1:
                    # foo_lang/parser/foo_lang.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop5





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IDENTIFIER"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:317:2: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' | '/*' ( options {greedy=false; } : . )* '*/' )
            alt9 = 2
            LA9_0 = self.input.LA(1)

            if (LA9_0 == 47) :
                LA9_1 = self.input.LA(2)

                if (LA9_1 == 47) :
                    alt9 = 1
                elif (LA9_1 == 42) :
                    alt9 = 2
                else:
                    nvae = NoViableAltException("", 9, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 9, 0, self.input)

                raise nvae

            if alt9 == 1:
                # foo_lang/parser/foo_lang.g:317:6: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
                pass 
                self.match("//")
                # foo_lang/parser/foo_lang.g:317:11: (~ ( '\\n' | '\\r' ) )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((0 <= LA6_0 <= 9) or (11 <= LA6_0 <= 12) or (14 <= LA6_0 <= 65534)) :
                        alt6 = 1


                    if alt6 == 1:
                        # foo_lang/parser/foo_lang.g:317:11: ~ ( '\\n' | '\\r' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65534):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop6


                # foo_lang/parser/foo_lang.g:317:25: ( '\\r' )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 13) :
                    alt7 = 1
                if alt7 == 1:
                    # foo_lang/parser/foo_lang.g:317:25: '\\r'
                    pass 
                    self.match(13)



                self.match(10)
                #action start
                _channel=HIDDEN;
                #action end


            elif alt9 == 2:
                # foo_lang/parser/foo_lang.g:318:9: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")
                # foo_lang/parser/foo_lang.g:318:14: ( options {greedy=false; } : . )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 42) :
                        LA8_1 = self.input.LA(2)

                        if (LA8_1 == 47) :
                            alt8 = 2
                        elif ((0 <= LA8_1 <= 46) or (48 <= LA8_1 <= 65534)) :
                            alt8 = 1


                    elif ((0 <= LA8_0 <= 41) or (43 <= LA8_0 <= 65534)) :
                        alt8 = 1


                    if alt8 == 1:
                        # foo_lang/parser/foo_lang.g:318:42: .
                        pass 
                        self.matchAny()


                    else:
                        break #loop8


                self.match("*/")
                #action start
                _channel=HIDDEN;
                #action end


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # foo_lang/parser/foo_lang.g:321:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # foo_lang/parser/foo_lang.g:321:9: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # foo_lang/parser/foo_lang.g:1:8: ( T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | T__80 | T__81 | T__82 | T__83 | T__84 | T__85 | T__86 | T__87 | INTEGER | FLOAT | UNDERSCORE | PLUS | MINUS | LBRACE | RBRACE | LPAREN | RPAREN | LBRACKET | RBRACKET | COLON | EQUALS | NOTEQUALS | COMMA | DOT | ASSIGN | ADD | SUB | AND | OR | NOT | GT | GTEQ | LT | LTEQ | MULT | DIV | MOD | IDENTIFIER | COMMENT | WS )
        alt10 = 56
        alt10 = self.dfa10.predict(self.input)
        if alt10 == 1:
            # foo_lang/parser/foo_lang.g:1:10: T__64
            pass 
            self.mT__64()


        elif alt10 == 2:
            # foo_lang/parser/foo_lang.g:1:16: T__65
            pass 
            self.mT__65()


        elif alt10 == 3:
            # foo_lang/parser/foo_lang.g:1:22: T__66
            pass 
            self.mT__66()


        elif alt10 == 4:
            # foo_lang/parser/foo_lang.g:1:28: T__67
            pass 
            self.mT__67()


        elif alt10 == 5:
            # foo_lang/parser/foo_lang.g:1:34: T__68
            pass 
            self.mT__68()


        elif alt10 == 6:
            # foo_lang/parser/foo_lang.g:1:40: T__69
            pass 
            self.mT__69()


        elif alt10 == 7:
            # foo_lang/parser/foo_lang.g:1:46: T__70
            pass 
            self.mT__70()


        elif alt10 == 8:
            # foo_lang/parser/foo_lang.g:1:52: T__71
            pass 
            self.mT__71()


        elif alt10 == 9:
            # foo_lang/parser/foo_lang.g:1:58: T__72
            pass 
            self.mT__72()


        elif alt10 == 10:
            # foo_lang/parser/foo_lang.g:1:64: T__73
            pass 
            self.mT__73()


        elif alt10 == 11:
            # foo_lang/parser/foo_lang.g:1:70: T__74
            pass 
            self.mT__74()


        elif alt10 == 12:
            # foo_lang/parser/foo_lang.g:1:76: T__75
            pass 
            self.mT__75()


        elif alt10 == 13:
            # foo_lang/parser/foo_lang.g:1:82: T__76
            pass 
            self.mT__76()


        elif alt10 == 14:
            # foo_lang/parser/foo_lang.g:1:88: T__77
            pass 
            self.mT__77()


        elif alt10 == 15:
            # foo_lang/parser/foo_lang.g:1:94: T__78
            pass 
            self.mT__78()


        elif alt10 == 16:
            # foo_lang/parser/foo_lang.g:1:100: T__79
            pass 
            self.mT__79()


        elif alt10 == 17:
            # foo_lang/parser/foo_lang.g:1:106: T__80
            pass 
            self.mT__80()


        elif alt10 == 18:
            # foo_lang/parser/foo_lang.g:1:112: T__81
            pass 
            self.mT__81()


        elif alt10 == 19:
            # foo_lang/parser/foo_lang.g:1:118: T__82
            pass 
            self.mT__82()


        elif alt10 == 20:
            # foo_lang/parser/foo_lang.g:1:124: T__83
            pass 
            self.mT__83()


        elif alt10 == 21:
            # foo_lang/parser/foo_lang.g:1:130: T__84
            pass 
            self.mT__84()


        elif alt10 == 22:
            # foo_lang/parser/foo_lang.g:1:136: T__85
            pass 
            self.mT__85()


        elif alt10 == 23:
            # foo_lang/parser/foo_lang.g:1:142: T__86
            pass 
            self.mT__86()


        elif alt10 == 24:
            # foo_lang/parser/foo_lang.g:1:148: T__87
            pass 
            self.mT__87()


        elif alt10 == 25:
            # foo_lang/parser/foo_lang.g:1:154: INTEGER
            pass 
            self.mINTEGER()


        elif alt10 == 26:
            # foo_lang/parser/foo_lang.g:1:162: FLOAT
            pass 
            self.mFLOAT()


        elif alt10 == 27:
            # foo_lang/parser/foo_lang.g:1:168: UNDERSCORE
            pass 
            self.mUNDERSCORE()


        elif alt10 == 28:
            # foo_lang/parser/foo_lang.g:1:179: PLUS
            pass 
            self.mPLUS()


        elif alt10 == 29:
            # foo_lang/parser/foo_lang.g:1:184: MINUS
            pass 
            self.mMINUS()


        elif alt10 == 30:
            # foo_lang/parser/foo_lang.g:1:190: LBRACE
            pass 
            self.mLBRACE()


        elif alt10 == 31:
            # foo_lang/parser/foo_lang.g:1:197: RBRACE
            pass 
            self.mRBRACE()


        elif alt10 == 32:
            # foo_lang/parser/foo_lang.g:1:204: LPAREN
            pass 
            self.mLPAREN()


        elif alt10 == 33:
            # foo_lang/parser/foo_lang.g:1:211: RPAREN
            pass 
            self.mRPAREN()


        elif alt10 == 34:
            # foo_lang/parser/foo_lang.g:1:218: LBRACKET
            pass 
            self.mLBRACKET()


        elif alt10 == 35:
            # foo_lang/parser/foo_lang.g:1:227: RBRACKET
            pass 
            self.mRBRACKET()


        elif alt10 == 36:
            # foo_lang/parser/foo_lang.g:1:236: COLON
            pass 
            self.mCOLON()


        elif alt10 == 37:
            # foo_lang/parser/foo_lang.g:1:242: EQUALS
            pass 
            self.mEQUALS()


        elif alt10 == 38:
            # foo_lang/parser/foo_lang.g:1:249: NOTEQUALS
            pass 
            self.mNOTEQUALS()


        elif alt10 == 39:
            # foo_lang/parser/foo_lang.g:1:259: COMMA
            pass 
            self.mCOMMA()


        elif alt10 == 40:
            # foo_lang/parser/foo_lang.g:1:265: DOT
            pass 
            self.mDOT()


        elif alt10 == 41:
            # foo_lang/parser/foo_lang.g:1:269: ASSIGN
            pass 
            self.mASSIGN()


        elif alt10 == 42:
            # foo_lang/parser/foo_lang.g:1:276: ADD
            pass 
            self.mADD()


        elif alt10 == 43:
            # foo_lang/parser/foo_lang.g:1:280: SUB
            pass 
            self.mSUB()


        elif alt10 == 44:
            # foo_lang/parser/foo_lang.g:1:284: AND
            pass 
            self.mAND()


        elif alt10 == 45:
            # foo_lang/parser/foo_lang.g:1:288: OR
            pass 
            self.mOR()


        elif alt10 == 46:
            # foo_lang/parser/foo_lang.g:1:291: NOT
            pass 
            self.mNOT()


        elif alt10 == 47:
            # foo_lang/parser/foo_lang.g:1:295: GT
            pass 
            self.mGT()


        elif alt10 == 48:
            # foo_lang/parser/foo_lang.g:1:298: GTEQ
            pass 
            self.mGTEQ()


        elif alt10 == 49:
            # foo_lang/parser/foo_lang.g:1:303: LT
            pass 
            self.mLT()


        elif alt10 == 50:
            # foo_lang/parser/foo_lang.g:1:306: LTEQ
            pass 
            self.mLTEQ()


        elif alt10 == 51:
            # foo_lang/parser/foo_lang.g:1:311: MULT
            pass 
            self.mMULT()


        elif alt10 == 52:
            # foo_lang/parser/foo_lang.g:1:316: DIV
            pass 
            self.mDIV()


        elif alt10 == 53:
            # foo_lang/parser/foo_lang.g:1:320: MOD
            pass 
            self.mMOD()


        elif alt10 == 54:
            # foo_lang/parser/foo_lang.g:1:324: IDENTIFIER
            pass 
            self.mIDENTIFIER()


        elif alt10 == 55:
            # foo_lang/parser/foo_lang.g:1:335: COMMENT
            pass 
            self.mCOMMENT()


        elif alt10 == 56:
            # foo_lang/parser/foo_lang.g:1:343: WS
            pass 
            self.mWS()







    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\2\uffff\7\44\1\66\3\44\1\uffff\1\44\2\100\1\102\1\104\7\uffff"
        u"\1\106\1\110\2\uffff\1\44\1\113\1\115\1\uffff\1\117\3\uffff\1\44"
        u"\1\121\14\44\3\uffff\1\136\7\44\2\uffff\1\100\7\uffff\1\146\6\uffff"
        u"\1\44\1\uffff\6\44\1\156\5\44\1\uffff\6\44\1\172\1\uffff\1\173"
        u"\1\44\1\175\1\44\1\177\2\44\1\uffff\1\44\1\u0083\5\44\1\u0089\1"
        u"\44\1\u008b\1\44\2\uffff\1\u008d\1\uffff\1\44\1\uffff\1\44\1\u0090"
        u"\1\44\1\uffff\1\u0092\1\u0093\3\44\1\uffff\1\44\1\uffff\1\44\1"
        u"\uffff\1\u0099\1\44\1\uffff\1\44\2\uffff\1\u009c\1\u009d\1\44\1"
        u"\u009f\1\44\1\uffff\1\u00a1\1\44\2\uffff\1\u00a3\1\uffff\1\44\1"
        u"\uffff\1\u00a5\1\uffff\1\44\1\uffff\1\u00a7\1\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\u00a8\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\11\1\uffff\1\151\1\157\1\141\1\145\1\146\1\141\1\145\1\53\1"
        u"\146\1\154\1\151\1\uffff\1\163\2\56\1\60\1\75\7\uffff\2\75\2\uffff"
        u"\1\162\2\75\1\uffff\1\52\3\uffff\1\164\1\60\1\156\1\163\1\146\1"
        u"\164\1\157\1\164\1\144\1\156\1\157\1\154\1\157\1\164\3\uffff\1"
        u"\60\1\160\1\164\1\163\1\164\1\165\1\155\1\145\2\uffff\1\56\7\uffff"
        u"\1\60\6\uffff\1\150\1\uffff\1\163\1\145\1\157\1\145\1\154\1\145"
        u"\1\60\1\143\1\155\1\163\1\141\1\165\1\uffff\1\157\5\145\1\60\1"
        u"\uffff\1\60\1\164\1\60\1\162\1\60\1\145\1\162\1\uffff\1\164\1\60"
        u"\1\145\1\164\2\162\1\147\1\60\1\156\1\60\1\163\2\uffff\1\60\1\uffff"
        u"\1\145\1\uffff\1\141\1\60\1\151\1\uffff\2\60\1\156\1\164\1\145"
        u"\1\uffff\1\144\1\uffff\1\164\1\uffff\1\60\1\156\1\uffff\1\157\2"
        u"\uffff\2\60\1\162\1\60\1\141\1\uffff\1\60\1\156\2\uffff\1\60\1"
        u"\uffff\1\155\1\uffff\1\60\1\uffff\1\160\1\uffff\1\60\1\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\1\175\1\uffff\1\151\2\157\1\171\1\156\1\165\1\145\1\75\1\156\1"
        u"\170\1\162\1\uffff\1\163\2\71\1\172\1\75\7\uffff\2\75\2\uffff\1"
        u"\162\2\75\1\uffff\1\57\3\uffff\1\164\1\172\1\156\1\163\1\146\1"
        u"\164\1\157\1\164\1\144\1\156\1\157\1\154\1\157\1\164\3\uffff\1"
        u"\172\1\160\1\164\1\163\1\164\1\165\1\155\1\145\2\uffff\1\71\7\uffff"
        u"\1\172\6\uffff\1\150\1\uffff\1\163\1\145\1\157\1\145\1\154\1\145"
        u"\1\172\1\143\1\155\1\163\1\141\1\165\1\uffff\1\157\5\145\1\172"
        u"\1\uffff\1\172\1\164\1\172\1\162\1\172\1\145\1\162\1\uffff\1\164"
        u"\1\172\1\145\1\164\2\162\1\147\1\172\1\156\1\172\1\163\2\uffff"
        u"\1\172\1\uffff\1\145\1\uffff\1\141\1\172\1\151\1\uffff\2\172\1"
        u"\156\1\164\1\145\1\uffff\1\144\1\uffff\1\164\1\uffff\1\172\1\156"
        u"\1\uffff\1\157\2\uffff\2\172\1\162\1\172\1\141\1\uffff\1\172\1"
        u"\156\2\uffff\1\172\1\uffff\1\155\1\uffff\1\172\1\uffff\1\160\1"
        u"\uffff\1\172\1\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\1\uffff\1\1\13\uffff\1\22\5\uffff\1\36\1\37\1\40\1\41\1\42\1\43"
        u"\1\44\2\uffff\1\47\1\50\3\uffff\1\63\1\uffff\1\65\1\66\1\70\16"
        u"\uffff\1\11\1\52\1\34\10\uffff\1\32\1\31\1\uffff\1\33\1\53\1\35"
        u"\1\45\1\51\1\46\1\56\1\uffff\1\60\1\57\1\62\1\61\1\67\1\64\1\uffff"
        u"\1\3\14\uffff\1\12\7\uffff\1\55\7\uffff\1\54\13\uffff\1\30\1\2"
        u"\1\uffff\1\14\1\uffff\1\23\3\uffff\1\15\5\uffff\1\13\1\uffff\1"
        u"\20\1\uffff\1\4\2\uffff\1\6\1\uffff\1\21\1\25\5\uffff\1\5\2\uffff"
        u"\1\10\1\16\1\uffff\1\17\1\uffff\1\26\1\uffff\1\24\1\uffff\1\7\1"
        u"\uffff\1\27"
        )

    DFA10_special = DFA.unpack(
        u"\u00a8\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\2\45\2\uffff\1\45\22\uffff\1\45\1\33\1\uffff\1\15\1"
        u"\uffff\1\43\2\uffff\1\25\1\26\1\41\1\11\1\34\1\22\1\35\1\42\1\17"
        u"\11\20\1\31\1\uffff\1\40\1\32\1\37\1\uffff\1\1\32\44\1\27\1\uffff"
        u"\1\30\1\uffff\1\21\1\uffff\1\6\1\5\1\4\1\3\1\13\1\7\2\44\1\12\5"
        u"\44\1\36\2\44\1\10\1\44\1\14\1\16\1\44\1\2\3\44\1\23\1\uffff\1"
        u"\24"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\51\15\uffff\1\50"),
        DFA.unpack(u"\1\52\11\uffff\1\54\11\uffff\1\53"),
        DFA.unpack(u"\1\55\7\uffff\1\56"),
        DFA.unpack(u"\1\61\12\uffff\1\62\5\uffff\1\60\2\uffff\1\57"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64\21\uffff\1\65"),
        DFA.unpack(u"\1\67\6\uffff\1\70\1\71"),
        DFA.unpack(u"\1\72\13\uffff\1\73"),
        DFA.unpack(u"\1\75\10\uffff\1\74"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77\1\uffff\12\77"),
        DFA.unpack(u"\1\77\1\uffff\12\101"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\116\4\uffff\1\116"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\120"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\1\125"),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\77\1\uffff\12\101"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\1\151"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\164"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\1\166"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u0084"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u008c"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u0094"),
        DFA.unpack(u"\1\u0095"),
        DFA.unpack(u"\1\u0096"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u009b"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u009e"),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\44\7\uffff\32\44\4\uffff\1\44\1\uffff\32\44"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #10

    DFA10 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(foo_langLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
