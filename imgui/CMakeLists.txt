cmake_minimum_required(VERSION 3.8)

project(sample_imgui)

include(../config.cmake)

include_directories(..)

set(app_SRCS
  main.cpp
  myglapp.cpp
  gl_app.cpp
  gl_frame.cpp
  image_util.cpp
  ../util/filename.cxx
  ${IMGUI_SRCS}
  ${GL3W_SRCS}
  ${NFD_SRCS}
  )
add_executable(${PROJECT_NAME} ${app_SRCS})
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS} ${OPENGL_gl_LIBRARY} ${GLFW_LIBS})

file(GLOB DATA_FILES data/icon.png ${OpenCV_DLLS})

add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy_if_different ${DATA_FILES} $<TARGET_FILE_DIR:${PROJECT_NAME}>
  )

