#include <stdio.h>

//------------------------------------------------------------------------------

const char* buffer = "heater booom heater foo target temperature 100 heat on heater bar\n heat off\n heat on\n";
int cursor = 0;

int yy_input(char* buf, int max_size) {
  buf[0] = buffer[cursor++];
  return buf[0] != 0;
}

#define YY_INPUT(buf, result, max_size) { result = yy_input(buf, max_size); }

//------------------------------------------------------------------------------

extern "C" {
  void yyerror(const char *str) { fprintf(stderr,"error: %s\n",str); }
  int  yywrap ()                { return 1; }
}

const char* heater_default = "default";
const char *heater=heater_default;

//------------------------------------------------------------------------------

#include "example7_yacc.h"
#include "example7_lex.c"
#include "example7_yacc.c"

//------------------------------------------------------------------------------

int main(int argc, char** argv)
{
  yyparse();
  return 0;
}

//------------------------------------------------------------------------------
