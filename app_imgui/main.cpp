#include "myglapp.h"

int main(int argc, char *argv[]) {
    MyGLApp app;
    app.setIconFile("icon.png");
    app.setWindowTitle("app_imgui");
    app.setWindowSize(800, 600);
    //app.setUiType(MyGLApp::UI_CUI);
    app.run();

    return 0;
}

