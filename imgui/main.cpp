#include "myglapp.h"

int main(int argc, char *argv[]) {
    MyGLApp app;
    app.setWindowTitle("MyGLApp");
    app.setWindowSize(800, 600);
    app.run();

    return 0;
}

