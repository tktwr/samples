#include <iostream>
#include <sstream>

using namespace std;

struct Vec3 {
    float x, y, z;
};

template <typename T0>
void PrintImpl(std::stringstream& ss, const T0& t0) {
    ss << t0;
}

template <>
void PrintImpl(std::stringstream& ss, const Vec3& v) {
    ss << v.x << " " << v.y << " " << v.z;
}

// end of recursive call
template <typename T0>
void AsStrImpl(std::stringstream& ss, const T0& t0) {
    PrintImpl(ss, t0);
}

// recursive call
template <typename T0, typename... T1>
void AsStrImpl(std::stringstream& ss, const T0& t0, const T1... t1) {
    PrintImpl(ss, t0);
    AsStrImpl(ss, t1...);
}

template <typename... T>
std::string AsStr(const T... t) {
    std::stringstream ss;
    AsStrImpl(ss, t...);
    return ss.str();
}

int main(int argc, char *argv[]) {
    cout << AsStr("int: ", 1, ", float: ", 1.23f) << endl;

    Vec3 v = {1, 2, 3};
    cout << AsStr("Vec3: ", v) << endl;

    return 0;
}

