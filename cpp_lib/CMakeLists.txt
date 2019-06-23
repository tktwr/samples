cmake_minimum_required(VERSION 3.8)

project(sample_cpp_lib CXX)

include($ENV{MY_LIBTT}/config/config.cmake)

add_executable(sample_cereal sample_cereal.cpp)
target_link_libraries(sample_cereal)

add_executable(sample_cmdline sample_cmdline.cpp)
target_link_libraries(sample_cmdline)

add_executable(sample_eigen sample_eigen.cpp)
target_link_libraries(sample_eigen)

add_executable(sample_glm sample_glm.cpp)
target_link_libraries(sample_glm)

add_executable(sample_json11 sample_json11.cpp ${JSON11_SRCS})
target_link_libraries(sample_json11)

#add_executable(sample_spdlog sample_spdlog.cpp)
#target_link_libraries(sample_spdlog)

