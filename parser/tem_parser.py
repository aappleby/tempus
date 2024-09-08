#!/usr/bin/python3

import parser
from parser.matcheroni import *
from parser.tem_lexer import *
from functools import cache

#---------------------------------------------------------------------------------------------------

class AtomNode(BaseNode):
  def __init__(self):
    self.name = None
    self.dir  = None
    self.type = None
    self.eq   = None
    self.val  = None
    pass
  pass

class BlockNode(BaseNode):    pass
class CallNode(BaseNode):     pass
class CaseNode(BaseNode):     pass
class DefaultNode(BaseNode):  pass
class ElseNode(BaseNode):     pass
class ExprNode(BaseNode):     pass
class IdentNode(BaseNode):    pass
class IfNode(BaseNode):       pass
class LambdaNode(BaseNode):   pass
class MatchNode(BaseNode):    pass
class PrimedNode(BaseNode):   pass
class ReturnNode(BaseNode):   pass
class SectionNode(BaseNode):  pass
class SquishNode(BaseNode):   pass
class TupleNode(BaseNode):    pass
class TypeNode(BaseNode):     pass

#---------------------------------------------------------------------------------------------------
# Define our atom types for the parser

def LexToAtom(type, span = None):
  if span is None:
    return Atom(type)
  return Atom(Lexeme(type, span))

ATOM_STRING   = LexToAtom(LexemeType.LEX_STRING)
ATOM_CHAR     = LexToAtom(LexemeType.LEX_CHAR)
ATOM_KEYWORD  = LexToAtom(LexemeType.LEX_KEYWORD)
ATOM_IDENT    = LexToAtom(LexemeType.LEX_IDENT)
ATOM_COMMENT  = LexToAtom(LexemeType.LEX_COMMENT)
ATOM_FLOAT    = LexToAtom(LexemeType.LEX_FLOAT)
ATOM_INT      = LexToAtom(LexemeType.LEX_INT)
ATOM_PUNC     = LexToAtom(LexemeType.LEX_PUNCT)
ATOM_OP       = LexToAtom(LexemeType.LEX_OP)

PUNCT_NEWLINE = LexToAtom(LexemeType.LEX_NEWLINE)

PUNCT_COMMA   = LexToAtom(LexemeType.LEX_PUNCT, ",")
PUNCT_SEMI    = LexToAtom(LexemeType.LEX_PUNCT, ";")
PUNCT_DOT     = LexToAtom(LexemeType.LEX_PUNCT, ".")
PUNCT_LPAREN  = LexToAtom(LexemeType.LEX_PUNCT, "(")
PUNCT_RPAREN  = LexToAtom(LexemeType.LEX_PUNCT, ")")
PUNCT_LBRACK  = LexToAtom(LexemeType.LEX_PUNCT, "[")
PUNCT_RBRACK  = LexToAtom(LexemeType.LEX_PUNCT, "]")
PUNCT_LBRACE  = LexToAtom(LexemeType.LEX_PUNCT, "{")
PUNCT_RBRACE  = LexToAtom(LexemeType.LEX_PUNCT, "}")
PUNCT_POUND   = LexToAtom(LexemeType.LEX_PUNCT, "#")

PUNCT_AT      = LexToAtom(LexemeType.LEX_PUNCT, "@")

KW_MATCH      = LexToAtom(LexemeType.LEX_KEYWORD, "match")
KW_CASE       = LexToAtom(LexemeType.LEX_KEYWORD, "case")
KW_DEFAULT    = LexToAtom(LexemeType.LEX_KEYWORD, "default")
KW_RETURN     = LexToAtom(LexemeType.LEX_KEYWORD, "return")
KW_ELSE       = LexToAtom(LexemeType.LEX_KEYWORD, "else")
KW_IF         = LexToAtom(LexemeType.LEX_KEYWORD, "if")
KW_SIGNED     = LexToAtom(LexemeType.LEX_KEYWORD, "signed")
KW_UNSIGNED   = LexToAtom(LexemeType.LEX_KEYWORD, "unsigned")

#---------------------------------------------------------------------------------------------------

def match_op(ops):
  def match(span, ctx):
    if len(span) and span[0].type == LexemeType.LEX_OP and span[0].text in ops:
      return span[1:]
    return Fail(span)
  return match

match_ident = Seq(
  Opt(PUNCT_DOT),
  ATOM_IDENT,
  Any(Seq(
    PUNCT_DOT,
    ATOM_IDENT,
  ))
)

#---------------------------------------------------------------------------------------------------
# Forward decls

def parse_stmt(span, ctx):
  return _parse_stmt(span, ctx)

def node_expr(span, ctx):
  return _node_expr(span, ctx)

def node_decl(span, ctx):
  return _node_decl(span, ctx)

parse_ident = Capture(match_ident)
node_primed = Node(PrimedNode, PUNCT_AT, Field("ident", parse_ident))
parse_expr_or_decl = Oneof(node_expr, node_decl)

#---------------------------------------------------------------------------------------------------

