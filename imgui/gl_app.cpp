#include "gl_app.h"
#include <nfd.h>
#include <stdio.h>
#include <string>

std::string f_open_file() {
    nfdchar_t *outPath = NULL;
    nfdresult_t result = NFD_OpenDialog(NULL, NULL, &outPath);

    std::string str;
    if ( result == NFD_OKAY ) {
        str = std::string(outPath);
        puts("Success!");
        puts(outPath);
        free(outPath);
    } else if ( result == NFD_CANCEL ) {
        puts("User pressed cancel.");
    } else {
        printf("Error: %s\n", NFD_GetError() );
    }

    return str;
}

std::string f_save_file() {
    nfdchar_t *outPath = NULL;
    nfdresult_t result = NFD_SaveDialog(NULL, NULL, &outPath);

    std::string str;
    if ( result == NFD_OKAY ) {
        str = std::string(outPath);
        puts("Success!");
        puts(outPath);
        free(outPath);
    } else if ( result == NFD_CANCEL ) {
        puts("User pressed cancel.");
    } else {
        printf("Error: %s\n", NFD_GetError() );
    }

    return str;
}

static void glfw_error_callback(int error, const char* description) {
    fprintf(stderr, "Glfw Error %d: %s\n", error, description);
}

GLApp::GLApp() {
    m_window_title = "GLApp";
    m_window = 0;
    m_w = 800;
    m_h = 600;
}

GLApp::~GLApp() {
}

void GLApp::setIcon(const std::string& fname) {
    tt::Image<tt::RGBA8> image;
    f_load_image(fname, image);

    GLFWimage glfw_image;
    glfw_image.width  = image.w();
    glfw_image.height = image.h();
    glfw_image.pixels = reinterpret_cast<unsigned char*>(image.data());

    glfwSetWindowIcon(m_window, 1, &glfw_image);
}

void GLApp::run() {
    init();
    mainLoop();
    shutdown();
}

void GLApp::init() {
    glfwSetErrorCallback(glfw_error_callback);
    if (!glfwInit()) {
        return;
    }

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 2);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
#if __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif
    m_window = glfwCreateWindow(m_w, m_h, m_window_title.c_str(), NULL, NULL);
    glfwMakeContextCurrent(m_window);
    glfwSwapInterval(1); // Enable vsync
    gl3wInit();

    // Setup Dear ImGui binding
    IMGUI_CHECKVERSION();
    ImGui::CreateContext();
    ImGuiIO& io = ImGui::GetIO(); (void)io;
    //io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;  // Enable Keyboard Controls
    //io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;   // Enable Gamepad Controls

    ImGui_ImplGlfw_InitForOpenGL(m_window, true);
    ImGui_ImplOpenGL3_Init();

    // Setup style
    ImGui::StyleColorsDark();
    //ImGui::StyleColorsClassic();
}

void GLApp::mainLoop() {
    while (!glfwWindowShouldClose(m_window)) {
        glfwPollEvents();

        // Start the ImGui frame
        ImGui_ImplOpenGL3_NewFrame();
        ImGui_ImplGlfw_NewFrame();
        ImGui::NewFrame();

        gui();

        // Rendering
        ImGui::Render();
        glfwMakeContextCurrent(m_window);
        glfwGetFramebufferSize(m_window, &m_w, &m_h);

        draw();

        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());

        glfwMakeContextCurrent(m_window);
        glfwSwapBuffers(m_window);
    }
}

void GLApp::shutdown() {
    // Cleanup
    ImGui_ImplOpenGL3_Shutdown();
    ImGui_ImplGlfw_Shutdown();
    ImGui::DestroyContext();

    glfwDestroyWindow(m_window);
    glfwTerminate();
}

