cmake_minimum_required(VERSION 3.6)

project(sample_cpp CXX)

include($ENV{MY_LIBTT_WIN}/config.cmake)

set(CMAKE_CXX_STANDARD 20)

add_executable(sample sample.cpp)
target_link_libraries(sample)

add_executable(sample_c++11 sample_c++11.cpp)
target_link_libraries(sample_c++11)

add_executable(sample_c++14 sample_c++14.cpp)
target_link_libraries(sample_c++14)

add_executable(sample_c++17 sample_c++17.cpp)
target_link_libraries(sample_c++17)

add_executable(sample_c++20 sample_c++20.cpp)
target_link_libraries(sample_c++20)

add_executable(sample_class sample_class.cpp)
target_link_libraries(sample_class)

add_executable(sample_cstdio sample_cstdio.cpp)
target_link_libraries(sample_cstdio)

add_executable(sample_fstream sample_fstream.cpp)
target_link_libraries(sample_fstream)

add_executable(sample_syntax sample_syntax.cpp)
target_link_libraries(sample_syntax)

add_executable(sample_thread sample_thread.cpp)
target_link_libraries(sample_thread)

add_executable(sample_template sample_template.cpp)
target_link_libraries(sample_template)

