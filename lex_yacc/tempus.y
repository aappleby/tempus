/*%define api.pure full*/
//%lex-param {yyscan_t scanner}
//%parse-param {yyscan_t scanner}

//%param { YYSTYPE * yylval }

%{
  #include "tempus_lex.h"

  #include <string>
  #include <vector>

  extern std::vector<std::string> string_stack;

  void yyerror(const char* c);

  #define YY_DECL int yylex(YYSTYPE * yylval, yyscan_t scanner)


%}

//------------------------------------------------------------------------------

%union {
  int    val_int;
  double val_float;
  char*  val_str;
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

//program : stmt ';' { printf("program!\n"); }
//stmt : ident OP_ASSIGN TOK_INT;
//ident : TOK_IDENT { printf("ident %s\n", $1); }

program     : expr_block;

prefix      : '-' | '+' | '!';
bin_op      : OP_BIN | prefix;
const       : TOK_INT | TOK_FLOAT | TOK_STRING;

ident       : '@' TOK_IDENT { printf("primed %s\n", $2); string_stack.push_back($2); } | TOK_IDENT
{
  int y = 0;
  printf("ident %s\n", $1);
  string_stack.push_back($1);
  y++;
};

parens      : '(' expr_tuple ')';
braces      : '{' expr_block ')';
bracks      : '[' expr_tuple ']';

expr_atom   : ident | parens | braces | bracks;
atom_link   : expr_atom | '.' expr_atom;
atom_list   : atom_link | atom_link atom_list;

lhs_expr    : atom_list { printf("lhs_expr\n"); };
type_expr   : atom_list;
rhs_expr
  : prefix atom_list bin_op rhs_expr
  |        atom_list bin_op rhs_expr
  | prefix const     bin_op rhs_expr
  |        const     bin_op rhs_expr
  | prefix atom_list
  |        atom_list
  | prefix const
  |        const
;

full_decl   : lhs_expr OP_TYPE type_expr OP_ASSIGN rhs_expr;
empty_decl  : lhs_expr OP_TYPE type_expr                   ;

assignment  : lhs_expr                   OP_ASSIGN rhs_expr {
  int x = 0;
  printf("Assignment %s\n", $2);
  string_stack.push_back($2);
  x++;
}

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
  | assignment { printf("expr assignment\n"); }
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
