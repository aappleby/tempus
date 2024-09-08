#include "tempus_types.h" // must be before yacc/lex headers
#include "tempus_yacc.h"
#include "tempus_lex.h"

#include <stdio.h>
#include <vector>
#include <string>

std::vector<std::string> string_stack;

//------------------------------------------------------------------------------

int tem_error (TEM_LTYPE*, yyscan_t yyscanner, sexpr**  result, const char *msg) {
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

int test_parse(const char* source) {
  yyscan_t scanner;
  temlex_init(&scanner);

  YY_BUFFER_STATE buffer = tem_scan_string(source, scanner);
  sexpr* node = nullptr;
  auto result = tem_parse(scanner, &node);

  tem_delete_buffer(buffer, scanner);
  temlex_destroy(scanner);
  return result;
}

//------------------------------------------------------------------------------

const char* sources[] = {
  "# foo  @x = 1; y : u32 = foo();",

  "# prefix ++x",
  "# suffix x++",
  "# prefix --x",
  "# suffix x--",
  "# prefix !x",
  "# suffix x!",

  "# if1 if (x) {}",
  "# if2 if (x) {} else {}",
  "# if3 if (x) {} else if () {}",
  "# if4 if (x) {} else if () {} else {}",
  "# if5 if (x) {} else if () {} else if () {}",
  "# if6 if (x) {} else if () {} else if () {} else {}",

  // why u no work
  //"# sign x = -y;",

  "# bar  a.b.c = zarp(blah : type = 229)()()[1,3,2];",
  "# asd  for (x : int = 0; x < 12; x = x + 1) { print(\"asldkflskjfd\") }",

  // isolated dot doesn't work as ident
  //"# func blah : func(int) = (x : int, y : int, z : int) { . = (x,y,z) };"

  "# func blah : func(int) = (x : int, y : int, z : int) { .a = (x,y,z) };"
};

int main(int argc, char** argv) {
  printf("Hello World %d %p\n", argc, argv);

  for (auto source : sources) {
    printf("Parsing '%.12s'...\n", source);
    auto result = test_parse(source);
    if (result) printf("FAIL\n");
  }

  return 0;
}

//------------------------------------------------------------------------------
