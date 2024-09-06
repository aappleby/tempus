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


    # Enter a parse tree produced by tempusParser#ident.
    def enterIdent(self, ctx:tempusParser.IdentContext):
        pass

    # Exit a parse tree produced by tempusParser#ident.
    def exitIdent(self, ctx:tempusParser.IdentContext):
        pass


    # Enter a parse tree produced by tempusParser#uninit_decl.
    def enterUninit_decl(self, ctx:tempusParser.Uninit_declContext):
        pass

    # Exit a parse tree produced by tempusParser#uninit_decl.
    def exitUninit_decl(self, ctx:tempusParser.Uninit_declContext):
        pass


    # Enter a parse tree produced by tempusParser#untyped_decl.
    def enterUntyped_decl(self, ctx:tempusParser.Untyped_declContext):
        pass

    # Exit a parse tree produced by tempusParser#untyped_decl.
    def exitUntyped_decl(self, ctx:tempusParser.Untyped_declContext):
        pass


    # Enter a parse tree produced by tempusParser#typed_expr.
    def enterTyped_expr(self, ctx:tempusParser.Typed_exprContext):
        pass

    # Exit a parse tree produced by tempusParser#typed_expr.
    def exitTyped_expr(self, ctx:tempusParser.Typed_exprContext):
        pass


    # Enter a parse tree produced by tempusParser#full_decl.
    def enterFull_decl(self, ctx:tempusParser.Full_declContext):
        pass

    # Exit a parse tree produced by tempusParser#full_decl.
    def exitFull_decl(self, ctx:tempusParser.Full_declContext):
        pass


    # Enter a parse tree produced by tempusParser#constant.
    def enterConstant(self, ctx:tempusParser.ConstantContext):
        pass

    # Exit a parse tree produced by tempusParser#constant.
    def exitConstant(self, ctx:tempusParser.ConstantContext):
        pass


    # Enter a parse tree produced by tempusParser#atom.
    def enterAtom(self, ctx:tempusParser.AtomContext):
        pass

    # Exit a parse tree produced by tempusParser#atom.
    def exitAtom(self, ctx:tempusParser.AtomContext):
        pass


    # Enter a parse tree produced by tempusParser#expr.
    def enterExpr(self, ctx:tempusParser.ExprContext):
        pass

    # Exit a parse tree produced by tempusParser#expr.
    def exitExpr(self, ctx:tempusParser.ExprContext):
        pass


    # Enter a parse tree produced by tempusParser#if_stmt.
    def enterIf_stmt(self, ctx:tempusParser.If_stmtContext):
        pass

    # Exit a parse tree produced by tempusParser#if_stmt.
    def exitIf_stmt(self, ctx:tempusParser.If_stmtContext):
        pass


    # Enter a parse tree produced by tempusParser#match_stmt.
    def enterMatch_stmt(self, ctx:tempusParser.Match_stmtContext):
        pass

    # Exit a parse tree produced by tempusParser#match_stmt.
    def exitMatch_stmt(self, ctx:tempusParser.Match_stmtContext):
        pass


    # Enter a parse tree produced by tempusParser#case_stmt.
    def enterCase_stmt(self, ctx:tempusParser.Case_stmtContext):
        pass

    # Exit a parse tree produced by tempusParser#case_stmt.
    def exitCase_stmt(self, ctx:tempusParser.Case_stmtContext):
        pass


    # Enter a parse tree produced by tempusParser#stmt.
    def enterStmt(self, ctx:tempusParser.StmtContext):
        pass

    # Exit a parse tree produced by tempusParser#stmt.
    def exitStmt(self, ctx:tempusParser.StmtContext):
        pass


    # Enter a parse tree produced by tempusParser#stmt_list.
    def enterStmt_list(self, ctx:tempusParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by tempusParser#stmt_list.
    def exitStmt_list(self, ctx:tempusParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by tempusParser#paren_list.
    def enterParen_list(self, ctx:tempusParser.Paren_listContext):
        pass

    # Exit a parse tree produced by tempusParser#paren_list.
    def exitParen_list(self, ctx:tempusParser.Paren_listContext):
        pass


    # Enter a parse tree produced by tempusParser#brace_list.
    def enterBrace_list(self, ctx:tempusParser.Brace_listContext):
        pass

    # Exit a parse tree produced by tempusParser#brace_list.
    def exitBrace_list(self, ctx:tempusParser.Brace_listContext):
        pass


    # Enter a parse tree produced by tempusParser#brack_list.
    def enterBrack_list(self, ctx:tempusParser.Brack_listContext):
        pass

    # Exit a parse tree produced by tempusParser#brack_list.
    def exitBrack_list(self, ctx:tempusParser.Brack_listContext):
        pass


    # Enter a parse tree produced by tempusParser#dummy.
    def enterDummy(self, ctx:tempusParser.DummyContext):
        pass

    # Exit a parse tree produced by tempusParser#dummy.
    def exitDummy(self, ctx:tempusParser.DummyContext):
        pass



del tempusParser