#!/usr/bin/python3

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

source = r"""
# top
// Simple 8n1 UART receiver in Metron

# params
clocks_per_bit = 4;
bits_per_byte = 10;
delay_mid = clocks_per_bit / 2;
delay_max = clocks_per_bit - 1;
count_max = bits_per_byte - 1;

# types
delay_reg : unsigned(max = delay_max);
count_reg : unsigned(max = count_max);
shift_reg : u8;

# ports
src >: u1;

dst.data  :> shift_reg = shift;
dst.valid :> u1 = 0;
dst.ready >: u1;

# state
delay : delay_reg = delay_max;
count : count_reg = count_max;
shift : shift_reg = 0;

# update
match (true) {
  case (delay < delay_max) {
    @delay = delay + 1;
  }
  case (count < count_max) {
    @delay = 0;
    @count = count + 1;
  }
  case (src == 0) {
    @delay = 0;
    @count = 0;
  }
}

if (delay == delay_mid) {
  @shift = src :: (shift >> 1);
  // I think this is wrong...
  dst.valid = @count == 8;
}

"""

lex_ctx    = matcheroni.Context(matcheroni.default_atom_cmp)
lex_fail   = tem_lexer.lex_string(source, lex_ctx)

print()
print(tem_parser.dump_tree(lex_ctx.stack))

parse_ctx  = matcheroni.Context(tem_lexer.atom_cmp_tokens)
parse_fail = tem_parser.parse_lexemes(lex_ctx.stack, parse_ctx)

print()
print(tem_parser.dump_tree(parse_ctx.stack))

if lex_fail:
    print("LEX FAIL")

if parse_fail:
    print("PARSE FAIL")