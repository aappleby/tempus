#!/usr/bin/python3

import argparse
import os
import sys
from tempus import tem_lexer
from tempus import tem_parser
from tempus import matcheroni

#==============================================================================

class Emitter:

  def __init__(self):
    self.ports = {}

  #========================================

  def emit_port_struct_decl(self, name, type):
    if "type" in type:
      #print(f"{name} has a type")
      pass
    else:
      for key, val in type.items():
        self.emit_port_struct_decl(key, val)
      #print(f"{name} has no type")
      print(f"  struct _{name} {{")
      for key, val in type.items():
        if "type" in val:
          print(f"    {val['type']['base'][0].text} {key};")
        else:
          print(f"    _{key} {key};")
      print(f"  }};")
      #print(tem_parser.dump_tree(type))

  def emit_port_struct_decls(self):
    for key, val in self.ports.items():
      self.emit_port_struct_decl(key, val)
    for key, val in self.ports.items():
      if "type" in val:
        print(f"  {val['type']['base'][0].text} {key};")
      else:
        print(f"  _{key} {key};")

  def add_port_path(self, path):
    cursor = self.ports
    while len(path):
      assert(path[0].eq("."))
      branch = path[1].text
      if branch not in cursor:
        cursor[branch] = {}
      cursor = cursor[branch]
      path = path[2:]
    return cursor

  def emit_port_structs(self, tree):
    for node in tree:
      if isinstance(node, tem_parser.AtomNode):
        if node.name[0].eq("."):
          leaf = self.add_port_path(node.name)
          leaf["type"] = node.type
          #print(leaf)
          #self.ports[node.name[1]].append(node)
    #print(tem_parser.dump_tree(self.ports))
    #print(self.ports)
    #for key, node in self.ports.items():
    #  print(tem_parser.dump_tree(node))
    self.emit_port_struct_decls()

  #========================================

  def emit(self, filename, trees):
    print(tem_parser.dump_tree(trees))
    print()

    print("//------------------------------------------------------------------------------")
    print()
    print("#include \"tem_helpers.hpp\"")
    print()

    mod_name = os.path.basename(filename)
    mod_name = os.path.splitext(mod_name)[0]

    print(f"struct {mod_name} {{")
    print()

    self.emit_port_structs(trees)
    print()

    print("};")
    print()
    print("//------------------------------------------------------------------------------")
    print()

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

    #print()
    #print(tem_parser.dump_tree(lex_ctx.stack))

    parse_ctx  = matcheroni.Context(tem_lexer.atom_cmp_tokens)
    parse_fail = tem_parser.parse_lexemes(lex_ctx.stack, parse_ctx)
    if parse_fail:
      raise ValueError("Parsing failed", parse_ctx.stack)

    #print()
    #print(tem_parser.dump_tree(parse_ctx.stack))
    emitter = Emitter()
    emitter.emit(flags.filename, parse_ctx.stack)

#==============================================================================

if __name__ == "__main__":
  main()