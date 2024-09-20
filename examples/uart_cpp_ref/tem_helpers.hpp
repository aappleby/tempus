#include <stdint.h>

typedef unsigned char u8;
typedef unsigned char u1;

template<int max>
struct counter {
    counter(int max) : _max(max) {}

    bool operator bool() { return x != 0; }

    template<typename T> counter& operator =  (T y) { x = y; }
    template<typename T> T        operator -  (T y) { return x - y; }
    template<typename T> T        operator +  (T y) { return x + y; }
    template<typename T> bool     operator == (T y) { return x == y; }

    int x;
    int _max;
};

