A tiny time-oriented programming language inspired by C, Verilog, and TLA+.

Tempus can be transpiled to C for use on CPUs and to Verilog for use on FPGAs. Perhaps eventually it will also support proofs via TLA+.

```
// Trivial counter in Tempus

[state]
x : int = 0;

[update]
@x = x + 1;
```
