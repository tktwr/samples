cmake_minimum_required(VERSION 3.6)

project(sample_cpp CXX)

include($ENV{MY_LIBTT_WIN}/config.cmake)

set(CMAKE_CXX_STANDARD 20)

function(func app cpp)
  add_executable(${app} ${cpp})
  target_link_libraries(${app})
endfunction()

set(APP
  sample_util
  )
set(APP_ALL
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
  sample_stream
  sample_string
  sample_syntax
  sample_template
  sample_thread
  sample_util
)

foreach(app IN LISTS APP)
  message("app: ${app}")
  func(${app} ${app}.cpp)
endforeach()

