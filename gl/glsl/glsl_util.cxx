#include "glsl_util.h"
#include <iostream>
#include <fstream>
#include <string>

GLuint f_compile_shader_source(GLuint program, GLenum type, const char* fname) {
	GLuint shader = glCreateShader(type);
	GLint compiled;

	std::ifstream ifile(fname);
	std::istreambuf_iterator<char> ifile_begin(ifile);
	std::istreambuf_iterator<char> ifile_end;
	std::string source(ifile_begin, ifile_end);
	const char* source_c_str = source.c_str();

	glShaderSource(shader, 1, &source_c_str, NULL);
	glCompileShader(shader);
	glGetShaderiv(shader, GL_COMPILE_STATUS, &compiled);
	if (!compiled) {
		std::cerr << "[GLSL] compile error" << std::endl;
	}
	glAttachShader(program, shader);

    return shader;
}

GLSLProgram::GLSLProgram() {
	m_program = 0;
	m_vert_shader = 0;
	m_frag_shader = 0;
}

GLSLProgram::~GLSLProgram() {
	glDeleteShader(m_vert_shader);
	glDeleteShader(m_frag_shader);
	glDeleteProgram(m_program);
}

void GLSLProgram::createProgram() {
	m_program = glCreateProgram();
}

void GLSLProgram::compileVertexShader(const char* fname) {
	m_vert_shader = f_compile_shader_source(m_program, GL_VERTEX_SHADER, fname);
}

void GLSLProgram::compileFragmentShader(const char* fname) {
	m_frag_shader = f_compile_shader_source(m_program, GL_FRAGMENT_SHADER, fname);
}

void GLSLProgram::linkProgram() {
	GLint linked;
	glLinkProgram(m_program);
	glGetProgramiv(m_program, GL_LINK_STATUS, &linked);
	if(!linked) {
		std::cerr << "[GLSL] link error" << std::endl;
	}
}

void GLSLProgram::useProgram() {
	glUseProgram(m_program);
}

void GLSLProgram::unuseProgram() {
	glUseProgram(0);
}

void GLSLProgram::setUniform3fv(const char* name, int count, float* values) {
	GLint loc = glGetUniformLocation(m_program, name);
	if (loc == -1)
		std::cerr << "[GLSL] unknown uniform variable: " << name << std::endl;
	else
		glUniform3fv(loc, count, values);
}

