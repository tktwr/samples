#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// *memo_cpp.string*
void f_string() {
    std::string s = "hello world";

    std::cout << "s        = " << s << std::endl;
    std::cout << "s.size() = " << s.size() << std::endl;
}

// *memo_cpp.string.match*
// *memo_cpp.string.find*
bool f_string_match() {
    std::string s = "hello world";
    std::string m = "world";

    auto i = s.find(m);
    if (i != std::string::npos) {
        std::cout << "matched: " << i << std::endl;
    } else {
        std::cout << "not matched" << std::endl;
    }
    return true;
}

// *memo_cpp.string.transform*
// *memo_cpp.string.tolower*
void f_string_transform() {
    std::string s = "Hello WORLD";

    std::cout << "s = " << s << std::endl;
    std::transform(s.begin(), s.end(), s.begin(), ::tolower);
    std::cout << "s = " << s << std::endl;
}

// *memo_cpp.string.substr*
void f_string_substr() {
    std::string s = "0123456789";
    std::string ss;

    ss = s.substr(0, 3);
    std::cout << "ss       = " << ss << std::endl;

    ss = s.substr(3, 3);
    std::cout << "ss       = " << ss << std::endl;
}

// *memo_cpp.string.path*
void f_string_path() {
    std::string fname = "C:\\a\\b\\c\\d.txt";
    std::replace(fname.begin(), fname.end(), '\\', '/');
    std::cout << fname << std::endl;

    size_t i = fname.rfind('/');
    std::string dir;
    if (i != std::string::npos) {
        dir = fname.substr(0, i + 1);
    }
    std::cout << dir << std::endl;
}

int main(int argc, char *argv[]) {
    f_string();
    f_string_match();
    f_string_transform();
    f_string_substr();
    f_string_path();
    return 0;
}

