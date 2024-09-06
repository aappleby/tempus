%token IDENT
%token CONST_INT
%token CONST_FLOAT
%token CONST_STRING
%token TYPE_OP
%token ASSIGN_OP
%token BIN_OP
%token SCOPE

%token KW_IF
%token KW_ELSE
%token KW_MATCH
%token KW_CASE

%%

program    : expr_block;

prefix     : '-' | '+' | '!';
bin_op     : BIN_OP | prefix;
const      : CONST_INT | CONST_FLOAT | CONST_STRING;

ident      : '@' IDENT | IDENT;
parens     : '(' expr_tuple ')';
braces     : '{' expr_block ')';
expr_atom  : ident | parens | braces;

atom_link  : expr_atom | '.' expr_atom | SCOPE expr_atom;
atom_list  : atom_link | atom_link atom_list;

lhs_expr   : atom_list;
type_expr  : atom_list;
rhs_expr
  : prefix atom_list
  | prefix atom_list bin_op rhs_expr
  |        atom_list
  |        atom_list bin_op rhs_expr
  | const
;

full_decl    : lhs_expr TYPE_OP type_expr ASSIGN_OP rhs_expr;
uninint_decl : lhs_expr TYPE_OP type_expr                   ;
assignment   : lhs_expr                   ASSIGN_OP rhs_expr;
typed_val    :          TYPE_OP type_expr ASSIGN_OP rhs_expr;
bare_name    : lhs_expr TYPE_OP                             ;
bare_type    :          TYPE_OP type_expr                   ;
bare_val     :                            ASSIGN_OP rhs_expr;
bare_expr    :                                      rhs_expr;

stmt_if
  : KW_IF parens braces
  | KW_IF parens braces KW_ELSE braces

stmt_case  : KW_CASE braces
case_block : stmt_case | stmt_case case_block;
stmt_match : KW_MATCH parens '{' case_block '}';

expr
  : full_decl
  | uninint_decl
  | assignment
  | typed_val
  | bare_name
  | bare_type
  | bare_val
  | bare_expr
  | stmt_if
  | stmt_match
;

expr_block : expr | expr ';' | expr ';' expr_block;
expr_tuple : expr | expr ',' | expr ',' expr_tuple;

%%
