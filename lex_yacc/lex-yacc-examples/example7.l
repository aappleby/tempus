%%

heater      { return KW_HEATER; }
heat        { return KW_HEAT; }
target      { return KW_TARGET; }
temperature { return KW_TEMP; }

on|off      { yylval.val_int = !strcmp(yytext,"on"); return CONST_STATE; }
[0-9]+      { yylval.val_int = atoi(yytext);         return CONST_NUMBER; }
[a-z0-9]+   { yylval.val_str = strdup(yytext);       return TOK_WORD; }

\n          { /* ignore end of line */; }
[ \t]+      { /* ignore whitespace */; }

%%
