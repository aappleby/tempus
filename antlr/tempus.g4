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

TYPE_OP   : (':' | '>:' | '<:') ;
BINARY_OP : ('+' | '-' | '*' | '/' | '<' | '>' | '<<' | '>>' | '&' | '|' | '^') ;
ASSIGN_OP : ('=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|=') ;

INT       : [+-]? [1-9][0-9]* ;
FLOAT     : [+-]? [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)? [fF]? ;
STRING    : '"' ~["\\\r\n]* '"';
IDENT     : [a-zA-Z_] [a-zA-Z0-9_]* ;

//------------------------------------------------------------------------------

program:	(stmt ';')* ;

ident        : '@'? '.'? IDENT ('.' IDENT)* ;
//bare_ident   : ident ':' ;
//bare_type    : ':' expr  ;
//bare_value   : '(' '=' expr ')' ;
uninit_decl  : ident TYPE_OP expr ;
untyped_decl : ident ASSIGN_OP expr ;
typed_expr   : TYPE_OP expr ASSIGN_OP expr ;
full_decl    : ident TYPE_OP expr ASSIGN_OP expr ;
constant     : INT | FLOAT | STRING ;

atom
  : full_decl
  | uninit_decl
  | untyped_decl
  | typed_expr
//  | '(' bare_type ')'
//  | '(' bare_ident ')'
//  | '(' '=' expr ')'
  | ident
  | constant
  | paren_list
  | brack_list
  | brace_list
;

expr  : atom+ (BINARY_OP atom+)* ;

if_stmt
  : KW_IF paren_list stmt 'else' stmt
  | KW_IF paren_list stmt ;

match_stmt : KW_MATCH paren_list brace_list;
case_stmt  : KW_CASE paren_list brace_list;

stmt : atom | if_stmt | match_stmt | case_stmt;

stmt_list
  : stmt (',' stmt)*
  | stmt (';' stmt)* ';'? ;

paren_list  : '(' stmt_list? ')' ;
brace_list  : '{' stmt_list? '}' ;
brack_list  : '[' stmt_list? ']' ;

//------------------------------------------------------------------------------

dummy : ;
