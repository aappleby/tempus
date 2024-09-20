#include "tem_helpers.hpp"
// Simple message transmitter with a delay between transmissions

struct simple_msg {
private:

    // consts
    static constexpr int max_delay = 20;
    static constexpr int max_cursor = 58 - 1;
    static constexpr char* text = "asdkjflskjfs";

public:

    // ports
    struct _dst {
        u8 data;
        u1 valid;
        u1 ready;
    };
    _dst dst;

private:
    // state
    counter<max_delay> delay;
    counter<max_cursor> cursor;

    void reset() {
        delay = max_delay;
        cursor = 0;
    }

public:
    // update
    void update() {
        if (delay)
            delay = delay - 1;
        else if (dst.ready) {
            if (cursor == max_cursor) {
                cursor = 0;
                delay = max_delay;
            }
            else cursor = cursor + 1;
        }
    }
};
