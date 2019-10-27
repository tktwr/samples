#include <stdio.h>
#include <string>
#include <iostream>
#include <opencv2/opencv.hpp>

const std::string DEFUALT_IMAGE = "../data/sample.jpg";

void f_image_create() {
    cv::Mat mat(480, 640, CV_8UC4);

    CV_Assert(mat.channels() == 4);

    for (int i = 0; i < mat.rows; ++i) {
        for (int j = 0; j < mat.cols; ++j) {
            cv::Vec4b& bgra = mat.at<cv::Vec4b>(i, j);
            bgra[0] = UCHAR_MAX; // Blue
            bgra[1] = cv::saturate_cast<uchar>((float (mat.cols - j)) / ((float)mat.cols) * UCHAR_MAX); // Green
            bgra[2] = cv::saturate_cast<uchar>((float (mat.rows - i)) / ((float)mat.rows) * UCHAR_MAX); // Red
            bgra[3] = UCHAR_MAX; // Alpha
        }
    }

    std::cout << "mat.rows: " << mat.rows << std::endl;
    std::cout << "mat.cols: " << mat.cols << std::endl;
    std::cout << "mat.data: " << reinterpret_cast<unsigned long long>(mat.data) << std::endl;

    cv::imwrite("_create.png", mat);
}

void f_image_filter(cv::Mat& src_img) {
    std::cout << "src_img.rows: " << src_img.rows << std::endl;
    std::cout << "src_img.cols: " << src_img.cols << std::endl;
    std::cout << "src_img.type(): " << src_img.type() << std::endl;
    std::cout << "src_img.depth(): " << src_img.depth() << std::endl;
    std::cout << "src_img.channels(): " << src_img.channels() << std::endl;
    std::cout << "src_img.elemSize(): " << src_img.elemSize() << std::endl;

    cv::Mat dst_img;

    cv::boxFilter(src_img, dst_img, src_img.type(), cv::Size(10, 10));
    cv::imwrite("_box_filter.png", dst_img);

    cv::bilateralFilter(src_img, dst_img, -1, 50, 20);
    cv::imwrite("_bilateral_filter.png", dst_img);
}

void f_image_morphology() {
    cv::Mat mat(400, 600, CV_8UC1);

    for (int i = 0; i < mat.rows; ++i) {
        for (int j = 0; j < mat.cols; ++j) {
            if (i > 195 && i < 205 && j > 150 && j < 450) {
                mat.at<uchar>(i, j) = 0;
            } else {
                mat.at<uchar>(i, j) = 255;
            }
        }
    }

    cv::imwrite("_morphology_orig.png", mat);

    cv::Mat dst_img;
    cv::erode(mat, dst_img, cv::Mat(), cv::Point(-1,-1), 4);
    cv::imwrite("_erode.png", dst_img);
    cv::dilate(mat, dst_img, cv::Mat(), cv::Point(-1,-1), 4);
    cv::imwrite("_dilate.png", dst_img);
}

int main(int argc, char **argv) {
    std::string fname = DEFUALT_IMAGE;

    if (argc == 2) {
        fname = argv[1];
    }

    cv::Mat src_img = cv::imread(fname.c_str(), cv::IMREAD_COLOR);

    if (src_img.empty()) {
        printf("No src_img data.\n");
        return -1;
    }

    cv::imwrite("_src_img.png", src_img);

    cv::namedWindow("display_image", cv::WINDOW_AUTOSIZE);
    cv::imshow("display_image", src_img);

    f_image_create();
    f_image_filter(src_img);
    f_image_morphology();

    cv::waitKey(0);

    return 0;
}
