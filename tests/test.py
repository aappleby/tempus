#!/usr/bin/python3

import glob
import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import tempus

from tempus import tem_lexer
from tempus import tem_parser
from tempus import matcheroni

#---------------------------------------------------------------------------------------------------

class TestTempus(unittest.TestCase):

  def parse_source(self, source):
    lex_ctx    = matcheroni.Context(matcheroni.default_atom_cmp)
    lex_fail   = tem_lexer.lex_string(source, lex_ctx)
    if lex_fail:
      raise ValueError("Lexing failed", lex_ctx.stack)
    parse_ctx  = matcheroni.Context(tem_lexer.atom_cmp_tokens)
    parse_fail = tem_parser.parse_lexemes(lex_ctx.stack, parse_ctx)
    if parse_fail:
      raise ValueError("Parsing failed", parse_ctx.stack)
    return parse_ctx.stack

  def parse_file(self, filename):
    print(filename)
    with open(filename, encoding="utf-8") as file:
      source = file.read()
      return self.parse_source(source)

  def parse_and_write_tree(self, filename):
    tree = self.parse_file(filename)
    with open(filename + ".tree", "w", encoding="utf-8") as file:
      file.write(tem_parser.dump_tree(tree))

  def test_tem_good(self):
    for filename in glob.glob("tem_good/*.tem"):
      self.parse_and_write_tree(filename)

  def test_uart(self):
    self.parse_and_write_tree("../examples/uart_tem/simple_msg.tem")
    self.parse_and_write_tree("../examples/uart_tem/simple_sink.tem")
    self.parse_and_write_tree("../examples/uart_tem/simple_rx.tem")
    self.parse_and_write_tree("../examples/uart_tem/simple_tx.tem")
    self.parse_and_write_tree("../examples/uart_tem/simple_top.tem")

#---------------------------------------------------------------------------------------------------

unittest.main()
