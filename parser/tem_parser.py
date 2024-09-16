#!/usr/bin/python3

from . import matcheroni
from . import tem_constants
from . import tem_lexer

from .matcheroni import *
from .tem_constants import *
from .tem_lexer import *

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

class CallNode(BaseNode):     pass
class CaseNode(BaseNode):     pass
class DefaultNode(BaseNode):  pass

class CondNode(BaseNode):     pass

class ExprNode(BaseNode):     pass
class IdentNode(BaseNode):    pass
class LambdaNode(BaseNode):   pass
class MarkerNode(BaseNode):   pass
class MatchNode(BaseNode):    pass

class ReturnNode(BaseNode):   pass
class SectionNode(BaseNode):  pass
class TupleNode(BaseNode):    pass
class TypeNode(BaseNode):     pass

class ParenNode(tuple):    pass
class CatNode(tuple):   pass

class BranchNode(list):   pass
class BlockNode(list):    pass

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
KW_ELIF       = LexToAtom(LexemeType.LEX_KEYWORD, "elif")
KW_ELSE       = LexToAtom(LexemeType.LEX_KEYWORD, "else")
KW_IF         = LexToAtom(LexemeType.LEX_KEYWORD, "if")
KW_SIGNED     = LexToAtom(LexemeType.LEX_KEYWORD, "signed")
KW_UNSIGNED   = LexToAtom(LexemeType.LEX_KEYWORD, "unsigned")

#---------------------------------------------------------------------------------------------------

def match_op(ops):
  def match(span, ctx2):
    if len(span) and span[0].type == LexemeType.LEX_OP and span[0].text in ops:
      return span[1:]
    return Fail(span)
  return match

cap_binop   = Capture(match_op(tem_constants.tem_binops))
match_ident = Some(PUNCT_DOT, ATOM_IDENT)
cap_ident   = Capture(match_ident)
cap_keyword = Capture(ATOM_KEYWORD)

#---------------------------------------------------------------------------------------------------
# Forward decls

def parse_stmt(span, ctx2):
  return _parse_stmt(span, ctx2)

def node_expr(span, ctx2):
  return _node_expr(span, ctx2)

def node_decl(span, ctx2):
  return _node_decl(span, ctx2)

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

stmt_delim = List2(BlockNode, Seq(PUNCT_LBRACE, Any(parse_stmt), PUNCT_RBRACE))
stmt_semi  = Seq(parse_stmt, PUNCT_SEMI)

stmt_delim_or_semi = Oneof(stmt_delim, stmt_semi)

node_tuple = Oneof(
  #Node(ParenNode, KeyVal("contents", parse_paren_tuple)),
  Tuple2(ParenNode, parse_paren_tuple),
  parse_brace_tuple
)

#---------------------------------------------------------------------------------------------------

node_call = Node(CallNode,
  KeyVal("func",   Capture(Oneof(match_ident, ATOM_KEYWORD))),
  KeyVal("params", node_tuple)
)

node_lambda = Node(LambdaNode,
  KeyVal("params", node_tuple),
  KeyVal("body",   stmt_delim)
)

cat_atom = Oneof(
  node_tuple,
  stmt_delim,
  cap_ident,
  #Capture(ATOM_KEYWORD),
)

cat_list = Tuple2(CatNode, AtLeast(2, cat_atom))

parse_expr_unit = Oneof(
  cat_list,
  cat_atom,
  Capture(ATOM_INT),
  Capture(ATOM_FLOAT),
  Capture(ATOM_STRING),
)

# unit op unit op unit...
_node_expr = Seq(parse_expr_unit, Any(Seq(cap_binop, parse_expr_unit)))

node_if = List2(BranchNode,
  Seq(
    KW_IF,
    Node(CondNode,
      KeyVal("condition",    parse_paren_tuple),
      KeyVal("then",         stmt_delim_or_semi),
    ),
    Any(Seq(
      KW_ELIF,
      Node(CondNode,
        KeyVal("condition",  parse_paren_tuple),
        KeyVal("then",       stmt_delim_or_semi),
      ),
    )),
    Opt(Seq(
      KW_ELSE,
      Node(CondNode,
        KeyVal("condition",  Nothing),
        KeyVal("then",       stmt_delim_or_semi),
      ),
    ))
  )
)

node_case = Node(CaseNode,
  KW_CASE,
  KeyVal("condition",  node_tuple),
  KeyVal("body",       Seq(parse_stmt, Opt(PUNCT_SEMI))),
)

node_default = Node(DefaultNode,
  KW_DEFAULT,
  KeyVal("body", stmt_delim),
)

node_match = Node(MatchNode,
  KW_MATCH,
  KeyVal("condition", node_tuple),
  PUNCT_LBRACE,
  KeyVal("body",
    List2(BlockNode, Any(Oneof(node_case, node_default)))
  ),
  PUNCT_RBRACE
)

node_type = Node(TypeNode,
  KeyVal("base", Oneof(
    node_call,
    node_tuple,
    cap_ident,
    cap_keyword
  )),
  Opt(KeyVal("suffix", node_tuple))
)

#----------------------------------------

decl_name = KeyVal("name", cap_ident)
decl_dir  = KeyVal("dir",  Capture(match_op(tem_declops)))
decl_type = KeyVal("type", node_type)
decl_eq   = KeyVal("eq",   Capture(match_op(tem_assignops)))
decl_val  = KeyVal("val",  node_expr)

_node_decl = Node(AtomNode, Railway({
  None      : [decl_name, decl_dir, decl_eq],
  decl_name : [decl_dir,  decl_eq],
  decl_dir  : [decl_type, None],
  decl_type : [decl_eq,   None],
  decl_eq   : [decl_val],
  decl_val  : [None]
}))

#----------------------------------------

node_marker = Node(MarkerNode, PUNCT_POUND, KeyVal("name", cap_ident))
node_return = Node(ReturnNode, KW_RETURN,   KeyVal("val",  Opt(node_expr)))

_parse_stmt = Oneof(
  # Order matters!
  node_if,
  node_match,
  node_return,
  node_marker,

  stmt_delim,
  node_decl,
  node_expr,
  PUNCT_SEMI
)

#---------------------------------------------------------------------------------------------------

def parse_lexemes(lexemes, ctx):
  span = lexemes
  while span:
    tail = parse_stmt(span, ctx)
    if isinstance(tail, Fail):
      ctx.stack.append(("fail @ ", span[0]))
      tail = span[1:]
    span = tail

#---------------------------------------------------------------------------------------------------

import doctest
import sys
import os

testresult = doctest.testmod(sys.modules[__name__])
print(f"Testing {__name__} : {testresult}")
