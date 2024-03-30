cmake_minimum_required(VERSION 2.8)

project(gl_prog)
include_directories(${PROJECT_SOURCE_DIR}/common)
include_directories(${PROJECT_SOURCE_DIR}/3rdparty/glew)
link_directories(${PROJECT_BINARY_DIR}/tt)

add_definitions(-DCMAKE_BUILD_TYPE=Release -DFREEGLUT_STATIC)

set(CMAKE_EXE_LINKER_FLAGS "-static -Wl,--subsystem,windows")
#set(CMAKE_INSTALL_PREFIX /usr/local/gl_prog)

if(WIN32)
  set(SDK_DIR C:/SDK)
  include_directories(${SDK_DIR}/include)
  link_directories(${SDK_DIR}/lib.x64)
endif(WIN32)

if(WIN32)
  #set(OPENGL_LIBS glut32 glu32 opengl32)
  #set(OPENGL_LIBS freeglut glu32 opengl32)
  set(OPENGL_LIBS freeglut_static glu32 opengl32 winmm gdi32)
else(WIN32)
  set(OPENGL_LIBS glut GLU GL)
endif(WIN32)

add_executable(gl2d gl2d/main.cxx)
target_link_libraries(gl2d ${OPENGL_LIBS})
install(TARGETS gl2d RUNTIME DESTINATION bin)

add_executable(gl3d gl3d/main.cxx)
target_link_libraries(gl3d ${OPENGL_LIBS})
install(TARGETS gl3d RUNTIME DESTINATION bin)

add_subdirectory(glsl)

include (InstallRequiredSystemLibraries)
#set (CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
#set (CPACK_PACKAGE_VERSION_MAJOR "${Tutorial_VERSION_MAJOR}")
#set (CPACK_PACKAGE_VERSION_MINOR "${Tutorial_VERSION_MINOR}")
include (CPack)

