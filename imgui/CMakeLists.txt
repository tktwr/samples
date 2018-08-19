cmake_minimum_required(VERSION 2.8)

project(sample_imgui CXX)

set(CMAKE_BUILD_TYPE Release)
#set(CMAKE_BUILD_TYPE Debug)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(IMGUI ${PROJECT_SOURCE_DIR}/../lib/imgui)
set(GLFW ${PROJECT_SOURCE_DIR}/../lib/imgui/examples/libs/glfw)
set(3RDPARTY ${PROJECT_SOURCE_DIR}/../3rdparty)

include_directories(
  ..
  ../lib/stb
  ${IMGUI}
  ${3RDPARTY}/include
)
link_directories(${3RDPARTY}/lib)

if(MSVC)
  message(STATUS "MSVC")
  include_directories(${GLFW}/include)
  link_directories(${GLFW}/lib-vc2010-64)
  set(GLFW_LIBS glfw3 legacy_stdio_definitions)
endif(MSVC)

if(MINGW)
  message(STATUS "MINGW")
  set(CMAKE_C_FLAGS "-static -Wall")
  set(CMAKE_CXX_FLAGS "-static -Wall -std=c++11")
  set(GLFW_LIBS glfw3)
endif(MINGW)

if(WIN32)
  message(STATUS "WIN32")
  set(OPENGL_LIBS glu32 opengl32 winmm gdi32)
endif(WIN32)

if(UNIX)
  message(STATUS "UNIX")
  set(OPENGL_LIBS GLU GL)
endif(UNIX)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(sample_imgui
  main.cpp
  gl_frame.cpp
  gl_app.cpp
  image_util.cpp
  ${IMGUI}/imgui.cpp
  ${IMGUI}/imgui_draw.cpp
)
target_link_libraries(sample_imgui 3rdparty ${OpenCV_LIBS} ${GLFW_LIBS} ${OPENGL_LIBS})

message(STATUS "PROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}")
message(STATUS "PROJECT_BINARY_DIR=${PROJECT_BINARY_DIR}")
message(STATUS "INCLUDE_DIRECTORIES=${INCLUDE_DIRECTORIES}")
message(STATUS "LINK_DIRECTORIES=${LINK_DIRECTORIES}")

