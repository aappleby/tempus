#pragma once

#include <string>
#include <vector>

extern std::vector<std::string> string_stack;

union TEM_STYPE;         // defined in tempus_yacc.h
struct TEM_LTYPE;        // defined in tempus_yacc.h
typedef void* yyscan_t;  // needed for tem_lex prototype

enum sexpr_type {
  SEXPR_ID, SEXPR_NUM, SEXPR_PAIR, SEXPR_NIL
};

struct sexpr
{
  sexpr_type type;
  union
  {
    int   num;
    char *id;
  } value;
  sexpr *left, *right;
};

int tem_lex  (TEM_STYPE*, TEM_LTYPE*, yyscan_t);
int tem_error(TEM_LTYPE*, yyscan_t, sexpr**, const char*);

#define YYSTYPE TEM_STYPE
#define YYLTYPE TEM_LTYPE
#define YY_DECL int tem_lex(TEM_STYPE* yylval_param, TEM_LTYPE*, yyscan_t yyscanner)
