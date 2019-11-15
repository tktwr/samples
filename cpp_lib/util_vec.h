#pragma once

#include <limits>
#include <iostream>

namespace tt2 {

using uchar  = unsigned char;
using ushort = unsigned short;
using uint   = unsigned int;
using ulong  = unsigned long;

template<typename T>
inline T clamp(T v, T l, T h) {
    return (v < l) ? l : (v > h) ? h : v;
}

template<typename T, typename O>
inline O cvt(T v) {
    return clamp<T>(v, std::numeric_limits<O>::min(), std::numeric_limits<O>::max());
}

inline uchar add(const uchar& v1, const uchar& v2) { return cvt<uint, uchar>(v1 + v2); }
inline uchar sub(const uchar& v1, const uchar& v2) { return cvt<uint, uchar>(v1 - v2); }
inline uchar mul(const uchar& v1, const uchar& v2) { return cvt<uint, uchar>(v1 * v2); }
inline uchar mul(const uchar& v1, const float& v2) { return cvt<uint, uchar>(v1 * v2); }
inline uchar mul(const float& v1, const uchar& v2) { return cvt<uint, uchar>(v1 * v2); }
inline uchar div(const uchar& v1, const uchar& v2) { return cvt<uint, uchar>(v1 / v2); }

inline ushort add(const ushort& v1, const ushort& v2) { return cvt<uint, ushort>(v1 + v2); }
inline ushort sub(const ushort& v1, const ushort& v2) { return cvt<uint, ushort>(v1 - v2); }
inline ushort mul(const ushort& v1, const ushort& v2) { return cvt<uint, ushort>(v1 * v2); }
inline ushort mul(const ushort& v1, const float & v2) { return cvt<uint, ushort>(v1 * v2); }
inline ushort mul(const float & v1, const ushort& v2) { return cvt<uint, ushort>(v1 * v2); }
inline ushort div(const ushort& v1, const ushort& v2) { return cvt<uint, ushort>(v1 / v2); }

inline int add(const int& v1, const int& v2)   { return cvt<long, int>(v1 + v2); }
inline int sub(const int& v1, const int& v2)   { return cvt<long, int>(v1 - v2); }
inline int mul(const int& v1, const int& v2)   { return cvt<long, int>(v1 * v2); }
inline int mul(const int& v1, const float& v2) { return cvt<long, int>(v1 * v2); }
inline int mul(const float& v1, const int& v2) { return cvt<long, int>(v1 * v2); }
inline int div(const int& v1, const int& v2)   { return cvt<long, int>(v1 / v2); }

inline float add(const float& v1, const float& v2) { return v1 + v2; }
inline float sub(const float& v1, const float& v2) { return v1 - v2; }
inline float mul(const float& v1, const float& v2) { return v1 * v2; }
inline float div(const float& v1, const float& v2) { return v1 / v2; }

template<typename T, int N>
inline void vec_add(T o[N], T a[N], T b[N]) {
    for (int i = 0; i < N; ++i) { o[i] = add(a[i], b[i]); }
}

template<typename T, int N>
inline void vec_sub(T o[N], T a[N], T b[N]) {
    for (int i = 0; i < N; ++i) { o[i] = sub(a[i], b[i]); }
}

template<typename T, int N>
inline void vec_mul(T o[N], T a[N], T b[N]) {
    for (int i = 0; i < N; ++i) { o[i] = mul(a[i], b[i]); }
}

template<typename T, int N>
inline void vec_mul(T o[N], T a[N], float f) {
    for (int i = 0; i < N; ++i) { o[i] = mul(a[i], f); }
}

template<typename T, int N>
inline void vec_mul(T o[N], float f, T a[N]) {
    for (int i = 0; i < N; ++i) { o[i] = mul(f, a[i]); }
}

template<typename T, int N>
inline void vec_div(T o[N], T a[N], T b[N]) {
    for (int i = 0; i < N; ++i) { o[i] = div(a[i], b[i]); }
}

template<typename T, int N>
inline void vec_print(T a[N]) {
    for (int i = 0; i < N; ++i) { std::cout << float(a[i]) << " "; }
    std::cout << std::endl;
}

template<typename T, int N>
inline void vec_print(const std::string& s, T a[N]) {
    std::cout << s;
    vec_print<T, N>(a);
}

inline void u8vec2_print(const std::string& s, uchar a[2]) {
    vec_print<uchar, 2>(s, a);
}

inline void u8vec3_print(const std::string& s, uchar a[3]) {
    vec_print<uchar, 3>(s, a);
}

inline void u8vec4_print(const std::string& s, uchar a[4]) {
    vec_print<uchar, 4>(s, a);
}

inline void u16vec2_print(const std::string& s, ushort a[2]) {
    vec_print<ushort, 2>(s, a);
}

inline void u16vec3_print(const std::string& s, ushort a[3]) {
    vec_print<ushort, 3>(s, a);
}

inline void u16vec4_print(const std::string& s, ushort a[4]) {
    vec_print<ushort, 4>(s, a);
}

}

