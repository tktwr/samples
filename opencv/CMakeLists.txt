cmake_minimum_required(VERSION 2.8)
set(CMAKE_C_COMPILER clang)
set(CMAKE_CXX_COMPILER clang++)

project(opencv_samples CXX)

add_definitions("-static -Wall -std=c++11")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(display_image display_image.cpp)
#target_link_libraries(display_image ${OpenCV_LIBS} -static)
target_link_libraries(display_image opencv_highgui opencv_imgproc opencv_core -static)

message(STATUS "OpenCV_INCLUDE_DIRS=${OpenCV_INCLUDE_DIRS}")
message(STATUS "OpenCV_LIBS=${OpenCV_LIBS}")

