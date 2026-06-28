rm -f test_yacc
rm -f tempus_lex.c tempus_lex.h
rm -f tempus_yacc.c tempus_yacc.h
rm -f *.o

echo "# Running lex"
flex  --header-file=tempus_lex.h --outfile=tempus_lex.c tempus.l

echo "# Running yacc"
bison -v -Wcounterexamples --report=all --header=tempus_yacc.h --output=tempus_yacc.c tempus.y

echo "# Compiling lexer"
g++ -Wall -O0 -g -c tempus_lex.c    -o tempus_lex.o

echo "# Compiling parser"
g++ -Wall -O0 -g -c tempus_yacc.c   -o tempus_yacc.o

echo "# Compiling main"
g++ -Wall -O0 -g -c test_yacc.cpp -o test_yacc.o

echo "# Linking"
g++ -O0 -g test_yacc.o tempus_lex.o tempus_yacc.o -o test_yacc

