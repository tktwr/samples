// *memo_sample_image*
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include <stb_image.h>
#include <stb_image_write.h>
#include <iostream>
#include <util/image.h>
#include <util/time.h>
#include <glm/glm.hpp>
#include <spdlog/spdlog.h>

using namespace std;

inline float bytes2kb(std::size_t bytes) {
    return bytes / 1024.f;
}

inline float bytes2mb(std::size_t bytes) {
    return bytes / 1024.f / 1024.f;
}

void f_image_save(const char* fname, std::size_t w, std::size_t h, int comp, const float* data) {
    unsigned char* dst_data = new unsigned char[w * h * 3];
    unsigned char* dst = dst_data;
    const float* src = data;

    for (int i=0; i<w*h*3; i++) {
        dst[i] = (unsigned char)(src[i] * 255);
    }
    stbi_write_png(fname, w, h, 3, dst_data, 0);

    delete [] dst_data;
}

void f_image_time() {
    auto console = spdlog::get("console");

    tt::Image<glm::vec3> image;
    tt::Time t;
    tt::TimeCollection tc;
    std::vector<int> nthreads{0, 1, 4, -1};
    std::size_t width = 4000;
    std::size_t height = 4000;

    for (int i=0; i<3; i++) {
        cout << "=== " << i << " ===" << endl;

        image.clear();

        t.start();
        image.resize(width, height);
        t.end();
        console->info("Image<glm::vec3>::resize() {} ms", t.getElapsedMSec());
        console->info("w={} h={} size={:.1f} MB", image.w(), image.h(), bytes2mb(image.size() * image.sizeOfDataType()));

        t.start();
        image.clear();
        t.end();
        console->info("Image<glm::vec3>::clear() {} ms", t.getElapsedMSec());

        t.start();
        image.alloc(width, height);
        t.end();
        console->info("Image<glm::vec3>::alloc() {} ms", t.getElapsedMSec());

        t.start();
        image.fill(glm::vec3(1, 1, 1));
        t.end();
        console->info("Image<glm::vec3>::fill() {} ms", t.getElapsedMSec());

        for (auto j : nthreads) {
            t.start();
            tt::f_image_foreach<glm::vec3>(image, [](tt::Image<glm::vec3>& image, int x, int y) {
                int w = image.w();
                int h = image.h();
                image.setValue(x, y, glm::vec3(float(x)/w, float(y)/h, 1));
            }, j);
            t.end();
            console->info("f_image_foreach<glm::vec3>: nthreads={} {} ms", j, t.getElapsedMSec());
        }
        f_image_save("out.png", image.w(), image.h(), 3, (float*)(image.data()));

        for (auto j : nthreads) {
            t.start();
            tt::f_image_foreach_row<glm::vec3>(image, [](tt::Image<glm::vec3>& image, int y) {
                const int w = image.w();
                for (int x=0; x<w; x++) {
                    image.setValue(x, y, glm::vec3(x, y, 1));
                }
            }, j);
            t.end();
            console->info("f_image_foreach_row<glm::vec3>: nthreads={} {} ms", j, t.getElapsedMSec());
        }

        for (auto j : nthreads) {
            t.start();
            tt::f_image_foreach_col<glm::vec3>(image, [](tt::Image<glm::vec3>& image, int x) {
                const int h = image.h();
                for (int y=0; y<h; y++) {
                    image.setValue(x, y, glm::vec3(x, y, 1));
                }
            }, j);
            t.end();
            console->info("f_image_foreach_col<glm::vec3>: nthreads={} {} ms", j, t.getElapsedMSec());
        }

        t.start();
        glm::vec3* p = image.data();
        for (int y=0; y<image.h(); y++) {
            for (int x=0; x<image.h(); x++) {
                *p = glm::vec3(x, y, 1);
                p++;
            }
        }
        t.end();
        console->info("loop: {} ms", t.getElapsedMSec());
    }
}

void f_image_usage() {
    tt::Image<int> image(10, 5);
    int nthreads = 0;

    {
        // explicit func
        std::function<void(tt::Image<int>&, int, int)> func = [](tt::Image<int>& image, int x, int y) {
            cout << x << " ";
            if (x == image.w() - 1) cout << endl;
        };
        // no need to specify the template param
        tt::f_image_foreach(image, func, nthreads);
        cout << endl;
    }

    {
        // auto func
        auto func = [](tt::Image<int>& image, int x, int y) {
            cout << x << " ";
            if (x == image.w() - 1) cout << endl;
        };
        // need to specify the template param
        tt::f_image_foreach<int>(image, func, nthreads);
        cout << endl;
    }

    {
        // lamda func
        // need to specify the template param
        tt::f_image_foreach<int>(image, [](tt::Image<int>& image, int x, int y) {
            cout << x << " ";
            if (x == image.w() - 1) cout << endl;
        }, nthreads);
        cout << endl;
    }

    {
        // lamda func
        tt::f_image_foreach<int>(image, [](tt::Image<int>& image, int x, int y) {
            image.setValue(x, y, x);
        }, nthreads);
        tt::f_image_print(image);
        cout << endl;
    }

    {
        // lamda func
        tt::f_image_foreach<int>(image, [](tt::Image<int>& image, int x, int y) {
            int val = image.getValue(x, y);
            val++;
            image.setValue(x, y, val);
        }, nthreads);
        tt::f_image_print(image);
        cout << endl;
    }
}

int main(int argc, char *argv[]) {
    spdlog::set_pattern("[%l] %v");
    auto console = spdlog::stdout_logger_mt("console");

    f_image_usage();
    f_image_time();

    return 0;
}
