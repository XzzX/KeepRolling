from KeepRollingVisitor import KeepRollingVisitor
from KeepRollingParser import KeepRollingParser
from KeepRollingLexer import KeepRollingLexer

import numpy as np


class KeepRollingEval(KeepRollingVisitor):
    def visitPrint_expr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitExpr_datum(self, ctx):
        return self.visit(ctx.datum())

    def visitDatum_int(self, ctx):
        return int(ctx.getText())

    def visitDatum_list(self, ctx):
        return self.visit(ctx.int_list())

    def visitInt_list(self, ctx):
        int_list = []
        for child in ctx.children:
            if (child.symbol.type == KeepRollingLexer.INT):
                int_list.append(int(child.symbol.text))
        return int_list

    def visitDatum_roll(self, ctx):
        return self.visit(ctx.roll())

    def visitRoll(self, ctx):
        assert(len(ctx.children) == 3)
        count = int(ctx.children[0].getText())
        dice = int(ctx.children[2].getText())
        return list(np.random.random_integers(1, dice, count))

    def visitExpr_reduction(self, ctx):
        datum = self.visit(ctx.datum())
        op = ctx.children[2].symbol.type
        if op == KeepRollingLexer.OP_PLUS:
            return sum(datum)
        elif op == KeepRollingLexer.OP_LESS:
            return min(datum)
        elif op == KeepRollingLexer.OP_GREATER:
            return max(datum)