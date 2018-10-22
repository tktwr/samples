#ifndef gl_app_h
#define gl_app_h

#include <GL/gl3w.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <imgui.h>
#include <imgui_impl_glfw.h>
#include <imgui_impl_opengl3.h>
#include <util/image.h>
#include "image_util.h"
#include <string>
#include <vector>
#include <array>

class GLApp {
public:
    GLApp();
    virtual ~GLApp();

    void setWindowTitle(const std::string& s) { m_window_title = s; }
    void setWindowSize(int w, int h) { m_w = w; m_h = h; }
    void setIcon(const std::string& fname);

    void glClearColor(const float v[4]) {
        ::glClearColor(v[0], v[1], v[2], v[3]);
    }

    virtual void exec(const std::string& line) {}

    void run();

    virtual void gui() {}
    virtual void draw() {}

    virtual void init();
    virtual void mainLoop();
    virtual void shutdown();

    int w() const { return m_w; }
    int h() const { return m_h; }

    struct Command {
        std::string name;
        std::string args;
        std::string desc;
    };

protected:
    std::string m_window_title;
    GLFWwindow* m_window;
    int m_w, m_h;
    std::vector<Command> m_commands;
};

std::string f_open_file();
std::string f_save_file();

#endif  // gl_app_h

