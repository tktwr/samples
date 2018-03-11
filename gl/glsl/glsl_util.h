#ifndef glsl_util_h
#define glsl_util_h

#include "myglut.h"

class GLSLProgram
{
public:
	GLSLProgram();
	virtual ~GLSLProgram();

	void createProgram();
	void compileVertexShader(const char* fname);
	void compileFragmentShader(const char* fname);
	void linkProgram();
	void useProgram();
	void unuseProgram();

	void setUniform3fv(const char* name, int count, float* values);

private:
	GLuint m_program;
	GLuint m_vert_shader;
	GLuint m_frag_shader;
};

#endif  // glsl_util_h

