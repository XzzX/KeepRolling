# Generated from KeepRolling.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .KeepRollingParser import KeepRollingParser
else:
    from KeepRollingParser import KeepRollingParser

# This class defines a complete generic visitor for a parse tree produced by KeepRollingParser.

class KeepRollingVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by KeepRollingParser#prog.
    def visitProg(self, ctx:KeepRollingParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KeepRollingParser#expr.
    def visitExpr(self, ctx:KeepRollingParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KeepRollingParser#num_int.
    def visitNum_int(self, ctx:KeepRollingParser.Num_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KeepRollingParser#num_reduction.
    def visitNum_reduction(self, ctx:KeepRollingParser.Num_reductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KeepRollingParser#lst_roll.
    def visitLst_roll(self, ctx:KeepRollingParser.Lst_rollContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KeepRollingParser#lst_lst.
    def visitLst_lst(self, ctx:KeepRollingParser.Lst_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KeepRollingParser#lst_map.
    def visitLst_map(self, ctx:KeepRollingParser.Lst_mapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KeepRollingParser#red_op.
    def visitRed_op(self, ctx:KeepRollingParser.Red_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KeepRollingParser#map_op.
    def visitMap_op(self, ctx:KeepRollingParser.Map_opContext):
        return self.visitChildren(ctx)



del KeepRollingParser