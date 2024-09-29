#include "tem_helpers.hpp"

template<
int clocks_per_bit = 4,
int bits_per_byte = 10,
int delay_mid = clocks_per_bit / 2,
int delay_max = clocks_per_bit - 1,
int count_max = bits_per_byte - 1
>
struct simple_rx {

  u1 src;
  struct _dst {
    u8 data;
    u1 valid;
    u1 ready;
  };
  _dst dst;

  counter<delay_max> delay_reg;
  counter<count_max> count_reg;
  u8 shift_reg;

  counter<delay_max> _delay_reg;
  counter<count_max> _count_reg;
  u8 _shift_reg;

  void reset() {
    delay_reg = delay_max;
    count_reg = count_max;
    shift_reg = 0;
  }

  void tock() {
    dst.data = shift;
    dst.valid = 0;

    _delay_reg = delay_reg;
    _count_reg = count_reg;
    _shift_reg = shift_reg;

    /*match (true)*/ {
      if (true == (delay < delay_max)) {
        _delay = delay + 1;
      }
      else if (true == (count < count_max)) {
        _delay = 0;
        _count = count + 1;
      }
      else if (true == (src == 0)) {
        _delay = 0;
        _count = 0;
      }
    }

    if (delay == delay_mid) {
      _shift = (src << 7) | (shift >> 1);
      // I think this is wrong...
      dst.valid = _count == 8;
    }
  }

  void tick() {
    delay_reg = _delay_reg;
    count_reg = _count_reg;
    shift_reg = _shift_reg;
  }

};