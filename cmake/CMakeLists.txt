cmake_minimum_required(VERSION 3.8)

project(sample_cmake)

include(../config.cmake)

set(app_SRCS sample_cmake.cpp)

add_executable(${PROJECT_NAME} ${app_SRCS})
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS} ${OPENGL_gl_LIBRARY} ${GLFW_LIBS})

file(GLOB DATA_FILES icon.png ${OpenCV_DLLS})

add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy_if_different ${DATA_FILES} $<TARGET_FILE_DIR:${PROJECT_NAME}>
  )

