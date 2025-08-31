#!/usr/bin/python3
# pylint: disable=bad-indentation

import doctest
import sys
from enum import Enum
from functools import cache

from . import matcheroni
from . import tem_constants

from .matcheroni import Span, Some, Opt, Atoms, Atom, Seq, Oneof, Range, Any
from .matcheroni import Lit, NotAtom, Until, Charset, Fail, NotAtoms

#---------------------------------------------------------------------------------------------------

# pylint: disable=too-few-public-methods
class Lexeme:
  def __init__(self, lex_type, span):
    assert isinstance(span, Span)
    self.lex_type = lex_type
    self.span = span

  def to_str(self):
    return str(self.span)

  def __repr__(self):
    span = self.to_str().encode('unicode_escape').decode('utf-8')
    if len(span) > 40:
      span = span[:40] + "..."

    match self.lex_type:
      case LexemeType.LEX_NEWLINE:
        return f"{self.lex_type.name}"
      case _:
        return f"{self.lex_type.name}({span})"

  def eq(self, x):
    if isinstance(x, str):
      return self.to_str() == x
    raise ValueError(f"Don't know how to eq a lexeme vs {type(x)} = {x}")

  #def __eq__(self, x):
  #  if isinstance(x, str):
  #    return self.text == x
  #  raise ValueError(f"Don't know how to eq a lexeme vs {type(x)} = {x}")

#---------------------------------------------------------------------------------------------------

def strcmp(str1, str2):
  if str1 < str2:
    return -1
  if str1 > str2:
    return 1
  return 0

def atom_cmp_tokens(a, b):
  if isinstance(a, Lexeme) and isinstance(b, Lexeme):
    if a.lex_type.value != b.lex_type.value:
      return b.lex_type.value - a.lex_type.value
    return strcmp(a.to_str(), b.to_str())

  if isinstance(a, Lexeme) and isinstance(b, Enum):
    return b.value - a.lex_type.value
  return matcheroni.default_atom_cmp(a, b)

#---------------------------------------------------------------------------------------------------

LexemeType = Enum(
  'LexemeType',
  [
    "LEX_SPACE",
    "LEX_NEWLINE",
    "LEX_STRING",
    "LEX_KEYWORD",
    "LEX_IDENT",
    "LEX_COMMENT",
    "LEX_FLOAT",
    "LEX_INT",
    "LEX_PUNCT",
    "LEX_CHAR",
    "LEX_BINOP",
    "LEX_DECLOP",
    "LEX_ASSIGNOP",
    "LEX_AFFIX"
  ]
)

def lex_to_color(lex_type):
  match lex_type:
    case LexemeType.LEX_SPACE    : return 0x804040
    case LexemeType.LEX_NEWLINE  : return 0x404080
    case LexemeType.LEX_STRING   : return 0x4488AA
    case LexemeType.LEX_KEYWORD  : return 0x0088FF
    case LexemeType.LEX_IDENT    : return 0xCCCC40
    case LexemeType.LEX_COMMENT  : return 0x66AA66
    case LexemeType.LEX_FLOAT    : return 0xFF88AA
    case LexemeType.LEX_INT      : return 0xFF8888
    case LexemeType.LEX_PUNCT    : return 0x808080
    case LexemeType.LEX_CHAR     : return 0x44DDDD
    case LexemeType.LEX_BINOP    : return 0x888888
    case LexemeType.LEX_DECLOP   : return 0x888888
    case LexemeType.LEX_ASSIGNOP : return 0x888888
    case LexemeType.LEX_AFFIX    : return 0x888888
  return 0xFF00FF

#---------------------------------------------------------------------------------------------------

match_space = Some(Atoms(' ', '\t'))

match_dots = Some(Atom('.'))

match_newline = Seq(Opt(Atom('\r')), Atom('\n'))

sign = Atoms('+','-')

@cache
def ticked(c):
  return Seq(Opt(Atom('\'')), c)

nondigit     = Oneof(Range('a', 'z'), Range('A', 'Z'), Atom('_'))

dec_digit    = Range('0', '9')
dec_digits   = Seq(dec_digit, Any(ticked(dec_digit)))
dec_constant = dec_digits

hex_prefix   = Oneof(Lit("0x"), Lit("0X"))
hex_digit    = Oneof(Range('0','9'), Range('a','f'), Range('A', 'F'))
hex_digits   = Seq(hex_digit, Any(ticked(hex_digit)))
hex_constant = Seq(hex_prefix, hex_digits)

