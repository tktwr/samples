// *memo_cpp.17*
#include <filesystem>
#include <iostream>
#include <fstream>
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
    float fval = 123.456f;
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
void f_any() {
    std::any x = 3;
    int n = std::any_cast<int>(x);

    std::cout << n << std::endl;

    x = "Hello";
    const char* s = std::any_cast<const char*>(x);

    std::cout << s << std::endl;

    try {
        double d = std::any_cast<double>(x);
    } catch (const std::bad_any_cast& e) {
        std::cout << e.what() << std::endl;
    }
}

//-------------------------------------------------------------------------
// *memo_cpp.17.f_filesystem*
// *memo_cpp.17.f_filesystem_path*
namespace fs = std::filesystem;
std::string ODIR = "_output/fs/";

void f_filesystem_path() {
    fs::path p = "/a/b/c/d.txt";
    std::cout << "p         : " << p.string() << std::endl;
    std::cout << "directory : " << p.parent_path() << std::endl;
    std::cout << "filename  : " << p.filename() << std::endl;
    std::cout << "stem      : " << p.stem() << std::endl;
    std::cout << "extension : " << p.extension() << std::endl;

    fs::path cp = fs::current_path();
	fs::path pp = cp.parent_path();
	fs::path ap = fs::absolute("./test.txt");

    std::cout << cp.string() << std::endl;
	std::cout << pp.string() << std::endl;
	std::cout << ap.string() << std::endl;
	std::cout << ap.generic_string() << std::endl;
}

void f_init_test_dir() {
    fs::create_directories(ODIR);
    std::ofstream ofs(ODIR+"test.txt");
    ofs << "hello world" << std::endl;
}

void f_filesystem() {
    f_init_test_dir();

    bool exists = fs::exists(ODIR+"test.txt");
	bool is_file = fs::is_regular_file(ODIR+"test.txt");
	bool is_dir = fs::is_directory(ODIR);

	std::cout << "exists: " << exists << std::endl;
	std::cout << "is_file: " << is_file << std::endl;
	std::cout << "is_dir: " << is_dir << std::endl;

    fs::create_directory(ODIR+"dir1");
	fs::create_directories(ODIR+"dir2/a/b");

	fs::copy(ODIR+"test.txt", ODIR+"test2.txt");
	fs::copy(ODIR+"dir2", ODIR+"dir3", fs::copy_options::recursive);

	fs::rename(ODIR+"test2.txt", ODIR+"test3.txt");
	fs::rename(ODIR+"test3.txt", ODIR+"dir3/test3.txt");

	fs::remove(ODIR+"test.txt");
	fs::remove_all(ODIR+"dir2");

    std::cout << "---" << std::endl;
    auto&& di = fs::directory_iterator(ODIR);
    for (auto f : di) {
        std::cout << f.path().string() << std::endl;
    }

    std::cout << "---" << std::endl;
    auto&& rdi = fs::recursive_directory_iterator(ODIR);
    for (auto f : rdi) {
        std::cout << f.path().string() << std::endl;
    }
}

//-------------------------------------------------------------------------
int main(int argc, char *argv[]) {
    f_nested_namespace();
    f_structured_bidings();
    f_any();
    f_filesystem_path();
    f_filesystem();

    return 0;
}

