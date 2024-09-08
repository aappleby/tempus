#ifndef temHEADER_H
#define temHEADER_H 1
#define temIN_HEADER 1

#line 6 "tempus_lex.h"

#line 8 "tempus_lex.h"

#define  YY_INT_ALIGNED short int

/* A lexical scanner generated by flex */

#define FLEX_SCANNER
#define YY_FLEX_MAJOR_VERSION 2
#define YY_FLEX_MINOR_VERSION 6
#define YY_FLEX_SUBMINOR_VERSION 4
#if YY_FLEX_SUBMINOR_VERSION > 0
#define FLEX_BETA
#endif

#ifdef yy_create_buffer
#define tem_create_buffer_ALREADY_DEFINED
#else
#define yy_create_buffer tem_create_buffer
#endif

#ifdef yy_delete_buffer
#define tem_delete_buffer_ALREADY_DEFINED
#else
#define yy_delete_buffer tem_delete_buffer
#endif

#ifdef yy_scan_buffer
#define tem_scan_buffer_ALREADY_DEFINED
#else
#define yy_scan_buffer tem_scan_buffer
#endif

#ifdef yy_scan_string
#define tem_scan_string_ALREADY_DEFINED
#else
#define yy_scan_string tem_scan_string
#endif

#ifdef yy_scan_bytes
#define tem_scan_bytes_ALREADY_DEFINED
#else
#define yy_scan_bytes tem_scan_bytes
#endif

#ifdef yy_init_buffer
#define tem_init_buffer_ALREADY_DEFINED
#else
#define yy_init_buffer tem_init_buffer
#endif

#ifdef yy_flush_buffer
#define tem_flush_buffer_ALREADY_DEFINED
#else
#define yy_flush_buffer tem_flush_buffer
#endif

#ifdef yy_load_buffer_state
#define tem_load_buffer_state_ALREADY_DEFINED
#else
#define yy_load_buffer_state tem_load_buffer_state
#endif

#ifdef yy_switch_to_buffer
#define tem_switch_to_buffer_ALREADY_DEFINED
#else
#define yy_switch_to_buffer tem_switch_to_buffer
#endif

#ifdef yypush_buffer_state
#define tempush_buffer_state_ALREADY_DEFINED
#else
#define yypush_buffer_state tempush_buffer_state
#endif

#ifdef yypop_buffer_state
#define tempop_buffer_state_ALREADY_DEFINED
#else
#define yypop_buffer_state tempop_buffer_state
#endif

#ifdef yyensure_buffer_stack
#define temensure_buffer_stack_ALREADY_DEFINED
#else
#define yyensure_buffer_stack temensure_buffer_stack
#endif

#ifdef yylex
#define temlex_ALREADY_DEFINED
#else
#define yylex temlex
#endif

#ifdef yyrestart
#define temrestart_ALREADY_DEFINED
#else
#define yyrestart temrestart
#endif

#ifdef yylex_init
#define temlex_init_ALREADY_DEFINED
#else
#define yylex_init temlex_init
#endif

#ifdef yylex_init_extra
#define temlex_init_extra_ALREADY_DEFINED
#else
#define yylex_init_extra temlex_init_extra
#endif

#ifdef yylex_destroy
#define temlex_destroy_ALREADY_DEFINED
#else
#define yylex_destroy temlex_destroy
#endif

#ifdef yyget_debug
#define temget_debug_ALREADY_DEFINED
#else
#define yyget_debug temget_debug
#endif

#ifdef yyset_debug
#define temset_debug_ALREADY_DEFINED
#else
#define yyset_debug temset_debug
#endif

#ifdef yyget_extra
#define temget_extra_ALREADY_DEFINED
#else
#define yyget_extra temget_extra
#endif

#ifdef yyset_extra
#define temset_extra_ALREADY_DEFINED
#else
#define yyset_extra temset_extra
#endif

#ifdef yyget_in
#define temget_in_ALREADY_DEFINED
#else
#define yyget_in temget_in
#endif

#ifdef yyset_in
#define temset_in_ALREADY_DEFINED
#else
#define yyset_in temset_in
#endif

