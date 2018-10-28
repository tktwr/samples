#ifndef image_util_h
#define image_util_h

#include <string>
#include <util/image.h>
#include <opencv2/opencv.hpp>

void   f_load_image(const std::string& fname, tt::Image4uc& image);
void   f_save_image(const std::string& fname, const tt::Image4uc& image);
void   f_draw_rect(tt::Image4uc& image, const tt::Vec2i& o, const tt::Vec2i& size, const tt::Color4uc& color);
void   f_fill_rect(tt::Image4uc& image, const tt::Vec2i& o, const tt::Vec2i& size, const tt::Color4uc& color);
void   f_create_vstripe_image(tt::Image4uc& image, int nw, const tt::Color4uc& color0, const tt::Color4uc& color1);
void   f_create_hstripe_image(tt::Image4uc& image, int nh, const tt::Color4uc& color0, const tt::Color4uc& color1);
void   f_create_checker_image(tt::Image4uc& image, int nw, int nh, const tt::Color4uc& color0, const tt::Color4uc& color1);
GLuint f_create_texture(const tt::Image4uc& image);
GLuint f_create_texture(GLsizei width, GLsizei height, const GLvoid* data);
void   f_image_to_cvmat(const tt::Image4uc& image, cv::Mat& mat);
void   f_cvmat_to_image(const cv::Mat& mat, tt::Image4uc& image);

namespace tt {

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

template<class T>
void f_image_flop(Image<T>& img) {
    img.foreach_row([&](int y) {
        for (int x=0; x<img.w()/2; x++) {
            int x2 = img.w() - 1 - x;
            T tmp = img.getValue(x, y);
            img.setValue(x, y, img.getValue(x2, y));
            img.setValue(x2, y, tmp);
        }
    });
}

template<class T>
void f_image_hgrad(Image<T>& img, const tt::Color4uc& co1, const tt::Color4uc& co2) {
    img.foreach_row([&](int y) {
        for (int x=0; x<img.w(); x++) {
            float t = float(x) / (img.w() - 1);
            tt::Color4uc co = (1 - t) * co1 + t * co2;
            img.setValue(x, y, co);
        }
    });
}

template<class T>
void f_image_vgrad(Image<T>& img, const tt::Color4uc& co1, const tt::Color4uc& co2) {
    img.foreach_row([&](int y) {
        float t = float(y) / (img.h() - 1);
        tt::Color4uc co = (1 - t) * co1 + t * co2;
        for (int x=0; x<img.w(); x++) {
            img.setValue(x, y, co);
        }
    });
}

}  // namespace tt

#endif  // image_util_h

