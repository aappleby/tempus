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


    # Visit a parse tree produced by tempusParser#prefix.
    def visitPrefix(self, ctx:tempusParser.PrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#const.
    def visitConst(self, ctx:tempusParser.ConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#ident.
    def visitIdent(self, ctx:tempusParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#parens.
    def visitParens(self, ctx:tempusParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#braces.
    def visitBraces(self, ctx:tempusParser.BracesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#bracks.
    def visitBracks(self, ctx:tempusParser.BracksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#expr_atom.
    def visitExpr_atom(self, ctx:tempusParser.Expr_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#atom_chain.
    def visitAtom_chain(self, ctx:tempusParser.Atom_chainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#lhs_expr.
    def visitLhs_expr(self, ctx:tempusParser.Lhs_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#type_expr.
    def visitType_expr(self, ctx:tempusParser.Type_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#rhs_expr.
    def visitRhs_expr(self, ctx:tempusParser.Rhs_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#full_decl.
    def visitFull_decl(self, ctx:tempusParser.Full_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#empty_decl.
    def visitEmpty_decl(self, ctx:tempusParser.Empty_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#assignment.
    def visitAssignment(self, ctx:tempusParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#typed_val.
    def visitTyped_val(self, ctx:tempusParser.Typed_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#bare_name.
    def visitBare_name(self, ctx:tempusParser.Bare_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#bare_type.
    def visitBare_type(self, ctx:tempusParser.Bare_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#bare_val.
    def visitBare_val(self, ctx:tempusParser.Bare_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#bare_expr.
    def visitBare_expr(self, ctx:tempusParser.Bare_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#stmt_if.
    def visitStmt_if(self, ctx:tempusParser.Stmt_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#stmt_case.
    def visitStmt_case(self, ctx:tempusParser.Stmt_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#stmt_match.
    def visitStmt_match(self, ctx:tempusParser.Stmt_matchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#stmt_for.
    def visitStmt_for(self, ctx:tempusParser.Stmt_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#expr.
    def visitExpr(self, ctx:tempusParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#expr_block.
    def visitExpr_block(self, ctx:tempusParser.Expr_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#expr_tuple.
    def visitExpr_tuple(self, ctx:tempusParser.Expr_tupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tempusParser#dummy.
    def visitDummy(self, ctx:tempusParser.DummyContext):
        return self.visitChildren(ctx)



del tempusParser