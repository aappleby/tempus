  #!/usr/bin/python3

from functools import cache
import doctest
import sys

#---------------------------------------------------------------------------------------------------

def default_atom_cmp(a, b):
  if isinstance(a, (str, int)) and isinstance(b, (str, int)):
    a_value = ord(a) if isinstance(a, str) else a
    b_value = ord(b) if isinstance(b, str) else b
    return b_value - a_value
  print(a)
  print(b)
  raise ValueError(F"Don't know how to compare {type(a)} and {type(b)}")

class Context:
  def __init__(self, cmp=default_atom_cmp):
    self.stack = []
    self.cmp = cmp

#---------------------------------------------------------------------------------------------------

class Fail:
  def __init__(self, span):
    self.span = span
  def __repr__(self):
    if isinstance(self.span, str):
      span = self.span.encode('unicode_escape').decode('utf-8')
    else:
      span = str(self.span)
    return f"Fail @ '{span}'"
  def __bool__(self):
    return False

#---------------------------------------------------------------------------------------------------

def apply(source, ctx, pattern):
  span = source
  any_fail = False
  while span:
    tail = pattern(span, ctx)
    if isinstance(tail, Fail):
      any_fail = True
      ctx.stack.append((f"fail @ {len(source) - len(span)}", span[0]))
      tail = span[1:]
    span = tail
  return any_fail

#---------------------------------------------------------------------------------------------------

# pylint: disable=unused-argument
def nothing(span, ctx2):
  return span

@cache
def And(pattern):
  r"""
  >>> And(Atom('a'))('asdf', Context())
  'asdf'
  >>> And(Atom('a'))('qwer', Context())
  Fail @ 'qwer'
  """
  def match(span, ctx2):
    tail = pattern(span, ctx2)
    return Fail(span) if isinstance(tail, Fail) else span
  return match

@cache
def Not(pattern):
  r"""
  >>> Not(Atom('a'))('asdf', Context())
  Fail @ 'asdf'
  >>> Not(Atom('a'))('qwer', Context())
  'qwer'
  """
  def match(span, ctx2):
    tail = pattern(span, ctx2)
    return span if isinstance(tail, Fail) else Fail(span)
  return match

#---------------------------------------------------------------------------------------------------

@cache
def Atom(const):
  r"""
  >>> Atom('a')('asdf', Context())
  'sdf'
  >>> Atom('a')('qwer', Context())
  Fail @ 'qwer'
  """
  def match(span, ctx2):
    assert(isinstance(span, (list, str)))
    assert(isinstance(ctx2, Context))
    return span[1:] if (span and not ctx2.cmp(span[0], const)) else Fail(span)
  return match

#---------------------------------------------------------------------------------------------------

@cache
def NotAtom(const):
  r"""
  >>> NotAtom('a')('asdf', Context())
  Fail @ 'asdf'
  >>> NotAtom('a')('qwer', Context())
  'wer'
  """
  def match(span, ctx2):
    return span[1:] if (span and ctx2.cmp(span[0], const)) else Fail(span)
  return match

#---------------------------------------------------------------------------------------------------

@cache
def Atoms(*oneof):
  r"""
  >>> Atoms('a', 'b')('asdf', Context())
  'sdf'
  >>> Atoms('b', 'a')('asdf', Context())
  'sdf'
  >>> Atoms('a', 'b')('qwer', Context())
  Fail @ 'qwer'
  """
  def match(span, ctx2):
    if not span:
      return Fail(span)
    for arg in oneof:
      if not ctx2.cmp(span[0], arg):
        return span[1:]
    return Fail(span)
  return match

#---------------------------------------------------------------------------------------------------

@cache
def NotAtoms(*seq):
  def match(span, ctx2):
    for arg in seq:
      if not ctx2.cmp(span[0], arg):
        return Fail(span)
    return span[1:]
  return match

#---------------------------------------------------------------------------------------------------

def AnyAtom(span, ctx2):
  r"""
  >>> AnyAtom('asdf', Context())
  'sdf'
  >>> AnyAtom('', Context())
  Fail @ ''
  """
  return span[1:] if span else Fail(span)

#---------------------------------------------------------------------------------------------------

