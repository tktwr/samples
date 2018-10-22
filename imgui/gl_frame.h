#ifndef gl_frame_h
#define gl_frame_h

#include "gl_app.h"

class GLTexture2D {
public:
    GLTexture2D() {
        m_w = 0;
        m_h = 0;
        m_id = 0;
    }
    ~GLTexture2D() {
        release();
    }
    int w() const { return m_w; }
    int h() const { return m_h; }
    GLuint id() const { return m_id; }
    void setImage(const tt::Image4uc& image);
    void setImage(GLsizei width, GLsizei height, const GLvoid* data);
    void release();
    void bind();

private:
    int m_w, m_h;
    GLuint m_id;
};

class GLFrame {
public:
    GLFrame() {}

    void init();
    void draw(float& scale, bool fit);

    void setWindowSize(int w, int h) { m_ww = w; m_wh = h; }
    int w() const { return m_w; }
    int h() const { return m_h; }
    GLuint getTexId() const { return m_tex.id(); }
    void setImage(const tt::Image4uc& image);

private:
    GLuint m_programId;
    GLuint m_vao;
    GLuint m_vbo_pos;
    GLuint m_vbo_color;
    GLuint m_vbo_uv;
    GLuint m_ebo;
    GLTexture2D m_tex;

    int m_ww, m_wh;
    int m_w, m_h;
};

#endif  // gl_frame_h

