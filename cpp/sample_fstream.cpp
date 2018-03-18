#include <fstream>
#include <iostream>
#include <string>

const char *g_text[] = {
    "example program.\n",
    "\n",
    "data 0\n",
    "data 1\n",
    "data 2.0\n",
    "\0"};

void f_write_text_file(const char *fname) {
    std::ofstream ofs(fname);
    for (int i = 0; g_text[i][0]; i++) {
        ofs << g_text[i];
    }
}

void f_read_text_file(const char *fname) {
    std::ifstream ifs(fname);
    std::string line;
    while (getline(ifs, line)) {
        std::cout << line << std::endl;
    }
}

void f_write_binary_file(const char *fname) {
    std::ofstream ofs(fname, std::ios::out | std::ios::binary);
}

void f_read_binary_file(const char *fname) {
    std::ifstream ifs(fname, std::ios::in | std::ios::binary);
}

int main(int argc, char *argv[]) {
    std::string fname = "data_fstream.txt";

    f_write_text_file(fname.c_str());
    f_read_text_file(fname.c_str());

    return 0;
}
