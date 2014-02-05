# $ANTLR 3.1 foo_lang/parser/foo_lang.g 2014-02-05 11:56:56

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *

         
from foo_lang import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__68=68
T__69=69
APPLY=22
T__66=66
EXTERNAL=6
LT=48
T__67=67
T__64=64
T__65=65
MOD=56
CONST=5
ANNOTATION=19
LBRACE=40
LTEQ=49
CASE=26
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
COMMENT=62
DOT=32
ADD=42
INTEGER=36
T__80=80
T__81=81
RBRACE=41
T__82=82
T__83=83
ON=23
NOTEQUALS=47
UNDERSCORE=58
MULT=54
MINUS=53
GTEQ=51
VALUE=30
T__85=85
T__84=84
LIST=12
T__87=87
ROOT=4
METHOD_CALL=11
T__86=86
DOMAIN=31
MANY=28
FUNC_DECL=8
COLON=33
WS=63
T__71=71
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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ROOT", "CONST", "EXTERNAL", "OBJECT", "FUNC_DECL", "ANON_FUNC_DECL", 
    "FUNC_CALL", "METHOD_CALL", "LIST", "PROPERTY", "IMPORT", "EXTEND", 
    "IF", "BLOCK", "VAR", "ANNOTATION", "ANNOTATED", "INC", "APPLY", "ON", 
    "ATOM", "CASES", "CASE", "TYPE", "MANY", "TUPLE", "VALUE", "DOMAIN", 
    "DOT", "COLON", "ASSIGN", "FLOAT", "INTEGER", "LPAREN", "RPAREN", "COMMA", 
    "LBRACE", "RBRACE", "ADD", "SUB", "OR", "AND", "EQUALS", "NOTEQUALS", 
    "LT", "LTEQ", "GT", "GTEQ", "PLUS", "MINUS", "MULT", "DIV", "MOD", "NOT", 
    "UNDERSCORE", "LBRACKET", "RBRACKET", "IDENTIFIER", "COMMENT", "WS", 
    "'@'", "'with'", "'do'", "'const'", "'before'", "'after'", "'function'", 
    "'return'", "'++'", "'if'", "'else'", "'case'", "'from'", "'import'", 
    "'extend'", "'true'", "'false'", "'#'", "'byte'", "'integer'", "'float'", 
    "'boolean'", "'timestamp'", "'use'"
]




