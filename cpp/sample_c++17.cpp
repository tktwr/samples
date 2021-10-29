// *memo_cpp.17*
#include <iostream>
#include <tuple>
#include <any>

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

void f_any() {
    // int型の値を代入して取り出す
    std::any x = 3;
    int n = std::any_cast<int>(x);

    std::cout << n << std::endl;

    // 文字列を再代入して取り出す
    x = "Hello";
    const char* s = std::any_cast<const char*>(x);

    std::cout << s << std::endl;

    // 間違った型で取り出そうとすると例外が送出される
    try {
        std::any_cast<double>(x);
    } catch (const std::bad_any_cast& e) {
        std::cout << e.what() << std::endl;
    }
}

int main(int argc, char *argv[]) {
    a::b::c::ival = 10;

    auto [bval, ival, fval] = f_a();
    std::cout << "bval : " << bval << std::endl;
    std::cout << "ival : " << ival << std::endl;
    std::cout << "fval : " << fval << std::endl;

    f_any();

    return 0;
}

