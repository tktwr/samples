#include "gl_frame.h"
#include <glm/gtc/matrix_transform.hpp>
#include <iostream>

#define USE_DEPTH_TEXTURE 1

const std::string g_vshader = R"#(
#version 410
layout(location = 0) in vec3 position;
layout(location = 1) in vec4 color;
layout(location = 2) in vec2 uv;
out vec4 v_color;
out vec2 v_uv;
uniform mat4 transform;

void main() {
    v_color = color;
    v_uv = uv;
    gl_Position = transform * vec4(position, 1.0);
}
)#";

const std::string g_fshader = R"#(
#version 410
in vec4 v_color;
in vec2 v_uv;
out vec4 f_color;
uniform sampler2D tex;

void main() {
    f_color = vec4(v_color.rgb, 1.0);
    //f_color = texture2D(tex, v_uv);
}
)#";

GLuint createShader(const char* vs, const char* fs) {
    GLuint vs_id = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vs_id, 1, &vs, NULL);
    glCompileShader(vs_id);

    GLuint fs_id = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fs_id, 1, &fs, NULL);
    glCompileShader(fs_id);

    GLuint prg_id = glCreateProgram();
    glAttachShader(prg_id, vs_id);
    glAttachShader(prg_id, fs_id);

    glLinkProgram(prg_id);

    return prg_id;
}

//////////////////////////////////////////////////

void GLTexture2D::setImage(const tt::Image4uc& image) {
    int w = image.w();
    int h = image.h();
    const uchar* data = reinterpret_cast<const uchar*>(image.data());
    setImage(w, h, data);
}

void GLTexture2D::setImage(GLsizei width, GLsizei height, const GLvoid* data) {
    release();
    glGenTextures(1, &m_id);
    glBindTexture(GL_TEXTURE_2D, m_id);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data);
}

void GLTexture2D::release() {
    if (m_id) {
        glDeleteTextures(1, &m_id);
        m_id = 0;
    }
}

void GLTexture2D::bind() {
    glBindTexture(GL_TEXTURE_2D, m_id);
}

//////////////////////////////////////////////////

void GLFBO::open(int w, int h) {
    m_w = w;
    m_h = h;

	glGenFramebuffers(1, &m_id);
	glBindFramebuffer(GL_FRAMEBUFFER, m_id);

	// create color0 texture
	glGenTextures(1, &m_tex_color0);
	glBindTexture(GL_TEXTURE_2D, m_tex_color0);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, m_w, m_h, 0, GL_RGBA, GL_UNSIGNED_BYTE, 0);

	// create depth texture
#if USE_DEPTH_TEXTURE
	glGenTextures(1, &m_tex_depth);
	glBindTexture(GL_TEXTURE_2D, m_tex_depth);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
	glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT, m_w, m_h, 0, GL_DEPTH_COMPONENT, GL_UNSIGNED_INT, 0);
#else
	glGenRenderbuffers(1, &m_tex_depth);
	glBindRenderbuffer(GL_RENDERBUFFER, m_tex_depth);
	glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT, m_w, m_h);
#endif

	// attach textures to a framebuffer object
	glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, m_tex_color0, 0);
#if USE_DEPTH_TEXTURE
	glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, m_tex_depth, 0);
#else
	glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, m_tex_depth);
#endif

	// default framebuffer
	glBindFramebuffer(GL_FRAMEBUFFER, 0);

    std::cout << "fbo:m_id: " << m_id << std::endl;
    std::cout << "fbo:m_tex_color0: " << m_tex_color0 << std::endl;
    std::cout << "fbo:m_tex_depth: " << m_tex_depth << std::endl;
}

void GLFBO::close() {
    if (m_id == 0) return;

	glBindFramebuffer(GL_FRAMEBUFFER, m_id);

	// detach textures
	glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, 0, 0);
#if USE_DEPTH_TEXTURE
	glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, 0, 0);
#else
	glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, 0);
#endif
	glDeleteTextures(1, &m_tex_color0);
	glDeleteTextures(1, &m_tex_depth);
	glDeleteFramebuffers(1, &m_id);

	glBindFramebuffer(GL_FRAMEBUFFER, 0);
}

void GLFBO::bind() {
	glGetIntegerv(GL_VIEWPORT, m_viewport);
	glBindFramebuffer(GL_FRAMEBUFFER, m_id);
}

void GLFBO::unbind() {
	glBindFramebuffer(GL_FRAMEBUFFER, 0);
	glViewport(m_viewport[0], m_viewport[1], m_viewport[2], m_viewport[3]);
}

