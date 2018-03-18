#include <opencv2/opencv.hpp>
#include <stdio.h>

using namespace cv;

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: display_image.exe image_file\n");
        return -1;
    }

    Mat image = imread(argv[1], 1);
    if (!image.data) {
        printf("No image data.\n");
        return -1;
    }
    namedWindow("display_image", WINDOW_AUTOSIZE);
    imshow("display_image", image);

    waitKey(0);

    return 0;
}
