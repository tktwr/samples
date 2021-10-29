#include <iostream>
#include <sstream>

using namespace std;

void f_istringstream(const std::string& line) {
    std::istringstream istr(line);
    istr.exceptions(std::ios::failbit);

    std::string token;

    try {
        std::string var;
        float fval;
        istr >> token >> var >> fval;
        std::cout << token << " " << var << " " << fval << std::endl;
    } catch(const std::exception& e) {
        std::cout << "catch!!" << std::endl;
        std::cout << e.what() << std::endl;
        std::cout << "error: token: " << token << std::endl;
    }
}

int main(int argc, char *argv[]) {
    f_istringstream("set x 1.23");
    f_istringstream("set x 1");
    f_istringstream("set x aaa");
    f_istringstream("set x -1.23");
    return 0;
}

