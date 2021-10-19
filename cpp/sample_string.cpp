// *memo_cpp.string*
#include <iostream>
#include <string>

using namespace std;

void f_string() {
    std::string s = "hello world";
    std::cout << "s = " << s << std::endl;
}

int main(int argc, char *argv[]) {
    f_string();
    return 0;
}

