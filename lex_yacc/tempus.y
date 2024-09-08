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

prefix      : '-' | '+' | '!';
const       : TOK_INT | TOK_FLOAT | TOK_STRING;

ident       : '@' TOK_IDENT | TOK_IDENT;

parens      : '(' expr_tuple ')';
braces      : '{' expr_block '}';
bracks      : '[' expr_tuple ']';

expr_atom   : ident | parens | braces | bracks;
atom_link   : expr_atom | '.' expr_atom;
atom_chain  : atom_link | atom_link atom_chain;

lhs_expr    : atom_chain;
type_expr   : atom_chain;

rhs_expr  : prefix    rhs_expr2 |       rhs_expr2;
rhs_expr2 : atom_chain rhs_expr3 | const rhs_expr3;
rhs_expr3 : OP_BIN    rhs_expr  | /**/;

full_decl   : lhs_expr OP_TYPE type_expr OP_ASSIGN rhs_expr;
empty_decl  : lhs_expr OP_TYPE type_expr                   ;

assignment  : lhs_expr                   OP_ASSIGN rhs_expr;

typed_val   :          OP_TYPE type_expr OP_ASSIGN rhs_expr;
bare_name   : lhs_expr OP_TYPE                             ;
bare_type   :          OP_TYPE type_expr                   ;
bare_val    :                            OP_ASSIGN rhs_expr;
bare_expr   :                                      rhs_expr;

stmt_if     : KW_IF parens braces;

stmt_ifelse
  : KW_IF parens braces KW_ELSE braces
  | KW_IF parens braces KW_ELSE stmt_if
;

stmt_case   : KW_CASE parens braces
case_block  : stmt_case | stmt_case case_block;
stmt_match  : KW_MATCH parens '{' case_block '}';
stmt_for    : KW_FOR '(' opt_expr ';' opt_expr ';' opt_expr ')' braces

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
  | stmt_ifelse
  | stmt_match
  | stmt_for;

opt_expr : expr | /**/ ;

expr_block : /**/ | expr | expr ';' expr_block;
expr_tuple : /**/ | expr | expr ',' expr_tuple;

%%

//------------------------------------------------------------------------------
