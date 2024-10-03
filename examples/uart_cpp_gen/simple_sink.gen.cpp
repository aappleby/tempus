#include "tem_helpers.hpp"

struct simple_sink {

  struct _src {
    u8 data;
    u1 valid;
    u1 ready;
  };
  _src src;
  u8 data;

};
