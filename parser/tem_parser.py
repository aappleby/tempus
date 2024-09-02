#!/usr/bin/python3

import parser
from parser.matcheroni import *
from parser.tem_lexer import *
from functools import cache

#---------------------------------------------------------------------------------------------------

class BaseNode:
    def items(self):
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def __contains__(self, key):
        return key in self.__dict__

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, val):
        self.__dict__[key] = val

    def __getattr__(self, key):
        return self.__dict__[key]

    def __setattr__(self, key, val):
        self.__dict__[key] = val

    def __repr__(self):
        return type(self).__name__ + ":" + self.__dict__.__repr__()

class BlockNode(BaseNode):    pass
class CallNode(BaseNode):     pass
class CaseNode(BaseNode):     pass
class DeclNode(BaseNode):     pass
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

def match_assignop(span, ctx):
  if len(span) and span[0].type == LexemeType.LEX_OP and span[0].text in parser.tem_constants.tem_assignops:
    return span[1:]
  return Fail(span)

def match_declop(span, ctx):
  if len(span) and span[0].type == LexemeType.LEX_OP and span[0].text in parser.tem_constants.tem_declops:
    return span[1:]
  return Fail(span)

def match_binop(span, ctx):
  if len(span) and span[0].type == LexemeType.LEX_OP and span[0].text in parser.tem_constants.tem_binops:
    return span[1:]
  return Fail(span)

#ident_rail = {
#  None         : [PUNCT_AT, ATOM_IDENT],
#  PUNCT_AT     : [ATOM_IDENT],
#  ATOM_IDENT   : [PUNCT_DOT, None],
#  PUNCT_DOT    : [ATOM_IDENT]
#}

# lvalue = Seq(Capture(match_ident), Any(array_suffix))

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

node_primed = Node(PrimedNode,
  PUNCT_AT,
  Field("ident", parse_ident)
)

parse_expr_or_decl = Oneof(
  node_expr,
  node_decl,
)

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
node_block = List2(BlockNode,
  PUNCT_LBRACE,
  Any(parse_stmt),
  PUNCT_RBRACE
)

parse_tuple = Oneof(
  parse_paren_tuple,
  parse_brace_tuple
)

#---------------------------------------------------------------------------------------------------

node_call = Node(CallNode,
  Field("func",   Capture(Oneof(match_ident, ATOM_KEYWORD))),
  Field("params", parse_tuple)
)

node_lambda = Node(LambdaNode,
  Field("params", parse_tuple),
  Field("body",   node_block)
)

parse_expr_unit = Oneof(
  node_lambda,   # (){}
  node_call,     # identifier()
  parse_tuple,    # ()
  node_block,    # {}
  node_primed,
  parse_ident,
  Capture(ATOM_INT),
  Capture(ATOM_FLOAT),
  Capture(ATOM_STRING),
)

# unit op unit op unit...
_node_expr = List2(ExprNode,
  parse_expr_unit,
  Any(Seq(Capture(match_binop), parse_expr_unit))
)

node_else = Node(ElseNode,
  KW_ELSE,
  Field("block", node_block),
)

node_if = Node(IfNode,
  KW_IF,
  Field("condition",  parse_tuple),
  Field("block",      node_block),
  Field("else",       Opt(node_else))
)

node_case = Node(CaseNode,
  KW_CASE,
  Field("condition",  parse_tuple),
  Field("block",      node_block),
)

node_default = Node(DefaultNode,
  KW_DEFAULT,
  Field("block", node_block),
)

node_match = Node(MatchNode,
  KW_MATCH,
  Field("condition", parse_tuple),
  PUNCT_LBRACE,
  Field("body",
    List2(BlockNode, Any(node_case, node_default))
  ),
  PUNCT_RBRACE
)

node_type = Node(TypeNode,
  Field("base", Oneof(
    node_call,
    parse_tuple,
    parse_ident
  )),
  Opt(Field("suffix", parse_tuple))
)

#----------------------------------------

decl_name = Field("name", Oneof(node_primed, parse_ident))
decl_dir  = Field("dir",  Capture(match_declop))
decl_type = Field("type", node_type)
decl_eq   = Field("eq",   Capture(match_assignop))
decl_val  = Field("val",  node_expr)

_node_decl = Node(DeclNode, Railway({
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
  PUNCT_LBRACK,
  Field("name", parse_ident),
  PUNCT_RBRACK,
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
doctest.testmod()
