#!/usr/bin/python3

from antlr4 import *
import tempusLexer
import tempusListener
import tempusParser
import tempusVisitor

#---------------------------------------------------------------------------------------------------

def print_tree(tree, level):
    if tree.getChildCount() == 0:
        sym = tempusParser.tempusParser.symbolicNames[tree.getSymbol().type]
        print('|  ' * level + f'{sym} ' + str(tree))
    else:
        print('|  ' * level, end='')
        print(tempusParser.tempusParser.ruleNames[tree.getRuleIndex()])
        for i in range(tree.getChildCount()):
            print_tree(tree.getChild(i), level + 1)

#---------------------------------------------------------------------------------------------------

class MyListener(ParseTreeListener):
  def __init__(self):
    self.indent = 0

  def enterEveryRule(self, ctx):
    print(' ' * self.indent + ctx.getText())
    self.indent += 2

  def exitEveryRule(self, ctx):
    self.indent -= 2

#---------------------------------------------------------------------------------------------------

class MyVisitor(tempusVisitor.tempusVisitor):
  def visit(self, tree):
    print("blep")
    super().visit(tree)

#---------------------------------------------------------------------------------------------------

if __name__ == "__main__":
  print("Hello Antlr World")

  src = """
  x : int = 10;
  x = 6 + 8;
  y : int;
  """

  lexer = tempusLexer.tempusLexer(InputStream(src))
  stream = CommonTokenStream(lexer)
  parser = tempusParser.tempusParser(stream)
  tree = parser.program()

  tree.toStringTree

  print_tree(tree, 0)

  #print(tree.stmt_list())

  #visitor = MyVisitor()
  #visitor.visit(tree)

  print("Goodbye Antlr World")
  pass
