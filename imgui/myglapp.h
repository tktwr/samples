#ifndef myglapp_h
#define myglapp_h

#include "gl_app.h"
#include "gl_frame.h"
#include <util/type.h>
#include <util/image.h>
#include <util/time.h>
#include <string>
#include "imgui_console.h"

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
    void cmd_rect(const tt::Vec2i& _o, const tt::Vec2i& _size);
    void cmd_rect_fill(const tt::Vec2i& o, const tt::Vec2i& size);
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
    void guiControlPanel();
    void guiConsolePanel();
    void guiScreenPanel();

    void init();
    void gui();
    void draw();

private:
    bool m_show_main_menu_bar;
    bool m_show_control_panel;
    bool m_show_console_panel;
    bool m_show_screen_panel;

    Console m_console;
    GLFrame m_glframe;
    float m_scale;
    bool m_fit;

    tt::Image4uc m_image;

    // color range: [0, 1]
    tt::Color4f m_color0;
    tt::Color4f m_color1;
    tt::Color4f m_clear_color;

    //tt::Vec2i m_screen_size = {1080, 1920};
    tt::Vec2i m_screen_size = {400, 711};
    tt::Vec2i m_console_size = {600, 400};

    std::string m_face_detector;
    tt::Time m_tm;
};

#endif  // myglapp_h

