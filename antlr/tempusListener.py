# Generated from tempus.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .tempusParser import tempusParser
else:
    from tempusParser import tempusParser

# This class defines a complete listener for a parse tree produced by tempusParser.
class tempusListener(ParseTreeListener):

    # Enter a parse tree produced by tempusParser#program.
    def enterProgram(self, ctx:tempusParser.ProgramContext):
        pass

    # Exit a parse tree produced by tempusParser#program.
    def exitProgram(self, ctx:tempusParser.ProgramContext):
        pass


    # Enter a parse tree produced by tempusParser#prefix.
    def enterPrefix(self, ctx:tempusParser.PrefixContext):
        pass

    # Exit a parse tree produced by tempusParser#prefix.
    def exitPrefix(self, ctx:tempusParser.PrefixContext):
        pass


    # Enter a parse tree produced by tempusParser#const.
    def enterConst(self, ctx:tempusParser.ConstContext):
        pass

    # Exit a parse tree produced by tempusParser#const.
    def exitConst(self, ctx:tempusParser.ConstContext):
        pass


    # Enter a parse tree produced by tempusParser#ident.
    def enterIdent(self, ctx:tempusParser.IdentContext):
        pass

    # Exit a parse tree produced by tempusParser#ident.
    def exitIdent(self, ctx:tempusParser.IdentContext):
        pass


    # Enter a parse tree produced by tempusParser#parens.
    def enterParens(self, ctx:tempusParser.ParensContext):
        pass

    # Exit a parse tree produced by tempusParser#parens.
    def exitParens(self, ctx:tempusParser.ParensContext):
        pass


    # Enter a parse tree produced by tempusParser#braces.
    def enterBraces(self, ctx:tempusParser.BracesContext):
        pass

    # Exit a parse tree produced by tempusParser#braces.
    def exitBraces(self, ctx:tempusParser.BracesContext):
        pass


    # Enter a parse tree produced by tempusParser#bracks.
    def enterBracks(self, ctx:tempusParser.BracksContext):
        pass

    # Exit a parse tree produced by tempusParser#bracks.
    def exitBracks(self, ctx:tempusParser.BracksContext):
        pass


    # Enter a parse tree produced by tempusParser#expr_atom.
    def enterExpr_atom(self, ctx:tempusParser.Expr_atomContext):
        pass

    # Exit a parse tree produced by tempusParser#expr_atom.
    def exitExpr_atom(self, ctx:tempusParser.Expr_atomContext):
        pass


    # Enter a parse tree produced by tempusParser#atom_chain.
    def enterAtom_chain(self, ctx:tempusParser.Atom_chainContext):
        pass

    # Exit a parse tree produced by tempusParser#atom_chain.
    def exitAtom_chain(self, ctx:tempusParser.Atom_chainContext):
        pass


    # Enter a parse tree produced by tempusParser#lhs_expr.
    def enterLhs_expr(self, ctx:tempusParser.Lhs_exprContext):
        pass

    # Exit a parse tree produced by tempusParser#lhs_expr.
    def exitLhs_expr(self, ctx:tempusParser.Lhs_exprContext):
        pass


    # Enter a parse tree produced by tempusParser#type_expr.
    def enterType_expr(self, ctx:tempusParser.Type_exprContext):
        pass

    # Exit a parse tree produced by tempusParser#type_expr.
    def exitType_expr(self, ctx:tempusParser.Type_exprContext):
        pass


    # Enter a parse tree produced by tempusParser#rhs_expr.
    def enterRhs_expr(self, ctx:tempusParser.Rhs_exprContext):
        pass

    # Exit a parse tree produced by tempusParser#rhs_expr.
    def exitRhs_expr(self, ctx:tempusParser.Rhs_exprContext):
        pass


    # Enter a parse tree produced by tempusParser#full_decl.
    def enterFull_decl(self, ctx:tempusParser.Full_declContext):
        pass

    # Exit a parse tree produced by tempusParser#full_decl.
    def exitFull_decl(self, ctx:tempusParser.Full_declContext):
        pass


    # Enter a parse tree produced by tempusParser#empty_decl.
    def enterEmpty_decl(self, ctx:tempusParser.Empty_declContext):
        pass

    # Exit a parse tree produced by tempusParser#empty_decl.
    def exitEmpty_decl(self, ctx:tempusParser.Empty_declContext):
        pass


    # Enter a parse tree produced by tempusParser#assignment.
    def enterAssignment(self, ctx:tempusParser.AssignmentContext):
        pass

    # Exit a parse tree produced by tempusParser#assignment.
    def exitAssignment(self, ctx:tempusParser.AssignmentContext):
        pass


    # Enter a parse tree produced by tempusParser#typed_val.
    def enterTyped_val(self, ctx:tempusParser.Typed_valContext):
        pass

    # Exit a parse tree produced by tempusParser#typed_val.
    def exitTyped_val(self, ctx:tempusParser.Typed_valContext):
        pass


    # Enter a parse tree produced by tempusParser#bare_name.
    def enterBare_name(self, ctx:tempusParser.Bare_nameContext):
        pass

    # Exit a parse tree produced by tempusParser#bare_name.
    def exitBare_name(self, ctx:tempusParser.Bare_nameContext):
        pass


    # Enter a parse tree produced by tempusParser#bare_type.
    def enterBare_type(self, ctx:tempusParser.Bare_typeContext):
        pass

    # Exit a parse tree produced by tempusParser#bare_type.
    def exitBare_type(self, ctx:tempusParser.Bare_typeContext):
        pass


    # Enter a parse tree produced by tempusParser#bare_val.
    def enterBare_val(self, ctx:tempusParser.Bare_valContext):
        pass

    # Exit a parse tree produced by tempusParser#bare_val.
    def exitBare_val(self, ctx:tempusParser.Bare_valContext):
        pass


    # Enter a parse tree produced by tempusParser#bare_expr.
    def enterBare_expr(self, ctx:tempusParser.Bare_exprContext):
        pass

    # Exit a parse tree produced by tempusParser#bare_expr.
    def exitBare_expr(self, ctx:tempusParser.Bare_exprContext):
        pass


    # Enter a parse tree produced by tempusParser#stmt_if.
    def enterStmt_if(self, ctx:tempusParser.Stmt_ifContext):
        pass

    # Exit a parse tree produced by tempusParser#stmt_if.
    def exitStmt_if(self, ctx:tempusParser.Stmt_ifContext):
        pass


    # Enter a parse tree produced by tempusParser#stmt_case.
    def enterStmt_case(self, ctx:tempusParser.Stmt_caseContext):
        pass

    # Exit a parse tree produced by tempusParser#stmt_case.
    def exitStmt_case(self, ctx:tempusParser.Stmt_caseContext):
        pass


    # Enter a parse tree produced by tempusParser#stmt_match.
    def enterStmt_match(self, ctx:tempusParser.Stmt_matchContext):
        pass

    # Exit a parse tree produced by tempusParser#stmt_match.
    def exitStmt_match(self, ctx:tempusParser.Stmt_matchContext):
        pass


    # Enter a parse tree produced by tempusParser#stmt_for.
    def enterStmt_for(self, ctx:tempusParser.Stmt_forContext):
        pass

    # Exit a parse tree produced by tempusParser#stmt_for.
    def exitStmt_for(self, ctx:tempusParser.Stmt_forContext):
        pass


    # Enter a parse tree produced by tempusParser#expr.
    def enterExpr(self, ctx:tempusParser.ExprContext):
        pass

    # Exit a parse tree produced by tempusParser#expr.
    def exitExpr(self, ctx:tempusParser.ExprContext):
        pass


    # Enter a parse tree produced by tempusParser#expr_block.
    def enterExpr_block(self, ctx:tempusParser.Expr_blockContext):
        pass

    # Exit a parse tree produced by tempusParser#expr_block.
    def exitExpr_block(self, ctx:tempusParser.Expr_blockContext):
        pass


    # Enter a parse tree produced by tempusParser#expr_tuple.
    def enterExpr_tuple(self, ctx:tempusParser.Expr_tupleContext):
        pass

    # Exit a parse tree produced by tempusParser#expr_tuple.
    def exitExpr_tuple(self, ctx:tempusParser.Expr_tupleContext):
        pass


    # Enter a parse tree produced by tempusParser#dummy.
    def enterDummy(self, ctx:tempusParser.DummyContext):
        pass

    # Exit a parse tree produced by tempusParser#dummy.
    def exitDummy(self, ctx:tempusParser.DummyContext):
        pass



del tempusParser