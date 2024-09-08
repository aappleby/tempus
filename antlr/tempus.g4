grammar tempus;

//------------------------------------------------------------------------------

WS        : [ \t]+                    -> channel(HIDDEN);
NL        : ('\r' | '\n' | '\r' '\n') -> channel(HIDDEN);
MLC       : '/*' .*? '*/'             -> channel(HIDDEN);
SLC       : '//' ~[\r\n]*             -> channel(HIDDEN);
SEMI      : ';' ;
LPAREN    : '(' ;
RPAREN    : ')' ;
LBRACE    : '{' ;
RBRACE    : '}' ;
LBRACK    : '[' ;
RBRACK    : ']' ;
DOT       : '.' ;
PRIME     : '@' ;

KW_IF     : 'if' ;
KW_ELSE   : 'else' ;
KW_MATCH  : 'match' ;
KW_CASE   : 'case' ;
KW_FOR    : 'for' ;

OP_TYPE   : (':' | '>:' | '<:') ;
OP_BIN    : ('+' | '-' | '*' | '/' | '<' | '>' | '<<' | '>>' | '&' | '|' | '^') ;
OP_ASSIGN : ('=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|=') ;

TOK_INT       : [+-]? [1-9][0-9]* ;
TOK_FLOAT     : [+-]? [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)? [fF]? ;
TOK_STRING    : '"' ~["\\\r\n]* '"';
TOK_IDENT     : [a-zA-Z_] [a-zA-Z0-9_]* ;

//------------------------------------------------------------------------------

program     : expr_block;

prefix      : '-' | '+' | '!';
const       : TOK_INT | TOK_FLOAT | TOK_STRING;

ident       : '@'? TOK_IDENT;

parens      : '(' expr_tuple? ')';
braces      : '{' expr_block? ')';
bracks      : '[' expr_tuple? ']';

expr_atom   : ident | parens | braces | bracks;
atom_chain  : ('.'? expr_atom)+;

lhs_expr    : atom_chain;
type_expr   : atom_chain;

rhs_expr    : prefix? (atom_chain | const) (OP_BIN rhs_expr)?;

full_decl   : lhs_expr OP_TYPE type_expr OP_ASSIGN rhs_expr;
empty_decl  : lhs_expr OP_TYPE type_expr                   ;
assignment  : lhs_expr                   OP_ASSIGN rhs_expr;
typed_val   :          OP_TYPE type_expr OP_ASSIGN rhs_expr;
bare_name   : lhs_expr OP_TYPE                             ;
bare_type   :          OP_TYPE type_expr                   ;
bare_val    :                            OP_ASSIGN rhs_expr;
bare_expr   :                                      rhs_expr;

stmt_if     : KW_IF parens braces (KW_ELSE (braces | stmt_if))?;

stmt_case   : KW_CASE parens braces;
stmt_match  : KW_MATCH parens '{' stmt_case+ '}';
stmt_for    : KW_FOR '(' expr? ';' expr? ';' expr? ')' braces;

expr : full_decl
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

expr_block : expr (';' expr)*;
expr_tuple : expr (',' expr)*;

//------------------------------------------------------------------------------

dummy : ;
