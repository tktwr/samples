cmake_minimum_required(VERSION 2.8)
set(CMAKE_C_COMPILER clang)
set(CMAKE_CXX_COMPILER clang++)

project(sample CXX)

add_definitions("-static -Wall -std=c++11")

add_executable(sample sample.cpp)
target_link_libraries(sample -static)

add_executable(sample_fstream sample_fstream.cpp)
target_link_libraries(sample_fstream -static)

add_executable(sample_cstdio sample_cstdio.cpp)
target_link_libraries(sample_cstdio -static)

add_executable(sample_image sample_image.cpp)
target_link_libraries(sample_image -static)

add_executable(sample_syntax sample_syntax.cpp)
target_link_libraries(sample_syntax -static)

add_executable(sample_c++11 sample_c++11.cpp)
target_link_libraries(sample_c++11 -static)

add_executable(sample_thread sample_thread.cpp)
target_link_libraries(sample_thread -static)

