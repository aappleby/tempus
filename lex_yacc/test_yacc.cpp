#include "tempus_types.h" // must be before yacc/lex headers
#include "tempus_yacc.h"
#include "tempus_lex.h"

#include <stdio.h>
#include <vector>
#include <string>
#include <stddef.h>

std::vector<std::string> string_stack;

//------------------------------------------------------------------------------

int tem_error (TEM_LTYPE* ltype, yyscan_t yyscanner, sexpr**  result, const char *msg) {
	fprintf(stderr, "%d:%d - %d:%d --> %s\n",
    ltype->first_line, ltype->first_column,
    ltype->last_line,  ltype->last_column,
    msg);
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

int test_parse_file(const char* filename) {
  FILE* f = fopen(filename, "r");
  fseek(f, 0, SEEK_END);
  size_t size = ftell(f);

  char* buf = new char[size + 1];
  memset(buf, 0, size + 1);

  fseek(f, 0, SEEK_SET);
  fread(buf, size, 1, f);
  fclose(f);
  buf[size] = 0;

  printf("size %ld\n", size);
  printf("contents %s\n", buf);

  int result = test_parse(buf);
  delete [] buf;
  return result;
}

//------------------------------------------------------------------------------

const char* sources[] = {
  "# foo  @x = 1; y : u32 = foo();",

  "# prefix ++x",
  "# prefix ++x;",
  "# suffix x++",
  "# prefix --x",
  "# suffix x--",
  "# prefix !x",
  "# suffix x!",
  "# affix  x = !++!++!--!--!x!--!++--!++!",
  "# signs  x = a + +y - -y;",

  "# lhs [] = 1;",
  "# lhs () = 1;",
  "# lhs {} = 1;",
  "# lhs {}[]().()foo().[](){} = 1;",

  "# block { } ",
  "# block { };",
  "# block {;;};;",
  "# block {;;} ",
  "# block {;;};",
  "# block {;;} ",
  "# block {x : blah = 1;;} ",
  "# block {for(;;){}} ",
  "# block {for(;;);} ",

  "# if2 if (x) {} else {};",
  "# if3 if (x) {} elif () {};",
  "# if4 if (x) {} elif () {} else {};",
  "# if5 if (x) {} elif () {} elif () {};",
  "# if6 if (x) {} elif () {} elif () {} else {};",

  "# bar  a.b.c = zarp(blah : type = 229)()()[1,3,2];",
  "# for1 for (x : int = 0; x < 12; x++) { print(\"asldkflskjfd\"); }",

  "# func blah : func(int) = (x : int, y : int, z : int) { .  = (x,y,z) };"
  "# func blah : func(int) = (x : int, y : int, z : int) { .a = (x,y,z) };",

  "# match1 match (x) { case (foo) { .. = x } case (bar) {}   case (baz) {}   }",
  
  R"(
  # match2
  match (x) {
    x = 3;
    case (foo) { .. = x }
    x = 3;
    case (bar) {y}
    x = 3;
    case (baz) {z}
    x = 3;
  }
  )",
  
  "# match3 match (x) {}",

};

int main(int argc, char** argv) {
  printf("Hello World %d %p\n", argc, argv);

  for (auto source : sources) {
    printf("Parsing '%.12s'...\n", source);
    auto result = test_parse(source);
    if (result) printf("FAIL\n");
  }

  //const char* filename = "../uart_tem/simple_rx.tem";
  //const char* filename = "scratch.tem";
  //if (test_parse_file(filename) == 0) {
  //  printf("Parse OK\n");
  //}

  return 0;
}

//------------------------------------------------------------------------------
