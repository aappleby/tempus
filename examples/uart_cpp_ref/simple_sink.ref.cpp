#include "tem_helpers.hpp"

struct simple_sink {

  struct _src {
    u8 data;
    u1 valid;
    u1 ready;
  };
  _src src;

  u8 data, _data;

  void reset() {
    data = 0;
  }

  void tock() {
    src.ready = 1;
    _data = data;
    if (src.valid) {
      _data = src.data;
    }
  }

  void tick() {
    data = _data;
  }
};