# Parenthesized, comma-delimited lists of mixed expressions and declarations. Trailing commas OK.
# Examples: (348, "foo", x : u32 = 7), (), (1,)
parse_paren_tuple = Railway({
  None         : [PUNCT_LPAREN],
  PUNCT_LPAREN : [node_expr, node_decl, PUNCT_RPAREN],
  node_expr    : [PUNCT_COMMA,          PUNCT_RPAREN],
  node_decl    : [PUNCT_COMMA,          PUNCT_RPAREN],
  PUNCT_COMMA  : [node_expr, node_decl, PUNCT_RPAREN],
  PUNCT_RPAREN : [None]
})

# Same as above except []
parse_brace_tuple = Railway({
  None         : [PUNCT_LBRACK],
  PUNCT_LBRACK : [node_expr, node_decl, PUNCT_RBRACK],
  node_expr    : [PUNCT_COMMA,          PUNCT_RBRACK],
  node_decl    : [PUNCT_COMMA,          PUNCT_RBRACK],
  PUNCT_COMMA  : [node_expr, node_decl, PUNCT_RPAREN],
  PUNCT_RBRACK : [None]
})

# Curly-braced, semicolon-delimited lists of statements. Excess semicolons are OK. No semicolon
# after the last statement is OK.
node_block = List2(BlockNode, PUNCT_LBRACE, Any(parse_stmt), PUNCT_RBRACE)

node_tuple = List2(TupleNode, Oneof(parse_paren_tuple, parse_brace_tuple))

#---------------------------------------------------------------------------------------------------

node_call = Node(CallNode,
  Field("func",   Capture(Oneof(match_ident, ATOM_KEYWORD))),
  Field("params", node_tuple)
)

node_lambda = Node(LambdaNode,
  Field("params", node_tuple),
  Field("body",   node_block)
)

squishable = Oneof(
  node_tuple,
  node_block,
  node_primed,
  parse_ident,
  Capture(ATOM_KEYWORD),
  Capture(ATOM_INT),
  Capture(ATOM_FLOAT),
  Capture(ATOM_STRING),
)

squish_list = List2(SquishNode, AtLeast(2, squishable))

parse_expr_unit = Oneof(
  squish_list,
  squishable
)

# unit op unit op unit...
_node_expr = Oneof(
  List2(ExprNode,
    parse_expr_unit,
    Capture(match_op(parser.tem_parser.tem_binops)),
    parse_expr_unit,
    Any(Seq(Capture(match_binop), parse_expr_unit))
  ),
  parse_expr_unit,
)

node_else = Node(ElseNode,
  KW_ELSE,
  Field("block", node_block),
)

node_if = Node(IfNode,
  KW_IF,
  Field("condition",  node_tuple),
  Field("block",      node_block),
  Field("else",       Opt(node_else))
)

node_case = Node(CaseNode,
  KW_CASE,
  Field("condition",  node_tuple),
  Field("block",      node_block),
)

node_default = Node(DefaultNode,
  KW_DEFAULT,
  Field("block", node_block),
)

node_match = Node(MatchNode,
  KW_MATCH,
  Field("condition", node_tuple),
  PUNCT_LBRACE,
  Field("body",
    List2(BlockNode, Any(node_case, node_default))
  ),
  PUNCT_RBRACE
)

node_type = Node(TypeNode,
  Field("base", Oneof(
    node_call,
    node_tuple,
    parse_ident
  )),
  Opt(Field("suffix", node_tuple))
)

#----------------------------------------

decl_name = Field("name", Oneof(node_primed, parse_ident))
decl_dir  = Field("dir",  Capture(match_op(parser.tem_parser.tem_declops)))
decl_type = Field("type", node_type)
decl_eq   = Field("eq",   Capture(match_op(parser.tem_constants.tem_assignops)))
decl_val  = Field("val",  node_expr)

_node_decl = Node(AtomNode, Railway({
  None      : [decl_name, decl_dir, decl_eq],
  decl_name : [decl_dir,  decl_eq],
  decl_dir  : [decl_type, None],
  decl_type : [decl_eq,   None],
  decl_eq   : [decl_val],
  decl_val  : [None]
}))

#----------------------------------------

node_return = Node(ReturnNode,
  KW_RETURN,
  Field("val", Opt(node_expr))
)

_parse_stmt = Oneof(
  node_match,
  node_if,
  node_return,
  node_decl,
  node_block,
  node_expr,
  PUNCT_SEMI
)

node_section = Node(SectionNode,
  PUNCT_POUND,
  Field("name", parse_ident),
  Field("body", Any(parse_stmt))
)

#---------------------------------------------------------------------------------------------------

def parse_lexemes(lexemes):
  span = lexemes
  ctx = []
  while span:
    tail = node_section(span, ctx)
    if isinstance(tail, Fail):
      ctx.append(span[0])
      tail = span[1:]
    span = tail
  return ctx

#---------------------------------------------------------------------------------------------------

import doctest
import sys
import os

testresult = doctest.testmod(sys.modules[__name__])
print(f"Testing {__name__} : {testresult}")