@cache
def Range(A, B):
  r"""
  >>> Range('a', 'z')('asdf', Context())
  'sdf'
  >>> Range('b', 'y')('asdf', Context())
  Fail @ 'asdf'
  >>> Range('a', 'z')('1234', Context())
  Fail @ '1234'
  """
  A = ord(A) if isinstance(A, str) else A
  B = ord(B) if isinstance(B, str) else B

  def match(span, ctx2):
    if span and ctx2.cmp(A, span[0]) >= 0 and ctx2.cmp(span[0], B) >= 0:
      return span[1:]
    return Fail(span)
  return match

#---------------------------------------------------------------------------------------------------

@cache
def Ranges(*args):
  r"""
  >>> Ranges('a', 'z', 'A', 'Z')('asdf', Context())
  'sdf'
  >>> Ranges('a', 'z', 'A', 'Z')('QWER', Context())
  'WER'
  >>> Ranges('a', 'z', 'A', 'Z')('1234', Context())
  Fail @ '1234'
  """

  ranges = []
  for i in range(0, len(args), 2):
    ranges.append(Range(args[i+0], args[i+1]))

  def match(span, ctx2):
    for r in ranges:
      tail = r(span, ctx2)
      if not isinstance(tail, Fail):
        return tail
    return Fail(span)
  return match

#---------------------------------------------------------------------------------------------------

@cache
def Lit(lit):
  r"""
  >>> Lit('foo')('foobar', Context())
  'bar'
  >>> Lit('foo')('barfoo', Context())
  Fail @ 'barfoo'
  """
  def match(span, ctx2):
    if len(span) < len(lit):
      return Fail(span)
    for i, c in enumerate(lit):
      if ctx2.cmp(span[i], c):
        return Fail(span)
    return span[len(lit):]
  return match

#---------------------------------------------------------------------------------------------------

@cache
def Charset(lit):
  def match(span, ctx2):
    return span[1:] if (span and span[0] in lit) else Fail(span)
  return match

#---------------------------------------------------------------------------------------------------

@cache
def Seq(*seq):
  r"""
  >>> Seq(Atom('a'), Atom('s'))('asdf', Context())
  'df'
  >>> Seq(Atom('a'), Atom('s'))('a', Context())
  Fail @ ''
  >>> Seq(Atom('a'), Atom('s'))('qwer', Context())
  Fail @ 'qwer'
  """
  def match(span, ctx2):
    top = len(ctx2.stack)
    for arg in seq:
      tail = arg(span, ctx2)
      if isinstance(tail, Fail):
        del ctx2.stack[top:]
        return tail
      span = tail
    return span
  return match

#---------------------------------------------------------------------------------------------------

@cache
def Oneof(*oneof):
  r"""
  >>> Oneof(Atom('a'), Atom('b'))('asdf', Context())
  'sdf'
  >>> Oneof(Atom('b'), Atom('a'))('asdf', Context())
  'sdf'
  >>> Oneof(Atom('b'), Atom('a'))('qwer', Context())
  Fail @ 'qwer'
  """
  def match(span, ctx2):
    top = len(ctx2.stack)
    for arg in oneof:
      tail = arg(span, ctx2)
      if not isinstance(tail, Fail):
        return tail
      del ctx2.stack[top:]
    return Fail(span)
  return match

#---------------------------------------------------------------------------------------------------

@cache
def Opt(*oneof):
  r"""
  >>> Opt(Atom('a'))('asdf', Context())
  'sdf'
  >>> Opt(Atom('b'), Atom('a'))('asdf', Context())
  'sdf'
  >>> Opt(Atom('a'))('qwer', Context())
  'qwer'
  """
  def match(span, ctx2):
    for pattern in oneof:
      tail = pattern(span, ctx2)
      if not isinstance(tail, Fail):
        return tail
    return span
  return match

@cache
def OptSeq(*seq):
  return Opt(Seq(*seq))

#---------------------------------------------------------------------------------------------------

@cache
def Any(*oneof):
  r"""
  >>> Any(Atom('a'))('aaaasdf', Context())
  'sdf'
  >>> Any(Atom('a'))('baaaasdf', Context())
  'baaaasdf'
  """
  pattern = Oneof(*oneof)
  def match(span, ctx2):
    while True:
      tail = pattern(span, ctx2)
      if isinstance(tail, Fail):
        return span
      span = tail
  return match

