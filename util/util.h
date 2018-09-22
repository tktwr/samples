#ifndef util_h
#define util_h

#include <string>

namespace tt {

typedef unsigned char  uchar;
typedef unsigned short ushort;
typedef unsigned int   uint;
typedef unsigned long  ulong;

template<typename T>
T f_clamp(T v, T l, T h) {
    return (v < l) ? l : (v > h) ? h : v;
}

void f_replace(std::string& str, const std::string& src, const std::string& dst) {
    auto pos = str.find(src);
    auto len = src.length();
    if (pos != std::string::npos) {
        str.replace(pos, len, dst);
    }
}

}  // namespace tt

#endif  // util_h

