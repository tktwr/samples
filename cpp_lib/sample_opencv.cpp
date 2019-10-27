// *memo_cpp_lib.opencv*
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;

void f_constructor() {
    // m(row, col)
    cv::Mat m(3, 4, CV_32F);
    std::cout << "dims = " << m.dims << std::endl;
    std::cout << "rows = " << m.rows << std::endl;
    std::cout << "cols = " << m.cols << std::endl;
}

void f_memory_order() {
    cv::Mat m(4, 4, CV_32F);
    std::cout << "dims = " << m.dims << std::endl;
    std::cout << "rows = " << m.rows << std::endl;
    std::cout << "cols = " << m.cols << std::endl;
    // row order input
    m = (cv::Mat_<float>(4, 4) <<
        1, 0, 0, 1,
        0, 1, 0, 1,
        0, 0, 1, 1,
        0, 0, 0, 1);
    std::cout << "m = " << m << std::endl;
}

int main(int argc, char *argv[]) {
    f_constructor();
    f_memory_order();
    return 0;
}

