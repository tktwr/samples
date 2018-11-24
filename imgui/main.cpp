#include "myglapp.h"

int main(int argc, char *argv[]) {
    MyGLApp app;
    app.setDataDir("../data/");
    app.setIconFile("icon.png");
    app.setWindowTitle("sample_imgui");
    app.setWindowSize(800, 600);
    app.run();

    return 0;
}

