#include "myglapp.h"
#include <opencv2/opencv.hpp>
#include <util/filename.h>
#include "image_util.h"

const std::string DATA = "../data/";

MyGLApp::MyGLApp() : GLApp() {
    m_show_main_menu_bar = true;
    m_show_control_panel = true;
    m_show_console_panel = true;
    m_show_screen_panel  = true;
    m_color0 = {1.f, 1.f, 1.f, 1.f};
    m_color1 = {0.f, 0.f, 0.f, 1.f};
    m_clear_color = {0.5f, 0.5f, 0.5f, 1.f};
    m_scale = 1.f;
    m_fit = true;
    //m_face_detector = DATA + "haarcascade_frontalface_default.xml";
    m_face_detector = DATA + "lbpcascade_animeface.xml";

    m_commands = {
        {"set_color0",        "color4f rgba",       "set color0"},
        {"set_color1",        "color4f rgba",       "set color1"},
        {"set_clear_color",   "color4f rgba",       "set clear color"},
        {"set_face_detector", "string file",        "set face detector"},
        {"image",             "vec2i wh",           "create an image"},
        {"get_value",         "vec2i xy",           "get a value"},
        {"set_value",         "vec2i xy",           "set a value"},
        {"rect",              "vec2i o vec2i size", "draw a rectangle"},
        {"rect_fill",         "vec2i o vec2i size", "fill a rectangle"},
        {"vstripe",           "int n",              "create a vertical stripe image"},
        {"hstripe",           "int n",              "create a horizontal stripe image"},
        {"checker",           "vec2i nxy",          "create a checker image"},
        {"hgrad",             "",                   "create a horizontal gradation image"},
        {"vgrad",             "",                   "create a vertical gradation image"},
        {"flip",              "",                   "flip an image"},
        {"flop",              "",                   "flop an image"},
        {"blur",              "vec2i ksize",        "blur an image"},
        {"bilateral",         "",                   "bilateral filter an image"},
        {"erode",             "int itr",            "erode an image"},
        {"dilate",            "int itr",            "dilate an image"},
        {"detect_face",       "",                   "detect faces"},
        {"load",              "",                   "load a file (config, image)"},
        {"save",              "",                   "save a file (config, image)"},
        {"scale",             "float f",            "set scale"},
        {"fit",               "",                   "set fit"},
        {"info",              "",                   "print info"},
        {"help",              "",                   "print help"},
        {"clear",             "",                   "clear console"},
        {"quit",              "",                   "exit the program"},
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

void MyGLApp::cmd_load_config(const std::string& fname) {
    std::ifstream ifs(fname);
    std::string line;
    while (getline(ifs, line)) {
        exec(line);
    }
}

void MyGLApp::cmd_save_config(const std::string& fname) {
    std::ofstream ofs(fname);

    ofs << "set_color0 " << m_color0 << std::endl;
    ofs << "set_color1 " << m_color1 << std::endl;
    ofs << "set_clear_color " << m_clear_color << std::endl;
    ofs << "set_face_detector " << m_face_detector << std::endl;
}

void MyGLApp::cmd_info() {
    m_console.output("m_face_detector %s", m_face_detector.c_str());
}

void MyGLApp::cmd_help() {
    int sz = m_commands.size();
    for (int i=0; i<sz; i++) {
        Command& cmd = m_commands[i];
        m_console.output("%s %s ... %s", cmd.name.c_str(), cmd.args.c_str(), cmd.desc.c_str());
    }
}

void MyGLApp::cmd_clear() {
    m_console.clear();
}

void MyGLApp::cmd_image(const tt::Vec2i& size) {
    m_image.alloc(size[0], size[1]);
    m_image.fill(tt::toColor4uc(m_color0));
}

void MyGLApp::cmd_get_value(int x, int y) {
    tt::Color4uc rgba = m_image.getValue(x, y);
    m_console.output("%d %d %d %d", rgba[0], rgba[1], rgba[2], rgba[3]);
}

void MyGLApp::cmd_set_value(int x, int y) {
    m_image.setValue(x, y, tt::toColor4uc(m_color0));
}

void MyGLApp::cmd_rect(const tt::Vec2i& _o, const tt::Vec2i& _size) {
    cv::Mat mat;
    f_image_to_cvmat(m_image, mat);
    cv::Point o(_o[0], _o[1]);
    cv::Point size(_size[0], _size[1]);
    cv::Scalar color(m_color0[0] * 255.f, m_color0[1] * 255.f, m_color0[2] * 255.f);
    cv::rectangle(mat, o, o+size, color);
    f_cvmat_to_image(mat, m_image);
}

void MyGLApp::cmd_rect_fill(const tt::Vec2i& o, const tt::Vec2i& size) {
    f_fill_rect(m_image, o, size, tt::toColor4uc(m_color0));
}

void MyGLApp::cmd_vstripe(int nw) {
    f_create_vstripe_image(m_image, nw, tt::toColor4uc(m_color0), tt::toColor4uc(m_color1));
}

void MyGLApp::cmd_hstripe(int nh) {
    f_create_hstripe_image(m_image, nh, tt::toColor4uc(m_color0), tt::toColor4uc(m_color1));
}

void MyGLApp::cmd_checker(const tt::Vec2i& n) {
    f_create_checker_image(m_image, n[0], n[1], tt::toColor4uc(m_color0), tt::toColor4uc(m_color1));
}

void MyGLApp::cmd_hgrad() {
    tt::f_image_hgrad(m_image, tt::toColor4uc(m_color0), tt::toColor4uc(m_color1));
}

void MyGLApp::cmd_vgrad() {
    tt::f_image_vgrad(m_image, tt::toColor4uc(m_color0), tt::toColor4uc(m_color1));
}

void MyGLApp::cmd_flip() {
    tt::f_image_flip(m_image);
}

void MyGLApp::cmd_flop() {
    tt::f_image_flop(m_image);
}

void MyGLApp::cmd_blur(const tt::Vec2i& ksize) {
    cv::Mat src, dst;
    f_image_to_cvmat(m_image, src);
    cv::boxFilter(src, dst, -1, cv::Size(ksize[0], ksize[1]));
    f_cvmat_to_image(dst, m_image);
}

void MyGLApp::cmd_bilateral() {
    cv::Mat src, dst;
    f_image_to_cvmat(m_image, src);
    cv::bilateralFilter(src, dst, -1, 50, 5);
    f_cvmat_to_image(dst, m_image);
}

void MyGLApp::cmd_erode(int iterations) {
    cv::Mat src, dst;
    f_image_to_cvmat(m_image, src);
    cv::erode(src, dst, cv::Mat(), cv::Point(-1,-1), iterations);
    f_cvmat_to_image(dst, m_image);
}

void MyGLApp::cmd_dilate(int iterations) {
    cv::Mat src, dst;
    f_image_to_cvmat(m_image, src);
    cv::dilate(src, dst, cv::Mat(), cv::Point(-1,-1), iterations);
    f_cvmat_to_image(dst, m_image);
}

void MyGLApp::cmd_detect_face() {
    cv::CascadeClassifier cascade;
    cascade.load(m_face_detector);

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

void MyGLApp::updateTexture() {
    m_glframe.setImage(m_image);
}

void MyGLApp::exec(const std::string& line) {
    std::istringstream istr(line);
    std::string token;
    istr >> token;

    if (token == "") return;
    if (token[0] == '#') return;
    if (token == "help") {
        cmd_help();
    } else if (token == "info") {
        cmd_info();
    } else if (token == "clear") {
        cmd_clear();
    } else if (token == "set_color0") {
        istr >> m_color0;
    } else if (token == "set_color1") {
        istr >> m_color1;
    } else if (token == "set_clear_color") {
        istr >> m_clear_color;
    } else if (token == "set_face_detector") {
        istr >> m_face_detector;
    } else if (token == "set_screen_size") {
        istr >> m_screen_size;
    } else if (token == "scale") {
        istr >> m_scale;
        m_fit = false;
    } else if (token == "fit") {
        m_fit = true;
    } else if (token == "image") {
        tt::Vec2i size = {256, 256};
        istr >> size;
        cmd_image(size);
        updateTexture();
    } else if (token == "get_value") {
        int x = 0;
        int y = 0;
        istr >> x >> y;
        cmd_get_value(x, y);
    } else if (token == "set_value") {
        int x = 0;
        int y = 0;
        istr >> x >> y;
        cmd_set_value(x, y);
        updateTexture();
    } else if (token == "rect") {
        tt::Vec2i o = {0, 0};
        tt::Vec2i size = {128, 128};
        istr >> o >> size;
        cmd_rect(o, size);
        updateTexture();
    } else if (token == "rect_fill") {
        tt::Vec2i o = {0, 0};
        tt::Vec2i size = {128, 128};
        istr >> o >> size;
        cmd_rect_fill(o, size);
        updateTexture();
    } else if (token == "vstripe") {
        int n = 8;
        istr >> n;
        cmd_vstripe(n);
        updateTexture();
    } else if (token == "hstripe") {
        int n = 8;
        istr >> n;
        cmd_hstripe(n);
        updateTexture();
    } else if (token == "checker") {
        tt::Vec2i n = {8, 8};
        istr >> n;
        cmd_checker(n);
        updateTexture();
    } else if (token == "hgrad") {
        cmd_hgrad();
        updateTexture();
    } else if (token == "vgrad") {
        cmd_vgrad();
        updateTexture();
    } else if (token == "flip") {
        cmd_flip();
        updateTexture();
    } else if (token == "flop") {
        cmd_flop();
        updateTexture();
    } else if (token == "blur") {
        tt::Vec2i ksize = {10, 10};
        istr >> ksize;
        cmd_blur(ksize);
        updateTexture();
    } else if (token == "bilateral") {
        cmd_bilateral();
        updateTexture();
    } else if (token == "erode") {
        int iterations = 1;
        istr >> iterations;
        cmd_erode(iterations);
        updateTexture();
    } else if (token == "dilate") {
        int iterations = 1;
        istr >> iterations;
        cmd_dilate(iterations);
        updateTexture();
    } else if (token == "detect_face") {
        cmd_detect_face();
        updateTexture();
    } else if (token == "load") {
        tt::FileName fname;
        istr >> fname;
        if (fname.ext() == ".cfg") {
            cmd_load_config(fname.str());
        } else {
            f_load_image(fname.str(), m_image);
        }
        updateTexture();
    } else if (token == "save") {
        tt::FileName fname;
        istr >> fname;
        if (fname.ext() == ".cfg") {
            cmd_save_config(fname.str());
        } else {
            f_save_image(fname.str(), m_image);
        }
    } else if (token == "crop") {
    } else if (token == "resize") {
    } else if (token == "quit") {
        glfwSetWindowShouldClose(m_window, 1);
    } else {
        if (line.size()) {
            m_console.shell(line);
        }
    }
}

void MyGLApp::guiMainMenuBar() {
    if (ImGui::BeginMainMenuBar()) {
        if (ImGui::BeginMenu("File")) {
            if (ImGui::MenuItem("Open...")) {
                std::string fname = f_open_file();
                if (fname != "") {
                    f_load_image(fname, m_image);
                    updateTexture();
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
            ImGui::MenuItem("Screen", NULL, &m_show_screen_panel);
            ImGui::MenuItem("Control", NULL, &m_show_control_panel);
            ImGui::MenuItem("Console", NULL, &m_show_console_panel);
            ImGui::EndMenu();
        }
        if (ImGui::BeginMenu("Help")) {
            ImGui::EndMenu();
        }
        ImGui::EndMainMenuBar();
    }
}

void MyGLApp::guiScreenPanel() {
    ImGui::SetNextWindowSize(ImVec2(m_screen_size[0] + 50, m_screen_size[1] + 150), ImGuiCond_Always);
    ImGui::SetNextWindowPos(ImVec2(100, 100), ImGuiCond_FirstUseEver);
    ImGui::Begin("Screen Panel", &m_show_screen_panel);
    {
        GLuint tex = m_glframe.getColorTexId();
        ImTextureID imtex = (ImTextureID)tex;
        ImGui::Image(imtex, ImVec2(m_screen_size[0], m_screen_size[1]), ImVec2(0,0), ImVec2(1,1), ImVec4(1.f, 1.f, 1.f, 1.f), ImVec4(1.f, 1.f, 1.f, 0.5f));
    }
    ImGuiIO& io = ImGui::GetIO();
    ImGui::LabelText("mouse", "%d, %d", int(io.MousePos.x), int(io.MousePos.y));
    {
        tt::Vec2i size = m_glframe.getImageSize();
        ImGui::LabelText("image size", "%d, %d", size[0], size[1]);
    }
    {
        tt::Vec2i size = m_glframe.getScreenSize();
        ImGui::LabelText("screen size", "%d, %d", size[0], size[1]);
    }
    ImGui::End();
}

void MyGLApp::guiControlPanel() {
    ImGuiStyle& style = ImGui::GetStyle();

    ImGui::Begin("Control Panel", &m_show_control_panel);
    if (ImGui::Button("Main Menu Bar Button")) {
        m_show_main_menu_bar = !m_show_main_menu_bar;
    }
    if (ImGui::Button("Console Button")) {
        m_show_console_panel = !m_show_console_panel;
    }
    ImGui::LabelText("window size", "%d, %d", w(), h());

    ImVec2 pos = ImGui::GetCursorScreenPos();
    ImGui::LabelText("cursor", "%f, %f", pos.x, pos.y);
    ImGuiIO& io = ImGui::GetIO();
    ImGui::LabelText("mouse", "%d, %d", int(io.MousePos.x), int(io.MousePos.y));

    ImGui::LabelText("image size", "%d, %d", m_image.w(), m_image.h());
    ImGui::ColorEdit4("color0", m_color0.data());
    ImGui::ColorEdit4("color1", m_color1.data());
    ImGui::SliderFloat("global alpha", &style.Alpha, 0.20f, 1.0f, "%.2f");
    ImGui::ColorEdit4("clear color", m_clear_color.data());
    ImGui::DragFloat("scale", &m_scale, 0.01f);
    ImGui::Checkbox("fit", &m_fit);

    {
        GLuint tex = m_glframe.getTexId();
        ImTextureID imtex = (ImTextureID)tex;
        tt::Vec2i size = m_glframe.getImageSize();
        float scale = float(size[0]) / size[1];
        ImVec2 ssize(scale * 200, 200);
        ImGui::Image(imtex, ssize, ImVec2(0,0), ImVec2(1,1), ImVec4(1.f, 1.f, 1.f, 1.f), ImVec4(1.f, 1.f, 1.f, 0.5f));
    }

    ImGui::End();
}

void MyGLApp::guiConsolePanel() {
    ImGui::SetNextWindowSize(ImVec2(m_console_size[0], m_console_size[1]), ImGuiCond_FirstUseEver);
    ImGui::SetNextWindowPos(ImVec2(0, 0), ImGuiCond_FirstUseEver);
    ImGui::Begin("Console", &m_show_console_panel);
    m_console.draw();
    ImGui::End();
}

void MyGLApp::init() {
    GLApp::init();
    setIcon(DATA + "icon.png");
    exec("image");
    exec("checker");
    m_glframe.init();
    GLFBO::check();
    m_tm.start();
}

void MyGLApp::gui() {
    if (m_show_main_menu_bar) guiMainMenuBar();
    if (m_show_control_panel) guiControlPanel();
    if (m_show_console_panel) guiConsolePanel();
    if (m_show_screen_panel)  guiScreenPanel();
}

void MyGLApp::draw() {
    glViewport(0, 0, m_w, m_h);
    glClearColor_tt(m_clear_color.data());
    glClear(GL_COLOR_BUFFER_BIT);

    m_glframe.setScreenSize(m_screen_size[0], m_screen_size[1]);

    m_tm.end();
    static int x = 0;
    static int y = 0;
    const tt::Color4f colors[] = {
        {1.f, 0.f, 0.f, 1.f},
        {0.f, 1.f, 0.f, 1.f},
        {0.f, 0.f, 1.f, 1.f}};
    if (int i = m_tm.getElapsedMSec() / 1000) {
        m_color0 = colors[i%3];
    }
    if (m_image.size() != 0) {
        cmd_set_value(x++, y);
        updateTexture();
    }
    if (x == m_image.w()) { x = 0; y++; }
    if (y == m_image.h()) y = 0;

    m_glframe.draw(m_scale, m_fit);
}

