#include "tempus_yacc.h"
#include "tempus_lex.h"

#include <stdio.h>
#include <vector>
#include <string>

std::vector<std::string> string_stack;

//------------------------------------------------------------------------------

void yyerror (yyscan_t locp, sexpr** result, char const *msg) {
	fprintf(stderr, "--> %s\n", msg);
}

//------------------------------------------------------------------------------

int main(int argc, char** argv) {
  printf("Hello World %d %p\n", argc, argv);

  yyscan_t scanner;
  yylex_init(&scanner);

  const char* source = R"(
  @x = 1;
  y : u32 = foo();
  )";

  YY_BUFFER_STATE buffer = yy_scan_string(source, scanner);
  sexpr* result = nullptr;
  yyparse(scanner, &result);

  yy_delete_buffer(buffer, scanner);
  yylex_destroy(scanner);

  for (auto& s : string_stack) {
    printf("string stack %s\n", s.c_str());
  }

  return 0;
}

//------------------------------------------------------------------------------
