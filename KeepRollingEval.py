from math import prod

import numpy as np

from KeepRollingVisitor import KeepRollingVisitor
from KeepRollingLexer import KeepRollingLexer


class KeepRollingEval(KeepRollingVisitor):

    def visitNum_int(self, ctx):
        return int(ctx.getText())

    def visitRed_op(self, ctx):
        return ctx.children[0].symbol.type

    def visitNum_reduction(self, ctx):
        assert (len(ctx.children) == 3)
        lst = self.visit(ctx.lst())
        op = self.visit(ctx.red_op())
        if op == KeepRollingLexer.OP_ADD:
            return sum(lst)
        elif op == KeepRollingLexer.OP_MUL:
            return prod(lst)
        elif op == KeepRollingLexer.OP_LES:
            return min(lst)
        elif op == KeepRollingLexer.OP_GRE:
            return max(lst)

    def visitLst_lst(self, ctx):
        int_list = []
        for child in ctx.children:
            if child.symbol.type == KeepRollingLexer.INT:
                int_list.append(int(child.symbol.text))
        return int_list

    def visitLst_roll(self, ctx):
        assert (len(ctx.children) == 3)
        count = int(ctx.children[0].getText())
        dice = int(ctx.children[2].getText())
        return list(np.random.randint(1, dice, count))

    def visitMap_op(self, ctx):
        return ctx.children[0].symbol.type

    def visitLst_map(self, ctx):
        assert (len(ctx.children) == 3)
        lst = self.visit(ctx.lst())
        op = self.visit(ctx.map_op())
        num = self.visit(ctx.num())
        if op == KeepRollingLexer.OP_ADD:
            return list(map(lambda x: x + num, lst))
        elif op == KeepRollingLexer.OP_SUB:
            return list(map(lambda x: x - num, lst))
        elif op == KeepRollingLexer.OP_MUL:
            return list(map(lambda x: x * num, lst))
        elif op == KeepRollingLexer.OP_DIV:
            return list(map(lambda x: x // num, lst))
        elif op == KeepRollingLexer.OP_LES:
            return list(map(lambda x: int(x < num), lst))
        elif op == KeepRollingLexer.OP_GRE:
            return list(map(lambda x: int(x > num), lst))
        elif op == KeepRollingLexer.OP_EQL:
            return list(map(lambda x: int(x == num), lst))
