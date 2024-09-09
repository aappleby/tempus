%define api.pure    full
%define api.prefix  {tem_}
%parse-param {yyscan_t yyscanner}
%lex-param   {yyscan_t yyscanner}
%parse-param {sexpr**  result}
%define parse.error verbose
%locations

%{
#include "tempus_types.h"
%}

//------------------------------------------------------------------------------

%union {
  int    val_int;
  double val_float;
  char*  val_str;
  sexpr* val_node;
}

//------------------------------------------------------------------------------

%token <val_str>   TOK_IDENT
%token <val_int>   TOK_INT
%token <val_float> TOK_FLOAT
%token <val_str>   TOK_STRING
%token <val_str>   OP_TYPE
%token <val_str>   OP_ASSIGN
%token <val_str>   OP_BIN
%token <val_str>   OP_AFFIX

%token KW_IF
%token KW_ELSE
%token KW_MATCH
%token KW_CASE
%token KW_FOR

//------------------------------------------------------------------------------

%%

program     : section | section program;
section     : marker expr_block;

marker      : '#' TOK_IDENT;

const       : TOK_INT | TOK_FLOAT | TOK_STRING;

ident       : '@' TOK_IDENT | TOK_IDENT;

parens      : '(' expr_tuple ')';
braces      : '{' expr_block '}';
bracks      : '[' expr_tuple ']';

delimited   : parens | braces | bracks;

expr_atom   : ident | parens | braces | bracks;
atom_link   : expr_atom | '.' expr_atom;
atom_chain  : atom_link | atom_link atom_chain;

lhs_expr    : atom_chain | '.';
type_expr   : atom_chain;

op_type : OP_TYPE | ':';
op_bin  : OP_BIN   | '+' | '-';
prefix  : OP_AFFIX | '+' | '-';
suffix  : OP_AFFIX;

prefix_chain : atom_chain   | prefix prefix_chain;
affix_chain  : prefix_chain | affix_chain suffix;

rhs_expr    : affix_chain expr_tail | const expr_tail;
expr_tail   : op_bin rhs_expr  | /**/;

full_decl   : lhs_expr op_type type_expr OP_ASSIGN rhs_expr;
empty_decl  : lhs_expr op_type type_expr                   ;

assignment  : lhs_expr                   OP_ASSIGN rhs_expr;

typed_val   :          op_type type_expr OP_ASSIGN rhs_expr;
bare_name   : lhs_expr op_type                             ;
bare_type   :          op_type type_expr                   ;
bare_val    :                            OP_ASSIGN rhs_expr;
bare_expr   :                                      rhs_expr;

stmt_if     : KW_IF parens delimited | KW_IF parens delimited else_chain;
else_chain  : KW_ELSE delimited | KW_ELSE stmt_if;

stmt_case   : KW_CASE parens expr
case_block  : stmt_case | stmt_case case_block;
stmt_match  : KW_MATCH parens '{' case_block '}';
stmt_for    : KW_FOR '(' opt_expr ';' opt_expr ';' opt_expr ')' expr;

expr
  : full_decl
  | empty_decl
  | assignment
  | typed_val
  | bare_name
  | bare_type
  | bare_val
  | bare_expr
  | stmt_if
  | stmt_match
  | stmt_for;

opt_expr : expr | /**/ ;

expr_block : /**/ | expr | expr ';' expr_block;
expr_tuple : /**/ | expr | expr ',' expr_tuple;

%%

//------------------------------------------------------------------------------
