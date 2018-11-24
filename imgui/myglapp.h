#ifndef myglapp_h
#define myglapp_h

#include "gl_app.h"
#include "gl_frame.h"
#include <util/type.h>
#include <util/image.h>
#include <util/time.h>
#include <string>
#include "imgui_console.h"

const std::string DATA = "../data/";

class MyGLApp : public GLApp {
public:
    MyGLApp();

    void cmd_load_config(const std::string& fname);
    void cmd_save_config(const std::string& fname);
    void cmd_help();
    void cmd_info();
    void cmd_clear();
    void cmd_image(const tt::Vec2i& size);
    void cmd_get_value(int x, int y);
    void cmd_set_value(int x, int y);
    void cmd_draw_line(const tt::Vec2i& p1, const tt::Vec2i& p2, int thickness);
    void cmd_draw_rect(const tt::Vec2i& o, const tt::Vec2i& size);
    void cmd_fill_rect(const tt::Vec2i& o, const tt::Vec2i& size);
    void cmd_vstripe(int nw);
    void cmd_hstripe(int nh);
    void cmd_checker(const tt::Vec2i& n);
    void cmd_hgrad();
    void cmd_vgrad();
    void cmd_flip();
    void cmd_flop();
    void cmd_blur(const tt::Vec2i& ksize);
    void cmd_bilateral();
    void cmd_erode(int iterations);
    void cmd_dilate(int iterations);
    void cmd_detect_face();

    void updateTexture();
    void exec(const std::string& line);

    void guiMainMenuBar();
    void guiScreenPanel();
    void guiControlPanel();
    void guiConsolePanel();
    void guiSamplePanel();

    void init();
    void gui();
    void draw();

private:
    Console m_console;
    GLFrame m_glframe;
    tt::Image4uc m_image;
    tt::Time m_tm;

    bool m_show_main_menu_bar = true;
    bool m_show_screen_panel = true;
    bool m_show_control_panel = true;
    bool m_show_console_panel = true;
    bool m_show_sample_panel = true;

    tt::Vec2i m_screen_size = {400, 711};
    tt::Vec2i m_console_size = {600, 400};

    // color range: [0, 1]
    tt::Color4f m_color0 = {1.f, 1.f, 1.f, 1.f};
    tt::Color4f m_color1 = {0.f, 0.f, 0.f, 1.f};
    tt::Color4f m_clear_color = {0.5f, 0.5f, 0.5f, 1.f};

    float m_display_scale = 1.f;
    float m_scale = 1.f;
    bool m_fit = true;

    //std::string m_face_detector = "haarcascade_frontalface_default.xml";
    std::string m_face_detector = "lbpcascade_animeface.xml";

    tt::Color4f m_sample_color = {1.f, 1.f, 1.f, 1.f};
};

#endif  // myglapp_h

