import unittest
from antlr4 import *
from antlr4.InputStream import InputStream
from KeepRollingLexer import KeepRollingLexer
from KeepRollingParser import KeepRollingParser
from KeepRollingEval import KeepRollingEval


class TestParser(unittest.TestCase):

    def interpret(self, cmd):
        self.lexer = KeepRollingLexer(InputStream(cmd))
        self.token_stream = CommonTokenStream(self.lexer)
        self.parser = KeepRollingParser(self.token_stream)
        self.tree = self.parser.prog()
        visitor = KeepRollingEval()
        return visitor.visit(self.tree)

    def test_num(self):
        res = self.interpret("345")
        self.assertIs(type(res), int)
        self.assertEqual(res, 345)

    def test_lst(self):
        res = self.interpret("[3,4,5]")
        self.assertIs(type(res), list)
        self.assertSequenceEqual(res, [3, 4, 5])

        res = self.interpret("100w6")
        self.assertIs(type(res), list)
        self.assertEqual(len(res), 100)
        for num in res:
            self.assertLess(num, 7)
            self.assertGreater(num, 0)

        res = self.interpret("100W6")
        self.assertIs(type(res), list)
        self.assertEqual(len(res), 100)
        for num in res:
            self.assertLess(num, 7)
            self.assertGreater(num, 0)

        res = self.interpret("100d6")
        self.assertIs(type(res), list)
        self.assertEqual(len(res), 100)
        for num in res:
            self.assertLess(num, 7)
            self.assertGreater(num, 0)

        res = self.interpret("100D6")
        self.assertIs(type(res), list)
        self.assertEqual(len(res), 100)
        for num in res:
            self.assertLess(num, 7)
            self.assertGreater(num, 0)

    def test_reduction(self):
        res = self.interpret("[1,2,3]!+")
        self.assertIs(type(res), int)
        self.assertEqual(res, 6)

        res = self.interpret("[2,2,3]!*")
        self.assertIs(type(res), int)
        self.assertEqual(res, 12)

        res = self.interpret("[7,2,3]!<")
        self.assertIs(type(res), int)
        self.assertEqual(res, 2)

        res = self.interpret("[1,6,3]!>")
        self.assertIs(type(res), int)
        self.assertEqual(res, 6)

    def test_map(self):
        res = self.interpret("[1,2,3]+3")
        self.assertIs(type(res), list)
        self.assertSequenceEqual(res, [4, 5, 6])

        res = self.interpret("[1,2,3]-3")
        self.assertIs(type(res), list)
        self.assertSequenceEqual(res, [-2, -1, 0])

        res = self.interpret("[1,2,3]*3")
        self.assertIs(type(res), list)
        self.assertSequenceEqual(res, [3, 6, 9])

        res = self.interpret("[1,2,3]/3")
        self.assertIs(type(res), list)
        self.assertSequenceEqual(res, [0, 0, 1])

        res = self.interpret("[1,2,3,4,5]>2")
        self.assertIs(type(res), list)
        self.assertSequenceEqual(res, [0, 0, 1, 1, 1])

        res = self.interpret("[1,2,3,4,5]<3")
        self.assertIs(type(res), list)
        self.assertSequenceEqual(res, [1, 1, 0, 0, 0])

        res = self.interpret("[1,2,3]=3")
        self.assertIs(type(res), list)
        self.assertSequenceEqual(res, [0, 0, 1])

    def test_complex(self):
        res = self.interpret("[1,2,3,4,2,3,5,6]>3!+")
        self.assertIs(type(res), int)
        self.assertEqual(res, 3)

        res = self.interpret("1W20 + 3W6!>")
        self.assertIs(type(res), list)
        self.assertEqual(len(res), 1)


if __name__ == '__main__':
    unittest.main()
