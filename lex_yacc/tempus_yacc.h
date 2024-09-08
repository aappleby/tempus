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
#ifndef TEM_DEBUG
# if defined YYDEBUG
#if YYDEBUG
#   define TEM_DEBUG 1
#  else
#   define TEM_DEBUG 0
#  endif
# else /* ! defined YYDEBUG */
#  define TEM_DEBUG 0
# endif /* ! defined YYDEBUG */
#endif  /* ! defined TEM_DEBUG */
#if TEM_DEBUG
extern int tem_debug;
#endif

/* Token kinds.  */
#ifndef TEM_TOKENTYPE
# define TEM_TOKENTYPE
  enum tem_tokentype
  {
    TEM_EMPTY = -2,
    TEM_EOF = 0,                   /* "end of file"  */
    TEM_error = 256,               /* error  */
    TEM_UNDEF = 257,               /* "invalid token"  */
    TOK_IDENT = 258,               /* TOK_IDENT  */
    TOK_INT = 259,                 /* TOK_INT  */
    TOK_FLOAT = 260,               /* TOK_FLOAT  */
    TOK_STRING = 261,              /* TOK_STRING  */
    OP_TYPE = 262,                 /* OP_TYPE  */
    OP_ASSIGN = 263,               /* OP_ASSIGN  */
    OP_BIN = 264,                  /* OP_BIN  */
    OP_AFFIX = 265,                /* OP_AFFIX  */
    KW_IF = 266,                   /* KW_IF  */
    KW_ELSE = 267,                 /* KW_ELSE  */
    KW_MATCH = 268,                /* KW_MATCH  */
    KW_CASE = 269,                 /* KW_CASE  */
    KW_FOR = 270                   /* KW_FOR  */
  };
  typedef enum tem_tokentype tem_token_kind_t;
#endif

/* Value type.  */
#if ! defined TEM_STYPE && ! defined TEM_STYPE_IS_DECLARED
union TEM_STYPE
{
#line 15 "tempus.y"

  int    val_int;
  double val_float;
  char*  val_str;
  sexpr* val_node;

#line 94 "tempus_yacc.h"

};
typedef union TEM_STYPE TEM_STYPE;
# define TEM_STYPE_IS_TRIVIAL 1
# define TEM_STYPE_IS_DECLARED 1
#endif

/* Location type.  */
#if ! defined TEM_LTYPE && ! defined TEM_LTYPE_IS_DECLARED
typedef struct TEM_LTYPE TEM_LTYPE;
struct TEM_LTYPE
{
  int first_line;
  int first_column;
  int last_line;
  int last_column;
};
# define TEM_LTYPE_IS_DECLARED 1
# define TEM_LTYPE_IS_TRIVIAL 1
#endif




int tem_parse (yyscan_t yyscanner, sexpr**  result);


#endif /* !YY_TEM_TEMPUS_YACC_H_INCLUDED  */
