import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from KeepRollingLexer import KeepRollingLexer
from KeepRollingParser import KeepRollingParser
from KeepRollingEval import KeepRollingEval

if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     input_stream = FileStream(sys.argv[1])
    # else:
    #     input_stream = InputStream(sys.stdin.readline())

    lexer = KeepRollingLexer(InputStream('123 \n [1,2,3] \n 3w6 \n 3D6 \n [1,2,3]!+ \n [1,2,3]!> \n [1,2,3]!< \n'))
    token_stream = CommonTokenStream(lexer)
    parser = KeepRollingParser(token_stream)
    tree = parser.prog()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    visitor = KeepRollingEval()
    visitor.visit(tree)