cmake_minimum_required(VERSION 2.8)

project(opencv_samples CXX)

add_definitions("-static -Wall -std=c++11")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(display_image display_image.cpp)
#target_link_libraries(display_image ${OpenCV_LIBS} -static)
target_link_libraries(display_image opencv_highgui opencv_imgproc opencv_core -static)

add_executable(detect_face detect_face.cpp)
target_link_libraries(detect_face ${OpenCV_LIBS} -static)

message(STATUS "OpenCV_INCLUDE_DIRS=${OpenCV_INCLUDE_DIRS}")
message(STATUS "OpenCV_LIBS=${OpenCV_LIBS}")