#ifdef yyget_out
#define temget_out_ALREADY_DEFINED
#else
#define yyget_out temget_out
#endif

#ifdef yyset_out
#define temset_out_ALREADY_DEFINED
#else
#define yyset_out temset_out
#endif

#ifdef yyget_leng
#define temget_leng_ALREADY_DEFINED
#else
#define yyget_leng temget_leng
#endif

#ifdef yyget_text
#define temget_text_ALREADY_DEFINED
#else
#define yyget_text temget_text
#endif

#ifdef yyget_lineno
#define temget_lineno_ALREADY_DEFINED
#else
#define yyget_lineno temget_lineno
#endif

#ifdef yyset_lineno
#define temset_lineno_ALREADY_DEFINED
#else
#define yyset_lineno temset_lineno
#endif

#ifdef yyget_column
#define temget_column_ALREADY_DEFINED
#else
#define yyget_column temget_column
#endif

#ifdef yyset_column
#define temset_column_ALREADY_DEFINED
#else
#define yyset_column temset_column
#endif

#ifdef yywrap
#define temwrap_ALREADY_DEFINED
#else
#define yywrap temwrap
#endif

#ifdef yyalloc
#define temalloc_ALREADY_DEFINED
#else
#define yyalloc temalloc
#endif

#ifdef yyrealloc
#define temrealloc_ALREADY_DEFINED
#else
#define yyrealloc temrealloc
#endif

#ifdef yyfree
#define temfree_ALREADY_DEFINED
#else
#define yyfree temfree
#endif

/* First, we deal with  platform-specific or compiler-specific issues. */

/* begin standard C headers. */
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>

/* end standard C headers. */

/* flex integer type definitions */

#ifndef FLEXINT_H
#define FLEXINT_H

/* C99 systems have <inttypes.h>. Non-C99 systems may or may not. */

#if defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L

/* C99 says to define __STDC_LIMIT_MACROS before including stdint.h,
 * if you want the limit (max/min) macros for int types. 
 */
#ifndef __STDC_LIMIT_MACROS
#define __STDC_LIMIT_MACROS 1
#endif

#include <inttypes.h>
typedef int8_t flex_int8_t;
typedef uint8_t flex_uint8_t;
typedef int16_t flex_int16_t;
typedef uint16_t flex_uint16_t;
typedef int32_t flex_int32_t;
typedef uint32_t flex_uint32_t;
#else
typedef signed char flex_int8_t;
typedef short int flex_int16_t;
typedef int flex_int32_t;
typedef unsigned char flex_uint8_t; 
typedef unsigned short int flex_uint16_t;
typedef unsigned int flex_uint32_t;

/* Limits of integral types. */
#ifndef INT8_MIN
#define INT8_MIN               (-128)
#endif
#ifndef INT16_MIN
#define INT16_MIN              (-32767-1)
#endif
#ifndef INT32_MIN
#define INT32_MIN              (-2147483647-1)
#endif
#ifndef INT8_MAX
#define INT8_MAX               (127)
#endif
#ifndef INT16_MAX
#define INT16_MAX              (32767)
#endif
#ifndef INT32_MAX
#define INT32_MAX              (2147483647)
#endif
#ifndef UINT8_MAX
#define UINT8_MAX              (255U)
#endif
#ifndef UINT16_MAX
#define UINT16_MAX             (65535U)
#endif
#ifndef UINT32_MAX
#define UINT32_MAX             (4294967295U)
#endif

#ifndef SIZE_MAX
#define SIZE_MAX               (~(size_t)0)
#endif

#endif /* ! C99 */

#endif /* ! FLEXINT_H */

/* begin standard C++ headers. */

/* TODO: this is always defined, so inline it */
#define yyconst const

#if defined(__GNUC__) && __GNUC__ >= 3
#define yynoreturn __attribute__((__noreturn__))
#else
#define yynoreturn
#endif

/* An opaque pointer. */
#ifndef YY_TYPEDEF_YY_SCANNER_T
#define YY_TYPEDEF_YY_SCANNER_T
typedef void* yyscan_t;
#endif

/* For convenience, these vars (plus the bison vars far below)
   are macros in the reentrant scanner. */