#---------------------------------------------------------------------------------------------------

@cache
def Rep(count, pattern):
  r"""
  >>> Rep(4, Atom('a'))('aaasdf', Context())
  Fail @ 'sdf'
  >>> Rep(4, Atom('a'))('aaaasdf', Context())
  'sdf'
  >>> Rep(4, Atom('a'))('aaaaasdf', Context())
  'asdf'
  """
  def match(span, ctx2):
    top = len(ctx2.stack)
    for _ in range(count):
      tail = pattern(span, ctx2)
      if isinstance(tail, Fail):
        del ctx2.stack[top:]
        return tail
      span = tail
    return span
  return match

def AtLeast(count, pattern):
  r"""
  >>> AtLeast(4, Atom('a'))('aaasdf', Context())
  Fail @ 'sdf'
  >>> AtLeast(4, Atom('a'))('aaaasdf', Context())
  'sdf'
  >>> AtLeast(4, Atom('a'))('aaaaasdf', Context())
  'sdf'
  """
  return Seq(Rep(count, pattern), Any(pattern))

#---------------------------------------------------------------------------------------------------

@cache
def Some(*oneof):
  r"""
  >>> Some(Atom('a'))('aaaasdf', Context())
  'sdf'
  >>> Some(Atom('a'))('baaaasdf', Context())
  Fail @ 'baaaasdf'
  """
  pattern = Oneof(*oneof)
  def match(span, ctx2):
    span = pattern(span, ctx2)
    if isinstance(span, Fail):
      return span
    while True:
      tail = pattern(span, ctx2)
      if isinstance(tail, Fail):
        return span
      span = tail
  return match

#---------------------------------------------------------------------------------------------------
# 'Until' matches anything until we see the given pattern or we hit EOF.
# The pattern is _not_ consumed.

@cache
def Until(pattern):
  return Any(Seq(Not(pattern), AnyAtom))

#---------------------------------------------------------------------------------------------------
# Separated = a,b,c,d,

@cache
def Cycle(*seq):
  def match(span, ctx2):
    while True:
      for pattern in seq:
        tail = pattern(span, ctx2)
        if isinstance(tail, Fail):
          return span
        span = tail
  return match

#---------------------------------------------------------------------------------------------------
# a,b,c,d,
# trailing delimiter OK

@cache
def Separated(pattern, delim):
  return Cycle(pattern, delim)

#---------------------------------------------------------------------------------------------------
# Joined = a.b.c.d
# trailing delimiter _not_ OK

@cache
def Joined(pattern, delim):
  return Seq(
    pattern,
    Any(Seq(delim, pattern))
  )

#---------------------------------------------------------------------------------------------------
# Delimited spans

@cache
def Delimited(ldelim, rdelim):
  return Seq(ldelim, Until(rdelim), rdelim)

#---------------------------------------------------------------------------------------------------
# Create stuff in the context

@cache
def Capture(pattern):
  """
  Adds all tokens in the span matched by 'pattern' to the context stack
  """
  def match(span, ctx2):
    tail = pattern(span, ctx2)
    if not isinstance(tail, Fail):
      ctx2.stack.extend(span[:len(span) - len(tail)])
    return tail
  return match

@cache
def Node(node_type, pattern):
  """
  Turns all (key, value) tuples added to the context stack after this matcher into a parse node.
  """
  def match(span, ctx2):
    assert isinstance(span, (list, str))
    assert isinstance(ctx2, Context)

    top = len(ctx2.stack)
    tail = pattern(span, ctx2)
    if isinstance(tail, Fail):
      del ctx2.stack[top:]
      return tail

    values = ctx2.stack[top:]
    del ctx2.stack[top:]

    for val in values:
      assert isinstance(val, tuple)
      assert len(val) == 2

    #if len(values) == 0:
    #  ctx2.stack.append(None)
    #  return tail

    result = node_type()

    for field in values:
      if not isinstance(field, tuple):
        print(f"Field {field} is not a tuple")
        assert False
      if field[0] in result and result[field[0]] is not None:
        print(f"field {field[0]}:{field[1]} was already in {result}")
        assert False
      result[field[0]] = field[1]

    ctx2.stack.append(result)
    return tail

  return match

