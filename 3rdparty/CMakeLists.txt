cmake_minimum_required(VERSION 2.8)

project(3rdparty)

set(CMAKE_BUILD_TYPE Release)
#set(CMAKE_BUILD_TYPE Debug)

include_directories(include)
include_directories(../lib/imgui)

if(MSVC)
  message(STATUS "MSVC")
endif(MSVC)

if(MINGW)
  message(STATUS "MINGW")
  set(CMAKE_C_COMPILER clang)
  set(CMAKE_CXX_COMPILER clang++)
  set(CMAKE_C_FLAGS "-static -Wall")
  set(CMAKE_CXX_FLAGS "-static -Wall -std=c++11")
endif(MINGW)

set(CMAKE_INSTALL_PREFIX ${PROJECT_SOURCE_DIR})

set(3rdparty_SRCS
  src/gl3w/gl3w.c
  src/nfd/nfd_common.c
  src/nfd/nfd_win.cpp
  src/imgui/imgui_impl_glfw.cpp
  src/imgui/imgui_impl_opengl3.cpp
)
add_library(3rdparty STATIC ${3rdparty_SRCS})
install(TARGETS 3rdparty ARCHIVE DESTINATION lib)

message(STATUS "PROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}")
message(STATUS "PROJECT_BINARY_DIR=${PROJECT_BINARY_DIR}")
message(STATUS "INCLUDE_DIRECTORIES=${INCLUDE_DIRECTORIES}")
message(STATUS "LINK_DIRECTORIES=${LINK_DIRECTORIES}")

