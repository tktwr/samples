// *memo_cpp.fstream*
#include <fstream>
#include <iostream>
#include <string>

#define ARRAY_SIZE 3

const std::string g_text = R"(example program.

data 0
data 1
data 2.0
)";
const int g_binary[ARRAY_SIZE] = {1, 2, 3};

void f_write_text_file(const char *fname) {
    std::ofstream ofs(fname);
    ofs << g_text;
}

void f_read_text_file(const char *fname) {
    std::ifstream ifs(fname);
    std::string line;
    while (std::getline(ifs, line)) {
        std::cout << line << std::endl;
    }
}

void f_write_binary_file(const char *fname) {
    std::ofstream ofs(fname, std::ios::binary);
    ofs.write(reinterpret_cast<const char*>(g_binary), sizeof(g_binary));
}

void f_read_binary_file(const char *fname) {
    std::ifstream ifs(fname, std::ios::binary);
    int data[ARRAY_SIZE];
    ifs.read(reinterpret_cast<char*>(data), sizeof(data));
    for (int i=0; i<ARRAY_SIZE; i++) {
        std::cout << data[i] << " ";
    }
    std::cout << std::endl;
}

int main(int argc, char *argv[]) {
    std::string fname_text = "data_fstream.txt";
    std::string fname_binary = "data_fstream.bin";

    f_write_text_file(fname_text.c_str());
    f_read_text_file(fname_text.c_str());
    f_write_binary_file(fname_binary.c_str());
    f_read_binary_file(fname_binary.c_str());

    return 0;
}
