#include <stdio.h>

//------------------------------------------------------------------------------

const char* buffer = R"(
@x = 1;
y : u32 = foo();
)";

int cursor = 0;

int yy_input(char* buf, int max_size) {
  buf[0] = buffer[cursor++];
  return buf[0] != 0;
}

//------------------------------------------------------------------------------

void yyerror(const char *str) { fprintf(stderr,"error: %s\n",str); }
int  yywrap ()                { return 1; }

//------------------------------------------------------------------------------

#include <vector>
#include <string>

std::vector<std::string> string_stack;


#include "tempus_yacc.h"
#include "tempus_lex.h"

//------------------------------------------------------------------------------

int main(int argc, char** argv) {
  printf("Hello World %d %p\n", argc, argv);

  //yyparse();

  yyscan_t scanner;
  yylex_init(&scanner);
  yyparse(scanner);
  yylex_destroy(scanner);

  for (auto& s : string_stack) {
    printf("string stack %s\n", s.c_str());
  }

  return 0;
}

//------------------------------------------------------------------------------
