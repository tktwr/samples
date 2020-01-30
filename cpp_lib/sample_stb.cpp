#define STB_IMAGE_IMPLEMENTATION
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include <stb_image.h>
#include <stb_image_write.h>
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
    std::string in_fname = argv[1];
    std::string out_fname = argv[2];

    int w, h, n;
    unsigned char* data = stbi_load(in_fname.c_str(), &w, &h, &n, 4);
    if (!data) {
        std::cerr << "fail to load image" << std::endl;
        return 0;
    }

    stbi_write_png(out_fname.c_str(), w, h, 4, data, 0);

    stbi_image_free(data);

    return 0;
}

