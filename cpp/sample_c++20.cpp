// *memo_cpp.20*
#include <iostream>
#ifdef USE_CPP20
#include <format>
#endif

using namespace std;

// *memo_cpp.20.format*
void f_format() {
#ifdef USE_CPP20
    std::string message = std::format("The answer is {}.", 42);
#endif
}

int main(int argc, char *argv[]) {
    f_format();
    return 0;
}

