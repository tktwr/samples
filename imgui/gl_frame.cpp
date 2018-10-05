#include "gl_frame.h"
#include <glm/gtc/matrix_transform.hpp>

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
    //f_color = vec4(v_color.rgb, 1.0);
    f_color = texture2D(tex, v_uv);
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

void GLFrame::setTexture(const tt::Image4uc& image) {
    m_w = image.w();
    m_h = image.h();

	if (m_texid) glDeleteTextures(1, &m_texid);

    m_texid = f_create_texture(image);
}

void GLFrame::init() {
    m_programId = createShader(g_vshader.c_str(), g_fshader.c_str());

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

    GLint loc_tex = glGetUniformLocation(m_programId, "tex");
    glUniform1i(loc_tex, 0);

    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);
}

void GLFrame::draw(float& scale, bool fit) {
    glUseProgram(m_programId);

    float sw = float(m_ww) / m_w;
    float sh = float(m_wh) / m_h;
    if (fit) {
        scale = sh;
    }
    glm::vec2 ssize = glm::vec2(m_w, m_h) * scale;
    glm::vec2 o = glm::vec2(m_ww, m_wh) * 0.5f - ssize * 0.5f;

    glm::mat4 mat = glm::ortho<float>(0, m_ww, 0, m_wh);
    mat = glm::translate(mat, glm::vec3(o, 0));
    mat = glm::scale(mat, glm::vec3(ssize, 1));
    mat = glm::translate(mat, glm::vec3(0, 1, 0));
    mat = glm::scale(mat, glm::vec3(1, -1, 1));

    GLint loc_xform = glGetUniformLocation(m_programId, "transform");
    glUniformMatrix4fv(loc_xform, 1, GL_FALSE, &(mat[0][0]));

    glBindVertexArray(m_vao);
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
    glBindVertexArray(0);

    glUseProgram(0);
}

