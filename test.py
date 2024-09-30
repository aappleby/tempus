#!/usr/bin/python3

import glob
import os
import unittest

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
    #print(filename)
    with open(filename, encoding="utf-8") as file:
      source = file.read()
      return self.parse_source(source)

  def parse_and_write_tree(self, filename):
    tree = self.parse_file(filename)
    with open(filename + ".tree", "w", encoding="utf-8") as file:
      file.write(tem_parser.dump_tree(tree))

  def test_tem_good(self):
    for filename in glob.glob("tests/tem_good/*.tem"):
      self.parse_and_write_tree(filename)

  def test_uart(self):
    self.parse_and_write_tree("examples/uart_tem/simple_msg.tem")
    self.parse_and_write_tree("examples/uart_tem/simple_sink.tem")
    self.parse_and_write_tree("examples/uart_tem/simple_rx.tem")
    self.parse_and_write_tree("examples/uart_tem/simple_tx.tem")
    self.parse_and_write_tree("examples/uart_tem/simple_top.tem")

  def test_ref_sv(self):
    files = glob.glob("examples/uart_sv_ref/simple*.sv")
    self.assertEqual(5, len(files))
    for filename in files:
      result = os.system(f"verilator -Iexamples/uart_sv_ref --lint-only {filename}")
      self.assertEqual(0, result)

#---------------------------------------------------------------------------------------------------

unittest.main()
