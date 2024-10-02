#include "tem_helpers.hpp"

struct simple_sink {

  struct _bar {
    u8 baz;
    u8 bez;
  };
  struct _foo {
    _bar bar;
  };
  struct _src {
    _foo foo;
    u8 data;
    u1 valid;
    u1 ready;
  };
  _src src;
  u8 data;

};
