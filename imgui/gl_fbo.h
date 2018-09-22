#ifndef gl_fbo_h
#define gl_fbo_h

#include "gl_app.h"

class GLFBO {
public:
	GLFBO(int w, int h) {
		m_w = w;
		m_h = h;
		m_id = 0;
		m_tex_color0 = 0;
		m_tex_depth = 0;
	}

	void push();
	void pop();
	void open();
	void close();
	void bind();
	void unbind();

	static void check();

private:
	int m_viewport[4];
	int m_w;
	int m_h;
	unsigned int m_id;
	unsigned int m_tex_color0;
	unsigned int m_tex_depth;
};

#endif  // gl_fbo_h

