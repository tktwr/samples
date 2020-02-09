cmake_minimum_required(VERSION 3.6)

project(sample_cpp_lib CXX)

include($ENV{MY_LIBTT_WIN}/config.cmake)

add_executable(sample_cereal sample_cereal.cpp)
target_link_libraries(sample_cereal)

add_executable(sample_cmdline sample_cmdline.cpp)
target_link_libraries(sample_cmdline)

add_executable(sample_eigen sample_eigen.cpp)
target_link_libraries(sample_eigen)

add_executable(sample_glm sample_glm.cpp)
target_link_libraries(sample_glm)

add_executable(sample_json11 sample_json11.cpp ${JSON11_SRCS})
target_link_libraries(sample_json11)

add_executable(sample_opencv sample_opencv.cpp)
target_link_libraries(sample_opencv ${OpenCV_LIBS})

#add_executable(sample_spdlog sample_spdlog.cpp)
#target_link_libraries(sample_spdlog)

add_executable(sample_stb sample_stb.cpp)
target_link_libraries(sample_stb)

file(GLOB DATA_FILES ${OpenCV_DLLS})

if(NOT ("${DATA_FILES}" STREQUAL ""))
    add_custom_command(TARGET sample_opencv POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different ${DATA_FILES} ${PROJECT_BINARY_DIR}
    )
endif()

