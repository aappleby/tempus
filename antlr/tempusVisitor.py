# Generated from tempus.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .tempusParser import tempusParser
else:
    from tempusParser import tempusParser

# This class defines a complete generic visitor for a parse tree produced by tempusParser.

class tempusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tempusParser#program.
    def visitProgram(self, ctx:tempusParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#ident.
    def visitIdent(self, ctx:tempusParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#uninit_decl.
    def visitUninit_decl(self, ctx:tempusParser.Uninit_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#untyped_decl.
    def visitUntyped_decl(self, ctx:tempusParser.Untyped_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#typed_expr.
    def visitTyped_expr(self, ctx:tempusParser.Typed_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#full_decl.
    def visitFull_decl(self, ctx:tempusParser.Full_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#constant.
    def visitConstant(self, ctx:tempusParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#atom.
    def visitAtom(self, ctx:tempusParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#expr.
    def visitExpr(self, ctx:tempusParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#if_stmt.
    def visitIf_stmt(self, ctx:tempusParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#match_stmt.
    def visitMatch_stmt(self, ctx:tempusParser.Match_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#case_stmt.
    def visitCase_stmt(self, ctx:tempusParser.Case_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#stmt.
    def visitStmt(self, ctx:tempusParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#stmt_list.
    def visitStmt_list(self, ctx:tempusParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#paren_list.
    def visitParen_list(self, ctx:tempusParser.Paren_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#brace_list.
    def visitBrace_list(self, ctx:tempusParser.Brace_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#brack_list.
    def visitBrack_list(self, ctx:tempusParser.Brack_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#dummy.
    def visitDummy(self, ctx:tempusParser.DummyContext):
        return self.visitChildren(ctx)



del tempusParser