#define yyin yyg->yyin_r
#define yyout yyg->yyout_r
#define yyextra yyg->yyextra_r
#define yyleng yyg->yyleng_r
#define yytext yyg->yytext_r
#define yylineno (YY_CURRENT_BUFFER_LVALUE->yy_bs_lineno)
#define yycolumn (YY_CURRENT_BUFFER_LVALUE->yy_bs_column)
#define yy_flex_debug yyg->yy_flex_debug_r

/* Size of default input buffer. */
#ifndef YY_BUF_SIZE
#ifdef __ia64__
/* On IA-64, the buffer size is 16k, not 8k.
 * Moreover, YY_BUF_SIZE is 2*YY_READ_BUF_SIZE in the general case.
 * Ditto for the __ia64__ case accordingly.
 */
#define YY_BUF_SIZE 32768
#else
#define YY_BUF_SIZE 16384
#endif /* __ia64__ */
#endif

#ifndef YY_TYPEDEF_YY_BUFFER_STATE
#define YY_TYPEDEF_YY_BUFFER_STATE
typedef struct yy_buffer_state *YY_BUFFER_STATE;
#endif

#ifndef YY_TYPEDEF_YY_SIZE_T
#define YY_TYPEDEF_YY_SIZE_T
typedef size_t yy_size_t;
#endif

#ifndef YY_STRUCT_YY_BUFFER_STATE
#define YY_STRUCT_YY_BUFFER_STATE
struct yy_buffer_state
	{
	FILE *yy_input_file;

	char *yy_ch_buf;		/* input buffer */
	char *yy_buf_pos;		/* current position in input buffer */

	/* Size of input buffer in bytes, not including room for EOB
	 * characters.
	 */
	int yy_buf_size;

	/* Number of characters read into yy_ch_buf, not including EOB
	 * characters.
	 */
	int yy_n_chars;

	/* Whether we "own" the buffer - i.e., we know we created it,
	 * and can realloc() it to grow it, and should free() it to
	 * delete it.
	 */
	int yy_is_our_buffer;

	/* Whether this is an "interactive" input source; if so, and
	 * if we're using stdio for input, then we want to use getc()
	 * instead of fread(), to make sure we stop fetching input after
	 * each newline.
	 */
	int yy_is_interactive;

	/* Whether we're considered to be at the beginning of a line.
	 * If so, '^' rules will be active on the next match, otherwise
	 * not.
	 */
	int yy_at_bol;

    int yy_bs_lineno; /**< The line count. */
    int yy_bs_column; /**< The column count. */

	/* Whether to try to fill the input buffer when we reach the
	 * end of it.
	 */
	int yy_fill_buffer;

	int yy_buffer_status;

	};
#endif /* !YY_STRUCT_YY_BUFFER_STATE */

void yyrestart ( FILE *input_file , yyscan_t yyscanner );
void yy_switch_to_buffer ( YY_BUFFER_STATE new_buffer , yyscan_t yyscanner );
YY_BUFFER_STATE yy_create_buffer ( FILE *file, int size , yyscan_t yyscanner );
void yy_delete_buffer ( YY_BUFFER_STATE b , yyscan_t yyscanner );
void yy_flush_buffer ( YY_BUFFER_STATE b , yyscan_t yyscanner );
void yypush_buffer_state ( YY_BUFFER_STATE new_buffer , yyscan_t yyscanner );
void yypop_buffer_state ( yyscan_t yyscanner );

YY_BUFFER_STATE yy_scan_buffer ( char *base, yy_size_t size , yyscan_t yyscanner );
YY_BUFFER_STATE yy_scan_string ( const char *yy_str , yyscan_t yyscanner );
YY_BUFFER_STATE yy_scan_bytes ( const char *bytes, int len , yyscan_t yyscanner );

void *yyalloc ( yy_size_t , yyscan_t yyscanner );
void *yyrealloc ( void *, yy_size_t , yyscan_t yyscanner );
void yyfree ( void * , yyscan_t yyscanner );

/* Begin user sect3 */

#define temwrap(yyscanner) (/*CONSTCOND*/1)
#define YY_SKIP_YYWRAP

#define yytext_ptr yytext_r

