%option nounput noinput noyywrap reentrant bison-bridge 

%{
#include <stdio.h>
#include "tempus_yacc.h"

int yy_input(char* buf, int max_size);
#define YY_INPUT(buf, result, max_size) { result = yy_input(buf, max_size); }

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

{L}({L}|{D})*      { yylval->val_str   = strdup(yytext);       return(TOK_IDENT); }
0[xX]{H}+          { yylval->val_int   = atoi(yytext);         return(TOK_INT); }
{D}+               { yylval->val_int   = atoi(yytext);         return(TOK_INT); }
{D}+{E}            { yylval->val_float = atof(yytext);         return(TOK_FLOAT); }
{D}+"."{D}*({E})?  { yylval->val_float = atof(yytext);         return(TOK_FLOAT); }
\"(\\.|[^\\"])*\"  { yylval->val_str   = strdup(yytext);       return(TOK_STRING); }

">>="       { yylval->val_str = strdup(yytext);       return(OP_ASSIGN); }
"<<="       { yylval->val_str = strdup(yytext);       return(OP_ASSIGN); }
"+="        { yylval->val_str = strdup(yytext);       return(OP_ASSIGN); }
"-="        { yylval->val_str = strdup(yytext);       return(OP_ASSIGN); }
"*="        { yylval->val_str = strdup(yytext);       return(OP_ASSIGN); }
"/="        { yylval->val_str = strdup(yytext);       return(OP_ASSIGN); }
"%="        { yylval->val_str = strdup(yytext);       return(OP_ASSIGN); }
"&="        { yylval->val_str = strdup(yytext);       return(OP_ASSIGN); }
"^="        { yylval->val_str = strdup(yytext);       return(OP_ASSIGN); }
"|="        { yylval->val_str = strdup(yytext);       return(OP_ASSIGN); }
"="         { yylval->val_str = strdup(yytext);       return(OP_ASSIGN); }

">:"        { yylval->val_str = strdup(yytext);       return(OP_TYPE); }
"<:"        { yylval->val_str = strdup(yytext);       return(OP_TYPE); }
":"         { yylval->val_str = strdup(yytext);       return(OP_TYPE); }

">>"        { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"<<"        { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"&&"        { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"||"        { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"<="        { yylval->val_str = strdup(yytext);       return(OP_BIN); }
">="        { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"=="        { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"!="        { yylval->val_str = strdup(yytext);       return(OP_BIN); }

"+"         { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"-"         { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"*"         { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"/"         { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"%"         { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"&"         { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"|"         { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"^"         { yylval->val_str = strdup(yytext);       return(OP_BIN); }
"<"         { yylval->val_str = strdup(yytext);       return(OP_BIN); }
">"         { yylval->val_str = strdup(yytext);       return(OP_BIN); }

[ \t\v\n\f] { }
.           { return yytext[0]; }

%%
