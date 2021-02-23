cmake_minimum_required(VERSION 3.6)

project(app)

add_executable(app main.cpp)

if(MSVC)
add_custom_command(TARGET ${PROJECT_NAME} PRE_BUILD
    COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/tools/make_ver.bat > ${CMAKE_CURRENT_SOURCE_DIR}/version.h
)
else()
add_custom_target(version.h ALL
    COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/tools/make_ver.bat > ${CMAKE_CURRENT_SOURCE_DIR}/version.h
)
endif()

file(GLOB DATA_FILES ${CMAKE_CURRENT_SOURCE_DIR}/data/icon.png)
add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different ${DATA_FILES} $<TARGET_FILE_DIR:${PROJECT_NAME}>
)

configure_file(${DATA_FILES} ${PROJECT_BINARY_DIR}/icon2.png)

message("PROJECT_NAME=${PROJECT_NAME}")
message("PROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}")
message("PROJECT_BINARY_DIR=${PROJECT_BINARY_DIR}")
message("CMAKE_SOURCE_DIR=${CMAKE_SOURCE_DIR}")
message("CMAKE_CURRENT_SOURCE_DIR=${CMAKE_CURRENT_SOURCE_DIR}")
message("CMAKE_CURRENT_LIST_DIR=${CMAKE_CURRENT_LIST_DIR}")
message("CMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}")
message("CMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}")
message("CMAKE_CXX_COMPILER_ID=${CMAKE_CXX_COMPILER_ID}")
message("HOME=$ENV{HOME}")
message("USERPROFILE=$ENV{USERPROFILE}")

set(Python_ROOT_DIR "~/.python-venv/torch")
find_package(Python COMPONENTS Interpreter Development)
message(STATUS "Python_EXECUTABLE=${Python_EXECUTABLE}")

