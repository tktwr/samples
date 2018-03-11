cmake_minimum_required(VERSION 2.8)
set(CMAKE_C_COMPILER clang)
set(CMAKE_CXX_COMPILER clang++)

project(sample CXX)

add_definitions("-static -Wall -std=c++11")

add_executable(sample sample.cpp)
target_link_libraries(sample -static)

add_executable(sample_fstream sample_fstream.cpp)
target_link_libraries(sample_fstream -static)

add_executable(sample_image sample_image.cpp)
target_link_libraries(sample_image -static)

