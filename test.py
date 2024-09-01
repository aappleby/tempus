#!/usr/bin/python3

import parser
import pprint
import glob

from parser.tem_lexer import Lexeme
from parser.tem_parser import BaseNode

#---------------------------------------------------------------------------------------------------

def print_indent(indent):
  print("  " * indent, end='')
  #for i in range(indent - 1):
  #  print("┃ ", end="")
  #print("┗ ", end='')

def dump_node(node, indent = 0):
  print(f"{type(node).__name__}{{}}")
  for key, val in node.items():
    print_indent(indent)
    print(f".{key} : ", end='')
    dump_variant(val, indent + 1)

def dump_array(array, indent = 0):
  print(f"Array[{len(array)}]")
  for key, val in enumerate(array):
    print_indent(indent)
    print(f"[{key}] : ", end="")
    dump_variant(val, indent + 1)

def dump_lexeme(lexeme, indent = 0):
  print(f"{lexeme.type.name} = {lexeme.text}")

def dump_variant(variant, indent = 0):
  if isinstance(variant, BaseNode):
    dump_node(variant, indent)
  elif isinstance(variant, list):
    dump_array(variant, indent)
  elif isinstance(variant, Lexeme):
    dump_lexeme(variant, indent)
  elif variant is None:
    print(f"<None>")
  else:
    print(f"??? {variant}")

#---------------------------------------------------------------------------------------------------

def test_parse(filename):

  source = open(filename).read()
  lexemes = parser.tem_lexer.lex_string(source)
  trees = parser.tem_parser.parse_lexemes(lexemes)

  for item in trees:
    if isinstance(item, parser.tem_lexer.Lexeme):
      print(f"Parsing file {filename} failed @ {item}")
      return False
  print(f"Parsing {filename} OK")
  return True

#---------------------------------------------------------------------------------------------------

if __name__ == "__main__":
  print("Test parsing of uart_tem/*.tem")
  for filename in glob.glob("uart_tem/*.tem"):
    test_parse(filename)

  filename = "scratch.tem"
  #filename = "tests/tem_good/functions.tem"
  #filename = "uart_tem/simple_rx.tem"

  print(f"Test parsing of {filename}")
  source = open(filename).read()
  lexemes = parser.tem_lexer.lex_string(source)

  #print()
  #print("# lexemes")
  #for lexeme in lexemes:
  #  print(lexeme)

  print()
  print("# parsing")
  trees = parser.tem_parser.parse_lexemes(lexemes)

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

  print()

  print("test end")
  pass