class foo_langParser(Parser):
    grammarFileName = "foo_lang/parser/foo_lang.g"
    antlr_version = version_str_to_tuple("3.1")
    antlr_version_str = "3.1"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)


        self.dfa13 = self.DFA13(
            self, 13,
            eot = self.DFA13_eot,
            eof = self.DFA13_eof,
            min = self.DFA13_min,
            max = self.DFA13_max,
            accept = self.DFA13_accept,
            special = self.DFA13_special,
            transition = self.DFA13_transition
            )

        self.dfa27 = self.DFA27(
            self, 27,
            eot = self.DFA27_eot,
            eof = self.DFA27_eof,
            min = self.DFA27_min,
            max = self.DFA27_max,
            accept = self.DFA27_accept,
            special = self.DFA27_special,
            transition = self.DFA27_transition
            )






                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

                      
    def getMissingSymbol(self, input, e, expectedTokenType, follow):
      # TODO: raise better exception -> RecognitionException?
      #raise RuntimeError("expecting different input...")
      print "Expected:", self.tokenNames[expectedTokenType], \
            "after", self.getCurrentInputSymbol(input)
      sys.exit(1)


    class start_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "start"
    # foo_lang/parser/foo_lang.g:51:1: start : ( instructions )? EOF -> ^( ROOT ( instructions )? ) ;
    def start(self, ):

        retval = self.start_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        instructions1 = None


        EOF2_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_instructions = RewriteRuleSubtreeStream(self._adaptor, "rule instructions")
        try:
            try:
                # foo_lang/parser/foo_lang.g:51:7: ( ( instructions )? EOF -> ^( ROOT ( instructions )? ) )
                # foo_lang/parser/foo_lang.g:51:9: ( instructions )? EOF
                pass 
                # foo_lang/parser/foo_lang.g:51:9: ( instructions )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 64 or (67 <= LA1_0 <= 70) or LA1_0 == 76 or LA1_0 == 78) :
                    alt1 = 1
                elif (LA1_0 == EOF) :
                    LA1_2 = self.input.LA(2)

                    if (self.synpred1_foo_lang()) :
                        alt1 = 1
                if alt1 == 1:
                    # foo_lang/parser/foo_lang.g:0:0: instructions
                    pass 
                    self._state.following.append(self.FOLLOW_instructions_in_start178)
                    instructions1 = self.instructions()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_instructions.add(instructions1.tree)



                EOF2=self.match(self.input, EOF, self.FOLLOW_EOF_in_start181) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF2)

                # AST Rewrite
                # elements: instructions
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 51:27: -> ^( ROOT ( instructions )? )
                    # foo_lang/parser/foo_lang.g:51:30: ^( ROOT ( instructions )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ROOT, "ROOT"), root_1)

                    # foo_lang/parser/foo_lang.g:51:37: ( instructions )?
                    if stream_instructions.hasNext():
                        self._adaptor.addChild(root_1, stream_instructions.nextTree())


                    stream_instructions.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "start"

    class instructions_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "instructions"
    # foo_lang/parser/foo_lang.g:52:1: instructions : ( instruction )* ;
    def instructions(self, ):

        retval = self.instructions_return()
        retval.start = self.input.LT(1)

        root_0 = None

        instruction3 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:52:14: ( ( instruction )* )
                # foo_lang/parser/foo_lang.g:52:16: ( instruction )*
                pass 
                root_0 = self._adaptor.nil()

                # foo_lang/parser/foo_lang.g:52:16: ( instruction )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 64 or (67 <= LA2_0 <= 70) or LA2_0 == 76 or LA2_0 == 78) :
                        alt2 = 1


                    if alt2 == 1:
                        # foo_lang/parser/foo_lang.g:52:17: instruction
                        pass 
                        self._state.following.append(self.FOLLOW_instruction_in_instructions198)
                        instruction3 = self.instruction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, instruction3.tree)


                    else:
                        break #loop2





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "instructions"

    class instruction_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "instruction"
    # foo_lang/parser/foo_lang.g:53:1: instruction : ( declaration | directive | extension );
    def instruction(self, ):

        retval = self.instruction_return()
        retval.start = self.input.LT(1)

        root_0 = None

        declaration4 = None

        directive5 = None

        extension6 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:54:3: ( declaration | directive | extension )
                alt3 = 3
                LA3 = self.input.LA(1)
                if LA3 == 64 or LA3 == 67 or LA3 == 68 or LA3 == 69 or LA3 == 70:
                    alt3 = 1
                elif LA3 == 76:
                    alt3 = 2
                elif LA3 == 78:
                    alt3 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # foo_lang/parser/foo_lang.g:54:5: declaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_declaration_in_instruction209)
                    declaration4 = self.declaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, declaration4.tree)


                elif alt3 == 2:
                    # foo_lang/parser/foo_lang.g:55:5: directive
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_directive_in_instruction215)
                    directive5 = self.directive()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, directive5.tree)


                elif alt3 == 3:
                    # foo_lang/parser/foo_lang.g:56:5: extension
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_extension_in_instruction221)
                    extension6 = self.extension()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, extension6.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "instruction"

    class declaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "declaration"
    # foo_lang/parser/foo_lang.g:61:1: declaration : ( annotated_declaration | constant_declaration | event_handler_declaration | function_declaration );
    def declaration(self, ):

        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        annotated_declaration7 = None

        constant_declaration8 = None

        event_handler_declaration9 = None

        function_declaration10 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:62:3: ( annotated_declaration | constant_declaration | event_handler_declaration | function_declaration )
                alt4 = 4
                LA4 = self.input.LA(1)
                if LA4 == 64:
                    alt4 = 1
                elif LA4 == 67:
                    alt4 = 2
                elif LA4 == 68 or LA4 == 69:
                    alt4 = 3
                elif LA4 == 70:
                    alt4 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # foo_lang/parser/foo_lang.g:62:5: annotated_declaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_annotated_declaration_in_declaration236)
                    annotated_declaration7 = self.annotated_declaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, annotated_declaration7.tree)


                elif alt4 == 2:
                    # foo_lang/parser/foo_lang.g:63:5: constant_declaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_constant_declaration_in_declaration242)
                    constant_declaration8 = self.constant_declaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, constant_declaration8.tree)


                elif alt4 == 3:
                    # foo_lang/parser/foo_lang.g:64:5: event_handler_declaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_event_handler_declaration_in_declaration248)
                    event_handler_declaration9 = self.event_handler_declaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, event_handler_declaration9.tree)


                elif alt4 == 4:
                    # foo_lang/parser/foo_lang.g:65:5: function_declaration
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_declaration_in_declaration254)
                    function_declaration10 = self.function_declaration()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function_declaration10.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "declaration"

    class annotated_declaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotated_declaration"
    # foo_lang/parser/foo_lang.g:68:1: annotated_declaration : annotation apply_declaration -> ^( ANNOTATED annotation apply_declaration ) ;
    def annotated_declaration(self, ):

        retval = self.annotated_declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        annotation11 = None

        apply_declaration12 = None


        stream_annotation = RewriteRuleSubtreeStream(self._adaptor, "rule annotation")
        stream_apply_declaration = RewriteRuleSubtreeStream(self._adaptor, "rule apply_declaration")
        try:
            try:
                # foo_lang/parser/foo_lang.g:69:3: ( annotation apply_declaration -> ^( ANNOTATED annotation apply_declaration ) )
                # foo_lang/parser/foo_lang.g:69:5: annotation apply_declaration
                pass 
                self._state.following.append(self.FOLLOW_annotation_in_annotated_declaration267)
                annotation11 = self.annotation()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_annotation.add(annotation11.tree)
                self._state.following.append(self.FOLLOW_apply_declaration_in_annotated_declaration269)
                apply_declaration12 = self.apply_declaration()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_apply_declaration.add(apply_declaration12.tree)

                # AST Rewrite
                # elements: apply_declaration, annotation
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 69:34: -> ^( ANNOTATED annotation apply_declaration )
                    # foo_lang/parser/foo_lang.g:69:37: ^( ANNOTATED annotation apply_declaration )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ANNOTATED, "ANNOTATED"), root_1)

                    self._adaptor.addChild(root_1, stream_annotation.nextTree())
                    self._adaptor.addChild(root_1, stream_apply_declaration.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "annotated_declaration"

    class annotation_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "annotation"
    # foo_lang/parser/foo_lang.g:72:1: annotation : '@' function_call_expression -> ^( ANNOTATION function_call_expression ) ;
    def annotation(self, ):

        retval = self.annotation_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal13 = None
        function_call_expression14 = None


        char_literal13_tree = None
        stream_64 = RewriteRuleTokenStream(self._adaptor, "token 64")
        stream_function_call_expression = RewriteRuleSubtreeStream(self._adaptor, "rule function_call_expression")
        try:
            try:
                # foo_lang/parser/foo_lang.g:73:3: ( '@' function_call_expression -> ^( ANNOTATION function_call_expression ) )
                # foo_lang/parser/foo_lang.g:73:5: '@' function_call_expression
                pass 
                char_literal13=self.match(self.input, 64, self.FOLLOW_64_in_annotation292) 
                if self._state.backtracking == 0:
                    stream_64.add(char_literal13)
                self._state.following.append(self.FOLLOW_function_call_expression_in_annotation294)
                function_call_expression14 = self.function_call_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_function_call_expression.add(function_call_expression14.tree)

                # AST Rewrite
                # elements: function_call_expression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 73:34: -> ^( ANNOTATION function_call_expression )
                    # foo_lang/parser/foo_lang.g:73:37: ^( ANNOTATION function_call_expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ANNOTATION, "ANNOTATION"), root_1)

                    self._adaptor.addChild(root_1, stream_function_call_expression.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "annotation"

    class apply_declaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "apply_declaration"
    # foo_lang/parser/foo_lang.g:76:1: apply_declaration : ( 'with' identifier DOT identifier 'do' function_expression -> ^( APPLY ^( PROPERTY identifier identifier ) function_expression ) | 'with' identifier 'do' function_expression -> ^( APPLY ^( DOMAIN identifier ) function_expression ) );
    def apply_declaration(self, ):

        retval = self.apply_declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal15 = None
        DOT17 = None
        string_literal19 = None
        string_literal21 = None
        string_literal23 = None
        identifier16 = None

        identifier18 = None

        function_expression20 = None

        identifier22 = None

        function_expression24 = None


        string_literal15_tree = None
        DOT17_tree = None
        string_literal19_tree = None
        string_literal21_tree = None
        string_literal23_tree = None
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_function_expression = RewriteRuleSubtreeStream(self._adaptor, "rule function_expression")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # foo_lang/parser/foo_lang.g:77:3: ( 'with' identifier DOT identifier 'do' function_expression -> ^( APPLY ^( PROPERTY identifier identifier ) function_expression ) | 'with' identifier 'do' function_expression -> ^( APPLY ^( DOMAIN identifier ) function_expression ) )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 65) :
                    LA5_1 = self.input.LA(2)

                    if (LA5_1 == IDENTIFIER or LA5_1 == 65 or (76 <= LA5_1 <= 78) or LA5_1 == 87) :
                        LA5_2 = self.input.LA(3)

                        if (LA5_2 == DOT) :
                            alt5 = 1
                        elif (LA5_2 == 66) :
                            alt5 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 5, 2, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 5, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # foo_lang/parser/foo_lang.g:77:5: 'with' identifier DOT identifier 'do' function_expression
                    pass 
                    string_literal15=self.match(self.input, 65, self.FOLLOW_65_in_apply_declaration315) 
                    if self._state.backtracking == 0:
                        stream_65.add(string_literal15)
                    self._state.following.append(self.FOLLOW_identifier_in_apply_declaration317)
                    identifier16 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier16.tree)
                    DOT17=self.match(self.input, DOT, self.FOLLOW_DOT_in_apply_declaration319) 
                    if self._state.backtracking == 0:
                        stream_DOT.add(DOT17)
                    self._state.following.append(self.FOLLOW_identifier_in_apply_declaration321)
                    identifier18 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier18.tree)
                    string_literal19=self.match(self.input, 66, self.FOLLOW_66_in_apply_declaration323) 
                    if self._state.backtracking == 0:
                        stream_66.add(string_literal19)
                    self._state.following.append(self.FOLLOW_function_expression_in_apply_declaration325)
                    function_expression20 = self.function_expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_function_expression.add(function_expression20.tree)

                    # AST Rewrite
                    # elements: identifier, identifier, function_expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 78:5: -> ^( APPLY ^( PROPERTY identifier identifier ) function_expression )
                        # foo_lang/parser/foo_lang.g:78:8: ^( APPLY ^( PROPERTY identifier identifier ) function_expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(APPLY, "APPLY"), root_1)

                        # foo_lang/parser/foo_lang.g:78:16: ^( PROPERTY identifier identifier )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROPERTY, "PROPERTY"), root_2)

                        self._adaptor.addChild(root_2, stream_identifier.nextTree())
                        self._adaptor.addChild(root_2, stream_identifier.nextTree())

                        self._adaptor.addChild(root_1, root_2)
                        self._adaptor.addChild(root_1, stream_function_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt5 == 2:
                    # foo_lang/parser/foo_lang.g:79:5: 'with' identifier 'do' function_expression
                    pass 
                    string_literal21=self.match(self.input, 65, self.FOLLOW_65_in_apply_declaration351) 
                    if self._state.backtracking == 0:
                        stream_65.add(string_literal21)
                    self._state.following.append(self.FOLLOW_identifier_in_apply_declaration353)
                    identifier22 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier22.tree)
                    string_literal23=self.match(self.input, 66, self.FOLLOW_66_in_apply_declaration355) 
                    if self._state.backtracking == 0:
                        stream_66.add(string_literal23)
                    self._state.following.append(self.FOLLOW_function_expression_in_apply_declaration357)
                    function_expression24 = self.function_expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_function_expression.add(function_expression24.tree)

                    # AST Rewrite
                    # elements: identifier, function_expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 80:5: -> ^( APPLY ^( DOMAIN identifier ) function_expression )
                        # foo_lang/parser/foo_lang.g:80:8: ^( APPLY ^( DOMAIN identifier ) function_expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(APPLY, "APPLY"), root_1)

                        # foo_lang/parser/foo_lang.g:80:16: ^( DOMAIN identifier )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(DOMAIN, "DOMAIN"), root_2)

                        self._adaptor.addChild(root_2, stream_identifier.nextTree())

                        self._adaptor.addChild(root_1, root_2)
                        self._adaptor.addChild(root_1, stream_function_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "apply_declaration"

    class constant_declaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "constant_declaration"
    # foo_lang/parser/foo_lang.g:83:1: constant_declaration : 'const' typed_value -> ^( CONST typed_value ) ;
    def constant_declaration(self, ):

        retval = self.constant_declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal25 = None
        typed_value26 = None


        string_literal25_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_typed_value = RewriteRuleSubtreeStream(self._adaptor, "rule typed_value")
        try:
            try:
                # foo_lang/parser/foo_lang.g:83:21: ( 'const' typed_value -> ^( CONST typed_value ) )
                # foo_lang/parser/foo_lang.g:83:23: 'const' typed_value
                pass 
                string_literal25=self.match(self.input, 67, self.FOLLOW_67_in_constant_declaration387) 
                if self._state.backtracking == 0:
                    stream_67.add(string_literal25)
                self._state.following.append(self.FOLLOW_typed_value_in_constant_declaration389)
                typed_value26 = self.typed_value()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typed_value.add(typed_value26.tree)

                # AST Rewrite
                # elements: typed_value
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 83:43: -> ^( CONST typed_value )
                    # foo_lang/parser/foo_lang.g:83:46: ^( CONST typed_value )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CONST, "CONST"), root_1)

                    self._adaptor.addChild(root_1, stream_typed_value.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "constant_declaration"

    class typed_value_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "typed_value"
    # foo_lang/parser/foo_lang.g:85:1: typed_value : ( identifier COLON type ASSIGN literal -> ^( VALUE identifier type literal ) | identifier ASSIGN FLOAT -> ^( VALUE identifier ^( TYPE TYPE['float'] ) FLOAT ) | identifier ASSIGN INTEGER -> ^( VALUE identifier ^( TYPE TYPE['integer'] ) INTEGER ) | identifier ASSIGN boolean_literal -> ^( VALUE identifier ^( TYPE TYPE['boolean'] ) boolean_literal ) );
    def typed_value(self, ):

        retval = self.typed_value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON28 = None
        ASSIGN30 = None
        ASSIGN33 = None
        FLOAT34 = None
        ASSIGN36 = None
        INTEGER37 = None
        ASSIGN39 = None
        identifier27 = None

        type29 = None

        literal31 = None

        identifier32 = None

        identifier35 = None

        identifier38 = None

        boolean_literal40 = None


        COLON28_tree = None
        ASSIGN30_tree = None
        ASSIGN33_tree = None
        FLOAT34_tree = None
        ASSIGN36_tree = None
        INTEGER37_tree = None
        ASSIGN39_tree = None
        stream_INTEGER = RewriteRuleTokenStream(self._adaptor, "token INTEGER")
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_FLOAT = RewriteRuleTokenStream(self._adaptor, "token FLOAT")
        stream_ASSIGN = RewriteRuleTokenStream(self._adaptor, "token ASSIGN")
        stream_boolean_literal = RewriteRuleSubtreeStream(self._adaptor, "rule boolean_literal")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        stream_literal = RewriteRuleSubtreeStream(self._adaptor, "rule literal")
        try:
            try:
                # foo_lang/parser/foo_lang.g:86:3: ( identifier COLON type ASSIGN literal -> ^( VALUE identifier type literal ) | identifier ASSIGN FLOAT -> ^( VALUE identifier ^( TYPE TYPE['float'] ) FLOAT ) | identifier ASSIGN INTEGER -> ^( VALUE identifier ^( TYPE TYPE['integer'] ) INTEGER ) | identifier ASSIGN boolean_literal -> ^( VALUE identifier ^( TYPE TYPE['boolean'] ) boolean_literal ) )
                alt6 = 4
                LA6_0 = self.input.LA(1)

                if (LA6_0 == IDENTIFIER or LA6_0 == 65 or (76 <= LA6_0 <= 78) or LA6_0 == 87) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == ASSIGN) :
                        LA6 = self.input.LA(3)
                        if LA6 == FLOAT:
                            alt6 = 2
                        elif LA6 == INTEGER:
                            alt6 = 3
                        elif LA6 == 79 or LA6 == 80:
                            alt6 = 4
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 6, 2, self.input)

                            raise nvae

                    elif (LA6_1 == COLON) :
                        alt6 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 6, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # foo_lang/parser/foo_lang.g:86:6: identifier COLON type ASSIGN literal
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_typed_value408)
                    identifier27 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier27.tree)
                    COLON28=self.match(self.input, COLON, self.FOLLOW_COLON_in_typed_value410) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON28)
                    self._state.following.append(self.FOLLOW_type_in_typed_value412)
                    type29 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_type.add(type29.tree)
                    ASSIGN30=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_typed_value414) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN30)
                    self._state.following.append(self.FOLLOW_literal_in_typed_value416)
                    literal31 = self.literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_literal.add(literal31.tree)

                    # AST Rewrite
                    # elements: identifier, literal, type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 87:5: -> ^( VALUE identifier type literal )
                        # foo_lang/parser/foo_lang.g:87:8: ^( VALUE identifier type literal )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VALUE, "VALUE"), root_1)

                        self._adaptor.addChild(root_1, stream_identifier.nextTree())
                        self._adaptor.addChild(root_1, stream_type.nextTree())
                        self._adaptor.addChild(root_1, stream_literal.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt6 == 2:
                    # foo_lang/parser/foo_lang.g:88:5: identifier ASSIGN FLOAT
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_typed_value438)
                    identifier32 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier32.tree)
                    ASSIGN33=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_typed_value440) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN33)
                    FLOAT34=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_typed_value442) 
                    if self._state.backtracking == 0:
                        stream_FLOAT.add(FLOAT34)

                    # AST Rewrite
                    # elements: identifier, FLOAT
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 89:5: -> ^( VALUE identifier ^( TYPE TYPE['float'] ) FLOAT )
                        # foo_lang/parser/foo_lang.g:89:8: ^( VALUE identifier ^( TYPE TYPE['float'] ) FLOAT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VALUE, "VALUE"), root_1)

                        self._adaptor.addChild(root_1, stream_identifier.nextTree())
                        # foo_lang/parser/foo_lang.g:89:27: ^( TYPE TYPE['float'] )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE, "TYPE"), root_2)

                        self._adaptor.addChild(root_2, self._adaptor.create(TYPE, 'float'))

                        self._adaptor.addChild(root_1, root_2)
                        self._adaptor.addChild(root_1, stream_FLOAT.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt6 == 3:
                    # foo_lang/parser/foo_lang.g:90:5: identifier ASSIGN INTEGER
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_typed_value469)
                    identifier35 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier35.tree)
                    ASSIGN36=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_typed_value471) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN36)
                    INTEGER37=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_typed_value473) 
                    if self._state.backtracking == 0:
                        stream_INTEGER.add(INTEGER37)

                    # AST Rewrite
                    # elements: INTEGER, identifier
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 91:5: -> ^( VALUE identifier ^( TYPE TYPE['integer'] ) INTEGER )
                        # foo_lang/parser/foo_lang.g:91:8: ^( VALUE identifier ^( TYPE TYPE['integer'] ) INTEGER )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VALUE, "VALUE"), root_1)

                        self._adaptor.addChild(root_1, stream_identifier.nextTree())
                        # foo_lang/parser/foo_lang.g:91:27: ^( TYPE TYPE['integer'] )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE, "TYPE"), root_2)

                        self._adaptor.addChild(root_2, self._adaptor.create(TYPE, 'integer'))

                        self._adaptor.addChild(root_1, root_2)
                        self._adaptor.addChild(root_1, stream_INTEGER.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt6 == 4:
                    # foo_lang/parser/foo_lang.g:92:5: identifier ASSIGN boolean_literal
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_typed_value500)
                    identifier38 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier38.tree)
                    ASSIGN39=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_typed_value502) 
                    if self._state.backtracking == 0:
                        stream_ASSIGN.add(ASSIGN39)
                    self._state.following.append(self.FOLLOW_boolean_literal_in_typed_value504)
                    boolean_literal40 = self.boolean_literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_boolean_literal.add(boolean_literal40.tree)

                    # AST Rewrite
                    # elements: identifier, boolean_literal
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 93:5: -> ^( VALUE identifier ^( TYPE TYPE['boolean'] ) boolean_literal )
                        # foo_lang/parser/foo_lang.g:93:8: ^( VALUE identifier ^( TYPE TYPE['boolean'] ) boolean_literal )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VALUE, "VALUE"), root_1)

                        self._adaptor.addChild(root_1, stream_identifier.nextTree())
                        # foo_lang/parser/foo_lang.g:93:27: ^( TYPE TYPE['boolean'] )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE, "TYPE"), root_2)

                        self._adaptor.addChild(root_2, self._adaptor.create(TYPE, 'boolean'))

                        self._adaptor.addChild(root_1, root_2)
                        self._adaptor.addChild(root_1, stream_boolean_literal.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "typed_value"

    class event_handler_declaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "event_handler_declaration"
    # foo_lang/parser/foo_lang.g:96:1: event_handler_declaration : event_timing identifier identifier 'do' function_expression -> ^( ON event_timing identifier identifier function_expression ) ;
    def event_handler_declaration(self, ):

        retval = self.event_handler_declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal44 = None
        event_timing41 = None

        identifier42 = None

        identifier43 = None

        function_expression45 = None


        string_literal44_tree = None
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_function_expression = RewriteRuleSubtreeStream(self._adaptor, "rule function_expression")
        stream_event_timing = RewriteRuleSubtreeStream(self._adaptor, "rule event_timing")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # foo_lang/parser/foo_lang.g:97:3: ( event_timing identifier identifier 'do' function_expression -> ^( ON event_timing identifier identifier function_expression ) )
                # foo_lang/parser/foo_lang.g:97:5: event_timing identifier identifier 'do' function_expression
                pass 
                self._state.following.append(self.FOLLOW_event_timing_in_event_handler_declaration538)
                event_timing41 = self.event_timing()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_event_timing.add(event_timing41.tree)
                self._state.following.append(self.FOLLOW_identifier_in_event_handler_declaration540)
                identifier42 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(identifier42.tree)
                self._state.following.append(self.FOLLOW_identifier_in_event_handler_declaration542)
                identifier43 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(identifier43.tree)
                string_literal44=self.match(self.input, 66, self.FOLLOW_66_in_event_handler_declaration544) 
                if self._state.backtracking == 0:
                    stream_66.add(string_literal44)
                self._state.following.append(self.FOLLOW_function_expression_in_event_handler_declaration546)
                function_expression45 = self.function_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_function_expression.add(function_expression45.tree)

                # AST Rewrite
                # elements: identifier, identifier, event_timing, function_expression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 98:5: -> ^( ON event_timing identifier identifier function_expression )
                    # foo_lang/parser/foo_lang.g:98:8: ^( ON event_timing identifier identifier function_expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ON, "ON"), root_1)

                    self._adaptor.addChild(root_1, stream_event_timing.nextTree())
                    self._adaptor.addChild(root_1, stream_identifier.nextTree())
                    self._adaptor.addChild(root_1, stream_identifier.nextTree())
                    self._adaptor.addChild(root_1, stream_function_expression.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "event_handler_declaration"

    class event_timing_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "event_timing"
    # foo_lang/parser/foo_lang.g:101:1: event_timing : ( 'before' | 'after' );
    def event_timing(self, ):

        retval = self.event_timing_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set46 = None

        set46_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:101:13: ( 'before' | 'after' )
                # foo_lang/parser/foo_lang.g:
                pass 
                root_0 = self._adaptor.nil()

                set46 = self.input.LT(1)
                if (68 <= self.input.LA(1) <= 69):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set46))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "event_timing"

    class function_declaration_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "function_declaration"
    # foo_lang/parser/foo_lang.g:103:1: function_declaration : 'function' identifier LPAREN ( function_param_list )? RPAREN function_body -> ^( FUNC_DECL identifier ( function_param_list )? function_body ) ;
    def function_declaration(self, ):

        retval = self.function_declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal47 = None
        LPAREN49 = None
        RPAREN51 = None
        identifier48 = None

        function_param_list50 = None

        function_body52 = None


        string_literal47_tree = None
        LPAREN49_tree = None
        RPAREN51_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_function_param_list = RewriteRuleSubtreeStream(self._adaptor, "rule function_param_list")
        stream_function_body = RewriteRuleSubtreeStream(self._adaptor, "rule function_body")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # foo_lang/parser/foo_lang.g:104:3: ( 'function' identifier LPAREN ( function_param_list )? RPAREN function_body -> ^( FUNC_DECL identifier ( function_param_list )? function_body ) )
                # foo_lang/parser/foo_lang.g:104:5: 'function' identifier LPAREN ( function_param_list )? RPAREN function_body
                pass 
                string_literal47=self.match(self.input, 70, self.FOLLOW_70_in_function_declaration588) 
                if self._state.backtracking == 0:
                    stream_70.add(string_literal47)
                self._state.following.append(self.FOLLOW_identifier_in_function_declaration590)
                identifier48 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(identifier48.tree)
                LPAREN49=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_function_declaration592) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN49)
                # foo_lang/parser/foo_lang.g:104:34: ( function_param_list )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == IDENTIFIER or LA7_0 == 65 or (76 <= LA7_0 <= 78) or LA7_0 == 87) :
                    alt7 = 1
                if alt7 == 1:
                    # foo_lang/parser/foo_lang.g:104:35: function_param_list
                    pass 
                    self._state.following.append(self.FOLLOW_function_param_list_in_function_declaration595)
                    function_param_list50 = self.function_param_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_function_param_list.add(function_param_list50.tree)



                RPAREN51=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function_declaration599) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN51)
                self._state.following.append(self.FOLLOW_function_body_in_function_declaration601)
                function_body52 = self.function_body()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_function_body.add(function_body52.tree)

                # AST Rewrite
                # elements: function_body, identifier, function_param_list
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 105:6: -> ^( FUNC_DECL identifier ( function_param_list )? function_body )
                    # foo_lang/parser/foo_lang.g:105:9: ^( FUNC_DECL identifier ( function_param_list )? function_body )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNC_DECL, "FUNC_DECL"), root_1)

                    self._adaptor.addChild(root_1, stream_identifier.nextTree())
                    # foo_lang/parser/foo_lang.g:105:32: ( function_param_list )?
                    if stream_function_param_list.hasNext():
                        self._adaptor.addChild(root_1, stream_function_param_list.nextTree())


                    stream_function_param_list.reset();
                    self._adaptor.addChild(root_1, stream_function_body.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "function_declaration"

    class function_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "function_expression"
    # foo_lang/parser/foo_lang.g:107:1: function_expression : ( 'function' ( identifier )? LPAREN ( function_param_list )? RPAREN function_body -> ^( ANON_FUNC_DECL ( identifier )? ( function_param_list )? function_body ) | identifier );
    def function_expression(self, ):

        retval = self.function_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal53 = None
        LPAREN55 = None
        RPAREN57 = None
        identifier54 = None

        function_param_list56 = None

        function_body58 = None

        identifier59 = None


        string_literal53_tree = None
        LPAREN55_tree = None
        RPAREN57_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_function_param_list = RewriteRuleSubtreeStream(self._adaptor, "rule function_param_list")
        stream_function_body = RewriteRuleSubtreeStream(self._adaptor, "rule function_body")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # foo_lang/parser/foo_lang.g:108:3: ( 'function' ( identifier )? LPAREN ( function_param_list )? RPAREN function_body -> ^( ANON_FUNC_DECL ( identifier )? ( function_param_list )? function_body ) | identifier )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 70) :
                    alt10 = 1
                elif (LA10_0 == IDENTIFIER or LA10_0 == 65 or (76 <= LA10_0 <= 78) or LA10_0 == 87) :
                    alt10 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # foo_lang/parser/foo_lang.g:108:5: 'function' ( identifier )? LPAREN ( function_param_list )? RPAREN function_body
                    pass 
                    string_literal53=self.match(self.input, 70, self.FOLLOW_70_in_function_expression631) 
                    if self._state.backtracking == 0:
                        stream_70.add(string_literal53)
                    # foo_lang/parser/foo_lang.g:108:16: ( identifier )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == IDENTIFIER or LA8_0 == 65 or (76 <= LA8_0 <= 78) or LA8_0 == 87) :
                        alt8 = 1
                    if alt8 == 1:
                        # foo_lang/parser/foo_lang.g:0:0: identifier
                        pass 
                        self._state.following.append(self.FOLLOW_identifier_in_function_expression633)
                        identifier54 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_identifier.add(identifier54.tree)



                    LPAREN55=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_function_expression636) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN55)
                    # foo_lang/parser/foo_lang.g:108:35: ( function_param_list )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == IDENTIFIER or LA9_0 == 65 or (76 <= LA9_0 <= 78) or LA9_0 == 87) :
                        alt9 = 1
                    if alt9 == 1:
                        # foo_lang/parser/foo_lang.g:108:36: function_param_list
                        pass 
                        self._state.following.append(self.FOLLOW_function_param_list_in_function_expression639)
                        function_param_list56 = self.function_param_list()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_function_param_list.add(function_param_list56.tree)



                    RPAREN57=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function_expression643) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN57)
                    self._state.following.append(self.FOLLOW_function_body_in_function_expression645)
                    function_body58 = self.function_body()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_function_body.add(function_body58.tree)

                    # AST Rewrite
                    # elements: identifier, function_body, function_param_list
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 109:6: -> ^( ANON_FUNC_DECL ( identifier )? ( function_param_list )? function_body )
                        # foo_lang/parser/foo_lang.g:109:9: ^( ANON_FUNC_DECL ( identifier )? ( function_param_list )? function_body )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ANON_FUNC_DECL, "ANON_FUNC_DECL"), root_1)

                        # foo_lang/parser/foo_lang.g:109:26: ( identifier )?
                        if stream_identifier.hasNext():
                            self._adaptor.addChild(root_1, stream_identifier.nextTree())


                        stream_identifier.reset();
                        # foo_lang/parser/foo_lang.g:109:38: ( function_param_list )?
                        if stream_function_param_list.hasNext():
                            self._adaptor.addChild(root_1, stream_function_param_list.nextTree())


                        stream_function_param_list.reset();
                        self._adaptor.addChild(root_1, stream_function_body.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt10 == 2:
                    # foo_lang/parser/foo_lang.g:110:5: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_function_expression670)
                    identifier59 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier59.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "function_expression"

    class function_param_list_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "function_param_list"
    # foo_lang/parser/foo_lang.g:112:1: function_param_list : p+= identifier ( COMMA p+= identifier )* -> ^( LIST ( $p)+ ) ;
    def function_param_list(self, ):

        retval = self.function_param_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA60 = None
        list_p = None
        p = None

        p = None
        COMMA60_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # foo_lang/parser/foo_lang.g:112:20: (p+= identifier ( COMMA p+= identifier )* -> ^( LIST ( $p)+ ) )
                # foo_lang/parser/foo_lang.g:112:22: p+= identifier ( COMMA p+= identifier )*
                pass 
                self._state.following.append(self.FOLLOW_identifier_in_function_param_list681)
                p = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(p.tree)
                if list_p is None:
                    list_p = []
                list_p.append(p.tree)

                # foo_lang/parser/foo_lang.g:112:36: ( COMMA p+= identifier )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == COMMA) :
                        alt11 = 1


                    if alt11 == 1:
                        # foo_lang/parser/foo_lang.g:112:37: COMMA p+= identifier
                        pass 
                        COMMA60=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_function_param_list684) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA60)
                        self._state.following.append(self.FOLLOW_identifier_in_function_param_list688)
                        p = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_identifier.add(p.tree)
                        if list_p is None:
                            list_p = []
                        list_p.append(p.tree)



                    else:
                        break #loop11



                # AST Rewrite
                # elements: p
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: p
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                    stream_p = RewriteRuleSubtreeStream(self._adaptor, "token p", list_p)
                    root_0 = self._adaptor.nil()
                    # 112:59: -> ^( LIST ( $p)+ )
                    # foo_lang/parser/foo_lang.g:112:62: ^( LIST ( $p)+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LIST, "LIST"), root_1)

                    # foo_lang/parser/foo_lang.g:112:69: ( $p)+
                    if not (stream_p.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_p.hasNext():
                        self._adaptor.addChild(root_1, stream_p.nextTree())


                    stream_p.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "function_param_list"

    class function_body_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "function_body"
    # foo_lang/parser/foo_lang.g:113:1: function_body : block_statement ;
    def function_body(self, ):

        retval = self.function_body_return()
        retval.start = self.input.LT(1)

        root_0 = None

        block_statement61 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:113:14: ( block_statement )
                # foo_lang/parser/foo_lang.g:113:16: block_statement
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_block_statement_in_function_body706)
                block_statement61 = self.block_statement()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block_statement61.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "function_body"

    class statements_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "statements"
    # foo_lang/parser/foo_lang.g:115:1: statements : ( statement )* ;
    def statements(self, ):

        retval = self.statements_return()
        retval.start = self.input.LT(1)

        root_0 = None

        statement62 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:115:11: ( ( statement )* )
                # foo_lang/parser/foo_lang.g:115:13: ( statement )*
                pass 
                root_0 = self._adaptor.nil()

                # foo_lang/parser/foo_lang.g:115:13: ( statement )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == LBRACE or LA12_0 == IDENTIFIER or LA12_0 == 65 or LA12_0 == 71 or LA12_0 == 73 or (75 <= LA12_0 <= 78) or LA12_0 == 87) :
                        alt12 = 1


                    if alt12 == 1:
                        # foo_lang/parser/foo_lang.g:115:14: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements714)
                        statement62 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, statement62.tree)


                    else:
                        break #loop12





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "statements"

    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "statement"
    # foo_lang/parser/foo_lang.g:116:1: statement : ( block_statement | assignment_statement | increment_statement | if_statement | case_statement | call_expression | 'return' );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal69 = None
        block_statement63 = None

        assignment_statement64 = None

        increment_statement65 = None

        if_statement66 = None

        case_statement67 = None

        call_expression68 = None


        string_literal69_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:117:3: ( block_statement | assignment_statement | increment_statement | if_statement | case_statement | call_expression | 'return' )
                alt13 = 7
                alt13 = self.dfa13.predict(self.input)
                if alt13 == 1:
                    # foo_lang/parser/foo_lang.g:117:5: block_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_block_statement_in_statement725)
                    block_statement63 = self.block_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block_statement63.tree)


                elif alt13 == 2:
                    # foo_lang/parser/foo_lang.g:118:5: assignment_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_assignment_statement_in_statement731)
                    assignment_statement64 = self.assignment_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assignment_statement64.tree)


                elif alt13 == 3:
                    # foo_lang/parser/foo_lang.g:119:5: increment_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_increment_statement_in_statement737)
                    increment_statement65 = self.increment_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, increment_statement65.tree)


                elif alt13 == 4:
                    # foo_lang/parser/foo_lang.g:120:5: if_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_if_statement_in_statement743)
                    if_statement66 = self.if_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, if_statement66.tree)


                elif alt13 == 5:
                    # foo_lang/parser/foo_lang.g:121:5: case_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_case_statement_in_statement749)
                    case_statement67 = self.case_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, case_statement67.tree)


                elif alt13 == 6:
                    # foo_lang/parser/foo_lang.g:122:5: call_expression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_call_expression_in_statement755)
                    call_expression68 = self.call_expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, call_expression68.tree)


                elif alt13 == 7:
                    # foo_lang/parser/foo_lang.g:123:5: 'return'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal69=self.match(self.input, 71, self.FOLLOW_71_in_statement761)
                    if self._state.backtracking == 0:

                        string_literal69_tree = self._adaptor.createWithPayload(string_literal69)
                        self._adaptor.addChild(root_0, string_literal69_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "statement"

    class block_statement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "block_statement"
    # foo_lang/parser/foo_lang.g:126:1: block_statement : ( LBRACE RBRACE -> ^( BLOCK ) | LBRACE ( statement )+ RBRACE -> ^( BLOCK ( statement )+ ) );
    def block_statement(self, ):

        retval = self.block_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACE70 = None
        RBRACE71 = None
        LBRACE72 = None
        RBRACE74 = None
        statement73 = None


        LBRACE70_tree = None
        RBRACE71_tree = None
        LBRACE72_tree = None
        RBRACE74_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # foo_lang/parser/foo_lang.g:127:3: ( LBRACE RBRACE -> ^( BLOCK ) | LBRACE ( statement )+ RBRACE -> ^( BLOCK ( statement )+ ) )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == LBRACE) :
                    LA15_1 = self.input.LA(2)

                    if (LA15_1 == RBRACE) :
                        alt15 = 1
                    elif (LA15_1 == LBRACE or LA15_1 == IDENTIFIER or LA15_1 == 65 or LA15_1 == 71 or LA15_1 == 73 or (75 <= LA15_1 <= 78) or LA15_1 == 87) :
                        alt15 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 15, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # foo_lang/parser/foo_lang.g:127:5: LBRACE RBRACE
                    pass 
                    LBRACE70=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_block_statement774) 
                    if self._state.backtracking == 0:
                        stream_LBRACE.add(LBRACE70)
                    RBRACE71=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_block_statement776) 
                    if self._state.backtracking == 0:
                        stream_RBRACE.add(RBRACE71)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 127:30: -> ^( BLOCK )
                        # foo_lang/parser/foo_lang.g:127:33: ^( BLOCK )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt15 == 2:
                    # foo_lang/parser/foo_lang.g:128:5: LBRACE ( statement )+ RBRACE
                    pass 
                    LBRACE72=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_block_statement799) 
                    if self._state.backtracking == 0:
                        stream_LBRACE.add(LBRACE72)
                    # foo_lang/parser/foo_lang.g:128:12: ( statement )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == LBRACE or LA14_0 == IDENTIFIER or LA14_0 == 65 or LA14_0 == 71 or LA14_0 == 73 or (75 <= LA14_0 <= 78) or LA14_0 == 87) :
                            alt14 = 1


                        if alt14 == 1:
                            # foo_lang/parser/foo_lang.g:0:0: statement
                            pass 
                            self._state.following.append(self.FOLLOW_statement_in_block_statement801)
                            statement73 = self.statement()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_statement.add(statement73.tree)


                        else:
                            if cnt14 >= 1:
                                break #loop14

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1


                    RBRACE74=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_block_statement804) 
                    if self._state.backtracking == 0:
                        stream_RBRACE.add(RBRACE74)

                    # AST Rewrite
                    # elements: statement
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 128:30: -> ^( BLOCK ( statement )+ )
                        # foo_lang/parser/foo_lang.g:128:33: ^( BLOCK ( statement )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_1)

                        # foo_lang/parser/foo_lang.g:128:41: ( statement )+
                        if not (stream_statement.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_statement.hasNext():
                            self._adaptor.addChild(root_1, stream_statement.nextTree())


                        stream_statement.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "block_statement"

    class assignment_statement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "assignment_statement"
    # foo_lang/parser/foo_lang.g:130:1: assignment_statement : variable ( ASSIGN | ADD | SUB ) expression ;
    def assignment_statement(self, ):

        retval = self.assignment_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set76 = None
        variable75 = None

        expression77 = None


        set76_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:131:3: ( variable ( ASSIGN | ADD | SUB ) expression )
                # foo_lang/parser/foo_lang.g:131:5: variable ( ASSIGN | ADD | SUB ) expression
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_variable_in_assignment_statement823)
                variable75 = self.variable()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, variable75.tree)
                set76 = self.input.LT(1)
                set76 = self.input.LT(1)
                if self.input.LA(1) == ASSIGN or (ADD <= self.input.LA(1) <= SUB):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set76), root_0)
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self._state.following.append(self.FOLLOW_expression_in_assignment_statement834)
                expression77 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression77.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "assignment_statement"

    class increment_statement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "increment_statement"
    # foo_lang/parser/foo_lang.g:134:1: increment_statement : variable '++' -> ^( INC variable ) ;
    def increment_statement(self, ):

        retval = self.increment_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal79 = None
        variable78 = None


        string_literal79_tree = None
        stream_72 = RewriteRuleTokenStream(self._adaptor, "token 72")
        stream_variable = RewriteRuleSubtreeStream(self._adaptor, "rule variable")
        try:
            try:
                # foo_lang/parser/foo_lang.g:135:3: ( variable '++' -> ^( INC variable ) )
                # foo_lang/parser/foo_lang.g:135:5: variable '++'
                pass 
                self._state.following.append(self.FOLLOW_variable_in_increment_statement847)
                variable78 = self.variable()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_variable.add(variable78.tree)
                string_literal79=self.match(self.input, 72, self.FOLLOW_72_in_increment_statement849) 
                if self._state.backtracking == 0:
                    stream_72.add(string_literal79)

                # AST Rewrite
                # elements: variable
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 135:30: -> ^( INC variable )
                    # foo_lang/parser/foo_lang.g:135:33: ^( INC variable )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INC, "INC"), root_1)

                    self._adaptor.addChild(root_1, stream_variable.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "increment_statement"

    class if_statement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "if_statement"
    # foo_lang/parser/foo_lang.g:138:1: if_statement : ( 'if' LPAREN expression RPAREN statement 'else' statement -> ^( IF expression statement statement ) | 'if' LPAREN expression RPAREN statement -> ^( IF expression statement ) );
    def if_statement(self, ):

        retval = self.if_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal80 = None
        LPAREN81 = None
        RPAREN83 = None
        string_literal85 = None
        string_literal87 = None
        LPAREN88 = None
        RPAREN90 = None
        expression82 = None

        statement84 = None

        statement86 = None

        expression89 = None

        statement91 = None


        string_literal80_tree = None
        LPAREN81_tree = None
        RPAREN83_tree = None
        string_literal85_tree = None
        string_literal87_tree = None
        LPAREN88_tree = None
        RPAREN90_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # foo_lang/parser/foo_lang.g:139:3: ( 'if' LPAREN expression RPAREN statement 'else' statement -> ^( IF expression statement statement ) | 'if' LPAREN expression RPAREN statement -> ^( IF expression statement ) )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == 73) :
                    LA16_1 = self.input.LA(2)

                    if (self.synpred29_foo_lang()) :
                        alt16 = 1
                    elif (True) :
                        alt16 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 16, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # foo_lang/parser/foo_lang.g:139:5: 'if' LPAREN expression RPAREN statement 'else' statement
                    pass 
                    string_literal80=self.match(self.input, 73, self.FOLLOW_73_in_if_statement881) 
                    if self._state.backtracking == 0:
                        stream_73.add(string_literal80)
                    LPAREN81=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_if_statement883) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN81)
                    self._state.following.append(self.FOLLOW_expression_in_if_statement885)
                    expression82 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression82.tree)
                    RPAREN83=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_if_statement887) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN83)
                    self._state.following.append(self.FOLLOW_statement_in_if_statement889)
                    statement84 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_statement.add(statement84.tree)
                    string_literal85=self.match(self.input, 74, self.FOLLOW_74_in_if_statement891) 
                    if self._state.backtracking == 0:
                        stream_74.add(string_literal85)
                    self._state.following.append(self.FOLLOW_statement_in_if_statement893)
                    statement86 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_statement.add(statement86.tree)

                    # AST Rewrite
                    # elements: expression, statement, statement
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 140:5: -> ^( IF expression statement statement )
                        # foo_lang/parser/foo_lang.g:140:8: ^( IF expression statement statement )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IF, "IF"), root_1)

                        self._adaptor.addChild(root_1, stream_expression.nextTree())
                        self._adaptor.addChild(root_1, stream_statement.nextTree())
                        self._adaptor.addChild(root_1, stream_statement.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt16 == 2:
                    # foo_lang/parser/foo_lang.g:141:5: 'if' LPAREN expression RPAREN statement
                    pass 
                    string_literal87=self.match(self.input, 73, self.FOLLOW_73_in_if_statement915) 
                    if self._state.backtracking == 0:
                        stream_73.add(string_literal87)
                    LPAREN88=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_if_statement917) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN88)
                    self._state.following.append(self.FOLLOW_expression_in_if_statement919)
                    expression89 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression89.tree)
                    RPAREN90=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_if_statement921) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN90)
                    self._state.following.append(self.FOLLOW_statement_in_if_statement923)
                    statement91 = self.statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_statement.add(statement91.tree)

                    # AST Rewrite
                    # elements: statement, expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 142:5: -> ^( IF expression statement )
                        # foo_lang/parser/foo_lang.g:142:8: ^( IF expression statement )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IF, "IF"), root_1)

                        self._adaptor.addChild(root_1, stream_expression.nextTree())
                        self._adaptor.addChild(root_1, stream_statement.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "if_statement"

    class case_statement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "case_statement"
    # foo_lang/parser/foo_lang.g:145:1: case_statement : 'case' expression LBRACE ( case_clauses )? ( else_clause )? RBRACE -> ^( CASES expression ( case_clauses )? ) ;
    def case_statement(self, ):

        retval = self.case_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal92 = None
        LBRACE94 = None
        RBRACE97 = None
        expression93 = None

        case_clauses95 = None

        else_clause96 = None


        string_literal92_tree = None
        LBRACE94_tree = None
        RBRACE97_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_75 = RewriteRuleTokenStream(self._adaptor, "token 75")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_else_clause = RewriteRuleSubtreeStream(self._adaptor, "rule else_clause")
        stream_case_clauses = RewriteRuleSubtreeStream(self._adaptor, "rule case_clauses")
        try:
            try:
                # foo_lang/parser/foo_lang.g:146:3: ( 'case' expression LBRACE ( case_clauses )? ( else_clause )? RBRACE -> ^( CASES expression ( case_clauses )? ) )
                # foo_lang/parser/foo_lang.g:146:5: 'case' expression LBRACE ( case_clauses )? ( else_clause )? RBRACE
                pass 
                string_literal92=self.match(self.input, 75, self.FOLLOW_75_in_case_statement950) 
                if self._state.backtracking == 0:
                    stream_75.add(string_literal92)
                self._state.following.append(self.FOLLOW_expression_in_case_statement952)
                expression93 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression93.tree)
                LBRACE94=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_case_statement954) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE94)
                # foo_lang/parser/foo_lang.g:146:30: ( case_clauses )?
                alt17 = 2
                LA17 = self.input.LA(1)
                if LA17 == IDENTIFIER or LA17 == 65 or LA17 == 76 or LA17 == 77 or LA17 == 78 or LA17 == 87:
                    alt17 = 1
                elif LA17 == 74:
                    LA17_2 = self.input.LA(2)

                    if (self.synpred30_foo_lang()) :
                        alt17 = 1
                elif LA17 == RBRACE:
                    LA17_3 = self.input.LA(2)

                    if (self.synpred30_foo_lang()) :
                        alt17 = 1
                if alt17 == 1:
                    # foo_lang/parser/foo_lang.g:0:0: case_clauses
                    pass 
                    self._state.following.append(self.FOLLOW_case_clauses_in_case_statement956)
                    case_clauses95 = self.case_clauses()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_case_clauses.add(case_clauses95.tree)



                # foo_lang/parser/foo_lang.g:146:44: ( else_clause )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == 74) :
                    alt18 = 1
                if alt18 == 1:
                    # foo_lang/parser/foo_lang.g:0:0: else_clause
                    pass 
                    self._state.following.append(self.FOLLOW_else_clause_in_case_statement959)
                    else_clause96 = self.else_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_else_clause.add(else_clause96.tree)



                RBRACE97=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_case_statement962) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE97)

                # AST Rewrite
                # elements: expression, case_clauses
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 147:5: -> ^( CASES expression ( case_clauses )? )
                    # foo_lang/parser/foo_lang.g:147:8: ^( CASES expression ( case_clauses )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CASES, "CASES"), root_1)

                    self._adaptor.addChild(root_1, stream_expression.nextTree())
                    # foo_lang/parser/foo_lang.g:147:27: ( case_clauses )?
                    if stream_case_clauses.hasNext():
                        self._adaptor.addChild(root_1, stream_case_clauses.nextTree())


                    stream_case_clauses.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "case_statement"

    class case_clauses_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "case_clauses"
    # foo_lang/parser/foo_lang.g:150:1: case_clauses : ( case_clause )* ;
    def case_clauses(self, ):

        retval = self.case_clauses_return()
        retval.start = self.input.LT(1)

        root_0 = None

        case_clause98 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:150:13: ( ( case_clause )* )
                # foo_lang/parser/foo_lang.g:150:15: ( case_clause )*
                pass 
                root_0 = self._adaptor.nil()

                # foo_lang/parser/foo_lang.g:150:15: ( case_clause )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == IDENTIFIER or LA19_0 == 65 or (76 <= LA19_0 <= 78) or LA19_0 == 87) :
                        alt19 = 1


                    if alt19 == 1:
                        # foo_lang/parser/foo_lang.g:0:0: case_clause
                        pass 
                        self._state.following.append(self.FOLLOW_case_clause_in_case_clauses987)
                        case_clause98 = self.case_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, case_clause98.tree)


                    else:
                        break #loop19





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "case_clauses"

    class case_clause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "case_clause"
    # foo_lang/parser/foo_lang.g:151:1: case_clause : function_call_expression block_statement -> ^( CASE function_call_expression block_statement ) ;
    def case_clause(self, ):

        retval = self.case_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        function_call_expression99 = None

        block_statement100 = None


        stream_block_statement = RewriteRuleSubtreeStream(self._adaptor, "rule block_statement")
        stream_function_call_expression = RewriteRuleSubtreeStream(self._adaptor, "rule function_call_expression")
        try:
            try:
                # foo_lang/parser/foo_lang.g:152:3: ( function_call_expression block_statement -> ^( CASE function_call_expression block_statement ) )
                # foo_lang/parser/foo_lang.g:152:5: function_call_expression block_statement
                pass 
                self._state.following.append(self.FOLLOW_function_call_expression_in_case_clause997)
                function_call_expression99 = self.function_call_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_function_call_expression.add(function_call_expression99.tree)
                self._state.following.append(self.FOLLOW_block_statement_in_case_clause999)
                block_statement100 = self.block_statement()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_block_statement.add(block_statement100.tree)

                # AST Rewrite
                # elements: function_call_expression, block_statement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 153:5: -> ^( CASE function_call_expression block_statement )
                    # foo_lang/parser/foo_lang.g:153:8: ^( CASE function_call_expression block_statement )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CASE, "CASE"), root_1)

                    self._adaptor.addChild(root_1, stream_function_call_expression.nextTree())
                    self._adaptor.addChild(root_1, stream_block_statement.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "case_clause"

    class else_clause_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "else_clause"
    # foo_lang/parser/foo_lang.g:155:1: else_clause : 'else' statement -> ^( CASE 'else' statement ) ;
    def else_clause(self, ):

        retval = self.else_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal101 = None
        statement102 = None


        string_literal101_tree = None
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # foo_lang/parser/foo_lang.g:155:12: ( 'else' statement -> ^( CASE 'else' statement ) )
                # foo_lang/parser/foo_lang.g:155:14: 'else' statement
                pass 
                string_literal101=self.match(self.input, 74, self.FOLLOW_74_in_else_clause1022) 
                if self._state.backtracking == 0:
                    stream_74.add(string_literal101)
                self._state.following.append(self.FOLLOW_statement_in_else_clause1024)
                statement102 = self.statement()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_statement.add(statement102.tree)

                # AST Rewrite
                # elements: 74, statement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 155:31: -> ^( CASE 'else' statement )
                    # foo_lang/parser/foo_lang.g:155:34: ^( CASE 'else' statement )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CASE, "CASE"), root_1)

                    self._adaptor.addChild(root_1, stream_74.nextNode())
                    self._adaptor.addChild(root_1, stream_statement.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "else_clause"

    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "expression"
    # foo_lang/parser/foo_lang.g:157:1: expression : logical_expression ;
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        logical_expression103 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:157:11: ( logical_expression )
                # foo_lang/parser/foo_lang.g:157:13: logical_expression
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_logical_expression_in_expression1041)
                logical_expression103 = self.logical_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, logical_expression103.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "expression"

    class logical_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "logical_expression"
    # foo_lang/parser/foo_lang.g:162:1: logical_expression : or_expression ;
    def logical_expression(self, ):

        retval = self.logical_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        or_expression104 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:162:19: ( or_expression )
                # foo_lang/parser/foo_lang.g:162:21: or_expression
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_or_expression_in_logical_expression1051)
                or_expression104 = self.or_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, or_expression104.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "logical_expression"

    class or_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "or_expression"
    # foo_lang/parser/foo_lang.g:164:1: or_expression : and_expression ( OR and_expression )* ;
    def or_expression(self, ):

        retval = self.or_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR106 = None
        and_expression105 = None

        and_expression107 = None


        OR106_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:165:3: ( and_expression ( OR and_expression )* )
                # foo_lang/parser/foo_lang.g:165:5: and_expression ( OR and_expression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_and_expression_in_or_expression1061)
                and_expression105 = self.and_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, and_expression105.tree)
                # foo_lang/parser/foo_lang.g:165:20: ( OR and_expression )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == OR) :
                        LA20_2 = self.input.LA(2)

                        if (self.synpred33_foo_lang()) :
                            alt20 = 1




                    if alt20 == 1:
                        # foo_lang/parser/foo_lang.g:165:21: OR and_expression
                        pass 
                        OR106=self.match(self.input, OR, self.FOLLOW_OR_in_or_expression1064)
                        if self._state.backtracking == 0:

                            OR106_tree = self._adaptor.createWithPayload(OR106)
                            self._adaptor.addChild(root_0, OR106_tree)

                        self._state.following.append(self.FOLLOW_and_expression_in_or_expression1066)
                        and_expression107 = self.and_expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, and_expression107.tree)


                    else:
                        break #loop20





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "or_expression"

    class and_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "and_expression"
    # foo_lang/parser/foo_lang.g:168:1: and_expression : equality_expression ( AND equality_expression )* ;
    def and_expression(self, ):

        retval = self.and_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND109 = None
        equality_expression108 = None

        equality_expression110 = None


        AND109_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:169:3: ( equality_expression ( AND equality_expression )* )
                # foo_lang/parser/foo_lang.g:169:5: equality_expression ( AND equality_expression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_equality_expression_in_and_expression1081)
                equality_expression108 = self.equality_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, equality_expression108.tree)
                # foo_lang/parser/foo_lang.g:169:25: ( AND equality_expression )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == AND) :
                        LA21_2 = self.input.LA(2)

                        if (self.synpred34_foo_lang()) :
                            alt21 = 1




                    if alt21 == 1:
                        # foo_lang/parser/foo_lang.g:169:26: AND equality_expression
                        pass 
                        AND109=self.match(self.input, AND, self.FOLLOW_AND_in_and_expression1084)
                        if self._state.backtracking == 0:

                            AND109_tree = self._adaptor.createWithPayload(AND109)
                            root_0 = self._adaptor.becomeRoot(AND109_tree, root_0)

                        self._state.following.append(self.FOLLOW_equality_expression_in_and_expression1087)
                        equality_expression110 = self.equality_expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, equality_expression110.tree)


                    else:
                        break #loop21





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "and_expression"

    class equality_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "equality_expression"
    # foo_lang/parser/foo_lang.g:172:1: equality_expression : order_expression ( ( EQUALS | NOTEQUALS ) order_expression )* ;
    def equality_expression(self, ):

        retval = self.equality_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set112 = None
        order_expression111 = None

        order_expression113 = None


        set112_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:173:3: ( order_expression ( ( EQUALS | NOTEQUALS ) order_expression )* )
                # foo_lang/parser/foo_lang.g:173:5: order_expression ( ( EQUALS | NOTEQUALS ) order_expression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_order_expression_in_equality_expression1102)
                order_expression111 = self.order_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, order_expression111.tree)
                # foo_lang/parser/foo_lang.g:173:22: ( ( EQUALS | NOTEQUALS ) order_expression )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((EQUALS <= LA22_0 <= NOTEQUALS)) :
                        LA22_2 = self.input.LA(2)

                        if (self.synpred36_foo_lang()) :
                            alt22 = 1




                    if alt22 == 1:
                        # foo_lang/parser/foo_lang.g:173:23: ( EQUALS | NOTEQUALS ) order_expression
                        pass 
                        set112 = self.input.LT(1)
                        set112 = self.input.LT(1)
                        if (EQUALS <= self.input.LA(1) <= NOTEQUALS):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set112), root_0)
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_order_expression_in_equality_expression1114)
                        order_expression113 = self.order_expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, order_expression113.tree)


                    else:
                        break #loop22





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "equality_expression"

    class order_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "order_expression"
    # foo_lang/parser/foo_lang.g:176:1: order_expression : left= additive_expression ( ( LT | LTEQ | GT | GTEQ ) additive_expression )* ;
    def order_expression(self, ):

        retval = self.order_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set114 = None
        left = None

        additive_expression115 = None


        set114_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:177:3: (left= additive_expression ( ( LT | LTEQ | GT | GTEQ ) additive_expression )* )
                # foo_lang/parser/foo_lang.g:177:5: left= additive_expression ( ( LT | LTEQ | GT | GTEQ ) additive_expression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_additive_expression_in_order_expression1131)
                left = self.additive_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, left.tree)
                # foo_lang/parser/foo_lang.g:178:5: ( ( LT | LTEQ | GT | GTEQ ) additive_expression )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if ((LT <= LA23_0 <= GTEQ)) :
                        LA23_2 = self.input.LA(2)

                        if (self.synpred40_foo_lang()) :
                            alt23 = 1




                    if alt23 == 1:
                        # foo_lang/parser/foo_lang.g:178:6: ( LT | LTEQ | GT | GTEQ ) additive_expression
                        pass 
                        set114 = self.input.LT(1)
                        set114 = self.input.LT(1)
                        if (LT <= self.input.LA(1) <= GTEQ):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set114), root_0)
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_additive_expression_in_order_expression1155)
                        additive_expression115 = self.additive_expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, additive_expression115.tree)


                    else:
                        break #loop23





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "order_expression"

    class additive_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "additive_expression"
    # foo_lang/parser/foo_lang.g:181:1: additive_expression : left= multiplicative_expression ( ( PLUS | MINUS ) multiplicative_expression )* ;
    def additive_expression(self, ):

        retval = self.additive_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set116 = None
        left = None

        multiplicative_expression117 = None


        set116_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:182:3: (left= multiplicative_expression ( ( PLUS | MINUS ) multiplicative_expression )* )
                # foo_lang/parser/foo_lang.g:182:5: left= multiplicative_expression ( ( PLUS | MINUS ) multiplicative_expression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_multiplicative_expression_in_additive_expression1172)
                left = self.multiplicative_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, left.tree)
                # foo_lang/parser/foo_lang.g:183:5: ( ( PLUS | MINUS ) multiplicative_expression )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if ((PLUS <= LA24_0 <= MINUS)) :
                        LA24_2 = self.input.LA(2)

                        if (self.synpred42_foo_lang()) :
                            alt24 = 1




                    if alt24 == 1:
                        # foo_lang/parser/foo_lang.g:183:6: ( PLUS | MINUS ) multiplicative_expression
                        pass 
                        set116 = self.input.LT(1)
                        set116 = self.input.LT(1)
                        if (PLUS <= self.input.LA(1) <= MINUS):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set116), root_0)
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_multiplicative_expression_in_additive_expression1188)
                        multiplicative_expression117 = self.multiplicative_expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, multiplicative_expression117.tree)


                    else:
                        break #loop24





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "additive_expression"

    class multiplicative_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "multiplicative_expression"
    # foo_lang/parser/foo_lang.g:186:1: multiplicative_expression : unary_expression ( ( MULT | DIV | MOD ) unary_expression )* ;
    def multiplicative_expression(self, ):

        retval = self.multiplicative_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set119 = None
        unary_expression118 = None

        unary_expression120 = None


        set119_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:187:3: ( unary_expression ( ( MULT | DIV | MOD ) unary_expression )* )
                # foo_lang/parser/foo_lang.g:187:5: unary_expression ( ( MULT | DIV | MOD ) unary_expression )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_unary_expression_in_multiplicative_expression1203)
                unary_expression118 = self.unary_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, unary_expression118.tree)
                # foo_lang/parser/foo_lang.g:187:22: ( ( MULT | DIV | MOD ) unary_expression )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if ((MULT <= LA25_0 <= MOD)) :
                        LA25_2 = self.input.LA(2)

                        if (self.synpred45_foo_lang()) :
                            alt25 = 1




                    if alt25 == 1:
                        # foo_lang/parser/foo_lang.g:187:23: ( MULT | DIV | MOD ) unary_expression
                        pass 
                        set119 = self.input.LT(1)
                        set119 = self.input.LT(1)
                        if (MULT <= self.input.LA(1) <= MOD):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set119), root_0)
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_unary_expression_in_multiplicative_expression1221)
                        unary_expression120 = self.unary_expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, unary_expression120.tree)


                    else:
                        break #loop25





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "multiplicative_expression"

    class unary_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "unary_expression"
    # foo_lang/parser/foo_lang.g:190:1: unary_expression : ( NOT )? primary_expression ;
    def unary_expression(self, ):

        retval = self.unary_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT121 = None
        primary_expression122 = None


        NOT121_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:191:3: ( ( NOT )? primary_expression )
                # foo_lang/parser/foo_lang.g:191:5: ( NOT )? primary_expression
                pass 
                root_0 = self._adaptor.nil()

                # foo_lang/parser/foo_lang.g:191:8: ( NOT )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == NOT) :
                    LA26_1 = self.input.LA(2)

                    if (self.synpred46_foo_lang()) :
                        alt26 = 1
                if alt26 == 1:
                    # foo_lang/parser/foo_lang.g:0:0: NOT
                    pass 
                    NOT121=self.match(self.input, NOT, self.FOLLOW_NOT_in_unary_expression1236)
                    if self._state.backtracking == 0:

                        NOT121_tree = self._adaptor.createWithPayload(NOT121)
                        root_0 = self._adaptor.becomeRoot(NOT121_tree, root_0)




                self._state.following.append(self.FOLLOW_primary_expression_in_unary_expression1240)
                primary_expression122 = self.primary_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, primary_expression122.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "unary_expression"

    class primary_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "primary_expression"
    # foo_lang/parser/foo_lang.g:194:1: primary_expression : ( LPAREN logical_expression RPAREN | literal | call_expression | variable | atom | matching_expression );
    def primary_expression(self, ):

        retval = self.primary_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN123 = None
        RPAREN125 = None
        logical_expression124 = None

        literal126 = None

        call_expression127 = None

        variable128 = None

        atom129 = None

        matching_expression130 = None


        LPAREN123_tree = None
        RPAREN125_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:195:3: ( LPAREN logical_expression RPAREN | literal | call_expression | variable | atom | matching_expression )
                alt27 = 6
                alt27 = self.dfa27.predict(self.input)
                if alt27 == 1:
                    # foo_lang/parser/foo_lang.g:195:5: LPAREN logical_expression RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN123=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_primary_expression1253)
                    self._state.following.append(self.FOLLOW_logical_expression_in_primary_expression1256)
                    logical_expression124 = self.logical_expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, logical_expression124.tree)
                    RPAREN125=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_primary_expression1258)


                elif alt27 == 2:
                    # foo_lang/parser/foo_lang.g:196:5: literal
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_literal_in_primary_expression1265)
                    literal126 = self.literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, literal126.tree)


                elif alt27 == 3:
                    # foo_lang/parser/foo_lang.g:197:5: call_expression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_call_expression_in_primary_expression1271)
                    call_expression127 = self.call_expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, call_expression127.tree)


                elif alt27 == 4:
                    # foo_lang/parser/foo_lang.g:198:5: variable
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_variable_in_primary_expression1277)
                    variable128 = self.variable()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, variable128.tree)


                elif alt27 == 5:
                    # foo_lang/parser/foo_lang.g:199:5: atom
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_atom_in_primary_expression1283)
                    atom129 = self.atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, atom129.tree)


                elif alt27 == 6:
                    # foo_lang/parser/foo_lang.g:200:5: matching_expression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_matching_expression_in_primary_expression1289)
                    matching_expression130 = self.matching_expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, matching_expression130.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "primary_expression"

    class call_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "call_expression"
    # foo_lang/parser/foo_lang.g:203:1: call_expression : ( method_call_expression -> ^( METHOD_CALL method_call_expression ) | function_call_expression -> ^( FUNC_CALL function_call_expression ) );
    def call_expression(self, ):

        retval = self.call_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        method_call_expression131 = None

        function_call_expression132 = None


        stream_function_call_expression = RewriteRuleSubtreeStream(self._adaptor, "rule function_call_expression")
        stream_method_call_expression = RewriteRuleSubtreeStream(self._adaptor, "rule method_call_expression")
        try:
            try:
                # foo_lang/parser/foo_lang.g:204:3: ( method_call_expression -> ^( METHOD_CALL method_call_expression ) | function_call_expression -> ^( FUNC_CALL function_call_expression ) )
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == IDENTIFIER or LA28_0 == 65 or (76 <= LA28_0 <= 78) or LA28_0 == 87) :
                    LA28_1 = self.input.LA(2)

                    if (LA28_1 == DOT) :
                        alt28 = 1
                    elif (LA28_1 == LPAREN) :
                        alt28 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 28, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae

                if alt28 == 1:
                    # foo_lang/parser/foo_lang.g:204:5: method_call_expression
                    pass 
                    self._state.following.append(self.FOLLOW_method_call_expression_in_call_expression1302)
                    method_call_expression131 = self.method_call_expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_method_call_expression.add(method_call_expression131.tree)

                    # AST Rewrite
                    # elements: method_call_expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 204:30: -> ^( METHOD_CALL method_call_expression )
                        # foo_lang/parser/foo_lang.g:204:33: ^( METHOD_CALL method_call_expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHOD_CALL, "METHOD_CALL"), root_1)

                        self._adaptor.addChild(root_1, stream_method_call_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt28 == 2:
                    # foo_lang/parser/foo_lang.g:205:5: function_call_expression
                    pass 
                    self._state.following.append(self.FOLLOW_function_call_expression_in_call_expression1318)
                    function_call_expression132 = self.function_call_expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_function_call_expression.add(function_call_expression132.tree)

                    # AST Rewrite
                    # elements: function_call_expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 205:30: -> ^( FUNC_CALL function_call_expression )
                        # foo_lang/parser/foo_lang.g:205:33: ^( FUNC_CALL function_call_expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNC_CALL, "FUNC_CALL"), root_1)

                        self._adaptor.addChild(root_1, stream_function_call_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "call_expression"

    class method_call_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "method_call_expression"
    # foo_lang/parser/foo_lang.g:209:1: method_call_expression : identifier DOT ( identifier DOT )* function_call_expression ;
    def method_call_expression(self, ):

        retval = self.method_call_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOT134 = None
        DOT136 = None
        identifier133 = None

        identifier135 = None

        function_call_expression137 = None


        DOT134_tree = None
        DOT136_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:209:24: ( identifier DOT ( identifier DOT )* function_call_expression )
                # foo_lang/parser/foo_lang.g:209:26: identifier DOT ( identifier DOT )* function_call_expression
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_method_call_expression1338)
                identifier133 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier133.tree)
                DOT134=self.match(self.input, DOT, self.FOLLOW_DOT_in_method_call_expression1340)
                # foo_lang/parser/foo_lang.g:209:42: ( identifier DOT )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == IDENTIFIER or LA29_0 == 65 or (76 <= LA29_0 <= 78) or LA29_0 == 87) :
                        LA29_1 = self.input.LA(2)

                        if (LA29_1 == DOT) :
                            alt29 = 1




                    if alt29 == 1:
                        # foo_lang/parser/foo_lang.g:209:43: identifier DOT
                        pass 
                        self._state.following.append(self.FOLLOW_identifier_in_method_call_expression1344)
                        identifier135 = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifier135.tree)
                        DOT136=self.match(self.input, DOT, self.FOLLOW_DOT_in_method_call_expression1346)


                    else:
                        break #loop29


                self._state.following.append(self.FOLLOW_function_call_expression_in_method_call_expression1351)
                function_call_expression137 = self.function_call_expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, function_call_expression137.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "method_call_expression"

    class function_call_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "function_call_expression"
    # foo_lang/parser/foo_lang.g:210:1: function_call_expression : identifier LPAREN ( argument_list )? RPAREN ;
    def function_call_expression(self, ):

        retval = self.function_call_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN139 = None
        RPAREN141 = None
        identifier138 = None

        argument_list140 = None


        LPAREN139_tree = None
        RPAREN141_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:210:25: ( identifier LPAREN ( argument_list )? RPAREN )
                # foo_lang/parser/foo_lang.g:210:27: identifier LPAREN ( argument_list )? RPAREN
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_function_call_expression1357)
                identifier138 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier138.tree)
                LPAREN139=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_function_call_expression1359)
                # foo_lang/parser/foo_lang.g:210:46: ( argument_list )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if ((FLOAT <= LA30_0 <= LPAREN) or LA30_0 == LBRACE or (EQUALS <= LA30_0 <= GTEQ) or (NOT <= LA30_0 <= LBRACKET) or LA30_0 == IDENTIFIER or LA30_0 == 65 or (76 <= LA30_0 <= 81) or LA30_0 == 87) :
                    alt30 = 1
                if alt30 == 1:
                    # foo_lang/parser/foo_lang.g:210:47: argument_list
                    pass 
                    self._state.following.append(self.FOLLOW_argument_list_in_function_call_expression1363)
                    argument_list140 = self.argument_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, argument_list140.tree)



                RPAREN141=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function_call_expression1367)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "function_call_expression"

    class argument_list_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "argument_list"
    # foo_lang/parser/foo_lang.g:211:1: argument_list : a+= expression ( COMMA a+= expression )* -> ^( LIST ( $a)+ ) ;
    def argument_list(self, ):

        retval = self.argument_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA142 = None
        list_a = None
        a = None

        a = None
        COMMA142_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        try:
            try:
                # foo_lang/parser/foo_lang.g:211:14: (a+= expression ( COMMA a+= expression )* -> ^( LIST ( $a)+ ) )
                # foo_lang/parser/foo_lang.g:211:16: a+= expression ( COMMA a+= expression )*
                pass 
                self._state.following.append(self.FOLLOW_expression_in_argument_list1376)
                a = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(a.tree)
                if list_a is None:
                    list_a = []
                list_a.append(a.tree)

                # foo_lang/parser/foo_lang.g:211:30: ( COMMA a+= expression )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == COMMA) :
                        alt31 = 1


                    if alt31 == 1:
                        # foo_lang/parser/foo_lang.g:211:31: COMMA a+= expression
                        pass 
                        COMMA142=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_argument_list1379) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA142)
                        self._state.following.append(self.FOLLOW_expression_in_argument_list1383)
                        a = self.expression()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_expression.add(a.tree)
                        if list_a is None:
                            list_a = []
                        list_a.append(a.tree)



                    else:
                        break #loop31



                # AST Rewrite
                # elements: a
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: a
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                    stream_a = RewriteRuleSubtreeStream(self._adaptor, "token a", list_a)
                    root_0 = self._adaptor.nil()
                    # 211:53: -> ^( LIST ( $a)+ )
                    # foo_lang/parser/foo_lang.g:211:56: ^( LIST ( $a)+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LIST, "LIST"), root_1)

                    # foo_lang/parser/foo_lang.g:211:63: ( $a)+
                    if not (stream_a.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_a.hasNext():
                        self._adaptor.addChild(root_1, stream_a.nextTree())


                    stream_a.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "argument_list"

    class variable_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "variable"
    # foo_lang/parser/foo_lang.g:215:1: variable : ( property_expression | identifier -> ^( VAR identifier ) );
    def variable(self, ):

        retval = self.variable_return()
        retval.start = self.input.LT(1)

        root_0 = None

        property_expression143 = None

        identifier144 = None


        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # foo_lang/parser/foo_lang.g:216:3: ( property_expression | identifier -> ^( VAR identifier ) )
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == IDENTIFIER or LA32_0 == 65 or (76 <= LA32_0 <= 78) or LA32_0 == 87) :
                    LA32_1 = self.input.LA(2)

                    if (LA32_1 == DOT) :
                        alt32 = 1
                    elif (LA32_1 == EOF or LA32_1 == ASSIGN or (RPAREN <= LA32_1 <= MOD) or (RBRACKET <= LA32_1 <= IDENTIFIER) or LA32_1 == 65 or (71 <= LA32_1 <= 78) or LA32_1 == 87) :
                        alt32 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 32, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae

                if alt32 == 1:
                    # foo_lang/parser/foo_lang.g:216:5: property_expression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_property_expression_in_variable1407)
                    property_expression143 = self.property_expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, property_expression143.tree)


                elif alt32 == 2:
                    # foo_lang/parser/foo_lang.g:217:5: identifier
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_variable1413)
                    identifier144 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier144.tree)

                    # AST Rewrite
                    # elements: identifier
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 217:26: -> ^( VAR identifier )
                        # foo_lang/parser/foo_lang.g:217:29: ^( VAR identifier )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VAR, "VAR"), root_1)

                        self._adaptor.addChild(root_1, stream_identifier.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "variable"

    class property_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "property_expression"
    # foo_lang/parser/foo_lang.g:220:1: property_expression : o+= identifier DOT (o+= identifier DOT )* p= identifier -> ^( PROPERTY ( $o)+ $p) ;
    def property_expression(self, ):

        retval = self.property_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOT145 = None
        DOT146 = None
        list_o = None
        p = None

        o = None

        o = None
        DOT145_tree = None
        DOT146_tree = None
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # foo_lang/parser/foo_lang.g:221:3: (o+= identifier DOT (o+= identifier DOT )* p= identifier -> ^( PROPERTY ( $o)+ $p) )
                # foo_lang/parser/foo_lang.g:221:5: o+= identifier DOT (o+= identifier DOT )* p= identifier
                pass 
                self._state.following.append(self.FOLLOW_identifier_in_property_expression1446)
                o = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(o.tree)
                if list_o is None:
                    list_o = []
                list_o.append(o.tree)

                DOT145=self.match(self.input, DOT, self.FOLLOW_DOT_in_property_expression1448) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT145)
                # foo_lang/parser/foo_lang.g:221:23: (o+= identifier DOT )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == IDENTIFIER or LA33_0 == 65 or (76 <= LA33_0 <= 78) or LA33_0 == 87) :
                        LA33_1 = self.input.LA(2)

                        if (LA33_1 == DOT) :
                            alt33 = 1




                    if alt33 == 1:
                        # foo_lang/parser/foo_lang.g:221:24: o+= identifier DOT
                        pass 
                        self._state.following.append(self.FOLLOW_identifier_in_property_expression1453)
                        o = self.identifier()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_identifier.add(o.tree)
                        if list_o is None:
                            list_o = []
                        list_o.append(o.tree)

                        DOT146=self.match(self.input, DOT, self.FOLLOW_DOT_in_property_expression1455) 
                        if self._state.backtracking == 0:
                            stream_DOT.add(DOT146)


                    else:
                        break #loop33


                self._state.following.append(self.FOLLOW_identifier_in_property_expression1461)
                p = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(p.tree)

                # AST Rewrite
                # elements: p, o
                # token labels: 
                # rule labels: retval, p
                # token list labels: 
                # rule list labels: o
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if p is not None:
                        stream_p = RewriteRuleSubtreeStream(self._adaptor, "token p", p.tree)
                    else:
                        stream_p = RewriteRuleSubtreeStream(self._adaptor, "token p", None)

                    stream_o = RewriteRuleSubtreeStream(self._adaptor, "token o", list_o)
                    root_0 = self._adaptor.nil()
                    # 222:5: -> ^( PROPERTY ( $o)+ $p)
                    # foo_lang/parser/foo_lang.g:222:8: ^( PROPERTY ( $o)+ $p)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROPERTY, "PROPERTY"), root_1)

                    # foo_lang/parser/foo_lang.g:222:19: ( $o)+
                    if not (stream_o.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_o.hasNext():
                        self._adaptor.addChild(root_1, stream_o.nextTree())


                    stream_o.reset()
                    self._adaptor.addChild(root_1, stream_p.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "property_expression"

    class directive_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "directive"
    # foo_lang/parser/foo_lang.g:232:1: directive : import_directive ;
    def directive(self, ):

        retval = self.directive_return()
        retval.start = self.input.LT(1)

        root_0 = None

        import_directive147 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:232:11: ( import_directive )
                # foo_lang/parser/foo_lang.g:232:13: import_directive
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_import_directive_in_directive1493)
                import_directive147 = self.import_directive()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, import_directive147.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "directive"

    class import_directive_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "import_directive"
    # foo_lang/parser/foo_lang.g:234:1: import_directive : 'from' identifier 'import' identifier -> ^( IMPORT identifier identifier ) ;
    def import_directive(self, ):

        retval = self.import_directive_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal148 = None
        string_literal150 = None
        identifier149 = None

        identifier151 = None


        string_literal148_tree = None
        string_literal150_tree = None
        stream_77 = RewriteRuleTokenStream(self._adaptor, "token 77")
        stream_76 = RewriteRuleTokenStream(self._adaptor, "token 76")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # foo_lang/parser/foo_lang.g:234:18: ( 'from' identifier 'import' identifier -> ^( IMPORT identifier identifier ) )
                # foo_lang/parser/foo_lang.g:234:20: 'from' identifier 'import' identifier
                pass 
                string_literal148=self.match(self.input, 76, self.FOLLOW_76_in_import_directive1501) 
                if self._state.backtracking == 0:
                    stream_76.add(string_literal148)
                self._state.following.append(self.FOLLOW_identifier_in_import_directive1503)
                identifier149 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(identifier149.tree)
                string_literal150=self.match(self.input, 77, self.FOLLOW_77_in_import_directive1505) 
                if self._state.backtracking == 0:
                    stream_77.add(string_literal150)
                self._state.following.append(self.FOLLOW_identifier_in_import_directive1507)
                identifier151 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(identifier151.tree)

                # AST Rewrite
                # elements: identifier, identifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 235:20: -> ^( IMPORT identifier identifier )
                    # foo_lang/parser/foo_lang.g:235:23: ^( IMPORT identifier identifier )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IMPORT, "IMPORT"), root_1)

                    self._adaptor.addChild(root_1, stream_identifier.nextTree())
                    self._adaptor.addChild(root_1, stream_identifier.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "import_directive"

    class extension_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "extension"
    # foo_lang/parser/foo_lang.g:239:1: extension : 'extend' identifier 'with' literal -> ^( EXTEND identifier literal ) ;
    def extension(self, ):

        retval = self.extension_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal152 = None
        string_literal154 = None
        identifier153 = None

        literal155 = None


        string_literal152_tree = None
        string_literal154_tree = None
        stream_78 = RewriteRuleTokenStream(self._adaptor, "token 78")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        stream_literal = RewriteRuleSubtreeStream(self._adaptor, "rule literal")
        try:
            try:
                # foo_lang/parser/foo_lang.g:239:11: ( 'extend' identifier 'with' literal -> ^( EXTEND identifier literal ) )
                # foo_lang/parser/foo_lang.g:239:13: 'extend' identifier 'with' literal
                pass 
                string_literal152=self.match(self.input, 78, self.FOLLOW_78_in_extension1546) 
                if self._state.backtracking == 0:
                    stream_78.add(string_literal152)
                self._state.following.append(self.FOLLOW_identifier_in_extension1548)
                identifier153 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(identifier153.tree)
                string_literal154=self.match(self.input, 65, self.FOLLOW_65_in_extension1550) 
                if self._state.backtracking == 0:
                    stream_65.add(string_literal154)
                self._state.following.append(self.FOLLOW_literal_in_extension1552)
                literal155 = self.literal()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_literal.add(literal155.tree)

                # AST Rewrite
                # elements: literal, identifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 240:13: -> ^( EXTEND identifier literal )
                    # foo_lang/parser/foo_lang.g:240:16: ^( EXTEND identifier literal )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXTEND, "EXTEND"), root_1)

                    self._adaptor.addChild(root_1, stream_identifier.nextTree())
                    self._adaptor.addChild(root_1, stream_literal.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "extension"

    class literal_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "literal"
    # foo_lang/parser/foo_lang.g:244:1: literal : ( numeric_literal | boolean_literal | object_literal | list_literal );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)

        root_0 = None

        numeric_literal156 = None

        boolean_literal157 = None

        object_literal158 = None

        list_literal159 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:244:8: ( numeric_literal | boolean_literal | object_literal | list_literal )
                alt34 = 4
                LA34 = self.input.LA(1)
                if LA34 == FLOAT or LA34 == INTEGER:
                    alt34 = 1
                elif LA34 == 79 or LA34 == 80:
                    alt34 = 2
                elif LA34 == LBRACE:
                    alt34 = 3
                elif LA34 == LBRACKET:
                    alt34 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae

                if alt34 == 1:
                    # foo_lang/parser/foo_lang.g:244:10: numeric_literal
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_numeric_literal_in_literal1583)
                    numeric_literal156 = self.numeric_literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, numeric_literal156.tree)


                elif alt34 == 2:
                    # foo_lang/parser/foo_lang.g:244:28: boolean_literal
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_boolean_literal_in_literal1587)
                    boolean_literal157 = self.boolean_literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, boolean_literal157.tree)


                elif alt34 == 3:
                    # foo_lang/parser/foo_lang.g:244:46: object_literal
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_object_literal_in_literal1591)
                    object_literal158 = self.object_literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, object_literal158.tree)


                elif alt34 == 4:
                    # foo_lang/parser/foo_lang.g:244:63: list_literal
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_list_literal_in_literal1595)
                    list_literal159 = self.list_literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, list_literal159.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "literal"

    class boolean_literal_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "boolean_literal"
    # foo_lang/parser/foo_lang.g:245:1: boolean_literal : ( 'true' | 'false' );
    def boolean_literal(self, ):

        retval = self.boolean_literal_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set160 = None

        set160_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:245:16: ( 'true' | 'false' )
                # foo_lang/parser/foo_lang.g:
                pass 
                root_0 = self._adaptor.nil()

                set160 = self.input.LT(1)
                if (79 <= self.input.LA(1) <= 80):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set160))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "boolean_literal"

    class numeric_literal_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "numeric_literal"
    # foo_lang/parser/foo_lang.g:246:1: numeric_literal : ( INTEGER | FLOAT );
    def numeric_literal(self, ):

        retval = self.numeric_literal_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set161 = None

        set161_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:246:16: ( INTEGER | FLOAT )
                # foo_lang/parser/foo_lang.g:
                pass 
                root_0 = self._adaptor.nil()

                set161 = self.input.LT(1)
                if (FLOAT <= self.input.LA(1) <= INTEGER):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set161))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "numeric_literal"

    class object_literal_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "object_literal"
    # foo_lang/parser/foo_lang.g:247:1: object_literal : LBRACE ( property_type_value_list )? RBRACE -> ^( OBJECT ( property_type_value_list )? ) ;
    def object_literal(self, ):

        retval = self.object_literal_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACE162 = None
        RBRACE164 = None
        property_type_value_list163 = None


        LBRACE162_tree = None
        RBRACE164_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_property_type_value_list = RewriteRuleSubtreeStream(self._adaptor, "rule property_type_value_list")
        try:
            try:
                # foo_lang/parser/foo_lang.g:247:15: ( LBRACE ( property_type_value_list )? RBRACE -> ^( OBJECT ( property_type_value_list )? ) )
                # foo_lang/parser/foo_lang.g:247:17: LBRACE ( property_type_value_list )? RBRACE
                pass 
                LBRACE162=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_object_literal1621) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE162)
                # foo_lang/parser/foo_lang.g:247:24: ( property_type_value_list )?
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == IDENTIFIER or LA35_0 == 65 or (76 <= LA35_0 <= 78) or LA35_0 == 87) :
                    alt35 = 1
                if alt35 == 1:
                    # foo_lang/parser/foo_lang.g:247:25: property_type_value_list
                    pass 
                    self._state.following.append(self.FOLLOW_property_type_value_list_in_object_literal1624)
                    property_type_value_list163 = self.property_type_value_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_property_type_value_list.add(property_type_value_list163.tree)



                RBRACE164=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_object_literal1628) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE164)

                # AST Rewrite
                # elements: property_type_value_list
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 248:17: -> ^( OBJECT ( property_type_value_list )? )
                    # foo_lang/parser/foo_lang.g:248:20: ^( OBJECT ( property_type_value_list )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OBJECT, "OBJECT"), root_1)

                    # foo_lang/parser/foo_lang.g:248:29: ( property_type_value_list )?
                    if stream_property_type_value_list.hasNext():
                        self._adaptor.addChild(root_1, stream_property_type_value_list.nextTree())


                    stream_property_type_value_list.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "object_literal"

    class property_type_value_list_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "property_type_value_list"
    # foo_lang/parser/foo_lang.g:249:1: property_type_value_list : property_type_value ( property_type_value )* ;
    def property_type_value_list(self, ):

        retval = self.property_type_value_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        property_type_value165 = None

        property_type_value166 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:249:25: ( property_type_value ( property_type_value )* )
                # foo_lang/parser/foo_lang.g:249:27: property_type_value ( property_type_value )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_property_type_value_in_property_type_value_list1659)
                property_type_value165 = self.property_type_value()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, property_type_value165.tree)
                # foo_lang/parser/foo_lang.g:249:47: ( property_type_value )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == IDENTIFIER or LA36_0 == 65 or (76 <= LA36_0 <= 78) or LA36_0 == 87) :
                        alt36 = 1


                    if alt36 == 1:
                        # foo_lang/parser/foo_lang.g:249:48: property_type_value
                        pass 
                        self._state.following.append(self.FOLLOW_property_type_value_in_property_type_value_list1662)
                        property_type_value166 = self.property_type_value()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, property_type_value166.tree)


                    else:
                        break #loop36





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "property_type_value_list"

    class property_type_value_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "property_type_value"
    # foo_lang/parser/foo_lang.g:250:1: property_type_value : typed_value -> ^( PROPERTY typed_value ) ;
    def property_type_value(self, ):

        retval = self.property_type_value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        typed_value167 = None


        stream_typed_value = RewriteRuleSubtreeStream(self._adaptor, "rule typed_value")
        try:
            try:
                # foo_lang/parser/foo_lang.g:250:20: ( typed_value -> ^( PROPERTY typed_value ) )
                # foo_lang/parser/foo_lang.g:250:22: typed_value
                pass 
                self._state.following.append(self.FOLLOW_typed_value_in_property_type_value1670)
                typed_value167 = self.typed_value()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typed_value.add(typed_value167.tree)

                # AST Rewrite
                # elements: typed_value
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 250:34: -> ^( PROPERTY typed_value )
                    # foo_lang/parser/foo_lang.g:250:37: ^( PROPERTY typed_value )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROPERTY, "PROPERTY"), root_1)

                    self._adaptor.addChild(root_1, stream_typed_value.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "property_type_value"

    class atom_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "atom"
    # foo_lang/parser/foo_lang.g:252:1: atom : '#' identifier -> ^( ATOM identifier ) ;
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal168 = None
        identifier169 = None


        char_literal168_tree = None
        stream_81 = RewriteRuleTokenStream(self._adaptor, "token 81")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # foo_lang/parser/foo_lang.g:252:6: ( '#' identifier -> ^( ATOM identifier ) )
                # foo_lang/parser/foo_lang.g:252:8: '#' identifier
                pass 
                char_literal168=self.match(self.input, 81, self.FOLLOW_81_in_atom1686) 
                if self._state.backtracking == 0:
                    stream_81.add(char_literal168)
                self._state.following.append(self.FOLLOW_identifier_in_atom1688)
                identifier169 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(identifier169.tree)

                # AST Rewrite
                # elements: identifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 252:23: -> ^( ATOM identifier )
                    # foo_lang/parser/foo_lang.g:252:26: ^( ATOM identifier )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ATOM, "ATOM"), root_1)

                    self._adaptor.addChild(root_1, stream_identifier.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "atom"

    class matching_expression_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "matching_expression"
    # foo_lang/parser/foo_lang.g:254:1: matching_expression : ( dontcare | comparison );
    def matching_expression(self, ):

        retval = self.matching_expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        dontcare170 = None

        comparison171 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:254:20: ( dontcare | comparison )
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == UNDERSCORE) :
                    alt37 = 1
                elif ((EQUALS <= LA37_0 <= GTEQ) or LA37_0 == NOT) :
                    alt37 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae

                if alt37 == 1:
                    # foo_lang/parser/foo_lang.g:254:22: dontcare
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_dontcare_in_matching_expression1703)
                    dontcare170 = self.dontcare()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, dontcare170.tree)


                elif alt37 == 2:
                    # foo_lang/parser/foo_lang.g:254:33: comparison
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_comparison_in_matching_expression1707)
                    comparison171 = self.comparison()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, comparison171.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "matching_expression"

    class dontcare_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "dontcare"
    # foo_lang/parser/foo_lang.g:255:1: dontcare : UNDERSCORE ;
    def dontcare(self, ):

        retval = self.dontcare_return()
        retval.start = self.input.LT(1)

        root_0 = None

        UNDERSCORE172 = None

        UNDERSCORE172_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:255:9: ( UNDERSCORE )
                # foo_lang/parser/foo_lang.g:255:11: UNDERSCORE
                pass 
                root_0 = self._adaptor.nil()

                UNDERSCORE172=self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_dontcare1713)
                if self._state.backtracking == 0:

                    UNDERSCORE172_tree = self._adaptor.createWithPayload(UNDERSCORE172)
                    self._adaptor.addChild(root_0, UNDERSCORE172_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "dontcare"

    class comparison_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "comparison"
    # foo_lang/parser/foo_lang.g:256:1: comparison : comparator expression ;
    def comparison(self, ):

        retval = self.comparison_return()
        retval.start = self.input.LT(1)

        root_0 = None

        comparator173 = None

        expression174 = None



        try:
            try:
                # foo_lang/parser/foo_lang.g:256:11: ( comparator expression )
                # foo_lang/parser/foo_lang.g:256:13: comparator expression
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_comparator_in_comparison1719)
                comparator173 = self.comparator()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    root_0 = self._adaptor.becomeRoot(comparator173.tree, root_0)
                self._state.following.append(self.FOLLOW_expression_in_comparison1722)
                expression174 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression174.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "comparison"

    class comparator_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "comparator"
    # foo_lang/parser/foo_lang.g:257:1: comparator : ( LT | LTEQ | GT | GTEQ | EQUALS | NOTEQUALS | NOT );
    def comparator(self, ):

        retval = self.comparator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set175 = None

        set175_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:257:11: ( LT | LTEQ | GT | GTEQ | EQUALS | NOTEQUALS | NOT )
                # foo_lang/parser/foo_lang.g:
                pass 
                root_0 = self._adaptor.nil()

                set175 = self.input.LT(1)
                if (EQUALS <= self.input.LA(1) <= GTEQ) or self.input.LA(1) == NOT:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set175))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "comparator"

    class list_literal_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "list_literal"
    # foo_lang/parser/foo_lang.g:259:1: list_literal : ( LBRACKET RBRACKET -> ^( LIST ) | LBRACKET i+= expression ( COMMA i+= expression )* RBRACKET -> ^( LIST ( $i)+ ) );
    def list_literal(self, ):

        retval = self.list_literal_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACKET176 = None
        RBRACKET177 = None
        LBRACKET178 = None
        COMMA179 = None
        RBRACKET180 = None
        list_i = None
        i = None

        i = None
        LBRACKET176_tree = None
        RBRACKET177_tree = None
        LBRACKET178_tree = None
        COMMA179_tree = None
        RBRACKET180_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        try:
            try:
                # foo_lang/parser/foo_lang.g:260:3: ( LBRACKET RBRACKET -> ^( LIST ) | LBRACKET i+= expression ( COMMA i+= expression )* RBRACKET -> ^( LIST ( $i)+ ) )
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == LBRACKET) :
                    LA39_1 = self.input.LA(2)

                    if (LA39_1 == RBRACKET) :
                        alt39 = 1
                    elif ((FLOAT <= LA39_1 <= LPAREN) or LA39_1 == LBRACE or (EQUALS <= LA39_1 <= GTEQ) or (NOT <= LA39_1 <= LBRACKET) or LA39_1 == IDENTIFIER or LA39_1 == 65 or (76 <= LA39_1 <= 81) or LA39_1 == 87) :
                        alt39 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 39, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae

                if alt39 == 1:
                    # foo_lang/parser/foo_lang.g:260:5: LBRACKET RBRACKET
                    pass 
                    LBRACKET176=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_list_literal1763) 
                    if self._state.backtracking == 0:
                        stream_LBRACKET.add(LBRACKET176)
                    RBRACKET177=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_list_literal1765) 
                    if self._state.backtracking == 0:
                        stream_RBRACKET.add(RBRACKET177)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 260:23: -> ^( LIST )
                        # foo_lang/parser/foo_lang.g:260:26: ^( LIST )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LIST, "LIST"), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt39 == 2:
                    # foo_lang/parser/foo_lang.g:261:5: LBRACKET i+= expression ( COMMA i+= expression )* RBRACKET
                    pass 
                    LBRACKET178=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_list_literal1777) 
                    if self._state.backtracking == 0:
                        stream_LBRACKET.add(LBRACKET178)
                    self._state.following.append(self.FOLLOW_expression_in_list_literal1781)
                    i = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(i.tree)
                    if list_i is None:
                        list_i = []
                    list_i.append(i.tree)

                    # foo_lang/parser/foo_lang.g:261:28: ( COMMA i+= expression )*
                    while True: #loop38
                        alt38 = 2
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == COMMA) :
                            alt38 = 1


                        if alt38 == 1:
                            # foo_lang/parser/foo_lang.g:261:29: COMMA i+= expression
                            pass 
                            COMMA179=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_list_literal1784) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA179)
                            self._state.following.append(self.FOLLOW_expression_in_list_literal1788)
                            i = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_expression.add(i.tree)
                            if list_i is None:
                                list_i = []
                            list_i.append(i.tree)



                        else:
                            break #loop38


                    RBRACKET180=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_list_literal1792) 
                    if self._state.backtracking == 0:
                        stream_RBRACKET.add(RBRACKET180)

                    # AST Rewrite
                    # elements: i
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: i
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                        stream_i = RewriteRuleSubtreeStream(self._adaptor, "token i", list_i)
                        root_0 = self._adaptor.nil()
                        # 261:60: -> ^( LIST ( $i)+ )
                        # foo_lang/parser/foo_lang.g:261:63: ^( LIST ( $i)+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LIST, "LIST"), root_1)

                        # foo_lang/parser/foo_lang.g:261:70: ( $i)+
                        if not (stream_i.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_i.hasNext():
                            self._adaptor.addChild(root_1, stream_i.nextTree())


                        stream_i.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "list_literal"

    class type_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "type"
    # foo_lang/parser/foo_lang.g:263:1: type : ( basic_type '*' -> ^( TYPE ^( MANY basic_type ) ) | basic_type -> ^( TYPE basic_type ) | tuple_type '*' -> ^( TYPE ^( MANY tuple_type ) ) | tuple_type -> ^( TYPE tuple_type ) );
    def type(self, ):

        retval = self.type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal182 = None
        char_literal185 = None
        basic_type181 = None

        basic_type183 = None

        tuple_type184 = None

        tuple_type186 = None


        char_literal182_tree = None
        char_literal185_tree = None
        stream_MULT = RewriteRuleTokenStream(self._adaptor, "token MULT")
        stream_tuple_type = RewriteRuleSubtreeStream(self._adaptor, "rule tuple_type")
        stream_basic_type = RewriteRuleSubtreeStream(self._adaptor, "rule basic_type")
        try:
            try:
                # foo_lang/parser/foo_lang.g:264:3: ( basic_type '*' -> ^( TYPE ^( MANY basic_type ) ) | basic_type -> ^( TYPE basic_type ) | tuple_type '*' -> ^( TYPE ^( MANY tuple_type ) ) | tuple_type -> ^( TYPE tuple_type ) )
                alt40 = 4
                LA40_0 = self.input.LA(1)

                if ((82 <= LA40_0 <= 86)) :
                    LA40_1 = self.input.LA(2)

                    if (self.synpred74_foo_lang()) :
                        alt40 = 1
                    elif (self.synpred75_foo_lang()) :
                        alt40 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 40, 1, self.input)

                        raise nvae

                elif (LA40_0 == LBRACKET) :
                    LA40_2 = self.input.LA(2)

                    if (self.synpred76_foo_lang()) :
                        alt40 = 3
                    elif (True) :
                        alt40 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 40, 2, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae

                if alt40 == 1:
                    # foo_lang/parser/foo_lang.g:264:5: basic_type '*'
                    pass 
                    self._state.following.append(self.FOLLOW_basic_type_in_type1812)
                    basic_type181 = self.basic_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_basic_type.add(basic_type181.tree)
                    char_literal182=self.match(self.input, MULT, self.FOLLOW_MULT_in_type1814) 
                    if self._state.backtracking == 0:
                        stream_MULT.add(char_literal182)

                    # AST Rewrite
                    # elements: basic_type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 264:20: -> ^( TYPE ^( MANY basic_type ) )
                        # foo_lang/parser/foo_lang.g:264:23: ^( TYPE ^( MANY basic_type ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE, "TYPE"), root_1)

                        # foo_lang/parser/foo_lang.g:264:30: ^( MANY basic_type )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(MANY, "MANY"), root_2)

                        self._adaptor.addChild(root_2, stream_basic_type.nextTree())

                        self._adaptor.addChild(root_1, root_2)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt40 == 2:
                    # foo_lang/parser/foo_lang.g:265:5: basic_type
                    pass 
                    self._state.following.append(self.FOLLOW_basic_type_in_type1832)
                    basic_type183 = self.basic_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_basic_type.add(basic_type183.tree)

                    # AST Rewrite
                    # elements: basic_type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 265:20: -> ^( TYPE basic_type )
                        # foo_lang/parser/foo_lang.g:265:23: ^( TYPE basic_type )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE, "TYPE"), root_1)

                        self._adaptor.addChild(root_1, stream_basic_type.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt40 == 3:
                    # foo_lang/parser/foo_lang.g:266:5: tuple_type '*'
                    pass 
                    self._state.following.append(self.FOLLOW_tuple_type_in_type1850)
                    tuple_type184 = self.tuple_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_tuple_type.add(tuple_type184.tree)
                    char_literal185=self.match(self.input, MULT, self.FOLLOW_MULT_in_type1852) 
                    if self._state.backtracking == 0:
                        stream_MULT.add(char_literal185)

                    # AST Rewrite
                    # elements: tuple_type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 266:20: -> ^( TYPE ^( MANY tuple_type ) )
                        # foo_lang/parser/foo_lang.g:266:23: ^( TYPE ^( MANY tuple_type ) )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE, "TYPE"), root_1)

                        # foo_lang/parser/foo_lang.g:266:30: ^( MANY tuple_type )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(MANY, "MANY"), root_2)

                        self._adaptor.addChild(root_2, stream_tuple_type.nextTree())

                        self._adaptor.addChild(root_1, root_2)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt40 == 4:
                    # foo_lang/parser/foo_lang.g:267:5: tuple_type
                    pass 
                    self._state.following.append(self.FOLLOW_tuple_type_in_type1870)
                    tuple_type186 = self.tuple_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_tuple_type.add(tuple_type186.tree)

                    # AST Rewrite
                    # elements: tuple_type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 267:20: -> ^( TYPE tuple_type )
                        # foo_lang/parser/foo_lang.g:267:23: ^( TYPE tuple_type )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPE, "TYPE"), root_1)

                        self._adaptor.addChild(root_1, stream_tuple_type.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "type"

    class basic_type_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "basic_type"
    # foo_lang/parser/foo_lang.g:269:1: basic_type : ( 'byte' | 'integer' | 'float' | 'boolean' | 'timestamp' );
    def basic_type(self, ):

        retval = self.basic_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set187 = None

        set187_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:269:12: ( 'byte' | 'integer' | 'float' | 'boolean' | 'timestamp' )
                # foo_lang/parser/foo_lang.g:
                pass 
                root_0 = self._adaptor.nil()

                set187 = self.input.LT(1)
                if (82 <= self.input.LA(1) <= 86):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set187))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "basic_type"

    class tuple_type_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "tuple_type"
    # foo_lang/parser/foo_lang.g:270:1: tuple_type : '[' t+= type ( COMMA t+= type )* ']' -> ^( TUPLE ( $t)+ ) ;
    def tuple_type(self, ):

        retval = self.tuple_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal188 = None
        COMMA189 = None
        char_literal190 = None
        list_t = None
        t = None

        t = None
        char_literal188_tree = None
        COMMA189_tree = None
        char_literal190_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self._adaptor, "token LBRACKET")
        stream_RBRACKET = RewriteRuleTokenStream(self._adaptor, "token RBRACKET")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        try:
            try:
                # foo_lang/parser/foo_lang.g:270:12: ( '[' t+= type ( COMMA t+= type )* ']' -> ^( TUPLE ( $t)+ ) )
                # foo_lang/parser/foo_lang.g:270:14: '[' t+= type ( COMMA t+= type )* ']'
                pass 
                char_literal188=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_tuple_type1915) 
                if self._state.backtracking == 0:
                    stream_LBRACKET.add(char_literal188)
                self._state.following.append(self.FOLLOW_type_in_tuple_type1919)
                t = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(t.tree)
                if list_t is None:
                    list_t = []
                list_t.append(t.tree)

                # foo_lang/parser/foo_lang.g:270:26: ( COMMA t+= type )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == COMMA) :
                        alt41 = 1


                    if alt41 == 1:
                        # foo_lang/parser/foo_lang.g:270:27: COMMA t+= type
                        pass 
                        COMMA189=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_tuple_type1922) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA189)
                        self._state.following.append(self.FOLLOW_type_in_tuple_type1926)
                        t = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_type.add(t.tree)
                        if list_t is None:
                            list_t = []
                        list_t.append(t.tree)



                    else:
                        break #loop41


                char_literal190=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_tuple_type1930) 
                if self._state.backtracking == 0:
                    stream_RBRACKET.add(char_literal190)

                # AST Rewrite
                # elements: t
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: t
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)

                    stream_t = RewriteRuleSubtreeStream(self._adaptor, "token t", list_t)
                    root_0 = self._adaptor.nil()
                    # 270:47: -> ^( TUPLE ( $t)+ )
                    # foo_lang/parser/foo_lang.g:270:50: ^( TUPLE ( $t)+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TUPLE, "TUPLE"), root_1)

                    # foo_lang/parser/foo_lang.g:270:58: ( $t)+
                    if not (stream_t.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_t.hasNext():
                        self._adaptor.addChild(root_1, stream_t.nextTree())


                    stream_t.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "tuple_type"

    class identifier_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "identifier"
    # foo_lang/parser/foo_lang.g:275:1: identifier : ( IDENTIFIER | 'from' | 'import' | 'with' | 'use' | 'extend' );
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set191 = None

        set191_tree = None

        try:
            try:
                # foo_lang/parser/foo_lang.g:275:11: ( IDENTIFIER | 'from' | 'import' | 'with' | 'use' | 'extend' )
                # foo_lang/parser/foo_lang.g:
                pass 
                root_0 = self._adaptor.nil()

                set191 = self.input.LT(1)
                if self.input.LA(1) == IDENTIFIER or self.input.LA(1) == 65 or (76 <= self.input.LA(1) <= 78) or self.input.LA(1) == 87:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set191))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            except RecognitionException, e:
              raise
        finally:

            pass

        return retval

    # $ANTLR end "identifier"

    # $ANTLR start "synpred1_foo_lang"
    def synpred1_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:51:9: ( instructions )
        # foo_lang/parser/foo_lang.g:51:9: instructions
        pass 
        self._state.following.append(self.FOLLOW_instructions_in_synpred1_foo_lang178)
        self.instructions()

        self._state.following.pop()


    # $ANTLR end "synpred1_foo_lang"



    # $ANTLR start "synpred29_foo_lang"
    def synpred29_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:139:5: ( 'if' LPAREN expression RPAREN statement 'else' statement )
        # foo_lang/parser/foo_lang.g:139:5: 'if' LPAREN expression RPAREN statement 'else' statement
        pass 
        self.match(self.input, 73, self.FOLLOW_73_in_synpred29_foo_lang881)
        self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_synpred29_foo_lang883)
        self._state.following.append(self.FOLLOW_expression_in_synpred29_foo_lang885)
        self.expression()

        self._state.following.pop()
        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred29_foo_lang887)
        self._state.following.append(self.FOLLOW_statement_in_synpred29_foo_lang889)
        self.statement()

        self._state.following.pop()
        self.match(self.input, 74, self.FOLLOW_74_in_synpred29_foo_lang891)
        self._state.following.append(self.FOLLOW_statement_in_synpred29_foo_lang893)
        self.statement()

        self._state.following.pop()


    # $ANTLR end "synpred29_foo_lang"



    # $ANTLR start "synpred30_foo_lang"
    def synpred30_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:146:30: ( case_clauses )
        # foo_lang/parser/foo_lang.g:146:30: case_clauses
        pass 
        self._state.following.append(self.FOLLOW_case_clauses_in_synpred30_foo_lang956)
        self.case_clauses()

        self._state.following.pop()


    # $ANTLR end "synpred30_foo_lang"



    # $ANTLR start "synpred33_foo_lang"
    def synpred33_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:165:21: ( OR and_expression )
        # foo_lang/parser/foo_lang.g:165:21: OR and_expression
        pass 
        self.match(self.input, OR, self.FOLLOW_OR_in_synpred33_foo_lang1064)
        self._state.following.append(self.FOLLOW_and_expression_in_synpred33_foo_lang1066)
        self.and_expression()

        self._state.following.pop()


    # $ANTLR end "synpred33_foo_lang"



    # $ANTLR start "synpred34_foo_lang"
    def synpred34_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:169:26: ( AND equality_expression )
        # foo_lang/parser/foo_lang.g:169:26: AND equality_expression
        pass 
        self.match(self.input, AND, self.FOLLOW_AND_in_synpred34_foo_lang1084)
        self._state.following.append(self.FOLLOW_equality_expression_in_synpred34_foo_lang1087)
        self.equality_expression()

        self._state.following.pop()


    # $ANTLR end "synpred34_foo_lang"



    # $ANTLR start "synpred36_foo_lang"
    def synpred36_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:173:23: ( ( EQUALS | NOTEQUALS ) order_expression )
        # foo_lang/parser/foo_lang.g:173:23: ( EQUALS | NOTEQUALS ) order_expression
        pass 
        if (EQUALS <= self.input.LA(1) <= NOTEQUALS):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_order_expression_in_synpred36_foo_lang1114)
        self.order_expression()

        self._state.following.pop()


    # $ANTLR end "synpred36_foo_lang"



    # $ANTLR start "synpred40_foo_lang"
    def synpred40_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:178:6: ( ( LT | LTEQ | GT | GTEQ ) additive_expression )
        # foo_lang/parser/foo_lang.g:178:6: ( LT | LTEQ | GT | GTEQ ) additive_expression
        pass 
        if (LT <= self.input.LA(1) <= GTEQ):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_additive_expression_in_synpred40_foo_lang1155)
        self.additive_expression()

        self._state.following.pop()


    # $ANTLR end "synpred40_foo_lang"



    # $ANTLR start "synpred42_foo_lang"
    def synpred42_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:183:6: ( ( PLUS | MINUS ) multiplicative_expression )
        # foo_lang/parser/foo_lang.g:183:6: ( PLUS | MINUS ) multiplicative_expression
        pass 
        if (PLUS <= self.input.LA(1) <= MINUS):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_multiplicative_expression_in_synpred42_foo_lang1188)
        self.multiplicative_expression()

        self._state.following.pop()


    # $ANTLR end "synpred42_foo_lang"



    # $ANTLR start "synpred45_foo_lang"
    def synpred45_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:187:23: ( ( MULT | DIV | MOD ) unary_expression )
        # foo_lang/parser/foo_lang.g:187:23: ( MULT | DIV | MOD ) unary_expression
        pass 
        if (MULT <= self.input.LA(1) <= MOD):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_unary_expression_in_synpred45_foo_lang1221)
        self.unary_expression()

        self._state.following.pop()


    # $ANTLR end "synpred45_foo_lang"



    # $ANTLR start "synpred46_foo_lang"
    def synpred46_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:191:5: ( NOT )
        # foo_lang/parser/foo_lang.g:191:5: NOT
        pass 
        self.match(self.input, NOT, self.FOLLOW_NOT_in_synpred46_foo_lang1236)


    # $ANTLR end "synpred46_foo_lang"



    # $ANTLR start "synpred74_foo_lang"
    def synpred74_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:264:5: ( basic_type '*' )
        # foo_lang/parser/foo_lang.g:264:5: basic_type '*'
        pass 
        self._state.following.append(self.FOLLOW_basic_type_in_synpred74_foo_lang1812)
        self.basic_type()

        self._state.following.pop()
        self.match(self.input, MULT, self.FOLLOW_MULT_in_synpred74_foo_lang1814)


    # $ANTLR end "synpred74_foo_lang"



    # $ANTLR start "synpred75_foo_lang"
    def synpred75_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:265:5: ( basic_type )
        # foo_lang/parser/foo_lang.g:265:5: basic_type
        pass 
        self._state.following.append(self.FOLLOW_basic_type_in_synpred75_foo_lang1832)
        self.basic_type()

        self._state.following.pop()


    # $ANTLR end "synpred75_foo_lang"



    # $ANTLR start "synpred76_foo_lang"
    def synpred76_foo_lang_fragment(self, ):
        # foo_lang/parser/foo_lang.g:266:5: ( tuple_type '*' )
        # foo_lang/parser/foo_lang.g:266:5: tuple_type '*'
        pass 
        self._state.following.append(self.FOLLOW_tuple_type_in_synpred76_foo_lang1850)
        self.tuple_type()

        self._state.following.pop()
        self.match(self.input, MULT, self.FOLLOW_MULT_in_synpred76_foo_lang1852)


    # $ANTLR end "synpred76_foo_lang"




    # Delegated rules

    def synpred42_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred42_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred76_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred76_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred36_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred36_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred30_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred30_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred75_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred75_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred40_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred40_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred1_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred46_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred46_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred74_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred74_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred33_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred33_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred45_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred45_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred29_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred29_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred34_foo_lang(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred34_foo_lang_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #13

    DFA13_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA13_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA13_min = DFA.unpack(
        u"\1\50\1\uffff\1\40\4\uffff\1\75\2\uffff\1\40\1\75"
        )

    DFA13_max = DFA.unpack(
        u"\1\127\1\uffff\1\110\4\uffff\1\127\2\uffff\1\110\1\127"
        )

    DFA13_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\4\1\5\1\7\1\3\1\uffff\1\6\1\2\2\uffff"
        )

    DFA13_special = DFA.unpack(
        u"\14\uffff"
        )

            
    DFA13_transition = [
        DFA.unpack(u"\1\1\24\uffff\1\2\3\uffff\1\2\5\uffff\1\5\1\uffff\1"
        u"\3\1\uffff\1\4\3\2\10\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\1\uffff\1\11\2\uffff\1\10\4\uffff\2\11\34\uffff"
        u"\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\3\uffff\1\12\12\uffff\3\12\10\uffff\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\13\1\uffff\1\11\2\uffff\1\10\4\uffff\2\11\34\uffff"
        u"\1\6"),
        DFA.unpack(u"\1\12\3\uffff\1\12\12\uffff\3\12\10\uffff\1\12")
    ]

    # class definition for DFA #13

    DFA13 = DFA
    # lookup tables for DFA #27

    DFA27_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA27_eof = DFA.unpack(
        u"\3\uffff\1\10\5\uffff\1\10\1\uffff"
        )

    DFA27_min = DFA.unpack(
        u"\1\43\2\uffff\1\40\2\uffff\1\75\2\uffff\1\40\1\75"
        )

    DFA27_max = DFA.unpack(
        u"\1\127\2\uffff\1\127\2\uffff\1\127\2\uffff\2\127"
        )

    DFA27_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\uffff\1\5\1\6\1\uffff\1\3\1\4\2\uffff"
        )

    DFA27_special = DFA.unpack(
        u"\13\uffff"
        )

            
    DFA27_transition = [
        DFA.unpack(u"\2\2\1\1\2\uffff\1\2\5\uffff\6\5\5\uffff\2\5\1\2\1\uffff"
        u"\1\3\3\uffff\1\3\12\uffff\3\3\2\2\1\4\5\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\4\uffff\1\7\4\10\2\uffff\15\10\3\uffff\2\10\3"
        u"\uffff\1\10\5\uffff\1\10\1\uffff\6\10\10\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11\3\uffff\1\11\12\uffff\3\11\10\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\4\uffff\1\7\4\10\2\uffff\15\10\3\uffff\2\10\3"
        u"\uffff\1\10\5\uffff\1\10\1\uffff\6\10\10\uffff\1\10"),
        DFA.unpack(u"\1\11\3\uffff\1\11\12\uffff\3\11\10\uffff\1\11")
    ]

    # class definition for DFA #27

    DFA27 = DFA
 

    FOLLOW_instructions_in_start178 = frozenset([])
    FOLLOW_EOF_in_start181 = frozenset([1])
    FOLLOW_instruction_in_instructions198 = frozenset([1, 64, 67, 68, 69, 70, 76, 78])
    FOLLOW_declaration_in_instruction209 = frozenset([1])
    FOLLOW_directive_in_instruction215 = frozenset([1])
    FOLLOW_extension_in_instruction221 = frozenset([1])
    FOLLOW_annotated_declaration_in_declaration236 = frozenset([1])
    FOLLOW_constant_declaration_in_declaration242 = frozenset([1])
    FOLLOW_event_handler_declaration_in_declaration248 = frozenset([1])
    FOLLOW_function_declaration_in_declaration254 = frozenset([1])
    FOLLOW_annotation_in_annotated_declaration267 = frozenset([65])
    FOLLOW_apply_declaration_in_annotated_declaration269 = frozenset([1])
    FOLLOW_64_in_annotation292 = frozenset([61, 65, 76, 77, 78, 87])
    FOLLOW_function_call_expression_in_annotation294 = frozenset([1])
    FOLLOW_65_in_apply_declaration315 = frozenset([61, 65, 76, 77, 78, 87])
    FOLLOW_identifier_in_apply_declaration317 = frozenset([32])
    FOLLOW_DOT_in_apply_declaration319 = frozenset([61, 65, 76, 77, 78, 87])
    FOLLOW_identifier_in_apply_declaration321 = frozenset([66])
    FOLLOW_66_in_apply_declaration323 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_function_expression_in_apply_declaration325 = frozenset([1])
    FOLLOW_65_in_apply_declaration351 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_apply_declaration353 = frozenset([66])
    FOLLOW_66_in_apply_declaration355 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_function_expression_in_apply_declaration357 = frozenset([1])
    FOLLOW_67_in_constant_declaration387 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_typed_value_in_constant_declaration389 = frozenset([1])
    FOLLOW_identifier_in_typed_value408 = frozenset([33])
    FOLLOW_COLON_in_typed_value410 = frozenset([59, 82, 83, 84, 85, 86])
    FOLLOW_type_in_typed_value412 = frozenset([34])
    FOLLOW_ASSIGN_in_typed_value414 = frozenset([35, 36, 40, 59, 79, 80])
    FOLLOW_literal_in_typed_value416 = frozenset([1])
    FOLLOW_identifier_in_typed_value438 = frozenset([34])
    FOLLOW_ASSIGN_in_typed_value440 = frozenset([35])
    FOLLOW_FLOAT_in_typed_value442 = frozenset([1])
    FOLLOW_identifier_in_typed_value469 = frozenset([34])
    FOLLOW_ASSIGN_in_typed_value471 = frozenset([36])
    FOLLOW_INTEGER_in_typed_value473 = frozenset([1])
    FOLLOW_identifier_in_typed_value500 = frozenset([34])
    FOLLOW_ASSIGN_in_typed_value502 = frozenset([79, 80])
    FOLLOW_boolean_literal_in_typed_value504 = frozenset([1])
    FOLLOW_event_timing_in_event_handler_declaration538 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_event_handler_declaration540 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_event_handler_declaration542 = frozenset([66])
    FOLLOW_66_in_event_handler_declaration544 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_function_expression_in_event_handler_declaration546 = frozenset([1])
    FOLLOW_set_in_event_timing0 = frozenset([1])
    FOLLOW_70_in_function_declaration588 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_function_declaration590 = frozenset([37])
    FOLLOW_LPAREN_in_function_declaration592 = frozenset([38, 61, 65, 70, 76, 77, 78, 87])
    FOLLOW_function_param_list_in_function_declaration595 = frozenset([38])
    FOLLOW_RPAREN_in_function_declaration599 = frozenset([40])
    FOLLOW_function_body_in_function_declaration601 = frozenset([1])
    FOLLOW_70_in_function_expression631 = frozenset([37, 61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_function_expression633 = frozenset([37])
    FOLLOW_LPAREN_in_function_expression636 = frozenset([38, 61, 65, 70, 76, 77, 78, 87])
    FOLLOW_function_param_list_in_function_expression639 = frozenset([38])
    FOLLOW_RPAREN_in_function_expression643 = frozenset([40])
    FOLLOW_function_body_in_function_expression645 = frozenset([1])
    FOLLOW_identifier_in_function_expression670 = frozenset([1])
    FOLLOW_identifier_in_function_param_list681 = frozenset([1, 39])
    FOLLOW_COMMA_in_function_param_list684 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_function_param_list688 = frozenset([1, 39])
    FOLLOW_block_statement_in_function_body706 = frozenset([1])
    FOLLOW_statement_in_statements714 = frozenset([1, 40, 61, 65, 70, 71, 73, 75, 76, 77, 78, 87])
    FOLLOW_block_statement_in_statement725 = frozenset([1])
    FOLLOW_assignment_statement_in_statement731 = frozenset([1])
    FOLLOW_increment_statement_in_statement737 = frozenset([1])
    FOLLOW_if_statement_in_statement743 = frozenset([1])
    FOLLOW_case_statement_in_statement749 = frozenset([1])
    FOLLOW_call_expression_in_statement755 = frozenset([1])
    FOLLOW_71_in_statement761 = frozenset([1])
    FOLLOW_LBRACE_in_block_statement774 = frozenset([41])
    FOLLOW_RBRACE_in_block_statement776 = frozenset([1])
    FOLLOW_LBRACE_in_block_statement799 = frozenset([40, 41, 61, 65, 70, 71, 73, 75, 76, 77, 78, 87])
    FOLLOW_statement_in_block_statement801 = frozenset([40, 41, 61, 65, 70, 71, 73, 75, 76, 77, 78, 87])
    FOLLOW_RBRACE_in_block_statement804 = frozenset([1])
    FOLLOW_variable_in_assignment_statement823 = frozenset([34, 42, 43])
    FOLLOW_set_in_assignment_statement825 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_expression_in_assignment_statement834 = frozenset([1])
    FOLLOW_variable_in_increment_statement847 = frozenset([72])
    FOLLOW_72_in_increment_statement849 = frozenset([1])
    FOLLOW_73_in_if_statement881 = frozenset([37])
    FOLLOW_LPAREN_in_if_statement883 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_expression_in_if_statement885 = frozenset([38])
    FOLLOW_RPAREN_in_if_statement887 = frozenset([40, 61, 65, 70, 71, 73, 74, 75, 76, 77, 78, 87])
    FOLLOW_statement_in_if_statement889 = frozenset([74])
    FOLLOW_74_in_if_statement891 = frozenset([40, 61, 65, 70, 71, 73, 75, 76, 77, 78, 87])
    FOLLOW_statement_in_if_statement893 = frozenset([1])
    FOLLOW_73_in_if_statement915 = frozenset([37])
    FOLLOW_LPAREN_in_if_statement917 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_expression_in_if_statement919 = frozenset([38])
    FOLLOW_RPAREN_in_if_statement921 = frozenset([40, 61, 65, 70, 71, 73, 75, 76, 77, 78, 87])
    FOLLOW_statement_in_if_statement923 = frozenset([1])
    FOLLOW_75_in_case_statement950 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_expression_in_case_statement952 = frozenset([40])
    FOLLOW_LBRACE_in_case_statement954 = frozenset([41, 61, 65, 70, 74, 76, 77, 78, 87])
    FOLLOW_case_clauses_in_case_statement956 = frozenset([41, 74])
    FOLLOW_else_clause_in_case_statement959 = frozenset([41])
    FOLLOW_RBRACE_in_case_statement962 = frozenset([1])
    FOLLOW_case_clause_in_case_clauses987 = frozenset([1, 61, 65, 70, 76, 77, 78, 87])
    FOLLOW_function_call_expression_in_case_clause997 = frozenset([40])
    FOLLOW_block_statement_in_case_clause999 = frozenset([1])
    FOLLOW_74_in_else_clause1022 = frozenset([40, 61, 65, 70, 71, 73, 75, 76, 77, 78, 87])
    FOLLOW_statement_in_else_clause1024 = frozenset([1])
    FOLLOW_logical_expression_in_expression1041 = frozenset([1])
    FOLLOW_or_expression_in_logical_expression1051 = frozenset([1])
    FOLLOW_and_expression_in_or_expression1061 = frozenset([1, 44])
    FOLLOW_OR_in_or_expression1064 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_and_expression_in_or_expression1066 = frozenset([1, 44])
    FOLLOW_equality_expression_in_and_expression1081 = frozenset([1, 45])
    FOLLOW_AND_in_and_expression1084 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_equality_expression_in_and_expression1087 = frozenset([1, 45])
    FOLLOW_order_expression_in_equality_expression1102 = frozenset([1, 46, 47])
    FOLLOW_set_in_equality_expression1105 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_order_expression_in_equality_expression1114 = frozenset([1, 46, 47])
    FOLLOW_additive_expression_in_order_expression1131 = frozenset([1, 48, 49, 50, 51])
    FOLLOW_set_in_order_expression1138 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_additive_expression_in_order_expression1155 = frozenset([1, 48, 49, 50, 51])
    FOLLOW_multiplicative_expression_in_additive_expression1172 = frozenset([1, 52, 53])
    FOLLOW_set_in_additive_expression1179 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_multiplicative_expression_in_additive_expression1188 = frozenset([1, 52, 53])
    FOLLOW_unary_expression_in_multiplicative_expression1203 = frozenset([1, 54, 55, 56])
    FOLLOW_set_in_multiplicative_expression1206 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_unary_expression_in_multiplicative_expression1221 = frozenset([1, 54, 55, 56])
    FOLLOW_NOT_in_unary_expression1236 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_primary_expression_in_unary_expression1240 = frozenset([1])
    FOLLOW_LPAREN_in_primary_expression1253 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_logical_expression_in_primary_expression1256 = frozenset([38])
    FOLLOW_RPAREN_in_primary_expression1258 = frozenset([1])
    FOLLOW_literal_in_primary_expression1265 = frozenset([1])
    FOLLOW_call_expression_in_primary_expression1271 = frozenset([1])
    FOLLOW_variable_in_primary_expression1277 = frozenset([1])
    FOLLOW_atom_in_primary_expression1283 = frozenset([1])
    FOLLOW_matching_expression_in_primary_expression1289 = frozenset([1])
    FOLLOW_method_call_expression_in_call_expression1302 = frozenset([1])
    FOLLOW_function_call_expression_in_call_expression1318 = frozenset([1])
    FOLLOW_identifier_in_method_call_expression1338 = frozenset([32])
    FOLLOW_DOT_in_method_call_expression1340 = frozenset([32, 61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_method_call_expression1344 = frozenset([32])
    FOLLOW_DOT_in_method_call_expression1346 = frozenset([32, 61, 65, 70, 76, 77, 78, 87])
    FOLLOW_function_call_expression_in_method_call_expression1351 = frozenset([1])
    FOLLOW_identifier_in_function_call_expression1357 = frozenset([37])
    FOLLOW_LPAREN_in_function_call_expression1359 = frozenset([35, 36, 37, 38, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_argument_list_in_function_call_expression1363 = frozenset([38])
    FOLLOW_RPAREN_in_function_call_expression1367 = frozenset([1])
    FOLLOW_expression_in_argument_list1376 = frozenset([1, 39])
    FOLLOW_COMMA_in_argument_list1379 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_expression_in_argument_list1383 = frozenset([1, 39])
    FOLLOW_property_expression_in_variable1407 = frozenset([1])
    FOLLOW_identifier_in_variable1413 = frozenset([1])
    FOLLOW_identifier_in_property_expression1446 = frozenset([32])
    FOLLOW_DOT_in_property_expression1448 = frozenset([32, 61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_property_expression1453 = frozenset([32])
    FOLLOW_DOT_in_property_expression1455 = frozenset([32, 61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_property_expression1461 = frozenset([1])
    FOLLOW_import_directive_in_directive1493 = frozenset([1])
    FOLLOW_76_in_import_directive1501 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_import_directive1503 = frozenset([77])
    FOLLOW_77_in_import_directive1505 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_import_directive1507 = frozenset([1])
    FOLLOW_78_in_extension1546 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_extension1548 = frozenset([65])
    FOLLOW_65_in_extension1550 = frozenset([35, 36, 40, 59, 79, 80])
    FOLLOW_literal_in_extension1552 = frozenset([1])
    FOLLOW_numeric_literal_in_literal1583 = frozenset([1])
    FOLLOW_boolean_literal_in_literal1587 = frozenset([1])
    FOLLOW_object_literal_in_literal1591 = frozenset([1])
    FOLLOW_list_literal_in_literal1595 = frozenset([1])
    FOLLOW_set_in_boolean_literal0 = frozenset([1])
    FOLLOW_set_in_numeric_literal0 = frozenset([1])
    FOLLOW_LBRACE_in_object_literal1621 = frozenset([41, 61, 65, 70, 76, 77, 78, 87])
    FOLLOW_property_type_value_list_in_object_literal1624 = frozenset([41])
    FOLLOW_RBRACE_in_object_literal1628 = frozenset([1])
    FOLLOW_property_type_value_in_property_type_value_list1659 = frozenset([1, 61, 65, 70, 76, 77, 78, 87])
    FOLLOW_property_type_value_in_property_type_value_list1662 = frozenset([1, 61, 65, 70, 76, 77, 78, 87])
    FOLLOW_typed_value_in_property_type_value1670 = frozenset([1])
    FOLLOW_81_in_atom1686 = frozenset([61, 65, 70, 76, 77, 78, 87])
    FOLLOW_identifier_in_atom1688 = frozenset([1])
    FOLLOW_dontcare_in_matching_expression1703 = frozenset([1])
    FOLLOW_comparison_in_matching_expression1707 = frozenset([1])
    FOLLOW_UNDERSCORE_in_dontcare1713 = frozenset([1])
    FOLLOW_comparator_in_comparison1719 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_expression_in_comparison1722 = frozenset([1])
    FOLLOW_set_in_comparator0 = frozenset([1])
    FOLLOW_LBRACKET_in_list_literal1763 = frozenset([60])
    FOLLOW_RBRACKET_in_list_literal1765 = frozenset([1])
    FOLLOW_LBRACKET_in_list_literal1777 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_expression_in_list_literal1781 = frozenset([39, 60])
    FOLLOW_COMMA_in_list_literal1784 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_expression_in_list_literal1788 = frozenset([39, 60])
    FOLLOW_RBRACKET_in_list_literal1792 = frozenset([1])
    FOLLOW_basic_type_in_type1812 = frozenset([54])
    FOLLOW_MULT_in_type1814 = frozenset([1])
    FOLLOW_basic_type_in_type1832 = frozenset([1])
    FOLLOW_tuple_type_in_type1850 = frozenset([54])
    FOLLOW_MULT_in_type1852 = frozenset([1])
    FOLLOW_tuple_type_in_type1870 = frozenset([1])
    FOLLOW_set_in_basic_type0 = frozenset([1])
    FOLLOW_LBRACKET_in_tuple_type1915 = frozenset([59, 82, 83, 84, 85, 86])
    FOLLOW_type_in_tuple_type1919 = frozenset([39, 60])
    FOLLOW_COMMA_in_tuple_type1922 = frozenset([59, 82, 83, 84, 85, 86])
    FOLLOW_type_in_tuple_type1926 = frozenset([39, 60])
    FOLLOW_RBRACKET_in_tuple_type1930 = frozenset([1])
    FOLLOW_set_in_identifier0 = frozenset([1])
    FOLLOW_instructions_in_synpred1_foo_lang178 = frozenset([1])
    FOLLOW_73_in_synpred29_foo_lang881 = frozenset([37])
    FOLLOW_LPAREN_in_synpred29_foo_lang883 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_expression_in_synpred29_foo_lang885 = frozenset([38])
    FOLLOW_RPAREN_in_synpred29_foo_lang887 = frozenset([40, 61, 65, 70, 71, 73, 74, 75, 76, 77, 78, 87])
    FOLLOW_statement_in_synpred29_foo_lang889 = frozenset([74])
    FOLLOW_74_in_synpred29_foo_lang891 = frozenset([40, 61, 65, 70, 71, 73, 75, 76, 77, 78, 87])
    FOLLOW_statement_in_synpred29_foo_lang893 = frozenset([1])
    FOLLOW_case_clauses_in_synpred30_foo_lang956 = frozenset([1])
    FOLLOW_OR_in_synpred33_foo_lang1064 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_and_expression_in_synpred33_foo_lang1066 = frozenset([1])
    FOLLOW_AND_in_synpred34_foo_lang1084 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_equality_expression_in_synpred34_foo_lang1087 = frozenset([1])
    FOLLOW_set_in_synpred36_foo_lang1105 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_order_expression_in_synpred36_foo_lang1114 = frozenset([1])
    FOLLOW_set_in_synpred40_foo_lang1138 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_additive_expression_in_synpred40_foo_lang1155 = frozenset([1])
    FOLLOW_set_in_synpred42_foo_lang1179 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_multiplicative_expression_in_synpred42_foo_lang1188 = frozenset([1])
    FOLLOW_set_in_synpred45_foo_lang1206 = frozenset([35, 36, 37, 40, 46, 47, 48, 49, 50, 51, 57, 58, 59, 61, 65, 70, 76, 77, 78, 79, 80, 81, 87])
    FOLLOW_unary_expression_in_synpred45_foo_lang1221 = frozenset([1])
    FOLLOW_NOT_in_synpred46_foo_lang1236 = frozenset([1])
    FOLLOW_basic_type_in_synpred74_foo_lang1812 = frozenset([54])
    FOLLOW_MULT_in_synpred74_foo_lang1814 = frozenset([1])
    FOLLOW_basic_type_in_synpred75_foo_lang1832 = frozenset([1])
    FOLLOW_tuple_type_in_synpred76_foo_lang1850 = frozenset([54])
    FOLLOW_MULT_in_synpred76_foo_lang1852 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("foo_langLexer", foo_langParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
