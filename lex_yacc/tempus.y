%start  block_start
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

marker         : '#' TOK_IDENT;
const          : TOK_INT | TOK_FLOAT | TOK_STRING;
ident          : '@' TOK_IDENT | TOK_IDENT;

op_type        : OP_TYPE | ':';
op_bin         : OP_BIN   | '+' | '-';
op_assign      : OP_ASSIGN;
prefix         : OP_AFFIX | '+' | '-';
suffix         : OP_AFFIX;

parens         : '(' list_start ')';
braces         : '{' block_start '}';
bracks         : '[' list_start ']';
atom           : ident | parens | braces | bracks;

//----------------------------------------


ident_start    :              ident_node;
ident_start    :              ident_dot;
ident_node     : atom         ident_start;
ident_node     : atom         ident_end;
ident_dot      : '.'          ident_start;
ident_dot      : '.'          ident_end;
ident_end      :              /**/;

//----------

expr_start     :              expr_prefix;
expr_prefix    : prefix       expr_prefix;
expr_prefix    :              expr_term;
expr_term      : ident_start  expr_suffix;
expr_term      : const        expr_suffix;
expr_suffix    : suffix       expr_suffix;
expr_suffix    :              expr_chain;
expr_chain     : op_bin       expr_start;
expr_chain     :              expr_end;
expr_end       :              /**/

//----------

stmt_start     :              stmt_lhs;
stmt_start     :              stmt_dir;
stmt_start     :              stmt_assign;
stmt_start     :              stmt_rhs;
stmt_lhs       : expr_start   stmt_dir;
stmt_lhs       : expr_start   stmt_assign;
stmt_dir       : op_type      stmt_type;
stmt_dir       : op_type      stmt_end;
stmt_type      : expr_start   stmt_assign;
stmt_type      : expr_start   stmt_end;
stmt_assign    : op_assign    stmt_rhs;
stmt_rhs       : expr_start   stmt_end;
stmt_end       :              /**/;

//----------

list_start     :              list_node;
list_start     :              list_end;
list_node      : stmt_start   list_delim;
list_node      : stmt_start   list_end;
list_delim     : ','          list_node;
list_end       :              /**/;

//----------
// Do I want KW_THEN?

ifelse_start   : KW_IF        ifelse_parens;
ifelse_parens  : parens       ifelse_body;
ifelse_body    : braces       ifelse_elif;
ifelse_body    : braces       ifelse_else;
ifelse_body    : braces       ifelse_end;
ifelse_elif    : KW_ELIF      ifelse_parens;
ifelse_else    : KW_ELSE      ifelse_tail;
ifelse_tail    : braces       ifelse_end;
ifelse_end     :              /**/;

//----------

match_start    : KW_MATCH     match_parens;
match_parens   : parens       match_body;
match_body     : braces       match_end;
match_end      :              /**/;

//----------

case_start     : KW_CASE      case_parens;
case_parens    : parens       case_body;
case_body      : braces       case_end;
case_end       :              /**/;

//----------

for_start      : KW_FOR       for_lparen;
for_lparen     : '('          for_init;
for_init       : stmt_start   for_semi1;
for_init       :              for_semi1;
for_semi1      : ';'          for_cond;
for_cond       : stmt_start   for_semi2;
for_cond       :              for_semi2;
for_semi2      : ';'          for_step;
for_step       : stmt_start   for_rparen;
for_step       :              for_rparen;
for_rparen     : ')'          for_end;
for_end        : braces       /**/;
for_end        : ';'          /**/;

//----------

flow_start     : ifelse_start | match_start | for_start | case_start;

//----------

block_start    :              block_mark;
block_start    :              block_flow;
block_start    :              block_stmt;
block_start    :              block_delim;
block_start    :              block_end;

block_mark     : marker       block_start;
block_flow     : flow_start   block_start;

block_stmt     : stmt_start   block_delim;
block_stmt     : stmt_start   block_end;

block_delim    : ';'          block_start;

block_end      :              /**/;

//------------------------------------------------------------------------------

%%

