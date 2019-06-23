cmake_minimum_required(VERSION 3.8)

project(app_imgui)

include($ENV{MY_LIBTT}/config/config.cmake)

set(app_SRCS
  main.cpp
  myglapp.cpp
  ${LIBTT_SRCS}
  ${IMGUI_SRCS}
  ${GL3W_SRCS}
  ${NFD_SRCS}
  ${JSON11_SRCS}
  )
add_executable(${PROJECT_NAME} ${app_SRCS})
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS} ${OPENGL_gl_LIBRARY} ${GLFW_LIBS})

file(GLOB DATA_FILES data/icon.png ${OpenCV_DLLS})

if(NOT ("${DATA_FILES}" STREQUAL ""))
  add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different ${DATA_FILES} $<TARGET_FILE_DIR:${PROJECT_NAME}>
    )
endif()

