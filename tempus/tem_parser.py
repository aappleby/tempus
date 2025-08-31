#!/usr/bin/python3
# pylint: disable=bad-indentation

import doctest
import sys
#from functools import cache

from . import tem_constants
from . import matcheroni
from .matcheroni import BaseNode, Atom, Fail, Capture, Some, Any, Railway, ListNode, Seq, Oneof
from .matcheroni import Span, Node, KeyVal, TupleNode, AtLeast, nothing, Opt
from .tem_constants import tem_declops, tem_assignops
from .tem_lexer import Lexeme, LexemeType

#---------------------------------------------------------------------------------------------------


# fmt : off
class BlockNode(list):        pass
class BranchNode(list):       pass
class ExprNode(list):         pass
class IdentNode(list):        pass

class CatNode(tuple):         pass
class ParenNode(tuple):       pass
class BrackNode(tuple):       pass

class AssignNode(BaseNode):   pass
class AtomNode(BaseNode):     pass
class CallNode(BaseNode):     pass
class CaseNode(BaseNode):     pass
class CondNode(BaseNode):     pass
class DefaultNode(BaseNode):  pass
class ForNode(BaseNode):      pass
class LambdaNode(BaseNode):   pass
class MarkerNode(BaseNode):   pass
class MatchNode(BaseNode):    pass
class ReturnNode(BaseNode):   pass
class SectionNode(BaseNode):  pass

class TypeNode(BaseNode):
  def __init__(self):
    self.base = None
    self.suffix = None

# fmt : on

#---------------------------------------------------------------------------------------------------
# Define our atom types for the parser

def lex_to_atom(lex_type, span = None):
  if span is None:
    return Atom(lex_type)
  return Atom(Lexeme(lex_type, Span(span)))

# fmt : off
ATOM_STRING   = lex_to_atom(LexemeType.LEX_STRING)
ATOM_CHAR     = lex_to_atom(LexemeType.LEX_CHAR)
ATOM_KEYWORD  = lex_to_atom(LexemeType.LEX_KEYWORD)
ATOM_IDENT    = lex_to_atom(LexemeType.LEX_IDENT)
ATOM_COMMENT  = lex_to_atom(LexemeType.LEX_COMMENT)
ATOM_FLOAT    = lex_to_atom(LexemeType.LEX_FLOAT)
ATOM_INT      = lex_to_atom(LexemeType.LEX_INT)
ATOM_PUNC     = lex_to_atom(LexemeType.LEX_PUNCT)
ATOM_BINOP    = lex_to_atom(LexemeType.LEX_BINOP)
ATOM_DECLOP   = lex_to_atom(LexemeType.LEX_DECLOP)
ATOM_ASSIGNOP = lex_to_atom(LexemeType.LEX_ASSIGNOP)
ATOM_AFFIX    = lex_to_atom(LexemeType.LEX_AFFIX)

PUNCT_NEWLINE = lex_to_atom(LexemeType.LEX_NEWLINE)

PUNCT_COMMA   = lex_to_atom(LexemeType.LEX_PUNCT, ",")
PUNCT_SEMI    = lex_to_atom(LexemeType.LEX_PUNCT, ";")
PUNCT_DOT     = lex_to_atom(LexemeType.LEX_PUNCT, ".")
PUNCT_LPAREN  = lex_to_atom(LexemeType.LEX_PUNCT, "(")
PUNCT_RPAREN  = lex_to_atom(LexemeType.LEX_PUNCT, ")")
PUNCT_LBRACK  = lex_to_atom(LexemeType.LEX_PUNCT, "[")
PUNCT_RBRACK  = lex_to_atom(LexemeType.LEX_PUNCT, "]")
PUNCT_LBRACE  = lex_to_atom(LexemeType.LEX_PUNCT, "{")
PUNCT_RBRACE  = lex_to_atom(LexemeType.LEX_PUNCT, "}")
PUNCT_POUND   = lex_to_atom(LexemeType.LEX_PUNCT, "#")

PUNCT_AT      = lex_to_atom(LexemeType.LEX_PUNCT, "@")

KW_MATCH      = lex_to_atom(LexemeType.LEX_KEYWORD, "match")
KW_CASE       = lex_to_atom(LexemeType.LEX_KEYWORD, "case")
KW_DEFAULT    = lex_to_atom(LexemeType.LEX_KEYWORD, "default")
KW_RETURN     = lex_to_atom(LexemeType.LEX_KEYWORD, "return")
KW_ELIF       = lex_to_atom(LexemeType.LEX_KEYWORD, "elif")
KW_ELSE       = lex_to_atom(LexemeType.LEX_KEYWORD, "else")
KW_IF         = lex_to_atom(LexemeType.LEX_KEYWORD, "if")
KW_SIGNED     = lex_to_atom(LexemeType.LEX_KEYWORD, "signed")
KW_UNSIGNED   = lex_to_atom(LexemeType.LEX_KEYWORD, "unsigned")
KW_FOR        = lex_to_atom(LexemeType.LEX_KEYWORD, "for")
# fmt : on

