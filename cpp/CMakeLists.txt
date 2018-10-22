cmake_minimum_required(VERSION 3.8)

project(sample CXX)

include(../config.cmake)

include_directories(..)

add_executable(sample sample.cpp)
target_link_libraries(sample)

add_executable(sample_array sample_array.cpp)
target_link_libraries(sample_array)

add_executable(sample_c++11 sample_c++11.cpp)
target_link_libraries(sample_c++11)

add_executable(sample_cereal sample_cereal.cpp)
target_link_libraries(sample_cereal)

add_executable(sample_cmdline sample_cmdline.cpp)
target_link_libraries(sample_cmdline)

add_executable(sample_cstdio sample_cstdio.cpp)
target_link_libraries(sample_cstdio)

add_executable(sample_fstream sample_fstream.cpp)
target_link_libraries(sample_fstream)

add_executable(sample_glm sample_glm.cpp)
target_link_libraries(sample_glm)

add_executable(sample_image sample_image.cpp)
target_link_libraries(sample_image)

add_executable(sample_spdlog sample_spdlog.cpp)
target_link_libraries(sample_spdlog)

add_executable(sample_syntax sample_syntax.cpp)
target_link_libraries(sample_syntax)

add_executable(sample_util sample_util.cpp)
target_link_libraries(sample_util)

add_executable(sample_thread sample_thread.cpp)
target_link_libraries(sample_thread)

