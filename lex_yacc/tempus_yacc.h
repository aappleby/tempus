/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_TEM_TEMPUS_YACC_H_INCLUDED
# define YY_TEM_TEMPUS_YACC_H_INCLUDED
/* Debug traces.  */
#ifndef TEMDEBUG
# if defined YYDEBUG
#if YYDEBUG
#   define TEMDEBUG 1
#  else
#   define TEMDEBUG 0
#  endif
# else /* ! defined YYDEBUG */
#  define TEMDEBUG 0
# endif /* ! defined YYDEBUG */
#endif  /* ! defined TEMDEBUG */
#if TEMDEBUG
extern int temdebug;
#endif
/* "%code requires" blocks.  */
#line 9 "tempus.y"


// #*#*#---------- BEGIN REQUIRES
#define YYSTYPE TEMSTYPE
#define YYLTYPE TEMLTYPE
union TEMSTYPE;
struct TEMLTYPE;
#ifndef FLEX_SCANNER
#include "tempus_lex.h"
#endif

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

int temlex  (TEMSTYPE*, TEMLTYPE*, yyscan_t);
int temerror(TEMLTYPE* , yyscan_t, sexpr**, const char*);

#undef  YY_DECL
#define YY_DECL int temlex (TEMSTYPE* yylval_param, TEMLTYPE* asdlfksj, yyscan_t yyscanner)

// #*#*#---------- END REQUIRES

#line 92 "tempus_yacc.h"

/* Token kinds.  */
#ifndef TEMTOKENTYPE
# define TEMTOKENTYPE
  enum temtokentype
  {
    TEMEMPTY = -2,
    TEMEOF = 0,                    /* "end of file"  */
    TEMerror = 256,                /* error  */
    TEMUNDEF = 257,                /* "invalid token"  */
    TOK_IDENT = 258,               /* TOK_IDENT  */
    TOK_INT = 259,                 /* TOK_INT  */
    TOK_FLOAT = 260,               /* TOK_FLOAT  */
    TOK_STRING = 261,              /* TOK_STRING  */
    OP_TYPE = 262,                 /* OP_TYPE  */
    OP_ASSIGN = 263,               /* OP_ASSIGN  */
    OP_BIN = 264,                  /* OP_BIN  */
    KW_IF = 265,                   /* KW_IF  */
    KW_ELSE = 266,                 /* KW_ELSE  */
    KW_MATCH = 267,                /* KW_MATCH  */
    KW_CASE = 268,                 /* KW_CASE  */
    KW_FOR = 269                   /* KW_FOR  */
  };
  typedef enum temtokentype temtoken_kind_t;
#endif

/* Value type.  */
#if ! defined TEMSTYPE && ! defined TEMSTYPE_IS_DECLARED
union TEMSTYPE
{
#line 60 "tempus.y"

  int    val_int;
  double val_float;
  char*  val_str;
  sexpr* val_node;

#line 130 "tempus_yacc.h"

};
typedef union TEMSTYPE TEMSTYPE;
# define TEMSTYPE_IS_TRIVIAL 1
# define TEMSTYPE_IS_DECLARED 1
#endif

/* Location type.  */
#if ! defined TEMLTYPE && ! defined TEMLTYPE_IS_DECLARED
typedef struct TEMLTYPE TEMLTYPE;
struct TEMLTYPE
{
  int first_line;
  int first_column;
  int last_line;
  int last_column;
};
# define TEMLTYPE_IS_DECLARED 1
# define TEMLTYPE_IS_TRIVIAL 1
#endif




int temparse (yyscan_t yyscanner, sexpr**  result);


#endif /* !YY_TEM_TEMPUS_YACC_H_INCLUDED  */
