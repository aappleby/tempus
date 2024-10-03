#!/usr/bin/python3

import glob
import os
import unittest

import tempus
from tempus import tem_lexer
from tempus import tem_parser
from tempus import matcheroni
from tempus.matcheroni import Context, Span

#---------------------------------------------------------------------------------------------------

class TestTempus(unittest.TestCase):

  def test_lex_sanity(self):
    lex_ctx  = Context()
    tempus.tem_lexer.lex_string(Span("case 1 foo \"asdf asdf asdf\""), lex_ctx)
    self.assertEqual(str(lex_ctx.stack), "[LEX_KEYWORD(case), LEX_INT(1), LEX_IDENT(foo), LEX_STRING(\"asdf asdf asdf\")]")

    lex_ctx  = Context()
    tempus.tem_lexer.lex_string(Span("++ -- % ^ &"), lex_ctx)
    self.assertEqual(str(lex_ctx.stack), "[LEX_AFFIX(++), LEX_AFFIX(--), LEX_BINOP(%), LEX_BINOP(^), LEX_BINOP(&)]")

    lex_ctx  = Context()
    tempus.tem_lexer.lex_string(Span("/*comment*/ 1.0e38 ; 'q' : +="), lex_ctx)
    self.assertEqual(str(lex_ctx.stack), "[LEX_FLOAT(1.0e38), LEX_PUNCT(;), LEX_CHAR('q'), LEX_DECLOP(:), LEX_ASSIGNOP(+=)]")

  def parse_source(self, source):
    lex_ctx    = matcheroni.Context(matcheroni.default_atom_cmp)
    lex_span   = matcheroni.Span(source)
    lex_fail   = tem_lexer.lex_string(lex_span, lex_ctx)
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
