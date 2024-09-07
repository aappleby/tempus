echo "# Running lex"
lex  -v --header-file=tempus_lex.h --outfile=tempus_lex.c tempus.l
echo

echo "# Running yacc"
yacc --header=tempus_yacc.h --output=tempus_yacc.c tempus.y
echo

#echo "# Compiling tempus_lex.c"
#gcc -c tempus_lex.c -o tempus_lex.o

#echo "# Compiling tempus_yacc.c"
#gcc -c tempus_yacc.c -o tempus_yacc.o

echo "# Compiling main.c"
gcc -c main.c -o main.o

#echo "# Linking main"
#gcc main.o tempus_lex.o tempus_yacc.o -o main

#echo "# Linking main"
gcc main.o -o main
