# Generated from KeepRolling.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\3\3\3\5\3\23\n\3\3\4\3\4\3\4\3\4\3\4\5\4\32\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\7\5!\n\5\f\5\16\5$\13\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5*\n\5\3\5\3\5\3\5\3\5\7\5\60\n\5\f\5\16\5\63")
        buf.write("\13\5\3\6\3\6\3\7\3\7\3\7\2\3\b\b\2\4\6\b\n\f\2\4\4\2")
        buf.write("\7\7\n\f\3\2\7\r\2\67\2\16\3\2\2\2\4\22\3\2\2\2\6\31\3")
        buf.write("\2\2\2\b)\3\2\2\2\n\64\3\2\2\2\f\66\3\2\2\2\16\17\5\4")
        buf.write("\3\2\17\3\3\2\2\2\20\23\5\6\4\2\21\23\5\b\5\2\22\20\3")
        buf.write("\2\2\2\22\21\3\2\2\2\23\5\3\2\2\2\24\32\7\17\2\2\25\26")
        buf.write("\5\b\5\2\26\27\7\3\2\2\27\30\5\n\6\2\30\32\3\2\2\2\31")
        buf.write("\24\3\2\2\2\31\25\3\2\2\2\32\7\3\2\2\2\33\34\b\5\1\2\34")
        buf.write("\35\7\4\2\2\35\"\7\17\2\2\36\37\7\5\2\2\37!\7\17\2\2 ")
        buf.write("\36\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2")
        buf.write("$\"\3\2\2\2%*\7\6\2\2&\'\7\17\2\2\'(\7\16\2\2(*\7\17\2")
        buf.write("\2)\33\3\2\2\2)&\3\2\2\2*\61\3\2\2\2+,\f\3\2\2,-\5\f\7")
        buf.write("\2-.\5\6\4\2.\60\3\2\2\2/+\3\2\2\2\60\63\3\2\2\2\61/\3")
        buf.write("\2\2\2\61\62\3\2\2\2\62\t\3\2\2\2\63\61\3\2\2\2\64\65")
        buf.write("\t\2\2\2\65\13\3\2\2\2\66\67\t\3\2\2\67\r\3\2\2\2\7\22")
        buf.write("\31\")\61")
        return buf.getvalue()