#ifdef YY_HEADER_EXPORT_START_CONDITIONS
#define INITIAL 0

#endif

#ifndef YY_NO_UNISTD_H
/* Special case for "unistd.h", since it is non-ANSI. We include it way
 * down here because we want the user's section 1 to have been scanned first.
 * The user has a chance to override it with an option.
 */
#include <unistd.h>
#endif

#ifndef YY_EXTRA_TYPE
#define YY_EXTRA_TYPE void *
#endif

int yylex_init (yyscan_t* scanner);

int yylex_init_extra ( YY_EXTRA_TYPE user_defined, yyscan_t* scanner);

/* Accessor methods to globals.
   These are made visible to non-reentrant scanners for convenience. */

int yylex_destroy ( yyscan_t yyscanner );

int yyget_debug ( yyscan_t yyscanner );

void yyset_debug ( int debug_flag , yyscan_t yyscanner );

YY_EXTRA_TYPE yyget_extra ( yyscan_t yyscanner );

void yyset_extra ( YY_EXTRA_TYPE user_defined , yyscan_t yyscanner );

FILE *yyget_in ( yyscan_t yyscanner );

void yyset_in  ( FILE * _in_str , yyscan_t yyscanner );

FILE *yyget_out ( yyscan_t yyscanner );

void yyset_out  ( FILE * _out_str , yyscan_t yyscanner );

			int yyget_leng ( yyscan_t yyscanner );

char *yyget_text ( yyscan_t yyscanner );

int yyget_lineno ( yyscan_t yyscanner );

void yyset_lineno ( int _line_number , yyscan_t yyscanner );

int yyget_column  ( yyscan_t yyscanner );

void yyset_column ( int _column_no , yyscan_t yyscanner );

/* Macros after this point can all be overridden by user definitions in
 * section 1.
 */

#ifndef YY_SKIP_YYWRAP
#ifdef __cplusplus
extern "C" int yywrap ( yyscan_t yyscanner );
#else
extern int yywrap ( yyscan_t yyscanner );
#endif
#endif

#ifndef yytext_ptr
static void yy_flex_strncpy ( char *, const char *, int , yyscan_t yyscanner);
#endif

#ifdef YY_NEED_STRLEN
static int yy_flex_strlen ( const char * , yyscan_t yyscanner);
#endif

#ifndef YY_NO_INPUT

#endif

/* Amount of stuff to slurp up with each read. */
#ifndef YY_READ_BUF_SIZE
#ifdef __ia64__
/* On IA-64, the buffer size is 16k, not 8k */
#define YY_READ_BUF_SIZE 16384
#else
#define YY_READ_BUF_SIZE 8192
#endif /* __ia64__ */
#endif

/* Number of entries by which start-condition stack grows. */
#ifndef YY_START_STACK_INCR
#define YY_START_STACK_INCR 25
#endif

/* Default declaration of generated scanner - a define so the user can
 * easily add parameters.
 */
#ifndef YY_DECL
#define YY_DECL_IS_OURS 1

extern int yylex (yyscan_t yyscanner);

#define YY_DECL int yylex (yyscan_t yyscanner)
#endif /* !YY_DECL */

/* yy_get_previous_state - get the state just before the EOB char was reached */

#undef YY_NEW_FILE
#undef YY_FLUSH_BUFFER
#undef yy_set_bol
#undef yy_new_buffer
#undef yy_set_interactive
#undef YY_DO_BEFORE_ACTION

#ifdef YY_DECL_IS_OURS
#undef YY_DECL_IS_OURS
#undef YY_DECL
#endif

