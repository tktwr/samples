cmake_minimum_required(VERSION 3.8)

project(3rdparty)

include(../config.cmake)

include_directories(include)

set(3rdparty_SRCS
  src/gl3w/gl3w.c
  src/nfd/nfd_common.c
  src/nfd/nfd_win.cpp
  src/imgui/imgui_impl_glfw.cpp
  src/imgui/imgui_impl_opengl3.cpp
)
add_library(3rdparty STATIC ${3rdparty_SRCS})
install(TARGETS 3rdparty ARCHIVE DESTINATION lib)

