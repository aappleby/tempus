%{
#include <stdio.h>
#include "tempus_yacc.h"
%}

D           [0-9]
L           [a-zA-Z_]
H           [a-fA-F0-9]
E           [Ee][+-]?{D}+

%%

"if"        { return(KW_IF); }
"else"      { return(KW_ELSE); }
"match"     { return(KW_MATCH); }
"case"      { return(KW_CASE); }
"for"       { return(KW_FOR); }

{L}({L}|{D})*      { return(TOK_IDENT); }
0[xX]{H}+          { return(TOK_INT); }
{D}+               { return(TOK_INT); }
{D}+{E}            { return(TOK_FLOAT); }
{D}+"."{D}*({E})?  { return(TOK_FLOAT); }
\"(\\.|[^\\"])*\"  { return(TOK_STRING); }

">>="       { return(OP_ASSIGN); }
"<<="       { return(OP_ASSIGN); }
"+="        { return(OP_ASSIGN); }
"-="        { return(OP_ASSIGN); }
"*="        { return(OP_ASSIGN); }
"/="        { return(OP_ASSIGN); }
"%="        { return(OP_ASSIGN); }
"&="        { return(OP_ASSIGN); }
"^="        { return(OP_ASSIGN); }
"|="        { return(OP_ASSIGN); }
"="         { return(OP_ASSIGN); }

">:"        { return(OP_TYPE); }
"<:"        { return(OP_TYPE); }
":"         { return(OP_TYPE); }

">>"        { return(OP_BIN); }
"<<"        { return(OP_BIN); }
"&&"        { return(OP_BIN); }
"||"        { return(OP_BIN); }
"<="        { return(OP_BIN); }
">="        { return(OP_BIN); }
"=="        { return(OP_BIN); }
"!="        { return(OP_BIN); }

"+"         { return(OP_BIN); }
"-"         { return(OP_BIN); }
"*"         { return(OP_BIN); }
"/"         { return(OP_BIN); }
"%"         { return(OP_BIN); }
"&"         { return(OP_BIN); }
"|"         { return(OP_BIN); }
"^"         { return(OP_BIN); }
"<"         { return(OP_BIN); }
">"         { return(OP_BIN); }

[ \t\v\n\f] { }
.           { return yytext[0]; }

%%
int yywrap() { return(1); }