#---------------------------------------------------------------------------------------------------

cap_binop    = Capture(ATOM_BINOP)
cap_declop   = Capture(ATOM_DECLOP)
cap_assignop = Capture(ATOM_ASSIGNOP)
cap_affix    = Capture(ATOM_AFFIX)
cap_keyword  = Capture(ATOM_KEYWORD)

node_ident = ListNode(IdentNode,
  Seq(
    Opt(Capture(PUNCT_AT)),
    Some(
      Capture(PUNCT_DOT),
      Capture(ATOM_IDENT)
    )
  )
)

#---------------------------------------------------------------------------------------------------
# Forward decls

def parse_stmt(span, ctx2):
  return _parse_stmt(span, ctx2)

def node_expr(span, ctx2):
  return _node_expr(span, ctx2)

def node_decl(span, ctx2):
  return _node_decl(span, ctx2)

#---------------------------------------------------------------------------------------------------

# Parenthesized, comma-delimited lists of mixed expressions and declarations. Trailing commas OK.
# Examples: (348, "foo", x : u32 = 7), (), (1,)
node_paren = TupleNode(ParenNode,
  Railway({
    None         : [PUNCT_LPAREN],
    PUNCT_LPAREN : [node_expr, node_decl, PUNCT_RPAREN],
    node_expr    : [PUNCT_COMMA,          PUNCT_RPAREN],
    node_decl    : [PUNCT_COMMA,          PUNCT_RPAREN],
    PUNCT_COMMA  : [node_expr, node_decl, PUNCT_RPAREN],
    PUNCT_RPAREN : [None]
  })
)

# Same as above except []
node_brack = TupleNode(BrackNode,
  Railway({
    None         : [PUNCT_LBRACK],
    PUNCT_LBRACK : [node_expr, node_decl, PUNCT_RBRACK],
    node_expr    : [PUNCT_COMMA,          PUNCT_RBRACK],
    node_decl    : [PUNCT_COMMA,          PUNCT_RBRACK],
    PUNCT_COMMA  : [node_expr, node_decl, PUNCT_RPAREN],
    PUNCT_RBRACK : [None]
  })
)

# Curly-braced, semicolon-delimited lists of statements. Excess semicolons are OK. No semicolon
# after the last statement is OK.

stmt_delim = ListNode(BlockNode, Seq(PUNCT_LBRACE, Any(parse_stmt), PUNCT_RBRACE))
stmt_semi  = Seq(parse_stmt, PUNCT_SEMI)

stmt_delim_or_semi = Oneof(stmt_delim, stmt_semi)

#---------------------------------------------------------------------------------------------------

node_call = Node(CallNode, Seq(
  KeyVal("func",   Oneof(node_ident, Capture(ATOM_KEYWORD))),
  KeyVal("params", node_paren)
))

node_lambda = Node(LambdaNode, Seq(
  KeyVal("params", node_paren),
  KeyVal("body",   stmt_delim)
))

cat_atom = Oneof(
  node_paren,
  node_brack,
  stmt_delim,
  node_ident,
)

cat_list = TupleNode(CatNode, AtLeast(2, cat_atom))

parse_expr_unit = Seq(
  Any(cap_affix),
  Oneof(
    #node_call, # if you don't capture a call it'll just show up as a cat node
    cat_list,
    cat_atom,
    Capture(ATOM_INT),
    Capture(ATOM_FLOAT),
    Capture(ATOM_STRING),
  ),
  Any(cap_affix)
)

# unit op unit op unit...
_node_expr = ListNode(ExprNode, Seq(parse_expr_unit, Any(Seq(cap_binop, parse_expr_unit))))

node_cond = Node(CondNode, Seq(
  KeyVal("condition",    node_paren),
  KeyVal("then",         Seq(parse_stmt, Opt(PUNCT_SEMI))),
))

node_else = Node(CondNode, Seq(
  KeyVal("condition",    nothing),
  KeyVal("then",         Seq(parse_stmt, Opt(PUNCT_SEMI))),
))

node_if = ListNode(BranchNode, Seq(
      Seq(KW_IF,   node_cond),
  Any(Seq(KW_ELIF, node_cond)),
  Opt(Seq(KW_ELSE, node_else))
))

