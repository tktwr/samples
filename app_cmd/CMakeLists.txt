cmake_minimum_required(VERSION 3.8)

project(app_cmd CXX)

include($ENV{MY_LIBTT_WIN}/config.cmake)

if (EXISTS ${PROJECT_SOURCE_DIR}/local.cmake)
  include(${PROJECT_SOURCE_DIR}/local.cmake)
endif()

set(app_SRCS
  main.cpp
  )
add_executable(${PROJECT_NAME} ${app_SRCS})

