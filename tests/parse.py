#!/usr/bin/python3

import argparse
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import tem_parser

from tem_parser import tem_lexer
from tem_parser import tem_parser
from tem_parser import matcheroni

#---------------------------------------------------------------------------------------------------

args = argparse.ArgumentParser()
args.add_argument("filename", type=str, default=None, nargs="?")
(flags, _) = args.parse_known_args()

if not flags.filename:
  sys.exit(-1)

file = open(flags.filename, encoding="utf-8")
source = file.read()
file.close()

lex_ctx    = matcheroni.Context(matcheroni.default_atom_cmp)
lex_fail   = tem_lexer.lex_string(source, lex_ctx)

print()
print(tem_parser.dump_tree(lex_ctx.stack))

parse_ctx  = matcheroni.Context(tem_lexer.atom_cmp_tokens)
parse_fail = tem_parser.parse_lexemes(lex_ctx.stack, parse_ctx)

print()
print(tem_parser.dump_tree(parse_ctx.stack))
