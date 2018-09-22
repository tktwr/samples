#include <iostream>
#include <util/util.h>

using namespace std;

int main(int argc, char *argv[]) {
    std::string s = "a bc de f";
    tt::f_replace(s, "bc", "BCD");
    cout << s << endl;
    return 0;
}

