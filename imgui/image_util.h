#ifndef image_util_h
#define image_util_h

#include <string>
#include <util/image.h>
#include <opencv2/opencv.hpp>

void   f_load_image(const std::string& fname, tt::Image<tt::RGBA8>& image);
void   f_save_image(const std::string& fname, const tt::Image<tt::RGBA8>& image);
void   f_rect(tt::Image<tt::RGBA8>& image, const std::array<int, 2>& o, const std::array<int, 2>& size, const tt::RGBA8& color);
void   f_fill_rect(tt::Image<tt::RGBA8>& image, const std::array<int, 2>& o, const std::array<int, 2>& size, const tt::RGBA8& color);
void   f_create_vstripe_image(tt::Image<tt::RGBA8>& image, int nw, const tt::RGBA8& color0, const tt::RGBA8& color1);
void   f_create_hstripe_image(tt::Image<tt::RGBA8>& image, int nh, const tt::RGBA8& color0, const tt::RGBA8& color1);
void   f_create_checker_image(tt::Image<tt::RGBA8>& image, int nw, int nh, const tt::RGBA8& color0, const tt::RGBA8& color1);
GLuint f_create_texture(tt::Image<tt::RGBA8>& image);
GLuint f_create_texture(GLsizei width, GLsizei height, const GLvoid* data);
void   f_image_to_cvmat(const tt::Image<tt::RGBA8>& image, cv::Mat& mat);
void   f_cvmat_to_image(const cv::Mat& mat, tt::Image<tt::RGBA8>& image);

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

}  // namespace tt

#endif  // image_util_h

