set(COPY_FILES
  vert.glsl
  frag.glsl
)

add_custom_target(copy_files_2 ALL)

foreach(FILENAME ${COPY_FILES})
  set(SRC "${CMAKE_CURRENT_SOURCE_DIR}/${FILENAME}")
  set(DST "${CMAKE_CURRENT_BINARY_DIR}/${FILENAME}")

  add_custom_command(
    TARGET copy_files_2
    COMMAND ${CMAKE_COMMAND} -E copy_if_different ${SRC} ${DST}
  )
endforeach(FILENAME)

add_executable(glsl main.cxx glsl_util.cxx ../3rdparty/glew/glew.c)
target_link_libraries(glsl ${OPENGL_LIBS})
install(TARGETS glsl RUNTIME DESTINATION bin)
install(FILES ${COPY_FILES} DESTINATION bin)

