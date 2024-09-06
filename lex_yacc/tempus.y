%token IDENT
%token CONST_INT
%token CONST_FLOAT
%token CONST_STRING
%token TYPE_OP
%token ASSIGN_OP
%token BIN_OP

%token KW_IF
%token KW_ELSE
%token KW_MATCH
%token KW_CASE
%token KW_FOR

%%

program     : expr_block;

prefix      : '-' | '+' | '!';
bin_op      : BIN_OP | prefix;
const       : CONST_INT | CONST_FLOAT | CONST_STRING;

ident       : '@' IDENT | IDENT;
parens      : '(' expr_tuple ')';
braces      : '{' expr_block ')';
bracks      : '[' expr_tuple ']';

expr_atom   : ident | parens | braces | bracks;
atom_link   : expr_atom | '.' expr_atom;
atom_list   : atom_link | atom_link atom_list;

lhs_expr    : atom_list;
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

full_decl   : lhs_expr TYPE_OP type_expr ASSIGN_OP rhs_expr;
empty_decl  : lhs_expr TYPE_OP type_expr                   ;
assignment  : lhs_expr                   ASSIGN_OP rhs_expr;
typed_val   :          TYPE_OP type_expr ASSIGN_OP rhs_expr;
bare_name   : lhs_expr TYPE_OP                             ;
bare_type   :          TYPE_OP type_expr                   ;
bare_val    :                            ASSIGN_OP rhs_expr;
bare_expr   :                                      rhs_expr;

stmt_if     : KW_IF parens braces;
stmt_ifelse : KW_IF parens braces KW_ELSE braces;
stmt_case   : KW_CASE braces
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
  | stmt_for
;

opt_expr : expr | /**/ ;

expr_block : expr | expr ';' | expr ';' expr_block;
expr_tuple : expr | expr ',' | expr ',' expr_tuple;

%%
