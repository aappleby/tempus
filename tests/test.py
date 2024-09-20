#!/usr/bin/python3

import argparse
import glob
import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import tem_parser

from tem_parser import tem_lexer
from tem_parser import tem_parser
from tem_parser import matcheroni

from tem_parser.tem_lexer import Lexeme
from tem_parser.tem_parser import BaseNode

# Loading modules runs self-test, add a break after them
print()

#---------------------------------------------------------------------------------------------------

def print_indent(indent):
  print("   " * indent, end='')
  #for i in range(indent - 1):
  #  print("┃ ", end="")
  #print("┗ ", end='')

def dump_node(node, indent = 0):
  print(f"{node.__class__.__name__}{{}}")
  for key, val in node.items():
    print_indent(indent + 1)
    if isinstance(key, int):
      print(f"[{key}] : ", end='')
    else:
      print(f".{key} : ", end='')
    dump_variant(val, indent + 1)

def dump_array(array, indent = 0):
  print(f"{array.__class__.__name__}[{len(array)}]")
  for key, val in enumerate(array):
    print_indent(indent + 1)
    print(f"[{key}] : ", end="")
    dump_variant(val, indent + 1)

def dump_tuple(t, indent = 0):
  print(f"{t.__class__.__name__}({len(t)})")
  for key, val in enumerate(t):
    print_indent(indent + 1)
    print(f"({key}) : ", end="")
    dump_variant(val, indent + 1)

def dump_lexeme(lexeme, *_):
  print(f"{lexeme.type.name} {repr(lexeme.text)[1:-1]}")

def dump_variant(variant, indent = 0):
  if isinstance(variant, BaseNode):
    dump_node(variant, indent)
  elif isinstance(variant, list):
    dump_array(variant, indent)
  elif isinstance(variant, tuple):
    dump_tuple(variant, indent)
  elif isinstance(variant, Lexeme):
    dump_lexeme(variant, indent)
  elif variant is None:
    print("<None>")
  else:
    print(f"??? {variant}")


#---------------------------------------------------------------------------------------------------

def test_parse(filename):

  source = open(filename, encoding="utf-8").read()

  lex_ctx    = matcheroni.Context(matcheroni.default_atom_cmp)
  lex_fail   = tem_lexer.lex_string(source, lex_ctx)
  parse_ctx  = matcheroni.Context(tem_lexer.atom_cmp_tokens)
  parse_fail = tem_parser.parse_lexemes(lex_ctx.stack, parse_ctx)

  if lex_fail or parse_fail:
    print(f"Parsing file {filename} failed")
    return False
  else:
    print(f"Parsing {filename} OK")
    return True

#---------------------------------------------------------------------------------------------------

def test_oneoff():
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
  lex_ctx = matcheroni.Context(matcheroni.default_atom_cmp)
  tem_lexer.lex_string(source, lex_ctx)
  parse_ctx = matcheroni.Context(tem_lexer.atom_cmp_tokens)
  tem_parser.parse_lexemes(lex_ctx.stack, parse_ctx)
  print("# trees")
  dump_variant(parse_ctx.stack)

#---------------------------------------------------------------------------------------------------

def main():

  args = argparse.ArgumentParser()
  args.add_argument("filename", type=str, nargs="?")
  (flags, _) = args.parse_known_args()

  print("Testing uart_tem/*.tem")
  for filename in glob.glob("../uart_tem/*.tem"):
    print(f"Testing {filename}")
    print("  ", end='')
    test_parse(filename)

  print("Testing tem_good/*.tem")
  for filename in glob.glob("../tem_good/*.tem"):
    print(f"Testing {filename}")
    print("  ", end='')
    test_parse(filename)
  
  if flags.filename:
    print(f"Testing {flags.filename}")
    test_parse(flags.filename)

#---------------------------------------------------------------------------------------------------

if __name__ == "__main__":
  main()

