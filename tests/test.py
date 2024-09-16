#!/usr/bin/python3

import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import parser
import glob
import argparse
import sys
import textwrap
import inspect

from parser import tem_lexer
from parser import tem_parser
from parser import matcheroni

from parser.tem_lexer import Lexeme
from parser.tem_parser import BaseNode

# Loading modules runs self-test, add a break after them
print()

#---------------------------------------------------------------------------------------------------

def print_indent(indent):
  """
  asdf
  """
  print("   " * indent, end='')
  #for i in range(indent - 1):
  #  print("┃ ", end="")
  #print("┗ ", end='')

def dump_node(node, indent = 0):
  """
  asdf
  """
  print(f"{node.__class__.__name__}{{}}")
  for key, val in node.items():
    print_indent(indent + 1)
    if type(key) == int:
      print(f"[{key}] : ", end='')
    else:
      print(f".{key} : ", end='')
    dump_variant(val, indent + 1)

def dump_array(array, indent = 0):
  """
  asdf
  """
  print(f"{array.__class__.__name__}[{len(array)}]")
  for key, val in enumerate(array):
    print_indent(indent + 1)
    print(f"[{key}] : ", end="")
    dump_variant(val, indent + 1)

def dump_tuple(t, indent = 0):
  """
  asdf
  """
  print(f"{t.__class__.__name__}({len(t)})")
  for key, val in enumerate(t):
    print_indent(indent + 1)
    print(f"({key}) : ", end="")
    dump_variant(val, indent + 1)

def dump_lexeme(lexeme, indent = 0):
  """
  asdf
  """
  print(f"{lexeme.type.name} {repr(lexeme.text)[1:-1]}")

def dump_variant(variant, indent = 0):
  """
  asdf
  """
  if isinstance(variant, BaseNode):
    dump_node(variant, indent)
  elif isinstance(variant, list):
    dump_array(variant, indent)
  elif isinstance(variant, tuple):
    dump_tuple(variant, indent)
  elif isinstance(variant, Lexeme):
    dump_lexeme(variant, indent)
  elif variant is None:
    print(f"<None>")
  else:
    print(f"??? {variant}")

#---------------------------------------------------------------------------------------------------

def test_parse(filename):

  source = open(filename).read()
  lexemes = tem_lexer.lex_string(source)
  trees = tem_parser.parse_lexemes(lexemes)

  for item in trees:
    if isinstance(item, tem_lexer.Lexeme):
      print(f"Parsing file {filename} failed @ {item}")
      return False
  print(f"Parsing {filename} OK")
  return True

#---------------------------------------------------------------------------------------------------

def run_tests():
  print("Running parse tests")
  for filename in glob.glob("../uart_tem/*.tem"):
    print(f"Testing {filename}")
    print("  ", end='')
    test_parse(filename)
  for filename in glob.glob("tem_good/*.tem"):
    print(f"Testing {filename}")
    print("  ", end='')
    test_parse(filename)
  print()

#---------------------------------------------------------------------------------------------------

if __name__ == "__main__":

  source  = inspect.cleandoc(r"""
    # Testcode
    if (blah) {
      @x = 1;
      y = 2;
      z = 3;
    }
    elif (blee) {
      y : int = 7;
      print("Hello world! %d\n", y);
      print("Goodbye Beeps! %d", y + 1);
    }
    elif (bloo) {
    }
    elif (blah) a = 7;
    else {
    }
    match(bar) {
      case (foo) x = 1
      case (baz) z = 7
    }
    """)
  print(source)
  print()
  lex_ctx = matcheroni.Context()
  tem_lexer.lex_string(source, lex_ctx)
  parse_ctx = matcheroni.Context()
  tem_parser.parse_lexemes(lex_ctx.stack, parse_ctx)
  print("# trees")
  dump_variant(parse_ctx.stack)

  sys.exit(0)

  run_tests()

  args = argparse.ArgumentParser()
  args.add_argument("filename", type=str, nargs="?")

  (flags, unrecognized) = args.parse_known_args()

  #filename = "scratch.tem"
  #filename = "tests/tem_good/functions.tem"
  #filename = "uart_tem/simple_rx.tem"

  if flags.filename:
    print(f"Parsing of {flags.filename}")
    source = open(flags.filename).read()
    lexemes = tem_lexer.lex_string(source)

    print()
    print("# parsing")
    trees = tem_parser.parse_lexemes(lexemes)

    failed = False
    for tree in trees:
      if isinstance(tree, Lexeme):
        print(f"Parsing failed at {tree}")
        failed = True

    if not failed:
      print()
      print("# trees")
      print("trees : ", end="")
      dump_variant(trees, 1)