void GLFBO::check() {
	switch (glCheckFramebufferStatus(GL_FRAMEBUFFER)) {
		case GL_FRAMEBUFFER_COMPLETE:
            std::cout << "fbo: good" << std::endl;
			break;
		case GL_FRAMEBUFFER_UNSUPPORTED:
            std::cout << "fbo: unsupported" << std::endl;
			break;
		default:
            std::cout << "fbo: bad" << std::endl;
			break;
	}
}

//////////////////////////////////////////////////

void GLFrame::setScreenSize(int w, int h) {
    if (m_screen_size != tt::Vec2i{w, h}) {
        m_screen_size[0] = w;
        m_screen_size[1] = h;
        m_fbo.close();
        m_fbo.open(w, h);
    }
}

void GLFrame::setImage(const tt::Image4uc& image) {
    m_image_size[0] = image.w();
    m_image_size[1] = image.h();
    m_tex.setImage(image);
}

void GLFrame::init() {
    m_prog_id = createShader(g_vshader.c_str(), g_fshader.c_str());

    GLfloat vertices[] = {
        0, 0, 0,
        1, 0, 0,
        1, 1, 0,
        0, 1, 0
    };
    GLfloat colors[] = {
        1, 0, 0, 1,
        0, 1, 0, 1,
        0, 0, 1, 1,
        1, 1, 1, 1
    };
    GLfloat uv[] = {
        0, 0,
        1, 0,
        1, 1,
        0, 1
    };
    int indices[] = {0, 1, 2, 0, 2, 3};

    glGenVertexArrays(1, &m_vao);
    glGenBuffers(1, &m_vbo_pos);
    glGenBuffers(1, &m_vbo_color);
    glGenBuffers(1, &m_vbo_uv);
    glGenBuffers(1, &m_ebo);

    glBindVertexArray(m_vao);

    // Position attribute
    glBindBuffer(GL_ARRAY_BUFFER, m_vbo_pos);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    GLint loc_pos = 0;
    glEnableVertexAttribArray(loc_pos);
    glVertexAttribPointer(loc_pos, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid*)0);

    // Color attribute
    glBindBuffer(GL_ARRAY_BUFFER, m_vbo_color);
    glBufferData(GL_ARRAY_BUFFER, sizeof(colors), colors, GL_STATIC_DRAW);
    GLint loc_color = 1;
    glEnableVertexAttribArray(loc_color);
    glVertexAttribPointer(loc_color, 4, GL_FLOAT, GL_FALSE, 4 * sizeof(GLfloat), (GLvoid*)0);

    // UV attribute
    glBindBuffer(GL_ARRAY_BUFFER, m_vbo_uv);
    glBufferData(GL_ARRAY_BUFFER, sizeof(uv), uv, GL_STATIC_DRAW);
    GLint loc_uv = 2;
    glEnableVertexAttribArray(loc_uv);
    glVertexAttribPointer(loc_uv, 2, GL_FLOAT, GL_FALSE, 2 * sizeof(GLfloat), (GLvoid*)0);

    // Element Array Buffer
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_ebo);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

    GLint loc_tex = glGetUniformLocation(m_prog_id, "tex");
    glUniform1i(loc_tex, 0);

    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);
}

void GLFrame::draw(float& scale, bool fit) {
    m_fbo.bind();

    glViewport(0, 0, m_screen_size[0], m_screen_size[1]);
    glClearColor_tt(m_clear_color.data());
    glClear(GL_COLOR_BUFFER_BIT);

    glUseProgram(m_prog_id);

    glm::vec2 src_win(m_image_size[0], m_image_size[1]);
    glm::vec2 dst_win(m_screen_size[0], m_screen_size[1]);
    if (fit) {
        glm::vec2 scale_win = dst_win / src_win;
        scale = std::min(std::abs(scale_win[0]), std::abs(scale_win[1]));
    }
    glm::vec2 ssize = src_win * scale;
    glm::vec2 o = dst_win * 0.5f - ssize * 0.5f;

    glm::mat4 mat = glm::ortho<float>(0, m_screen_size[0], 0, m_screen_size[1]);
    mat = glm::translate(mat, glm::vec3(o, 0));
    mat = glm::scale(mat, glm::vec3(ssize, 1));
    mat = glm::translate(mat, glm::vec3(0, 1, 0));
    mat = glm::scale(mat, glm::vec3(1, -1, 1));

    GLint loc_xform = glGetUniformLocation(m_prog_id, "transform");
    glUniformMatrix4fv(loc_xform, 1, GL_FALSE, &(mat[0][0]));

    glBindVertexArray(m_vao);
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
    glBindVertexArray(0);

    glUseProgram(0);

    m_fbo.unbind();
}

