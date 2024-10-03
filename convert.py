#!/usr/bin/python3

import argparse
import os
import sys
from tempus import tem_lexer
from tempus import tem_parser
from tempus import matcheroni

def tok_span_to_text(span):
  text   = span.base[span.start].span.base
  text_a = span.base[span.start].span.start
  text_b = span.base[span.stop-1].span.stop
  return text[text_a:text_b]

#==============================================================================

class Cursor:
  def __init__(self):
    self.source_file = None
    self.tok_cursor = None
    self.str_out = ""
    self.indent_level = 0
    self.at_comma = False
    self.line_dirty = False
    self.line_elided = False
    self.echo = False

  def __call__(self, *args, **kwargs):
    pass

  def start_line(self):
    pass

#==============================================================================

class Emitter:

  def __init__(self):
    self.filename = None
    self.tree = None
    self.ports = {}
    self.regs = []
    self.cursor = Cursor()
    self.at_newline = True

  #========================================

  def emit(self, *args, **kwargs):
    if self.at_newline:
      print("  " * self.cursor.indent_level, end="")
      self.at_newline = False
    print(*args, **kwargs, end="")
    return self

  def start_line(self):
    if not self.at_newline:
      self.newline()
    return self

  def newline(self):
    print("")
    self.at_newline = True
    return self

  #========================================

  def emit_node(self, node):
    match node:
      case tem_parser.AtomNode():
        pass
      case _:
        pass

  #========================================

  def emit_port_struct_decl(self, name, port_type):
    if "type" in port_type:
      pass
    else:
      for key, val in port_type.items():
        self.emit_port_struct_decl(key, val)
      self.emit(f"struct {self.mod_name}_{name} {{").newline().indent()
      for key, val in port_type.items():
        if "type" in val:
          self.emit(f"{val['type']['base'][0].to_str()} {key};").newline()
        else:
          self.emit(f"{self.mod_name}_{key} {key};").newline()
      self.dedent().emit("};").newline()
    return self

  #========================================

  def emit_port_struct_decls(self):
    for key, val in self.ports.items():
      self.emit_port_struct_decl(key, val)
    for key, val in self.ports.items():
      if "type" in val:
        self.emit(f"{val['type']['base'][0].to_str()} {key}, _{key};").newline()
      else:
        self.emit(f"{self.mod_name}_{key} {key}, _{key};").newline()
    return self.newline()

  #========================================

  def add_port_path(self, path):
    cursor = self.ports
    while len(path):
      assert(path[0].eq("."))
      branch = path[1].to_str()
      if branch not in cursor:
        cursor[branch] = {}
      cursor = cursor[branch]
      path = path[2:]
    return cursor

  #========================================

  def emit_port_structs(self):
    for node in self.tree:
      if isinstance(node, tem_parser.AtomNode):
        if node.name[0].eq("."):
          leaf = self.add_port_path(node.name)
          leaf["type"] = node.type
    return self.emit_port_struct_decls()

  #========================================

  def emit_expr(self, expr):
    if isinstance(expr, tem_lexer.Lexeme):
      self.emit(expr.to_str())
    elif isinstance(expr, tem_parser.ExprNode):
      for index, term in enumerate(expr):
        self.emit_expr(term)
        if index == len(expr) - 1:
          self.emit(";")
        else:
          self.emit(" ")
    else:
      self.emit("???")
    return self

  #========================================

  def emit_reg_name(self, reg):
    assert isinstance(reg.name, tem_parser.IdentNode)
    name = list(reg.name)
    if name[0].to_str() == ".":
      name = name[1:]
    for n in name:
      self.emit(n.to_str())
    return self

  #========================================

  def collect_regs(self):
    for node in self.tree:
      if isinstance(node, tem_parser.AtomNode):
        if "dir" in node and node.dir.to_str() == ":":
          self.regs.append(node)

  #========================================

  def emit_reset(self):
    self.collect_regs()

    self.emit("void reset() {").newline().indent()
    for reg in self.regs:
      self.emit_reg_name(reg).emit(" = ").emit_expr(reg.val).newline()
    self.dedent().emit("}").newline()
    self.newline()
    return self

  #========================================

  def emit_tock(self):
    self.emit("void tock() {").newline().indent()

    for key, _ in self.ports.items():
      self.emit(f"_{key} = {key};").newline()

    self.dedent().emit("}").newline()
    self.newline()
    return self

  #========================================

  def emit_tick(self):
    self.emit("void tick() {").newline().indent()

    for key, _ in self.ports.items():
      self.emit(f"{key} = _{key};").newline()

    self.dedent().emit("}").newline()
    self.newline()
    return self

  #========================================

  def indent(self):
    self.cursor.indent_level = self.cursor.indent_level + 1
    return self

  def dedent(self):
    self.cursor.indent_level = self.cursor.indent_level - 1
    return self

  def emit_divider(self):
    return self.emit("//" + "-" * 78).newline()

  #========================================

  def convert(self, filename, tree):
    self.filename = filename
    self.tree = tree

    print(tem_parser.dump_tree(self.tree))
    print()

    self.mod_name = os.path.basename(filename)
    self.mod_name = os.path.splitext(self.mod_name)[0]

    self.emit_divider().newline()
    self.emit("#include \"tem_helpers.hpp\"").newline().newline()

    self.emit(f"struct {self.mod_name} {{").newline().indent()

    self.emit_port_structs()
    self.emit_reset()
    self.emit_tock()
    self.emit_tick()

    self.dedent().emit("};").newline().newline()
    self.emit_divider()

#==============================================================================

def main():

  args = argparse.ArgumentParser()
  args.add_argument("filename", type=str, default=None, nargs="?")
  args.add_argument("-o",       dest="out", type=str, default=None, nargs=1, required=True)
  (flags, unknown) = args.parse_known_args()

  if flags.filename is None:
    args.print_help()
    sys.exit(1)

  with open(flags.filename, encoding="utf-8") as file:
    source = file.read()

    lex_ctx    = matcheroni.Context(matcheroni.default_atom_cmp)
    lex_fail   = tem_lexer.lex_string(source, lex_ctx)
    if lex_fail:
      raise ValueError("Lexing failed", lex_ctx.stack)

    parse_ctx  = matcheroni.Context(tem_lexer.atom_cmp_tokens)
    parse_fail = tem_parser.parse_lexemes(lex_ctx.stack, parse_ctx)
    if parse_fail:
      raise ValueError("Parsing failed", parse_ctx.stack)

    emitter = Emitter()
    emitter.convert(flags.filename, parse_ctx.stack)

    tock_terms = []

    for node in parse_ctx.stack:
      match node:
        case tem_parser.AtomNode():
          if not node.name[0].eq("."):
            tock_terms.append(node)
        case tem_parser.BranchNode():
          tock_terms.append(node)
        case tem_parser.MatchNode():
          tock_terms.append(node)
        case tem_parser.ExprNode():
          tock_terms.append(node)
        case tem_parser.CallNode():
          tock_terms.append(node)
        case _:
          print(f"Node is a {node.__class__.__name__}")

    print()
    for node in tock_terms:
      print(tem_parser.dump_variant(node))

#==============================================================================

if __name__ == "__main__":
  main()