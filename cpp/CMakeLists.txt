cmake_minimum_required(VERSION 2.8)

project(sample CXX)

set(CMAKE_BUILD_TYPE Release)
#set(CMAKE_BUILD_TYPE Debug)

if(WIN32)
else(WIN32)
  set(CMAKE_C_COMPILER clang)
  set(CMAKE_CXX_COMPILER clang++)
  add_definitions("-static -Wall -std=c++11")
  #add_definitions("-static -Wall -std=c++14")
  #add_definitions("-static -Wall -std=c++17")
  #add_definitions("-static -Wall -std=c++2a")
endif(WIN32)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
include_directories(.. ../lib/glm ../lib/stb ../lib/spdlog/include)
link_directories(../lib)

add_executable(sample sample.cpp)
target_link_libraries(sample)

add_executable(sample_array sample_array.cpp)
target_link_libraries(sample_array)

add_executable(sample_c++11 sample_c++11.cpp)
target_link_libraries(sample_c++11)

add_executable(sample_cstdio sample_cstdio.cpp)
target_link_libraries(sample_cstdio)

add_executable(sample_fstream sample_fstream.cpp)
target_link_libraries(sample_fstream)

add_executable(sample_glm sample_glm.cpp)
target_link_libraries(sample_glm)

add_executable(sample_image sample_image.cpp)
target_link_libraries(sample_image)

add_executable(sample_syntax sample_syntax.cpp)
target_link_libraries(sample_syntax)

add_executable(sample_thread sample_thread.cpp)
target_link_libraries(sample_thread)

add_executable(sample_spdlog sample_spdlog.cpp)
target_link_libraries(sample_spdlog)

message(STATUS "PROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}")
message(STATUS "PROJECT_BINARY_DIR=${PROJECT_BINARY_DIR}")
message(STATUS "INCLUDE_DIRECTORIES=${INCLUDE_DIRECTORIES}")
message(STATUS "LINK_DIRECTORIES=${LINK_DIRECTORIES}")

