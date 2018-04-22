// *memo_sample_opencv*
#include <stdio.h>
#include <string>
#include <opencv2/opencv.hpp>

using namespace cv;

const std::string DEFUALT_IMAGE = "../data/sample.jpg";

int main(int argc, char **argv) {
    std::string fname = DEFUALT_IMAGE;

    if (argc == 2) {
        fname = argv[1];
    }

    Mat src_img = imread(fname.c_str(), 1);

    if (!src_img.data) {
        printf("No src_img data.\n");
        return -1;
    }

    Mat dst_img;

    boxFilter(src_img, dst_img, src_img.type(), Size(10, 10));
    bilateralFilter(src_img, dst_img, -1, 50, 20);

    namedWindow("display_image", WINDOW_AUTOSIZE);
    imshow("display_image", dst_img);

    waitKey(0);

    return 0;
}
