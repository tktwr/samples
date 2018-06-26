// *memo_sample_chrono*
#include <iostream>
#include <chrono>

void f() {
}

int main(int argc, char *argv[]) {
    std::chrono::system_clock::time_point start, end;
    start = std::chrono::system_clock::now();
    f();
    end = std::chrono::system_clock::now();
    double elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count();
    std::cout << "elapsed time = " << elapsed << " ms" << std::endl;
    return 0;
}