#ifndef tem_create_buffer_ALREADY_DEFINED
#undef yy_create_buffer
#endif
#ifndef tem_delete_buffer_ALREADY_DEFINED
#undef yy_delete_buffer
#endif
#ifndef tem_scan_buffer_ALREADY_DEFINED
#undef yy_scan_buffer
#endif
#ifndef tem_scan_string_ALREADY_DEFINED
#undef yy_scan_string
#endif
#ifndef tem_scan_bytes_ALREADY_DEFINED
#undef yy_scan_bytes
#endif
#ifndef tem_init_buffer_ALREADY_DEFINED
#undef yy_init_buffer
#endif
#ifndef tem_flush_buffer_ALREADY_DEFINED
#undef yy_flush_buffer
#endif
#ifndef tem_load_buffer_state_ALREADY_DEFINED
#undef yy_load_buffer_state
#endif
#ifndef tem_switch_to_buffer_ALREADY_DEFINED
#undef yy_switch_to_buffer
#endif
#ifndef tempush_buffer_state_ALREADY_DEFINED
#undef yypush_buffer_state
#endif
#ifndef tempop_buffer_state_ALREADY_DEFINED
#undef yypop_buffer_state
#endif
#ifndef temensure_buffer_stack_ALREADY_DEFINED
#undef yyensure_buffer_stack
#endif
#ifndef temlex_ALREADY_DEFINED
#undef yylex
#endif
#ifndef temrestart_ALREADY_DEFINED
#undef yyrestart
#endif
#ifndef temlex_init_ALREADY_DEFINED
#undef yylex_init
#endif
#ifndef temlex_init_extra_ALREADY_DEFINED
#undef yylex_init_extra
#endif
#ifndef temlex_destroy_ALREADY_DEFINED
#undef yylex_destroy
#endif
#ifndef temget_debug_ALREADY_DEFINED
#undef yyget_debug
#endif
#ifndef temset_debug_ALREADY_DEFINED
#undef yyset_debug
#endif
#ifndef temget_extra_ALREADY_DEFINED
#undef yyget_extra
#endif
#ifndef temset_extra_ALREADY_DEFINED
#undef yyset_extra
#endif
#ifndef temget_in_ALREADY_DEFINED
#undef yyget_in
#endif
#ifndef temset_in_ALREADY_DEFINED
#undef yyset_in
#endif
#ifndef temget_out_ALREADY_DEFINED
#undef yyget_out
#endif
#ifndef temset_out_ALREADY_DEFINED
#undef yyset_out
#endif
#ifndef temget_leng_ALREADY_DEFINED
#undef yyget_leng
#endif
#ifndef temget_text_ALREADY_DEFINED
#undef yyget_text
#endif
#ifndef temget_lineno_ALREADY_DEFINED
#undef yyget_lineno
#endif
#ifndef temset_lineno_ALREADY_DEFINED
#undef yyset_lineno
#endif
#ifndef temget_column_ALREADY_DEFINED
#undef yyget_column
#endif
#ifndef temset_column_ALREADY_DEFINED
#undef yyset_column
#endif
#ifndef temwrap_ALREADY_DEFINED
#undef yywrap
#endif
#ifndef temget_lval_ALREADY_DEFINED
#undef yyget_lval
#endif
#ifndef temset_lval_ALREADY_DEFINED
#undef yyset_lval
#endif
#ifndef temget_lloc_ALREADY_DEFINED
#undef yyget_lloc
#endif
#ifndef temset_lloc_ALREADY_DEFINED
#undef yyset_lloc
#endif
#ifndef temalloc_ALREADY_DEFINED
#undef yyalloc
#endif
#ifndef temrealloc_ALREADY_DEFINED
#undef yyrealloc
#endif
#ifndef temfree_ALREADY_DEFINED
#undef yyfree
#endif
#ifndef temtext_ALREADY_DEFINED
#undef yytext
#endif
#ifndef temleng_ALREADY_DEFINED
#undef yyleng
#endif
#ifndef temin_ALREADY_DEFINED
#undef yyin
#endif
#ifndef temout_ALREADY_DEFINED
#undef yyout
#endif
#ifndef tem_flex_debug_ALREADY_DEFINED
#undef yy_flex_debug
#endif
#ifndef temlineno_ALREADY_DEFINED
#undef yylineno
#endif
#ifndef temtables_fload_ALREADY_DEFINED
#undef yytables_fload
#endif
#ifndef temtables_destroy_ALREADY_DEFINED
#undef yytables_destroy
#endif
#ifndef temTABLES_NAME_ALREADY_DEFINED
#undef yyTABLES_NAME
#endif

#line 74 "tempus.l"


#line 701 "tempus_lex.h"
#undef temIN_HEADER
#endif /* temHEADER_H */
