#ifndef tt_image_h
#define tt_image_h

#include <iostream>
#include <vector>
#include <thread>
#include <atomic>
#include <functional>
#include "array.h"
#include <string.h>

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
    f_image_foreach<T>(image, [](Image<T>& _image, int x, int y) {
        std::cout << _image.getValue(x, y) << " ";
        if (x == _image.w() - 1) std::cout << std::endl;
    }, 0);
    std::cout << std::flush;
}

template<class T>
void f_image_copy(Image<T>& dst, const Image<T>& src) {
    dst.alloc(src.w(), src.h());
    memcpy(dst.data(), src.data(), src.size() * src.sizeOfDataType());
}

template<class T>
void f_image_flip(Image<T>& img) {
	int w = img.w();
	int h = img.h();
	int lsize = w * img.sizeOfDataType();

	char* tmp = new char[lsize];

	for (int i=0; i<h/2; i++) {
		char* p1 = reinterpret_cast<char*>(img.data()) + i * lsize;
		char* p2 = reinterpret_cast<char*>(img.data()) + (h-1-i) * lsize;
		memcpy(tmp, p1, lsize);
		memcpy(p1, p2, lsize);
		memcpy(p2, tmp, lsize);
	}

	delete [] tmp;
}

template<typename T>
class RGBA {
public:
    RGBA() {}
	RGBA(T _x, T _y, T _z, T _w) { x=_x; y=_y; z=_z; w=_w; }
	RGBA(const T v[4]) { x=v[0]; y=v[1]; z=v[2]; w=v[3]; }
	// use default copy constructor
	// use default operator =()

	RGBA<T>& assign(T _x, T _y, T _z, T _w) { x=_x; y=_y; z=_z; w=_w; return *this; }
	RGBA<T>& assign(const T v[4]) { x=v[0]; y=v[1]; z=v[2]; w=v[3]; return *this; }

	      T* ptr()       { return &x; }
	const T* ptr() const { return &x; }
	      T& operator [](int i)       { return (&x)[i]; }
	const T& operator [](int i) const { return (&x)[i]; }

	bool operator==(const RGBA<T>& v) const { return x == v.x && y == v.y && z == v.z && w == v.w; }
	bool operator!=(const RGBA<T>& v) const { return !(*this == v); }

	T x, y, z, w;
};

typedef unsigned char  uchar;
typedef unsigned short ushort;
typedef RGBA<ushort> RGBA16;

template<typename T>
T f_clamp(T v, T l, T h) {
    return (v < l) ? l : (v > h) ? h : v;
}

class RGBA8 : public RGBA<uchar> {
public:
	RGBA8(uchar x, uchar y, uchar z, uchar w) : RGBA<uchar>(x, y, z, w) {}
	RGBA8(const uchar v[4]) : RGBA<uchar>(v) {}
    RGBA8(const float v[4]) { for (int i=0; i<4; i++) (*this)[i] = (uchar)(255.f * f_clamp(v[i], 0.f, 1.f)); }
};

}  // namespace tt

#endif  // tt_image_h

