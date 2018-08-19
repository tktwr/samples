#include "gl_app.h"
#include "gl_frame.h"
#include <string>
#include <GL/gl.h>
#include <opencv2/opencv.hpp>
#include <util/array_util.h>
#include "image_util.h"
#include "imgui_console.h"

class MyGLApp : public GLApp {
public:
    MyGLApp() : GLApp() {
        m_show_main_menu_bar = true;
        m_show_control_panel = true;
        m_show_console_panel = true;
        m_color0 = {1.f, 1.f, 1.f, 1.f};
        m_color1 = {0.f, 0.f, 0.f, 1.f};
        m_clear_color = {0.5f, 0.5f, 0.5f, 1.f};
        m_scale = 1.f;
        m_fit = true;

        m_commands = {
            {"set_color0", "r g b a",     "set color0"},
            {"set_color1", "r g b a",     "set color1"},
            {"image",     "w h",     "create an image"},
            {"rect",      "ox oy sx sy",  "fill a rectangle"},
            {"vstripe",   "n",       "create a vertical stripe image"},
            {"hstripe",   "n",       "create a horizontal stripe image"},
            {"checker",   "nx ny",   "create a checker image"},
            {"blur",      "kx ky",   "blur an image"},
            {"bilateral", "",        "bilateral filter an image"},
            {"erode",     "i",       "erode an image"},
            {"dilate",    "i",       "dilate an image"},
            {"detect_face", "",      "detect faces"},
            {"load",      "",        "load an image"},
            {"save",      "",        "save an image"},
            {"scale",     "f",       "set scale"},
            {"fit",       "",        "set fit"},
            {"help",      "",        "print help"},
            {"clear",     "",        "clear console"},
            {"quit",      "",        "exit the program"},
        };
        int sz = m_commands.size();
        for (int i=0; i<sz; i++) {
            Command& cmd = m_commands[i];
            m_console.addCommand(cmd.name);
        }
        m_console.setFunc([&](const std::string& line) {
            exec(line);
        });
    }
    void cmd_help() {
        int sz = m_commands.size();
        for (int i=0; i<sz; i++) {
            Command& cmd = m_commands[i];
            m_console.output("%s %s ... %s", cmd.name.c_str(), cmd.args.c_str(), cmd.desc.c_str());
        }
    }
    void cmd_clear() {
        m_console.clear();
    }

    void cmd_image(const std::array<int, 2>& size) {
        tt::RGBA8 rgba(m_color0.data());
        m_image.alloc(size[0], size[1]);
        m_image.fill(rgba);
    }
    void cmd_rect(const std::array<int, 2>& o, const std::array<int, 2>& size) {
        f_fill_rect(m_image, o, size, tt::RGBA8(m_color0.data()));
    }
    void cmd_vstripe(int nw) {
        f_create_vstripe_image(m_image, nw, tt::RGBA8(m_color0.data()), tt::RGBA8(m_color1.data()));
    }
    void cmd_hstripe(int nh) {
        f_create_hstripe_image(m_image, nh, tt::RGBA8(m_color0.data()), tt::RGBA8(m_color1.data()));
    }
    void cmd_checker(const std::array<int, 2>& n) {
        f_create_checker_image(m_image, n[0], n[1], tt::RGBA8(m_color0.data()), tt::RGBA8(m_color1.data()));
    }
    void cmd_blur(const std::array<int, 2>& ksize) {
        cv::Mat src, dst;
        f_image_to_cvmat(m_image, src);
        cv::boxFilter(src, dst, -1, cv::Size(ksize[0], ksize[1]));
        f_cvmat_to_image(dst, m_image);
    }
    void cmd_bilateral() {
        cv::Mat src, dst;
        f_image_to_cvmat(m_image, src);
        cv::bilateralFilter(src, dst, -1, 50, 5);
        f_cvmat_to_image(dst, m_image);
    }
    void cmd_erode(int iterations) {
        cv::Mat src, dst;
        f_image_to_cvmat(m_image, src);
        cv::erode(src, dst, cv::Mat(), cv::Point(-1,-1), iterations);
        f_cvmat_to_image(dst, m_image);
    }
    void cmd_dilate(int iterations) {
        cv::Mat src, dst;
        f_image_to_cvmat(m_image, src);
        cv::dilate(src, dst, cv::Mat(), cv::Point(-1,-1), iterations);
        f_cvmat_to_image(dst, m_image);
    }
    void cmd_detect_face() {
        cv::CascadeClassifier cascade;
        //cascade.load("haarcascade_frontalface_default.xml");
        cascade.load("lbpcascade_animeface.xml");

        cv::Mat mat;
        f_image_to_cvmat(m_image, mat);
        std::vector<cv::Rect> faces;
        cascade.detectMultiScale(mat, faces, 1.1, 3, 0, cv::Size(20, 20));
        for (int i = 0; i < faces.size(); i++){
            cv::Point o(faces[i].x, faces[i].y);
            cv::Point size(faces[i].width, faces[i].height);
            cv::Scalar color(m_color0[0] * 255.f, m_color0[1] * 255.f, m_color0[2] * 255.f);
            cv::rectangle(mat, o, o+size, color);
        }
        f_cvmat_to_image(mat, m_image);
    }
    void exec(const std::string& line) {
        std::istringstream istr(line);
        std::string token;
        istr >> token;

        if (token == "help") {
            cmd_help();
        } else if (token == "clear") {
            cmd_clear();
        } else if (token == "set_color0") {
            istr >> m_color0;
        } else if (token == "set_color1") {
            istr >> m_color1;
        } else if (token == "scale") {
            istr >> m_scale;
            m_fit = false;
        } else if (token == "fit") {
            m_fit = true;
        } else if (token == "image") {
            std::array<int, 2> size = {256, 256};
            istr >> size;
            cmd_image(size);
            gl_frame.setTexture(m_image);
        } else if (token == "rect") {
            std::array<int, 2> o = {0, 0};
            std::array<int, 2> size = {128, 128};
            istr >> o >> size;
            cmd_rect(o, size);
            gl_frame.setTexture(m_image);
        } else if (token == "vstripe") {
            int n = 8;
            istr >> n;
            cmd_vstripe(n);
            gl_frame.setTexture(m_image);
        } else if (token == "hstripe") {
            int n = 8;
            istr >> n;
            cmd_hstripe(n);
            gl_frame.setTexture(m_image);
        } else if (token == "checker") {
            std::array<int, 2> n = {8, 8};
            istr >> n;
            cmd_checker(n);
            gl_frame.setTexture(m_image);
        } else if (token == "blur") {
            std::array<int, 2> ksize = {10, 10};
            istr >> ksize;
            cmd_blur(ksize);
            gl_frame.setTexture(m_image);
        } else if (token == "bilateral") {
            cmd_bilateral();
            gl_frame.setTexture(m_image);
        } else if (token == "erode") {
            int iterations = 1;
            istr >> iterations;
            cmd_erode(iterations);
            gl_frame.setTexture(m_image);
        } else if (token == "dilate") {
            int iterations = 1;
            istr >> iterations;
            cmd_dilate(iterations);
            gl_frame.setTexture(m_image);
        } else if (token == "detect_face") {
            cmd_detect_face();
            gl_frame.setTexture(m_image);
        } else if (token == "load") {
            std::string fname;
            istr >> fname;
            f_load_image(fname, m_image);
            gl_frame.setTexture(m_image);
        } else if (token == "save") {
            std::string fname;
            istr >> fname;
            f_save_image(fname, m_image);
        } else if (token == "quit") {
            glfwSetWindowShouldClose(m_window, 1);
        } else {
            if (line.size()) {
                m_console.shell(line);
            }
        }
    }

