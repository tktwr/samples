// *memo_cpp.string*
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool f_match(const std::string& s, const std::string& m) {
    auto i = s.find(m);
    if (i != std::string::npos) {
        std::cout << "matched" << std::endl;
        std::cout << "i        = " << i << std::endl;
    } else {
        std::cout << "not matched" << std::endl;
    }
    return true;
}

void f_transform(const std::string& s0) {
    std::cout << "s0 = " << s0 << std::endl;
    std::string s = s0;
    std::transform(s.begin(), s.end(), s.begin(), ::tolower);
    std::cout << "s = " << s << std::endl;
}

void f_string() {
    std::string s = "hello world";

    std::cout << "s        = " << s << std::endl;
    std::cout << "s.size() = " << s.size() << std::endl;
    f_match(s, "world");
    f_transform("Hello WORLD");
}

void f_substr() {
    std::string s = "0123456789";
    std::string ss;

    ss = s.substr(0, 3);
    std::cout << "ss       = " << ss << std::endl;

    ss = s.substr(3, 3);
    std::cout << "ss       = " << ss << std::endl;
}

int main(int argc, char *argv[]) {
    f_string();
    f_substr();
    return 0;
}

