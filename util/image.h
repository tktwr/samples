#ifndef tt_image_h
#define tt_image_h

#include <iostream>
#include <vector>
#include <thread>
#include <atomic>
#include <functional>
#include <string.h>
#include "array.h"
#include "type.h"

namespace tt {

template<class T>
class Image {
public:
    Image() : m_w(0), m_h(0) {}
    Image(int w, int h) { resize(w, h); }

    void resize(int w, int h) {
        m_w = w;
        m_h = h;
        m_data.resize(w * h);
    }
    void alloc(int w, int h) {
        m_w = w;
        m_h = h;
        m_data.alloc(w * h);
    }

    void clear() {
        m_w = 0;
        m_h = 0;
        m_data.clear();
    }
    void fill(const T& v = T()) { m_data.fill(v); }

    bool empty() const { return m_data.empty(); }

    std::size_t size() const { return m_data.size(); }
    std::size_t sizeOfDataType() const { return m_data.sizeOfDataType(); }

    int w() const { return m_w; }
    int h() const { return m_h; }

    const T* data() const { return m_data.data(); }
          T* data()       { return m_data.data(); }

    T    getValue(int x, int y) const { return m_data[y * m_w + x]; }
    void setValue(int x, int y, const T& val) { m_data[y * m_w + x] = val; }

    void foreach_nothread(const std::function<void(T&, int, int)>& func) {
        for (int y = 0; y < m_h; y++) {
            for (int x = 0; x < m_w; x++) {
                T& val = m_data[y * m_w + x];
                func(val, x, y);
            }
        }
    }
    void foreach(const std::function<void(T&, int, int)>& func, int nthreads = -1) {
        if (nthreads == 0) {
            foreach_nothread(func);
            return;
        }
        if (nthreads == -1) {
            nthreads = std::thread::hardware_concurrency();
        }
        std::vector<std::thread> th;
        std::atomic<int> i(0);
        for (int t=0; t<nthreads; t++) {
            th.push_back(std::thread([&]() {
                int y = 0;
                while ((y = i++) < m_h) {
                    for (int x=0; x<m_w; x++) {
                        T& val = m_data[y * m_w + x];
                        func(val, x, y);
                    }
                }
            }));
        }
        for (auto& t : th) {
            t.join();
        }
    }
    void foreach_row_nothread(const std::function<void(int)>& func) {
        for (int y = 0; y < m_h; y++) {
            func(y);
        }
    }
    void foreach_row(const std::function<void(int)>& func, int nthreads = -1) {
        if (nthreads == 0) {
            foreach_row_nothread(func);
            return;
        }
        if (nthreads == -1) {
            nthreads = std::thread::hardware_concurrency();
        }
        std::vector<std::thread> th;
        std::atomic<int> i(0);
        for (int t=0; t<nthreads; t++) {
            th.push_back(std::thread([&]() {
                int y = 0;
                while ((y = i++) < m_h) {
                    func(y);
                }
            }));
        }
        for (auto& t : th) {
            t.join();
        }
    }

private:
    int m_w, m_h;
    Array<T> m_data;
};

template<class T>
void f_image_foreach(Image<T>& image, const std::function<void(Image<T>&, int, int)>& func, int nthreads = -1) {
    if (nthreads == 0) {
        for (int y = 0; y < image.h(); y++) {
            for (int x = 0; x < image.w(); x++) {
                func(image, x, y);
            }
        }
        return;
    }

    if (nthreads == -1) {
        nthreads = std::thread::hardware_concurrency();
    }
    std::vector<std::thread> th;
    std::atomic<int> i(0);
    for (int t=0; t<nthreads; t++) {
        th.push_back(std::thread([&]() {
                    int y = 0;
                    while ((y = i++) < image.h()) {
                        for (int x=0; x<image.w(); x++) {
                            func(image, x, y);
                        }
                    }
                }));
    }
    for (auto& t : th) {
        t.join();
    }
}

template<class T>
void f_image_foreach_row(Image<T>& image, const std::function<void(Image<T>&, int)>& func, int nthreads = -1) {
    if (nthreads == 0) {
        for (int y = 0; y < image.h(); y++) {
            func(image, y);
        }
        return;
    }

    if (nthreads == -1) {
        nthreads = std::thread::hardware_concurrency();
    }
    std::vector<std::thread> th;
    std::atomic<int> i(0);
    for (int t=0; t<nthreads; t++) {
        th.push_back(std::thread([&]() {
                    int y = 0;
                    while ((y = i++) < image.h()) {
                        func(image, y);
                    }
                }));
    }
    for (auto& t : th) {
        t.join();
    }
}

template<class T>
void f_image_foreach_col(Image<T>& image, const std::function<void(Image<T>&, int)>& func, int nthreads = -1) {
    if (nthreads == 0) {
        for (int x = 0; x < image.w(); x++) {
            func(image, x);
        }
        return;
    }

    if (nthreads == -1) {
        nthreads = std::thread::hardware_concurrency();
    }
    std::vector<std::thread> th;
    std::atomic<int> i(0);
    for (int t=0; t<nthreads; t++) {
        th.push_back(std::thread([&]() {
                    int x = 0;
                    while ((x = i++) < image.w()) {
                        func(image, x);
                    }
                }));
    }
    for (auto& t : th) {
        t.join();
    }
}

template<class T>
void f_image_print(Image<T>& image) {
    image.foreach([&](T& val, int x, int y) {
        std::cout << val << " ";
        if (x == image.w() - 1) std::cout << std::endl;
    }, 0);
    std::cout << std::flush;
}

template<class T>
void f_image_same_size(const Image<T>& img0, const Image<T>& img1) {
    return (img0.w() == img1.w()) && (img0.h() == img1.h());
}

template<class T>
void f_image_copy(Image<T>& dst, const Image<T>& src) {
    dst.alloc(src.w(), src.h());
    memcpy(dst.data(), src.data(), src.size() * src.sizeOfDataType());
}

typedef Image<Color1uc> Image1uc;
typedef Image<Color1us> Image1us;
typedef Image<Color1f>  Image1f;

typedef Image<Color3uc> Image3uc;
typedef Image<Color3us> Image3us;
typedef Image<Color3f>  Image3f;

typedef Image<Color4uc> Image4uc;
typedef Image<Color4us> Image4us;
typedef Image<Color4f>  Image4f;

}  // namespace tt

#endif  // tt_image_h

