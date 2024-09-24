#!/usr/bin/python3

import argparse
import glob
import os
import sys
import unittest
import inspect

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import tem_parser

from tem_parser import tem_lexer
from tem_parser import tem_parser
from tem_parser import matcheroni

from tem_parser.tem_lexer import Lexeme
from tem_parser.tem_parser import BaseNode

#---------------------------------------------------------------------------------------------------

def dump_indent(indent):
  return "  " * indent

def dump_node(node, indent = 0):
  result = f"{node.__class__.__name__}{{}}\n"
  for key, val in node.items():
    result += dump_indent(indent + 1)
    if isinstance(key, int):
      result += f"[{key}] : "
    else:
      result += f".{key} : "
    result += dump_variant(val, indent + 1)
  return result

def dump_array(array, indent = 0):
  result = f"{array.__class__.__name__}[{len(array)}]\n"
  for key, val in enumerate(array):
    result += dump_indent(indent + 1)
    result += f"[{key}] : "
    result += dump_variant(val, indent + 1)
  return result

def dump_tuple(t, indent = 0):
  result = f"{t.__class__.__name__}({len(t)})\n"
  for key, val in enumerate(t):
    result += dump_indent(indent + 1)
    result += f"({key}) : "
    result += dump_variant(val, indent + 1)
  return result

def dump_lexeme(lexeme, *_):
  return f"{lexeme.lex_type.name} {repr(lexeme.text)[1:-1]}\n"

def dump_variant(variant, indent = 0):
  result = ""
  if isinstance(variant, BaseNode):
    result += dump_node(variant, indent)
  elif isinstance(variant, list):
    result += dump_array(variant, indent)
  elif isinstance(variant, tuple):
    result += dump_tuple(variant, indent)
  elif isinstance(variant, Lexeme):
    result += dump_lexeme(variant, indent)
  elif variant is None:
    result += "<None>\n"
  else:
    result +=  f"??? {variant}\n"
  return result

def dump_tree(tree):
  return dump_variant(tree, 0).strip()

#---------------------------------------------------------------------------------------------------

def parse_source(source):
  lex_ctx    = matcheroni.Context(matcheroni.default_atom_cmp)
  lex_fail   = tem_lexer.lex_string(source, lex_ctx)
  if lex_fail:
    raise ValueError("Lexing failed", lex_ctx.stack)

  parse_ctx  = matcheroni.Context(tem_lexer.atom_cmp_tokens)
  parse_fail = tem_parser.parse_lexemes(lex_ctx.stack, parse_ctx)
  if parse_fail:
    raise ValueError("Parsing failed", parse_ctx.stack)

  return parse_ctx.stack

def parse_file(filename):
  print(filename)
  with open(filename, encoding="utf-8") as file:
    source = file.read()
    return parse_source(source)

#---------------------------------------------------------------------------------------------------

class TestTempus(unittest.TestCase):

  #----------------------------------------

  example1 = (
    #--------------------
    r"""
    # asdf
    x : int = 1;
    """,
    #--------------------
    r"""
    list[2]
      [0] : MarkerNode{}
        .name : LEX_IDENT asdf
      [1] : AtomNode{}
        .name : LEX_IDENT x
        .dir : LEX_OP :
        .type : TypeNode{}
          .base : LEX_IDENT int
        .eq : LEX_OP =
        .val : LEX_INT 1
    """
    #--------------------
  )

  def test_one(self):
    self.assertEqual(
      dump_tree(parse_source(self.example1[0])),
      inspect.cleandoc(self.example1[1])
    )

  #----------------------------------------

  def test_tem_good(self):
    for filename in glob.glob("tem_good/*.tem"):
      tree = parse_file(filename)
      with open(filename + ".tree", "w", encoding="utf-8") as file:
        file.write(dump_tree(tree))

  def test_uart(self):
    pass


  #----------------------------------------

#---------------------------------------------------------------------------------------------------

def main():
  # Loading modules runs self-test, add a break after them
  print()
  
  args = argparse.ArgumentParser()
  args.add_argument("filename", type=str, default=None, nargs="?")
  (flags, _) = args.parse_known_args()
  if flags.filename:
    print(f"Parsing {flags.filename}")
    with open(flags.filename, encoding="utf-8") as file:
      source = file.read()
      tree = parse_source(source)
  else:   
    print("Running unit tests")
    unittest.main()

  print("Done")

if __name__ == "__main__":
  main()