class KeepRollingParser ( Parser ):

    grammarFileName = "KeepRolling.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "'['", "','", "']'", "'+'", "'-'", 
                     "'/'", "'*'", "'>'", "'<'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "OP_ADD", "OP_SUB", "OP_DIV", "OP_MUL", 
                      "OP_GRE", "OP_LES", "OP_EQL", "DICE", "INT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_num = 2
    RULE_lst = 3
    RULE_red_op = 4
    RULE_map_op = 5

    ruleNames =  [ "prog", "expr", "num", "lst", "red_op", "map_op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    OP_ADD=5
    OP_SUB=6
    OP_DIV=7
    OP_MUL=8
    OP_GRE=9
    OP_LES=10
    OP_EQL=11
    DICE=12
    INT=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(KeepRollingParser.ExprContext,0)


        def getRuleIndex(self):
            return KeepRollingParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = KeepRollingParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(KeepRollingParser.NumContext,0)


        def lst(self):
            return self.getTypedRuleContext(KeepRollingParser.LstContext,0)


        def getRuleIndex(self):
            return KeepRollingParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = KeepRollingParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 16
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.lst(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KeepRollingParser.RULE_num

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Num_reductionContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KeepRollingParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lst(self):
            return self.getTypedRuleContext(KeepRollingParser.LstContext,0)

        def red_op(self):
            return self.getTypedRuleContext(KeepRollingParser.Red_opContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_reduction" ):
                return visitor.visitNum_reduction(self)
            else:
                return visitor.visitChildren(self)


    class Num_intContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KeepRollingParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(KeepRollingParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_int" ):
                return visitor.visitNum_int(self)
            else:
                return visitor.visitChildren(self)



    def num(self):

        localctx = KeepRollingParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_num)
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = KeepRollingParser.Num_intContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(KeepRollingParser.INT)
                pass

            elif la_ == 2:
                localctx = KeepRollingParser.Num_reductionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.lst(0)
                self.state = 20
                self.match(KeepRollingParser.T__0)
                self.state = 21
                self.red_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return KeepRollingParser.RULE_lst

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Lst_rollContext(LstContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KeepRollingParser.LstContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(KeepRollingParser.INT)
            else:
                return self.getToken(KeepRollingParser.INT, i)
        def DICE(self):
            return self.getToken(KeepRollingParser.DICE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLst_roll" ):
                return visitor.visitLst_roll(self)
            else:
                return visitor.visitChildren(self)


    class Lst_lstContext(LstContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KeepRollingParser.LstContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(KeepRollingParser.INT)
            else:
                return self.getToken(KeepRollingParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLst_lst" ):
                return visitor.visitLst_lst(self)
            else:
                return visitor.visitChildren(self)


    class Lst_mapContext(LstContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a KeepRollingParser.LstContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lst(self):
            return self.getTypedRuleContext(KeepRollingParser.LstContext,0)

        def map_op(self):
            return self.getTypedRuleContext(KeepRollingParser.Map_opContext,0)

        def num(self):
            return self.getTypedRuleContext(KeepRollingParser.NumContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLst_map" ):
                return visitor.visitLst_map(self)
            else:
                return visitor.visitChildren(self)



    def lst(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KeepRollingParser.LstContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_lst, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [KeepRollingParser.T__1]:
                localctx = KeepRollingParser.Lst_lstContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 26
                self.match(KeepRollingParser.T__1)
                self.state = 27
                self.match(KeepRollingParser.INT)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==KeepRollingParser.T__2:
                    self.state = 28
                    self.match(KeepRollingParser.T__2)
                    self.state = 29
                    self.match(KeepRollingParser.INT)
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 35
                self.match(KeepRollingParser.T__3)
                pass
            elif token in [KeepRollingParser.INT]:
                localctx = KeepRollingParser.Lst_rollContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(KeepRollingParser.INT)
                self.state = 37
                self.match(KeepRollingParser.DICE)
                self.state = 38
                self.match(KeepRollingParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KeepRollingParser.Lst_mapContext(self, KeepRollingParser.LstContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lst)
                    self.state = 41
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 42
                    self.map_op()
                    self.state = 43
                    self.num() 
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Red_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ADD(self):
            return self.getToken(KeepRollingParser.OP_ADD, 0)

        def OP_MUL(self):
            return self.getToken(KeepRollingParser.OP_MUL, 0)

        def OP_GRE(self):
            return self.getToken(KeepRollingParser.OP_GRE, 0)

        def OP_LES(self):
            return self.getToken(KeepRollingParser.OP_LES, 0)

        def getRuleIndex(self):
            return KeepRollingParser.RULE_red_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRed_op" ):
                return visitor.visitRed_op(self)
            else:
                return visitor.visitChildren(self)




    def red_op(self):

        localctx = KeepRollingParser.Red_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_red_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << KeepRollingParser.OP_ADD) | (1 << KeepRollingParser.OP_MUL) | (1 << KeepRollingParser.OP_GRE) | (1 << KeepRollingParser.OP_LES))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Map_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ADD(self):
            return self.getToken(KeepRollingParser.OP_ADD, 0)

        def OP_SUB(self):
            return self.getToken(KeepRollingParser.OP_SUB, 0)

        def OP_MUL(self):
            return self.getToken(KeepRollingParser.OP_MUL, 0)

        def OP_DIV(self):
            return self.getToken(KeepRollingParser.OP_DIV, 0)

        def OP_GRE(self):
            return self.getToken(KeepRollingParser.OP_GRE, 0)

        def OP_LES(self):
            return self.getToken(KeepRollingParser.OP_LES, 0)

        def OP_EQL(self):
            return self.getToken(KeepRollingParser.OP_EQL, 0)

        def getRuleIndex(self):
            return KeepRollingParser.RULE_map_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap_op" ):
                return visitor.visitMap_op(self)
            else:
                return visitor.visitChildren(self)




    def map_op(self):

        localctx = KeepRollingParser.Map_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_map_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << KeepRollingParser.OP_ADD) | (1 << KeepRollingParser.OP_SUB) | (1 << KeepRollingParser.OP_DIV) | (1 << KeepRollingParser.OP_MUL) | (1 << KeepRollingParser.OP_GRE) | (1 << KeepRollingParser.OP_LES) | (1 << KeepRollingParser.OP_EQL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.lst_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def lst_sempred(self, localctx:LstContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




