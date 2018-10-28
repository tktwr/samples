#ifndef gl_frame_h
#define gl_frame_h

#include "gl_app.h"

//////////////////////////////////////////////////

class GLTexture2D {
public:
    GLTexture2D() {}
    ~GLTexture2D() { release(); }

    int w() const { return m_w; }
    int h() const { return m_h; }
    GLuint id() const { return m_id; }
    void setImage(const tt::Image4uc& image);
    void setImage(GLsizei width, GLsizei height, const GLvoid* data);
    void release();
    void bind();

private:
    int m_w = 0;
    int m_h = 0;
    GLuint m_id = 0;
};

//////////////////////////////////////////////////

class GLFBO {
public:
	GLFBO() {}

	void open(int w, int h);
	void close();

	void bind();
	void unbind();

    GLuint getColorTexId() const { return m_tex_color0; }
    GLuint getDepthTexId() const { return m_tex_depth; }

	static void check();

private:
	int m_viewport[4] = {0, 0, 0, 0};
	int m_w = 0;
	int m_h = 0;
	GLuint m_id = 0;
	GLuint m_tex_color0 = 0;
	GLuint m_tex_depth = 0;
};

//////////////////////////////////////////////////

class GLFrame {
public:
    GLFrame() {}

    void init();
    void draw(float& scale, bool fit);

    GLuint getTexId() const { return m_tex.id(); }
    GLuint getColorTexId() const { return m_fbo.getColorTexId(); }
    GLuint getDepthTexId() const { return m_fbo.getDepthTexId(); }

    void setScreenSize(int w, int h);
    const tt::Vec2i& getScreenSize() const { return m_screen_size; }

    void setImage(const tt::Image4uc& image);
    const tt::Vec2i& getImageSize() const { return m_image_size; }

private:
    GLuint m_prog_id;
    GLuint m_vao;
    GLuint m_vbo_pos;
    GLuint m_vbo_color;
    GLuint m_vbo_uv;
    GLuint m_ebo;
    GLTexture2D m_tex;
    GLFBO m_fbo;

    tt::Color4f m_clear_color = {0.2f, 0.2f, 0.2f, 1.f};
    tt::Vec2i m_screen_size = {0, 0};
    tt::Vec2i m_image_size  = {0, 0};
};

#endif  // gl_frame_h

