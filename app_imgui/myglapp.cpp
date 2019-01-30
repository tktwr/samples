#include "myglapp.h"

using namespace std;

MyGLApp::MyGLApp() : GLApp() {
    m_commands = {
        {"info",          "",                     "print info"},
        {"help",          "",                     "print help"},
        {"clear",         "",                     "clear console"},
        {"quit",          "",                     "exit the program"},
    };

    registerCommands();
}

MyGLApp::~MyGLApp() {
}

void MyGLApp::cmd_info() {
}

void MyGLApp::exec(const std::string& line) {
    std::istringstream is(line);
    std::string token;

    is >> token;

    if (token == "") return;
    if (token[0] == '#') return;
    if (token == "quit") {
        cmd_quit();
    } else if (token == "clear") {
        cmd_clear();
    } else if (token == "help") {
        cmd_help();
    } else if (token == "info") {
        cmd_info();
    } else {
        if (line.size()) {
            m_console.shell(line);
        }
    }
}

void MyGLApp::drawGuiMainMenuBar() {
    if (ImGui::BeginMainMenuBar()) {
        if (ImGui::BeginMenu("File")) {
            if (ImGui::MenuItem("Quit", "CTRL+Q")) {
                cmd_quit();
            }
            ImGui::EndMenu();
        }
        if (ImGui::BeginMenu("View")) {
            ImGui::MenuItem("Main Menu Bar", "CTRL+M", &m_show_main_menu_bar);
            ImGui::MenuItem("Sample", NULL, &m_show_sample_panel);
            ImGui::MenuItem("Console", NULL, &m_show_console_panel);
            ImGui::EndMenu();
        }
        if (ImGui::BeginMenu("Help")) {
            if (ImGui::MenuItem("Commands")) {
                cmd_help();
            }
            ImGui::EndMenu();
        }
        ImGui::EndMainMenuBar();
    }
}

// ShowDemoWindow
void MyGLApp::drawGuiSamplePanel() {
    ImGui::Begin("Sample Panel", &m_show_sample_panel);
    if (ImGui::CollapsingHeader("CollapsingHeader"))
    {
        ImGui::Text("Text");
        ImGui::BulletText("BulletText0");
        ImGui::BulletText("BulletText1");
        ImGui::BulletText("BulletText2");
    }
    {
        const char* items[] = {"Classic", "Dark", "Light"};
        static int i = 1;
        if (ImGui::Combo("Style", &i, items, IM_ARRAYSIZE(items))) {
            switch (i) {
                case 0: ImGui::StyleColorsClassic(); break;
                case 1: ImGui::StyleColorsDark(); break;
                case 2: ImGui::StyleColorsLight(); break;
            }
        }
    }
    {
        ImGuiStyle& style = ImGui::GetStyle();
        ImGui::SliderFloat("global alpha", &style.Alpha, 0.20f, 1.0f, "%.2f");
    }
    {
        if (ImGui::Button("Button")) {
            m_console.output("Button pressed");
        }
    }
    {
        static int e = 0;
        ImGui::RadioButton("RadioButton0", &e, 0); ImGui::SameLine();
        ImGui::RadioButton("RadioButton1", &e, 1); ImGui::SameLine();
        ImGui::RadioButton("RadioButton2", &e, 2);
    }
    {
        static bool check = true;
        ImGui::Checkbox("Checkbox", &check);
    }
    ImGui::Separator();
    {
        ImGui::Text("Text");
    }
    {
        static int i = 0;
        ImGui::LabelText("LabelText", "%d", i);
    }
    {
        ImGuiIO& io = ImGui::GetIO();
        ImGui::LabelText("MousePos", "%d, %d", int(io.MousePos.x), int(io.MousePos.y));
    }
    {
        static char str[256] = "Hello, world!";
        ImGui::InputText("InputText", str, IM_ARRAYSIZE(str));
        ShowHelpTip("help");
    }
    {
        unsigned long end = (unsigned long)(m_tm.getElapsedMSec()) % 10000;
        float val = (float)(end) / 10000;
        ImGui::ProgressBar(val);
    }
    ImGui::Separator();
    {
        if (ImGui::TreeNode("TreeNode")) {
            ImGui::Text("tree0");
            ImGui::Text("tree1");
            ImGui::Text("tree2");
            ImGui::TreePop();
        }
    }
    {
        const char* items[] = {"item0", "item1", "item2", "item3", "item4", "item5"};
        static int i = 0;
        ImGui::Combo("Combo", &i, items, IM_ARRAYSIZE(items));
    }
    {
        const char* items[] = {"item0", "item1", "item2", "item3", "item4", "item5"};
        static int i = 0;
        ImGui::ListBox("ListBox", &i, items, IM_ARRAYSIZE(items), 4);
    }
    {
        const std::vector<std::string> items = {"item0", "item1", "item2", "item3", "item4", "item5"};
        static ArrayOfString ar(items);
        static int i = 0;
        ImGui::ListBox("ListBox2", &i, ar.getArray(), ar.size(), 4);
    }
    ImGui::Separator();
    {
        const tt::Color4f colors[] = {
            {1.f, 0.f, 0.f, 1.f},
            {0.f, 1.f, 0.f, 1.f},
            {0.f, 0.f, 1.f, 1.f}};
        if (int i = m_tm.getElapsedMSec() / 1000) {
            m_sample_color = colors[i%3];
        }

        ImGui::ColorEdit4("ColorEdit4", m_sample_color.data());
    }
    ImGui::Separator();
    {
        static int val = 0;
        ImGui::InputInt("InputInt", &val);
    }
    {
        static int val = 0;
        ImGui::SliderInt("SliderInt", &val, 0, 100, "[%d]");
    }
    {
        static int val = 0;
        ImGui::DragInt("DragInt", &val, 1, 0, 100, "[%d]");
    }
    {
        static float val = 0.0f;
        ImGui::DragFloat("DragFloat", &val, 0.01f);
    }
    {
        static float val[2] = {0.0f, 0.0f};
        ImGui::DragFloat2("DragFloat2", val, 0.01f);
    }
    ImGui::End();
}

void MyGLApp::drawGui() {
    if (m_show_main_menu_bar) drawGuiMainMenuBar();
    if (m_show_sample_panel) drawGuiSamplePanel();
    if (m_show_console_panel) drawGuiConsolePanel();
}

void MyGLApp::draw() {
    m_tm.end();

    glViewport(0, 0, m_window_size[0], m_window_size[1]);
    glClearColor(0.2f, 0.2f, 0.2f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);
}

void MyGLApp::init() {
    m_tm.start();
}

