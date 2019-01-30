#ifndef myglapp_h
#define myglapp_h

#include <string>
#include <tt/util/time.h>
#include <tt/glapp.h>

class MyGLApp : public GLApp {
public:
    MyGLApp();
    ~MyGLApp();

    void cmd_info();

    void exec(const std::string& line);

    void init();
    void drawGui();
    void draw();

    void drawGuiMainMenuBar();
    void drawGuiSamplePanel();

private:
    tt::Time m_tm;
    tt::Color4f m_sample_color = {1.f, 1.f, 1.f, 1.f};

    bool m_show_main_menu_bar = true;
    bool m_show_sample_panel = true;
};

#endif  // myglapp_h

