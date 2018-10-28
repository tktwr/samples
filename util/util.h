#ifndef tt_util_h
#define tt_util_h

#include <string>

namespace tt {

    inline float Bytes_to_KB(std::size_t bytes) {
        return bytes / 1024.f;
    }

    inline float Bytes_to_MB(std::size_t bytes) {
        return bytes / 1024.f / 1024.f;
    }

    inline float Bytes_to_GB(std::size_t bytes) {
        return bytes / 1024.f / 1024.f / 1024.f;
    }

    inline void f_replace(std::string& str, const std::string& src, const std::string& dst) {
        auto pos = str.find(src);
        auto len = src.length();
        if (pos != std::string::npos) {
            str.replace(pos, len, dst);
        }
    }

}

#endif  // tt_util_h

