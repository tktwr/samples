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

#endif  // image_util_h

