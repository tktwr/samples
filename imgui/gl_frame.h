#ifndef gl_frame_h
#define gl_frame_h

#include "gl_app.h"

class GLFrame {
public:
    GLFrame() {
        m_texid = 0;
    }

    void init();
    void draw(float& scale, bool fit);

    void setWindowSize(int w, int h) { m_ww = w; m_wh = h; }
    void setTexture(const tt::Image<tt::RGBA8>& image);

private:
    GLuint m_programId;
    GLuint m_vao;
    GLuint m_vbo_pos;
    GLuint m_vbo_color;
    GLuint m_vbo_uv;
    GLuint m_ebo;
    GLuint m_texid;

    int m_ww, m_wh;
    int m_w, m_h;
};

#endif  // gl_frame_h

