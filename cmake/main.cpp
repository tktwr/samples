#include <iostream>
#include "version.h"

using namespace std;

std::string GetGitCommit() {
    return A::GIT_COMMIT;
}

int main(int argc, char *argv[]) {
    std::cout << "Hello world." << std::endl;
    std::cout << "GIT_COMMIT: " << GetGitCommit() << std::endl;
    return 0;
}