node_case = Node(CaseNode, Seq(
  KW_CASE,
  KeyVal("condition",  node_paren),
  KeyVal("body",       Seq(parse_stmt, Opt(PUNCT_SEMI))),
))

node_default = Node(DefaultNode, Seq(
  KW_DEFAULT,
  KeyVal("body", stmt_delim),
))

node_match = Node(MatchNode, Seq(
  KW_MATCH,
  KeyVal("condition", node_paren),
  PUNCT_LBRACE,
  KeyVal("body",
    ListNode(BlockNode, Any(Oneof(node_case, node_default)))
  ),
  PUNCT_RBRACE
))

node_type = Node(TypeNode, Seq(
  KeyVal("base", Oneof(
    node_call,
    node_paren,
    node_ident,
    cap_keyword
  )),
  Opt(KeyVal("suffix", node_brack))
))

node_for = Node(ForNode, Seq(
  KW_FOR,
  PUNCT_LPAREN,
  KeyVal("init", Opt(parse_stmt)),
  PUNCT_SEMI,
  KeyVal("cond", Opt(parse_stmt)),
  PUNCT_SEMI,
  KeyVal("step", Opt(parse_stmt)),
  PUNCT_RPAREN,
  KeyVal("body", stmt_delim_or_semi)
))

#----------------------------------------

decl_name = KeyVal("name", node_ident)
decl_dir  = KeyVal("dir",  Capture(ATOM_DECLOP))
decl_type = KeyVal("type", node_type)
decl_eq   = KeyVal("eq",   Capture(ATOM_ASSIGNOP))
decl_val  = KeyVal("val",  node_expr)

#_node_assign = Node(AssignNode, Seq(decl_name, decl_eq, decl_val))

_node_decl = Node(AtomNode, Railway({
  None      : [decl_name, decl_dir, decl_eq],
  decl_name : [decl_dir,  decl_eq],
  decl_dir  : [decl_type, None],
  decl_type : [decl_eq,   None],
  decl_eq   : [decl_val],
  decl_val  : [None]
}))

#_node_decl = Oneof(_node_assign, _node_decl2)

#----------------------------------------

node_marker = Node(MarkerNode, Seq(PUNCT_POUND, KeyVal("name", Capture(ATOM_IDENT))))
node_return = Node(ReturnNode, Seq(KW_RETURN,   KeyVal("val",  Opt(node_expr))))

_parse_stmt = Oneof(
  # Order matters!
  node_if,
  node_for,
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
  return matcheroni.apply(lexemes, ctx, parse_stmt)

#---------------------------------------------------------------------------------------------------

def dump_indent(indent):
  return "  " * indent

def dump_node(node, indent = 0):
  result = f"{node.__class__.__name__}{{}}\n"
  for key, val in node.items():
    if key == "span":
      continue
    result += dump_indent(indent + 1)
    if isinstance(key, int):
      result += f"[{key}] : "
    else:
      result += f".{key} : "
    result += dump_variant(val, indent + 1)
  return result

def dump_array(array, indent = 0):
  #base_list = array.__class__.__name__ == "list"
  result = f"{array.__class__.__name__}[{len(array)}]\n"
  for key, val in enumerate(array):
    result += dump_indent(indent + 1)
    result += f"[{key}] : "
    result += dump_variant(val, indent + 1)
    #if base_list:
    #    result += "\n"
    #    result += dump_indent(indent)
  return result

def dump_tuple(t, indent = 0):
  result = f"{t.__class__.__name__}({len(t)})\n"
  for key, val in enumerate(t):
    result += dump_indent(indent + 1)
    result += f"({key}) : "
    result += dump_variant(val, indent + 1)
  return result

def dump_lexeme(lexeme, *_):
  return f"{lexeme.lex_type.name} {lexeme.to_str()}\n"

def dump_variant(variant, indent = 0):
  result = ""
  if isinstance(variant, BaseNode):
    result += dump_node(variant, indent)
  elif isinstance(variant, dict):
    result += dump_node(variant, indent)
  elif isinstance(variant, list):
    result += dump_array(variant, indent)
  elif isinstance(variant, tuple):
    result += dump_tuple(variant, indent)
  elif isinstance(variant, Lexeme):
    result += dump_lexeme(variant, indent)
  elif variant is None:
    result += "<None>\n"
  else:
    result +=  f"??? {variant}\n"
  return result

def dump_tree(tree):
  return dump_variant(tree, 0).strip()

#---------------------------------------------------------------------------------------------------

testresult = doctest.testmod(sys.modules[__name__])
#print(f"Testing {__name__} : {testresult}")
