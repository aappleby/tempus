echo "# Running lex"
lex  --header-file=tempus_lex.h --outfile=tempus_lex.c tempus.l
echo

echo "# Running yacc"
yacc --report=all --header=tempus_yacc.h --output=tempus_yacc.c tempus.y
echo

echo "# GCC"
g++ -O0 -g tempus_main.cpp -o tempus_main
echo