bin_prefix   = Oneof(Lit("0b"), Lit("0B"))
bin_digit    = Atoms('0', '1')
bin_digits   = Seq(bin_digit, Any(ticked(bin_digit)))
bin_constant = Seq(bin_prefix, bin_digits)

bit_suffix = Seq(
  Atoms('u', 's', 'b'),
  dec_constant
)

float_suffix = Seq(Atoms('e', 'E'), Opt(sign), dec_digits)

match_int = Seq(
  Oneof(
    dec_constant,
    hex_constant,
    bin_constant
  ),
  Opt(bit_suffix)
)

match_float = Seq(
  dec_digits,
  Atom('.'),
  dec_digits,
  Opt(float_suffix)
)

match_string = Seq(
  Atom('"'),
  Any(
    Lit("\\\""),
    NotAtom("\"")
  ),
  Atom('"')
)

match_comment = Oneof(
  Seq(Lit("//"), Until(Atom('\n'))),
  Seq(Lit("/*"), Until(Lit("*/")), Lit("*/"))
)

#match_punct = Charset("-,;:!?.()[]{}<>*/&#%^+=|~@")

match_punct = Charset(",;.()[]{}@#")

def make_match_op(ops):
  def match(span, _):
    for op in ops:
      if span.startswith(op):
        return span[len(op):]
    return Fail(span)
  return match

match_binop    = make_match_op(tem_constants.tem_binops)
match_declop   = make_match_op(tem_constants.tem_declops)
match_assignop = make_match_op(tem_constants.tem_assignops)
match_affix    = make_match_op(tem_constants.tem_affixes)

match_char = Seq(
  Atom('\''),
  NotAtoms('\'', '\\', '\n'),
  Atom('\'')
)

match_ident = Seq(nondigit, Any(dec_digit, nondigit))

def match_keyword(span, ctx2):
  tail = match_ident(span, ctx2)
  if isinstance(tail, Fail):
    return tail
  lexeme = span[:len(span) - len(tail)]
  return tail if lexeme in tem_constants.tem_keywords else Fail(span)

#---------------------------------------------------------------------------------------------------

def match_to_lex(pattern, lex_type):
  def match(span, ctx2):
    tail = pattern(span, ctx2)
    if not isinstance(tail, Fail):
      ctx2.stack.append(Lexeme(lex_type, span[:len(span) - len(tail)]))
    return tail
  return match

#---------------------------------------------------------------------------------------------------

def next_lexeme(span, ctx2):
  matchers = [
    match_space,
    #MatchToLex(match_newline,  LexemeType.LEX_NEWLINE),
    match_newline,
    match_to_lex(match_dots,     LexemeType.LEX_PUNCT),
    match_to_lex(match_string,   LexemeType.LEX_STRING),
    match_to_lex(match_char,     LexemeType.LEX_CHAR),
    match_to_lex(match_keyword,  LexemeType.LEX_KEYWORD),
    match_to_lex(match_ident,    LexemeType.LEX_IDENT),
    #MatchToLex(match_comment,  LexemeType.LEX_COMMENT),
    match_comment,
    match_to_lex(match_float,    LexemeType.LEX_FLOAT),
    match_to_lex(match_int,      LexemeType.LEX_INT),
    match_to_lex(match_affix,    LexemeType.LEX_AFFIX),
    match_to_lex(match_declop,   LexemeType.LEX_DECLOP),
    match_to_lex(Lit("=="),      LexemeType.LEX_BINOP), # dammit FIXME
    match_to_lex(match_assignop, LexemeType.LEX_ASSIGNOP),
    match_to_lex(match_binop,    LexemeType.LEX_BINOP),
    match_to_lex(match_punct,    LexemeType.LEX_PUNCT),
  ]

  for matcher in matchers:
    tail = matcher(span, ctx2)
    if not isinstance(tail, Fail):
      return tail

  raise ValueError(f"Don't know how to lex '{span[:8]}...'")

def lex_string(source, ctx):
  return matcheroni.apply(source, ctx, next_lexeme)

#---------------------------------------------------------------------------------------------------

testresult = doctest.testmod(sys.modules[__name__])
#print(f"Testing {__name__} : {testresult}")
