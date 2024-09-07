echo "# Lex"
lex  --header-file=example7_lex.h --outfile=example7_lex.c example7.l
echo

echo "# Yacc"
yacc --report=all --header=example7_yacc.h --output=example7_yacc.c example7.y
echo

echo "# GCC"
g++ main.cpp -o example7
echo
