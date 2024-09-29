#include "tem_helpers.hpp"

struct simple_msg {
public:

  static constexpr int max_delay = 20;
  static constexpr int max_cursor = 58 - 1;
  static constexpr const char* text = "asdkjflskjfs";

  struct _dst {
    u8 data;
    u1 valid;
    u1 ready;
  };
  _dst dst;

  counter<max_delay>  delay;
  counter<max_cursor> cursor;

  void reset() {
    delay = max_delay;
    cursor = 0;
  }

  void tock() {
  }

  void tick() {
    counter<max_delay> _delay = delay;
    counter<max_cursor> _cursor;

    if (delay)
      _delay = delay - 1;
    else if (dst.ready) {
      if (cursor == max_cursor) {
        _cursor = 0;
        _delay = max_delay;
      }
      else _cursor = cursor + 1;
    }

    delay = _delay;
    cursor = _cursor;
  }
};