@cache
def TupleNode(tuple_type, pattern):
  def match(span, ctx2):
    top = len(ctx2.stack)
    tail = pattern(span, ctx2)
    if isinstance(tail, Fail):
      del ctx2.stack[top:]
      return tail

    values = ctx2.stack[top:]
    del ctx2.stack[top:]
    ctx2.stack.append(tuple_type(values))
    return tail
  return match

@cache
def ListNode(list_type, pattern):
  def match(span, ctx2):
    top = len(ctx2.stack)
    tail = pattern(span, ctx2)
    if isinstance(tail, Fail):
      del ctx2.stack[top:]
      return tail

    values = ctx2.stack[top:]
    del ctx2.stack[top:]
    ctx2.stack.append(list_type(values))
    return tail

  return match

@cache
def KeyVal(key, pattern):
  """
  Turns the top of the context stack into a (name, value) tuple
  """
  def match(span, ctx2):
    top = len(ctx2.stack)
    tail = pattern(span, ctx2)
    if isinstance(tail, Fail):
      del ctx2.stack[top:]
      return Fail(span)

    values = ctx2.stack[top:]
    del ctx2.stack[top:]
    if len(values) == 0:
      field = (key, None)
    elif len(values) == 1:
      field = (key, values[0])
    else:
      field = (key, values)
    ctx2.stack.append(field)
    return tail

  return match

def Railway(railway):
  """
  Matches a complex pattern represented as a "railway diagram" of simpler patterns connected in a
  graph. Matching starts with the "None" state and searches for a path to another "None" state.

  The implementation is brute-force and recursive and can blow up badly in pathological cases.
  However, in patterns like the example below where there can be initial ambiguity between
  'parse_expr' and 'parse_decl', it is both more concise and more intelligible than the equivalent
  tree of "Any(Seq(Opt(Seq(...." stuff.

  This example parses parenthesized, comma-delimited lists of mixed expressions and declarations.
  Trailing commas OK. Examples: (348, "foo", x : u32 = 7), (), (1,)

  parse_paren_tuple = Railway({
    None         : [PUNCT_LPAREN],
    PUNCT_LPAREN : [parse_expr, parse_decl, PUNCT_RPAREN],
    parse_expr   : [PUNCT_COMMA,            PUNCT_RPAREN],
    parse_decl   : [PUNCT_COMMA,            PUNCT_RPAREN],
    PUNCT_COMMA  : [parse_expr, parse_decl, PUNCT_RPAREN],
    PUNCT_RPAREN : [None]
  })
  """

  def step(state, tail, ctx2):
    top = len(ctx2.stack)
    # If the current state doesn't match, we fail
    if state is not None:
      tail = state(tail, ctx2)
      if isinstance(tail, Fail):
        del ctx2.stack[top:]
        return tail

    # Check all the possible next steps from this state
    for next_state in railway[state]:
      # If we reach a None, matching succeeds.
      if next_state is None:
        return tail

      # If next_state matches, we succeed.
      next_tail = step(next_state, tail, ctx2)
      if not isinstance(next_tail, Fail):
        return next_tail

    # If none of the next_state patterns match, we fail
    del ctx2.stack[top:]
    return Fail(tail)

  def match(span, ctx2):
    assert isinstance(span, (list, str))
    return step(None, span, ctx2)

  return match

#---------------------------------------------------------------------------------------------------

class BaseNode:
  def items(self):
    return self.__dict__.items()

  def keys(self):
    return self.__dict__.keys()

  def __contains__(self, key):
    return key in self.__dict__

  def __getitem__(self, key):
    return self.__dict__[key]

  def __setitem__(self, key, val):
    self.__dict__[key] = val

  def __getattr__(self, key):
    return self.__dict__[key]

  def __setattr__(self, key, val):
    self.__dict__[key] = val

  def __repr__(self):
    return self.__class__.__name__ + ":" + self.__dict__.__repr__()

#---------------------------------------------------------------------------------------------------

testresult = doctest.testmod(sys.modules[__name__])
print(f"Testing {__name__} : {testresult}")