    void guiMainMenuBar() {
        if (ImGui::BeginMainMenuBar()) {
            if (ImGui::BeginMenu("File")) {
                if (ImGui::MenuItem("Open...")) {
                    std::string fname = f_open_file();
                    if (fname != "") {
                        f_load_image(fname, m_image);
                        gl_frame.setTexture(m_image);
                    }
                }
                if (ImGui::MenuItem("Save As...")) {
                    std::string fname = f_save_file();
                    if (fname != "") {
                        f_save_image(fname, m_image);
                    }
                }
                ImGui::Separator();
                if (ImGui::MenuItem("Quit", "CTRL+Q")) {
                    glfwSetWindowShouldClose(m_window, 1);
                }
                ImGui::EndMenu();
            }
            if (ImGui::BeginMenu("View")) {
                ImGui::MenuItem("Main Menu Bar", "CTRL+M", &m_show_main_menu_bar);
                ImGui::MenuItem("Console", NULL, &m_show_console_panel);
                ImGui::EndMenu();
            }
            if (ImGui::BeginMenu("Help")) {
                ImGui::EndMenu();
            }
            ImGui::EndMainMenuBar();
        }
    }
    void guiControlPanel() {
        ImGuiStyle& style = ImGui::GetStyle();

        ImGui::Begin("Control Panel", &m_show_control_panel);
        if (ImGui::Button("Main Menu Bar Button")) {
            m_show_main_menu_bar = !m_show_main_menu_bar;
        }
        if (ImGui::Button("Console Button")) {
            m_show_console_panel = !m_show_console_panel;
        }
        ImGui::LabelText("window size", "%d, %d", w(), h());
        ImGui::LabelText("image size", "%d, %d", m_image.w(), m_image.h());
        ImGui::ColorEdit4("color0", m_color0.data());
        ImGui::ColorEdit4("color1", m_color1.data());
        ImGui::SliderFloat("global alpha", &style.Alpha, 0.20f, 1.0f, "%.2f");
        ImGui::ColorEdit4("clear color", m_clear_color.data());
        ImGui::DragFloat("scale", &m_scale, 0.01f);
        ImGui::Checkbox("fit", &m_fit);
        ImGui::End();
    }
    void guiConsolePanel() {
        ImGui::Begin("Console", &m_show_console_panel);
        m_console.draw();
        ImGui::End();
    }

    void init() {
        GLApp::init();
        setIcon("icon.png");
        exec("image");
        exec("checker");
        gl_frame.init();
    }
    void gui() {
        if (m_show_main_menu_bar) guiMainMenuBar();
        if (m_show_control_panel) guiControlPanel();
        if (m_show_console_panel) guiConsolePanel();
    }
    void draw() {
        glViewport(0, 0, m_w, m_h);
        glClearColor(m_clear_color.data());
        glClear(GL_COLOR_BUFFER_BIT);

        gl_frame.setWindowSize(m_w, m_h);
        gl_frame.draw(m_scale, m_fit);
    }

private:
    bool m_show_main_menu_bar;
    bool m_show_control_panel;
    bool m_show_console_panel;

    Console m_console;
    GLFrame gl_frame;
    std::array<float, 4> m_clear_color;
    float m_scale;
    bool m_fit;

    tt::Image<tt::RGBA8> m_image;
    std::array<float, 4> m_color0;
    std::array<float, 4> m_color1;
};

int main(int, char**)
{
    MyGLApp app;
    app.setWindowTitle("MyGLApp");
    app.setWindowSize(800, 600);
    app.run();

    return 0;
}

