#define YYSTYPE TEMSTYPE
#define YYLTYPE TEMLTYPE
union TEMSTYPE;
struct TEMLTYPE;
#ifndef FLEX_SCANNER
#include "tempus_lex.h"
#endif

#include "tempus_yacc.h"

#include <stdio.h>
#include <vector>
#include <string>

std::vector<std::string> string_stack;

//------------------------------------------------------------------------------

int temerror (TEMLTYPE*, yyscan_t yyscanner, sexpr**  result, const char *msg) {
	fprintf(stderr, "--> %s\n", msg);
  return 0;
}

//------------------------------------------------------------------------------

void sexpr_free(sexpr *s)
{
	if (!s)
		return;

	if (s->type == SEXPR_ID)
		free(s->value.id);
	else if (s->type == SEXPR_PAIR)
	{
		sexpr_free(s->left);
		sexpr_free(s->right);
	}
	free(s);
}

//------------------------------------------------------------------------------

int main(int argc, char** argv) {
  printf("Hello World %d %p\n", argc, argv);

  yyscan_t scanner;
  temlex_init(&scanner);

  const char* source = R"(
  @x = 1;
  y : u32 = foo();
  )";

  YY_BUFFER_STATE buffer = tem_scan_string(source, scanner);
  sexpr* result = nullptr;
  temparse(scanner, &result);

  tem_delete_buffer(buffer, scanner);
  temlex_destroy(scanner);

  for (auto& s : string_stack) {
    printf("string stack %s\n", s.c_str());
  }

  return 0;
}

//------------------------------------------------------------------------------
