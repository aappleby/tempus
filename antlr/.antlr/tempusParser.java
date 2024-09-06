// Generated from /home/aappleby/repos/tempus/antlr/tempus.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class tempusParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, WS=2, NL=3, MLC=4, SLC=5, SEMI=6, LPAREN=7, RPAREN=8, LBRACE=9, 
		RBRACE=10, LBRACK=11, RBRACK=12, DOT=13, PRIME=14, KW_IF=15, KW_ELSE=16, 
		KW_MATCH=17, KW_CASE=18, TYPE_OP=19, BINARY_OP=20, ASSIGN_OP=21, INT=22, 
		FLOAT=23, STRING=24, IDENT=25;
	public static final int
		RULE_program = 0, RULE_ident = 1, RULE_uninit_decl = 2, RULE_untyped_decl = 3, 
		RULE_typed_expr = 4, RULE_full_decl = 5, RULE_constant = 6, RULE_atom = 7, 
		RULE_expr = 8, RULE_if_stmt = 9, RULE_match_stmt = 10, RULE_case_stmt = 11, 
		RULE_stmt = 12, RULE_stmt_list = 13, RULE_paren_list = 14, RULE_brace_list = 15, 
		RULE_brack_list = 16, RULE_dummy = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "ident", "uninit_decl", "untyped_decl", "typed_expr", "full_decl", 
			"constant", "atom", "expr", "if_stmt", "match_stmt", "case_stmt", "stmt", 
			"stmt_list", "paren_list", "brace_list", "brack_list", "dummy"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "','", null, null, null, null, "';'", "'('", "')'", "'{'", "'}'", 
			"'['", "']'", "'.'", "'@'", "'if'", "'else'", "'match'", "'case'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "WS", "NL", "MLC", "SLC", "SEMI", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "LBRACK", "RBRACK", "DOT", "PRIME", "KW_IF", "KW_ELSE", "KW_MATCH", 
			"KW_CASE", "TYPE_OP", "BINARY_OP", "ASSIGN_OP", "INT", "FLOAT", "STRING", 
			"IDENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "tempus.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public tempusParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(tempusParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(tempusParser.SEMI, i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 63892096L) != 0)) {
				{
				{
				setState(36);
				stmt();
				setState(37);
				match(SEMI);
				}
				}
				setState(43);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentContext extends ParserRuleContext {
		public List<TerminalNode> IDENT() { return getTokens(tempusParser.IDENT); }
		public TerminalNode IDENT(int i) {
			return getToken(tempusParser.IDENT, i);
		}
		public TerminalNode PRIME() { return getToken(tempusParser.PRIME, 0); }
		public List<TerminalNode> DOT() { return getTokens(tempusParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(tempusParser.DOT, i);
		}
		public IdentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ident; }
	}

	public final IdentContext ident() throws RecognitionException {
		IdentContext _localctx = new IdentContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_ident);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PRIME) {
				{
				setState(44);
				match(PRIME);
				}
			}

			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DOT) {
				{
				setState(47);
				match(DOT);
				}
			}

			setState(50);
			match(IDENT);
			setState(55);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(51);
					match(DOT);
					setState(52);
					match(IDENT);
					}
					} 
				}
				setState(57);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Uninit_declContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode TYPE_OP() { return getToken(tempusParser.TYPE_OP, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Uninit_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_uninit_decl; }
	}

	public final Uninit_declContext uninit_decl() throws RecognitionException {
		Uninit_declContext _localctx = new Uninit_declContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_uninit_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			ident();
			setState(59);
			match(TYPE_OP);
			setState(60);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Untyped_declContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode ASSIGN_OP() { return getToken(tempusParser.ASSIGN_OP, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Untyped_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_untyped_decl; }
	}

	public final Untyped_declContext untyped_decl() throws RecognitionException {
		Untyped_declContext _localctx = new Untyped_declContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_untyped_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			ident();
			setState(63);
			match(ASSIGN_OP);
			setState(64);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Typed_exprContext extends ParserRuleContext {
		public TerminalNode TYPE_OP() { return getToken(tempusParser.TYPE_OP, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ASSIGN_OP() { return getToken(tempusParser.ASSIGN_OP, 0); }
		public Typed_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typed_expr; }
	}

	public final Typed_exprContext typed_expr() throws RecognitionException {
		Typed_exprContext _localctx = new Typed_exprContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_typed_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(TYPE_OP);
			setState(67);
			expr();
			setState(68);
			match(ASSIGN_OP);
			setState(69);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Full_declContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode TYPE_OP() { return getToken(tempusParser.TYPE_OP, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ASSIGN_OP() { return getToken(tempusParser.ASSIGN_OP, 0); }
		public Full_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_full_decl; }
	}

	public final Full_declContext full_decl() throws RecognitionException {
		Full_declContext _localctx = new Full_declContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_full_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			ident();
			setState(72);
			match(TYPE_OP);
			setState(73);
			expr();
			setState(74);
			match(ASSIGN_OP);
			setState(75);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstantContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(tempusParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(tempusParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(tempusParser.STRING, 0); }
		public ConstantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constant; }
	}

	public final ConstantContext constant() throws RecognitionException {
		ConstantContext _localctx = new ConstantContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_constant);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomContext extends ParserRuleContext {
		public Full_declContext full_decl() {
			return getRuleContext(Full_declContext.class,0);
		}
		public Uninit_declContext uninit_decl() {
			return getRuleContext(Uninit_declContext.class,0);
		}
		public Untyped_declContext untyped_decl() {
			return getRuleContext(Untyped_declContext.class,0);
		}
		public Typed_exprContext typed_expr() {
			return getRuleContext(Typed_exprContext.class,0);
		}
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public ConstantContext constant() {
			return getRuleContext(ConstantContext.class,0);
		}
		public Paren_listContext paren_list() {
			return getRuleContext(Paren_listContext.class,0);
		}
		public Brack_listContext brack_list() {
			return getRuleContext(Brack_listContext.class,0);
		}
		public Brace_listContext brace_list() {
			return getRuleContext(Brace_listContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_atom);
		try {
			setState(88);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(79);
				full_decl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(80);
				uninit_decl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(81);
				untyped_decl();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(82);
				typed_expr();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(83);
				ident();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(84);
				constant();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(85);
				paren_list();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(86);
				brack_list();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(87);
				brace_list();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public List<AtomContext> atom() {
			return getRuleContexts(AtomContext.class);
		}
		public AtomContext atom(int i) {
			return getRuleContext(AtomContext.class,i);
		}
		public List<TerminalNode> BINARY_OP() { return getTokens(tempusParser.BINARY_OP); }
		public TerminalNode BINARY_OP(int i) {
			return getToken(tempusParser.BINARY_OP, i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expr);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(91); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(90);
					atom();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(93); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(103);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(95);
					match(BINARY_OP);
					setState(97); 
					_errHandler.sync(this);
					_alt = 1;
					do {
						switch (_alt) {
						case 1:
							{
							{
							setState(96);
							atom();
							}
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(99); 
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
					} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
					}
					} 
				}
				setState(105);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class If_stmtContext extends ParserRuleContext {
		public TerminalNode KW_IF() { return getToken(tempusParser.KW_IF, 0); }
		public Paren_listContext paren_list() {
			return getRuleContext(Paren_listContext.class,0);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public TerminalNode KW_ELSE() { return getToken(tempusParser.KW_ELSE, 0); }
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_if_stmt);
		try {
			setState(116);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(106);
				match(KW_IF);
				setState(107);
				paren_list();
				setState(108);
				stmt();
				setState(109);
				match(KW_ELSE);
				setState(110);
				stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(112);
				match(KW_IF);
				setState(113);
				paren_list();
				setState(114);
				stmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Match_stmtContext extends ParserRuleContext {
		public TerminalNode KW_MATCH() { return getToken(tempusParser.KW_MATCH, 0); }
		public Paren_listContext paren_list() {
			return getRuleContext(Paren_listContext.class,0);
		}
		public Brace_listContext brace_list() {
			return getRuleContext(Brace_listContext.class,0);
		}
		public Match_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_match_stmt; }
	}

	public final Match_stmtContext match_stmt() throws RecognitionException {
		Match_stmtContext _localctx = new Match_stmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_match_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(KW_MATCH);
			setState(119);
			paren_list();
			setState(120);
			brace_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Case_stmtContext extends ParserRuleContext {
		public TerminalNode KW_CASE() { return getToken(tempusParser.KW_CASE, 0); }
		public Paren_listContext paren_list() {
			return getRuleContext(Paren_listContext.class,0);
		}
		public Brace_listContext brace_list() {
			return getRuleContext(Brace_listContext.class,0);
		}
		public Case_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_case_stmt; }
	}

	public final Case_stmtContext case_stmt() throws RecognitionException {
		Case_stmtContext _localctx = new Case_stmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_case_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(KW_CASE);
			setState(123);
			paren_list();
			setState(124);
			brace_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public Match_stmtContext match_stmt() {
			return getRuleContext(Match_stmtContext.class,0);
		}
		public Case_stmtContext case_stmt() {
			return getRuleContext(Case_stmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_stmt);
		try {
			setState(130);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
			case LBRACE:
			case LBRACK:
			case DOT:
			case PRIME:
			case TYPE_OP:
			case INT:
			case FLOAT:
			case STRING:
			case IDENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				atom();
				}
				break;
			case KW_IF:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				if_stmt();
				}
				break;
			case KW_MATCH:
				enterOuterAlt(_localctx, 3);
				{
				setState(128);
				match_stmt();
				}
				break;
			case KW_CASE:
				enterOuterAlt(_localctx, 4);
				{
				setState(129);
				case_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Stmt_listContext extends ParserRuleContext {
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(tempusParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(tempusParser.SEMI, i);
		}
		public Stmt_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt_list; }
	}

	public final Stmt_listContext stmt_list() throws RecognitionException {
		Stmt_listContext _localctx = new Stmt_listContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_stmt_list);
		int _la;
		try {
			int _alt;
			setState(151);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(132);
				stmt();
				setState(137);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__0) {
					{
					{
					setState(133);
					match(T__0);
					setState(134);
					stmt();
					}
					}
					setState(139);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(140);
				stmt();
				setState(145);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(141);
						match(SEMI);
						setState(142);
						stmt();
						}
						} 
					}
					setState(147);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
				}
				setState(149);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==SEMI) {
					{
					setState(148);
					match(SEMI);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Paren_listContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(tempusParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(tempusParser.RPAREN, 0); }
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public Paren_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paren_list; }
	}

	public final Paren_listContext paren_list() throws RecognitionException {
		Paren_listContext _localctx = new Paren_listContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_paren_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			match(LPAREN);
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 63892096L) != 0)) {
				{
				setState(154);
				stmt_list();
				}
			}

			setState(157);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Brace_listContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(tempusParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(tempusParser.RBRACE, 0); }
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public Brace_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_brace_list; }
	}

	public final Brace_listContext brace_list() throws RecognitionException {
		Brace_listContext _localctx = new Brace_listContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_brace_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			match(LBRACE);
			setState(161);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 63892096L) != 0)) {
				{
				setState(160);
				stmt_list();
				}
			}

			setState(163);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Brack_listContext extends ParserRuleContext {
		public TerminalNode LBRACK() { return getToken(tempusParser.LBRACK, 0); }
		public TerminalNode RBRACK() { return getToken(tempusParser.RBRACK, 0); }
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public Brack_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_brack_list; }
	}

	public final Brack_listContext brack_list() throws RecognitionException {
		Brack_listContext _localctx = new Brack_listContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_brack_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			match(LBRACK);
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 63892096L) != 0)) {
				{
				setState(166);
				stmt_list();
				}
			}

			setState(169);
			match(RBRACK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DummyContext extends ParserRuleContext {
		public DummyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dummy; }
	}

	public final DummyContext dummy() throws RecognitionException {
		DummyContext _localctx = new DummyContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_dummy);
		try {
			enterOuterAlt(_localctx, 1);
			{
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0019\u00ae\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0005\u0000(\b\u0000\n\u0000\f\u0000+\t\u0000\u0001"+
		"\u0001\u0003\u0001.\b\u0001\u0001\u0001\u0003\u00011\b\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0005\u00016\b\u0001\n\u0001\f\u00019\t\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0003\u0007Y\b\u0007\u0001\b\u0004\b\\\b\b\u000b\b\f\b]\u0001\b\u0001"+
		"\b\u0004\bb\b\b\u000b\b\f\bc\u0005\bf\b\b\n\b\f\bi\t\b\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003"+
		"\tu\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u0083\b\f\u0001"+
		"\r\u0001\r\u0001\r\u0005\r\u0088\b\r\n\r\f\r\u008b\t\r\u0001\r\u0001\r"+
		"\u0001\r\u0005\r\u0090\b\r\n\r\f\r\u0093\t\r\u0001\r\u0003\r\u0096\b\r"+
		"\u0003\r\u0098\b\r\u0001\u000e\u0001\u000e\u0003\u000e\u009c\b\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0003\u000f\u00a2\b\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0003\u0010\u00a8\b\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0000\u0000\u0012"+
		"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a"+
		"\u001c\u001e \"\u0000\u0001\u0001\u0000\u0016\u0018\u00b5\u0000)\u0001"+
		"\u0000\u0000\u0000\u0002-\u0001\u0000\u0000\u0000\u0004:\u0001\u0000\u0000"+
		"\u0000\u0006>\u0001\u0000\u0000\u0000\bB\u0001\u0000\u0000\u0000\nG\u0001"+
		"\u0000\u0000\u0000\fM\u0001\u0000\u0000\u0000\u000eX\u0001\u0000\u0000"+
		"\u0000\u0010[\u0001\u0000\u0000\u0000\u0012t\u0001\u0000\u0000\u0000\u0014"+
		"v\u0001\u0000\u0000\u0000\u0016z\u0001\u0000\u0000\u0000\u0018\u0082\u0001"+
		"\u0000\u0000\u0000\u001a\u0097\u0001\u0000\u0000\u0000\u001c\u0099\u0001"+
		"\u0000\u0000\u0000\u001e\u009f\u0001\u0000\u0000\u0000 \u00a5\u0001\u0000"+
		"\u0000\u0000\"\u00ab\u0001\u0000\u0000\u0000$%\u0003\u0018\f\u0000%&\u0005"+
		"\u0006\u0000\u0000&(\u0001\u0000\u0000\u0000\'$\u0001\u0000\u0000\u0000"+
		"(+\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000)*\u0001\u0000\u0000"+
		"\u0000*\u0001\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000,.\u0005"+
		"\u000e\u0000\u0000-,\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000"+
		".0\u0001\u0000\u0000\u0000/1\u0005\r\u0000\u00000/\u0001\u0000\u0000\u0000"+
		"01\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u000027\u0005\u0019\u0000"+
		"\u000034\u0005\r\u0000\u000046\u0005\u0019\u0000\u000053\u0001\u0000\u0000"+
		"\u000069\u0001\u0000\u0000\u000075\u0001\u0000\u0000\u000078\u0001\u0000"+
		"\u0000\u00008\u0003\u0001\u0000\u0000\u000097\u0001\u0000\u0000\u0000"+
		":;\u0003\u0002\u0001\u0000;<\u0005\u0013\u0000\u0000<=\u0003\u0010\b\u0000"+
		"=\u0005\u0001\u0000\u0000\u0000>?\u0003\u0002\u0001\u0000?@\u0005\u0015"+
		"\u0000\u0000@A\u0003\u0010\b\u0000A\u0007\u0001\u0000\u0000\u0000BC\u0005"+
		"\u0013\u0000\u0000CD\u0003\u0010\b\u0000DE\u0005\u0015\u0000\u0000EF\u0003"+
		"\u0010\b\u0000F\t\u0001\u0000\u0000\u0000GH\u0003\u0002\u0001\u0000HI"+
		"\u0005\u0013\u0000\u0000IJ\u0003\u0010\b\u0000JK\u0005\u0015\u0000\u0000"+
		"KL\u0003\u0010\b\u0000L\u000b\u0001\u0000\u0000\u0000MN\u0007\u0000\u0000"+
		"\u0000N\r\u0001\u0000\u0000\u0000OY\u0003\n\u0005\u0000PY\u0003\u0004"+
		"\u0002\u0000QY\u0003\u0006\u0003\u0000RY\u0003\b\u0004\u0000SY\u0003\u0002"+
		"\u0001\u0000TY\u0003\f\u0006\u0000UY\u0003\u001c\u000e\u0000VY\u0003 "+
		"\u0010\u0000WY\u0003\u001e\u000f\u0000XO\u0001\u0000\u0000\u0000XP\u0001"+
		"\u0000\u0000\u0000XQ\u0001\u0000\u0000\u0000XR\u0001\u0000\u0000\u0000"+
		"XS\u0001\u0000\u0000\u0000XT\u0001\u0000\u0000\u0000XU\u0001\u0000\u0000"+
		"\u0000XV\u0001\u0000\u0000\u0000XW\u0001\u0000\u0000\u0000Y\u000f\u0001"+
		"\u0000\u0000\u0000Z\\\u0003\u000e\u0007\u0000[Z\u0001\u0000\u0000\u0000"+
		"\\]\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000"+
		"\u0000^g\u0001\u0000\u0000\u0000_a\u0005\u0014\u0000\u0000`b\u0003\u000e"+
		"\u0007\u0000a`\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000ca\u0001"+
		"\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000df\u0001\u0000\u0000\u0000"+
		"e_\u0001\u0000\u0000\u0000fi\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000"+
		"\u0000gh\u0001\u0000\u0000\u0000h\u0011\u0001\u0000\u0000\u0000ig\u0001"+
		"\u0000\u0000\u0000jk\u0005\u000f\u0000\u0000kl\u0003\u001c\u000e\u0000"+
		"lm\u0003\u0018\f\u0000mn\u0005\u0010\u0000\u0000no\u0003\u0018\f\u0000"+
		"ou\u0001\u0000\u0000\u0000pq\u0005\u000f\u0000\u0000qr\u0003\u001c\u000e"+
		"\u0000rs\u0003\u0018\f\u0000su\u0001\u0000\u0000\u0000tj\u0001\u0000\u0000"+
		"\u0000tp\u0001\u0000\u0000\u0000u\u0013\u0001\u0000\u0000\u0000vw\u0005"+
		"\u0011\u0000\u0000wx\u0003\u001c\u000e\u0000xy\u0003\u001e\u000f\u0000"+
		"y\u0015\u0001\u0000\u0000\u0000z{\u0005\u0012\u0000\u0000{|\u0003\u001c"+
		"\u000e\u0000|}\u0003\u001e\u000f\u0000}\u0017\u0001\u0000\u0000\u0000"+
		"~\u0083\u0003\u000e\u0007\u0000\u007f\u0083\u0003\u0012\t\u0000\u0080"+
		"\u0083\u0003\u0014\n\u0000\u0081\u0083\u0003\u0016\u000b\u0000\u0082~"+
		"\u0001\u0000\u0000\u0000\u0082\u007f\u0001\u0000\u0000\u0000\u0082\u0080"+
		"\u0001\u0000\u0000\u0000\u0082\u0081\u0001\u0000\u0000\u0000\u0083\u0019"+
		"\u0001\u0000\u0000\u0000\u0084\u0089\u0003\u0018\f\u0000\u0085\u0086\u0005"+
		"\u0001\u0000\u0000\u0086\u0088\u0003\u0018\f\u0000\u0087\u0085\u0001\u0000"+
		"\u0000\u0000\u0088\u008b\u0001\u0000\u0000\u0000\u0089\u0087\u0001\u0000"+
		"\u0000\u0000\u0089\u008a\u0001\u0000\u0000\u0000\u008a\u0098\u0001\u0000"+
		"\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008c\u0091\u0003\u0018"+
		"\f\u0000\u008d\u008e\u0005\u0006\u0000\u0000\u008e\u0090\u0003\u0018\f"+
		"\u0000\u008f\u008d\u0001\u0000\u0000\u0000\u0090\u0093\u0001\u0000\u0000"+
		"\u0000\u0091\u008f\u0001\u0000\u0000\u0000\u0091\u0092\u0001\u0000\u0000"+
		"\u0000\u0092\u0095\u0001\u0000\u0000\u0000\u0093\u0091\u0001\u0000\u0000"+
		"\u0000\u0094\u0096\u0005\u0006\u0000\u0000\u0095\u0094\u0001\u0000\u0000"+
		"\u0000\u0095\u0096\u0001\u0000\u0000\u0000\u0096\u0098\u0001\u0000\u0000"+
		"\u0000\u0097\u0084\u0001\u0000\u0000\u0000\u0097\u008c\u0001\u0000\u0000"+
		"\u0000\u0098\u001b\u0001\u0000\u0000\u0000\u0099\u009b\u0005\u0007\u0000"+
		"\u0000\u009a\u009c\u0003\u001a\r\u0000\u009b\u009a\u0001\u0000\u0000\u0000"+
		"\u009b\u009c\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000"+
		"\u009d\u009e\u0005\b\u0000\u0000\u009e\u001d\u0001\u0000\u0000\u0000\u009f"+
		"\u00a1\u0005\t\u0000\u0000\u00a0\u00a2\u0003\u001a\r\u0000\u00a1\u00a0"+
		"\u0001\u0000\u0000\u0000\u00a1\u00a2\u0001\u0000\u0000\u0000\u00a2\u00a3"+
		"\u0001\u0000\u0000\u0000\u00a3\u00a4\u0005\n\u0000\u0000\u00a4\u001f\u0001"+
		"\u0000\u0000\u0000\u00a5\u00a7\u0005\u000b\u0000\u0000\u00a6\u00a8\u0003"+
		"\u001a\r\u0000\u00a7\u00a6\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001\u0000"+
		"\u0000\u0000\u00a8\u00a9\u0001\u0000\u0000\u0000\u00a9\u00aa\u0005\f\u0000"+
		"\u0000\u00aa!\u0001\u0000\u0000\u0000\u00ab\u00ac\u0001\u0000\u0000\u0000"+
		"\u00ac#\u0001\u0000\u0000\u0000\u0011)-07X]cgt\u0082\u0089\u0091\u0095"+
		"\u0097\u009b\u00a1\u00a7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}