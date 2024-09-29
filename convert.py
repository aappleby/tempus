#!/usr/bin/python3

import argparse
import sys
from tempus import tem_lexer
from tempus import tem_parser
from tempus import matcheroni

#==============================================================================

def main():

  args = argparse.ArgumentParser()
  args.add_argument("filename", type=str, default=None, nargs="?")
  args.add_argument("-o",       dest="out", type=str, default=None, nargs=1, required=True)
  (flags, unknown) = args.parse_known_args()

  if flags.filename is None:
    args.print_help()
    sys.exit(1)

  with open(flags.filename, encoding="utf-8") as file:
    source = file.read()

    lex_ctx    = matcheroni.Context(matcheroni.default_atom_cmp)
    lex_fail   = tem_lexer.lex_string(source, lex_ctx)
    if lex_fail:
      raise ValueError("Lexing failed", lex_ctx.stack)

    print()
    print(tem_parser.dump_tree(lex_ctx.stack))

    parse_ctx  = matcheroni.Context(tem_lexer.atom_cmp_tokens)
    parse_fail = tem_parser.parse_lexemes(lex_ctx.stack, parse_ctx)
    if parse_fail:
      raise ValueError("Parsing failed", parse_ctx.stack)

    print()
    print(tem_parser.dump_tree(parse_ctx.stack))

#==============================================================================

if __name__ == "__main__":
  main()