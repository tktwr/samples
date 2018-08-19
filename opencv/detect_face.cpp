#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

Mat detectFaceInImage(Mat &image,string &cascade_file){
	CascadeClassifier cascade;
	cascade.load(cascade_file);

	vector<Rect> faces;
	cascade.detectMultiScale(image, faces, 1.1,3,0,Size(20,20));

	for (int i = 0; i < faces.size(); i++){
		rectangle(image, Point(faces[i].x,faces[i].y),Point(faces[i].x + faces[i].width,faces[i].y + faces[i].height),Scalar(0,200,0),3,CV_AA);
	}
	return image;
}

int main(int argc, char const *argv[]){
	Mat image = imread(argv[1]);
	string filename = "haarcascades/haarcascade_frontalface_default.xml";
	Mat detectFaceImage = detectFaceInImage(image, filename);
	imshow("detect face",detectFaceImage);
	waitKey(0);

	return 0;
}
