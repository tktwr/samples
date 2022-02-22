// *memo_cpp.17*
#include <filesystem>
#include <iostream>
#include <tuple>
#include <any>

using namespace std;

//-------------------------------------------------------------------------
// *memo_cpp.17.f_nested_namespace*
namespace a::b::c {
    int ival;
}

void f_nested_namespace() {
    a::b::c::ival = 10;
    std::cout << "a::b::c::ival : " << a::b::c::ival << std::endl;
}

//-------------------------------------------------------------------------
// *memo_cpp.17.f_structured_bidings*
std::tuple<bool, int, float> f_a() {
    bool bval = true;
    int ival = 123;
    float fval = 123.456;
    return {bval, ival, fval};
}

void f_structured_bidings() {
    auto [bval, ival, fval] = f_a();
    std::cout << "bval : " << bval << std::endl;
    std::cout << "ival : " << ival << std::endl;
    std::cout << "fval : " << fval << std::endl;
}

//-------------------------------------------------------------------------
// *memo_cpp.17.f_any*
/*
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
*/

//-------------------------------------------------------------------------
// *memo_cpp.17.f_filesystem*
void f_filesystem() {
    std::filesystem::path p = std::filesystem::current_path();
	std::filesystem::path pp = p.parent_path();
	std::filesystem::path ap = std::filesystem::absolute("./test.txt");

    std::cout << p.string() << std::endl;
	std::cout << pp.string() << std::endl;
	std::cout << ap.string() << std::endl;

    bool exists = std::filesystem::exists("./test.txt");
	bool is_dir = std::filesystem::is_directory("./test.txt");
	bool is_file = std::filesystem::is_regular_file("./test.txt");

	std::cout << "exists: " << exists << std::endl;
	std::cout << "is_dir: " << is_dir << std::endl;
	std::cout << "is_file: " << is_file << std::endl;
}

//-------------------------------------------------------------------------
int main(int argc, char *argv[]) {
    f_nested_namespace();
    f_structured_bidings();
    //f_any();
    f_filesystem();

    return 0;
}

