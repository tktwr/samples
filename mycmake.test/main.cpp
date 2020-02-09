#include <iostream>
#include "version.h"

using namespace std;

std::string GetGitBranch() {
    return version::GIT_BRANCH;
}

std::string GetGitCommit() {
    return version::GIT_COMMIT;
}

int main(int argc, char *argv[]) {
    std::cout << "Hello world." << std::endl;
    std::cout << "GIT_BRANCH: " << GetGitBranch() << std::endl;
    std::cout << "GIT_COMMIT: " << GetGitCommit() << std::endl;
    return 0;
}

