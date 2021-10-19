cmake_minimum_required(VERSION 3.6)

project(sample_cpp CXX)

include($ENV{MY_LIBTT_WIN}/config.cmake)

set(CMAKE_CXX_STANDARD 20)

function(func app)
  add_executable(${app} ${app}.cpp)
  target_link_libraries(${app})
endfunction()

set(APPS
  sample_c++11
  sample_c++14
  sample_c++17
  sample_c++20
  sample_class
  sample_cstdio
  sample_fstream
  sample_hello_world
  sample_move
  sample_stl
  sample_string
  sample_syntax
  sample_template
  sample_thread
)

foreach(app IN LISTS APPS)
  message("app: ${app}")
  func(${app})
endforeach()

