#include <stdio.h>

void yyerror(char* c);

#include "tempus_yacc.h"
#include "tempus_lex.h"

#include "tempus_yacc.c"
#include "tempus_lex.c"

int main(int argc, char** argv) {
  printf("Hello World %d %p\n", argc, argv);
  yyparse();
  return 0;
}
