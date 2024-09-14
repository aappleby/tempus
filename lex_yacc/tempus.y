%start  program
%define api.pure    full
%define api.prefix  {tem_}
%define parse.error verbose
%locations

%parse-param {yyscan_t yyscanner}
%lex-param   {yyscan_t yyscanner}
%parse-param {sexpr**  result}

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

%token <val_str>   TOK_MARKER
%token <val_str>   TOK_IDENT
%token <val_int>   TOK_INT
%token <val_float> TOK_FLOAT
%token <val_str>   TOK_STRING
%token <val_str>   OP_TYPE
%token <val_str>   OP_ASSIGN
%token <val_str>   OP_BIN
%token <val_str>   OP_AFFIX

%token KW_IF
%token KW_THEN
%token KW_ELIF
%token KW_ELSE
%token KW_MATCH
%token KW_CASE
%token KW_FOR

%%

//------------------------------------------------------------------------------

marker      : TOK_MARKER;
const       : TOK_INT | TOK_FLOAT | TOK_STRING;
ident       : TOK_IDENT;

op_type     : OP_TYPE | ':';
op_bin      : OP_BIN   | '+' | '-';
op_assign   : OP_ASSIGN;
prefix      : OP_AFFIX | '+' | '-';
suffix      : OP_AFFIX;

//------------------------------------------------------------------------------

program     : block;

parens      : '(' list ')';
braces      : '{' block '}';
bracks      : '[' list ']';
atom        : ident | parens | braces | bracks;

ident_term  : atom | '.';
ident_path  : ident_term ident_path | ident_term;

expr        : expr_prefix expr_term expr_suffix expr_chain;
expr_prefix : prefix expr_prefix | /**/;
expr_term   : ident_path | const;
expr_suffix : suffix expr_suffix | /**/;
expr_chain  : op_bin expr | /**/;

stmt        : expr stmt_dir | expr op_assign expr | stmt_dir | op_assign expr | expr;
stmt_dir    : op_type stmt_type | op_type;
stmt_type   : expr op_assign stmt | expr op_assign flow | expr;
opt_stmt    : stmt | /**/;

list        : stmt tail | /**/;
tail        : ',' stmt tail | /**/;

block       : marker block | flow block | stmt ';' block | ';' block | stmt | /**/;

for         : KW_FOR '(' opt_stmt ';' opt_stmt ';' opt_stmt ')' braces;
if          : KW_IF   parens braces elif else;
elif        : KW_ELIF parens braces elif | /**/;
else        : KW_ELSE braces | /**/;
match       : KW_MATCH parens braces;
case        : KW_CASE  parens braces;
flow        : for | if | match | case;

//------------------------------------------------------------------------------

%%

