// *memo_cpp.17*
#include <iostream>
#include <tuple>

using namespace std;

// *memo_cpp.17.nested_namespace*
// nested namespace
namespace a::b::c {
    int ival;
}

// *memo_cpp.17.structured_bidings*
std::tuple<bool, int, float> f_a() {
    bool bval = true;
    int ival = 123;
    float fval = 123.456;
    return {bval, ival, fval};
}

int main(int argc, char *argv[]) {
    a::b::c::ival = 10;

    auto [bval, ival, fval] = f_a();
    std::cout << "bval : " << bval << std::endl;
    std::cout << "ival : " << ival << std::endl;
    std::cout << "fval : " << fval << std::endl;

    return 0;
}

