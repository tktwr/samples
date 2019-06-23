#include "myglapp.h"
#include <json11.hpp>

using namespace std;

namespace ImGui {
    void StyleColorsCustom(ImGuiStyle* dst = NULL);
}

void ImGui::StyleColorsCustom(ImGuiStyle* dst)
{
    ImGuiStyle* style = dst ? dst : &ImGui::GetStyle();
    ImVec4* colors = style->Colors;

    colors[ImGuiCol_Text]                   = ImVec4(1.00f, 1.00f, 1.00f, 1.00f);
    colors[ImGuiCol_TextDisabled]           = ImVec4(0.50f, 0.50f, 0.50f, 1.00f);
    colors[ImGuiCol_WindowBg]               = ImVec4(0.06f, 0.06f, 0.06f, 0.94f);
    colors[ImGuiCol_ChildBg]                = ImVec4(1.00f, 1.00f, 1.00f, 0.00f);
    colors[ImGuiCol_PopupBg]                = ImVec4(0.08f, 0.08f, 0.08f, 0.94f);
    colors[ImGuiCol_Border]                 = ImVec4(0.43f, 0.43f, 0.50f, 0.50f);
    colors[ImGuiCol_BorderShadow]           = ImVec4(0.00f, 0.00f, 0.00f, 0.00f);
    colors[ImGuiCol_FrameBg]                = ImVec4(0.40f, 0.40f, 0.40f, 0.54f);
    colors[ImGuiCol_FrameBgHovered]         = ImVec4(0.26f, 0.59f, 0.98f, 0.40f);
    colors[ImGuiCol_FrameBgActive]          = ImVec4(0.26f, 0.59f, 0.98f, 0.67f);
    colors[ImGuiCol_TitleBg]                = ImVec4(0.04f, 0.04f, 0.04f, 1.00f);
    colors[ImGuiCol_TitleBgActive]          = ImVec4(0.30f, 0.30f, 0.30f, 1.00f);
    colors[ImGuiCol_TitleBgCollapsed]       = ImVec4(0.00f, 0.00f, 0.00f, 0.51f);
    colors[ImGuiCol_MenuBarBg]              = ImVec4(0.14f, 0.14f, 0.14f, 1.00f);
    colors[ImGuiCol_ScrollbarBg]            = ImVec4(0.02f, 0.02f, 0.02f, 0.53f);
    colors[ImGuiCol_ScrollbarGrab]          = ImVec4(0.31f, 0.31f, 0.31f, 1.00f);
    colors[ImGuiCol_ScrollbarGrabHovered]   = ImVec4(0.41f, 0.41f, 0.41f, 1.00f);
    colors[ImGuiCol_ScrollbarGrabActive]    = ImVec4(0.51f, 0.51f, 0.51f, 1.00f);
    colors[ImGuiCol_CheckMark]              = ImVec4(0.26f, 0.59f, 0.98f, 1.00f);
    colors[ImGuiCol_SliderGrab]             = ImVec4(0.24f, 0.52f, 0.88f, 1.00f);
    colors[ImGuiCol_SliderGrabActive]       = ImVec4(0.26f, 0.59f, 0.98f, 1.00f);
    colors[ImGuiCol_Button]                 = ImVec4(0.50f, 0.50f, 0.50f, 0.40f);
    colors[ImGuiCol_ButtonHovered]          = ImVec4(0.26f, 0.59f, 0.98f, 1.00f);
    colors[ImGuiCol_ButtonActive]           = ImVec4(0.06f, 0.53f, 0.98f, 1.00f);
    colors[ImGuiCol_Header]                 = ImVec4(0.26f, 0.59f, 0.98f, 0.31f);
    colors[ImGuiCol_HeaderHovered]          = ImVec4(0.26f, 0.59f, 0.98f, 0.80f);
    colors[ImGuiCol_HeaderActive]           = ImVec4(0.26f, 0.59f, 0.98f, 1.00f);
    colors[ImGuiCol_Separator]              = colors[ImGuiCol_Border];
    colors[ImGuiCol_SeparatorHovered]       = ImVec4(0.10f, 0.40f, 0.75f, 0.78f);
    colors[ImGuiCol_SeparatorActive]        = ImVec4(0.10f, 0.40f, 0.75f, 1.00f);
    colors[ImGuiCol_ResizeGrip]             = ImVec4(0.26f, 0.59f, 0.98f, 0.25f);
    colors[ImGuiCol_ResizeGripHovered]      = ImVec4(0.26f, 0.59f, 0.98f, 0.67f);
    colors[ImGuiCol_ResizeGripActive]       = ImVec4(0.26f, 0.59f, 0.98f, 0.95f);
    colors[ImGuiCol_PlotLines]              = ImVec4(0.61f, 0.61f, 0.61f, 1.00f);
    colors[ImGuiCol_PlotLinesHovered]       = ImVec4(1.00f, 0.43f, 0.35f, 1.00f);
    colors[ImGuiCol_PlotHistogram]          = ImVec4(0.90f, 0.70f, 0.00f, 1.00f);
    colors[ImGuiCol_PlotHistogramHovered]   = ImVec4(1.00f, 0.60f, 0.00f, 1.00f);
    colors[ImGuiCol_TextSelectedBg]         = ImVec4(0.26f, 0.59f, 0.98f, 0.35f);
    colors[ImGuiCol_DragDropTarget]         = ImVec4(1.00f, 1.00f, 0.00f, 0.90f);
    colors[ImGuiCol_NavHighlight]           = ImVec4(0.26f, 0.59f, 0.98f, 1.00f);
    colors[ImGuiCol_NavWindowingHighlight]  = ImVec4(1.00f, 1.00f, 1.00f, 0.70f);
    colors[ImGuiCol_NavWindowingDimBg]      = ImVec4(0.80f, 0.80f, 0.80f, 0.20f);
    colors[ImGuiCol_ModalWindowDimBg]       = ImVec4(0.80f, 0.80f, 0.80f, 0.35f);
}

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
            ImGui::MenuItem("Style", NULL, &m_show_style_panel);
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
        const char* items[] = {"Classic", "Dark", "Light", "Custom"};
        static int i = 1;
        if (ImGui::Combo("Style", &i, items, IM_ARRAYSIZE(items))) {
            switch (i) {
                case 0: ImGui::StyleColorsClassic(); break;
                case 1: ImGui::StyleColorsDark(); break;
                case 2: ImGui::StyleColorsLight(); break;
                case 3: ImGui::StyleColorsCustom(); break;
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

void save_style() {
}

void color_gui(ImVec4* colors, ImGuiCol_ id, const char* name) {
    ImVec4& val = colors[id];
    //ImGui::DragFloat4(name, &val.x, 0.01f);
    ImGui::ColorEdit4(name, &val.x);
}

void MyGLApp::drawGuiStylePanel() {
    ImGuiStyle* style = &ImGui::GetStyle();
    ImVec4* colors = style->Colors;

    ImGui::Begin("Style Panel", &m_show_style_panel);
    color_gui(colors, ImGuiCol_Text, "ImGuiCol_Text");
    color_gui(colors, ImGuiCol_TextDisabled, "ImGuiCol_TextDisabled");
    color_gui(colors, ImGuiCol_WindowBg, "ImGuiCol_WindowBg");
    color_gui(colors, ImGuiCol_ChildBg, "ImGuiCol_ChildBg");
    color_gui(colors, ImGuiCol_PopupBg, "ImGuiCol_PopupBg");
    color_gui(colors, ImGuiCol_Border, "ImGuiCol_Border");
    color_gui(colors, ImGuiCol_BorderShadow, "ImGuiCol_BorderShadow");
    color_gui(colors, ImGuiCol_FrameBg, "ImGuiCol_FrameBg");
    color_gui(colors, ImGuiCol_FrameBgHovered, "ImGuiCol_FrameBgHovered");
    color_gui(colors, ImGuiCol_FrameBgActive, "ImGuiCol_FrameBgActive");
    color_gui(colors, ImGuiCol_TitleBg, "ImGuiCol_TitleBg");
    color_gui(colors, ImGuiCol_TitleBgActive, "ImGuiCol_TitleBgActive");
    color_gui(colors, ImGuiCol_TitleBgCollapsed, "ImGuiCol_TitleBgCollapsed");
    color_gui(colors, ImGuiCol_MenuBarBg, "ImGuiCol_MenuBarBg");
    color_gui(colors, ImGuiCol_ScrollbarBg, "ImGuiCol_ScrollbarBg");
    color_gui(colors, ImGuiCol_ScrollbarGrab, "ImGuiCol_ScrollbarGrab");
    color_gui(colors, ImGuiCol_ScrollbarGrabHovered, "ImGuiCol_ScrollbarGrabHovered");
    color_gui(colors, ImGuiCol_ScrollbarGrabActive, "ImGuiCol_ScrollbarGrabActive");
    color_gui(colors, ImGuiCol_CheckMark, "ImGuiCol_CheckMark");
    color_gui(colors, ImGuiCol_SliderGrab, "ImGuiCol_SliderGrab");
    color_gui(colors, ImGuiCol_SliderGrabActive, "ImGuiCol_SliderGrabActive");
    color_gui(colors, ImGuiCol_Button, "ImGuiCol_Button");
    color_gui(colors, ImGuiCol_ButtonHovered, "ImGuiCol_ButtonHovered");
    color_gui(colors, ImGuiCol_ButtonActive, "ImGuiCol_ButtonActive");
    color_gui(colors, ImGuiCol_Header, "ImGuiCol_Header");
    color_gui(colors, ImGuiCol_HeaderHovered, "ImGuiCol_HeaderHovered");
    color_gui(colors, ImGuiCol_HeaderActive, "ImGuiCol_HeaderActive");
    color_gui(colors, ImGuiCol_Separator, "ImGuiCol_Separator");
    color_gui(colors, ImGuiCol_SeparatorHovered, "ImGuiCol_SeparatorHovered");
    color_gui(colors, ImGuiCol_SeparatorActive, "ImGuiCol_SeparatorActive");
    color_gui(colors, ImGuiCol_ResizeGrip, "ImGuiCol_ResizeGrip");
    color_gui(colors, ImGuiCol_ResizeGripHovered, "ImGuiCol_ResizeGripHovered");
    color_gui(colors, ImGuiCol_ResizeGripActive, "ImGuiCol_ResizeGripActive");
    color_gui(colors, ImGuiCol_PlotLines, "ImGuiCol_PlotLines");
    color_gui(colors, ImGuiCol_PlotLinesHovered, "ImGuiCol_PlotLinesHovered");
    color_gui(colors, ImGuiCol_PlotHistogram, "ImGuiCol_PlotHistogram");
    color_gui(colors, ImGuiCol_PlotHistogramHovered, "ImGuiCol_PlotHistogramHovered");
    color_gui(colors, ImGuiCol_TextSelectedBg, "ImGuiCol_TextSelectedBg");
    color_gui(colors, ImGuiCol_DragDropTarget, "ImGuiCol_DragDropTarget");
    color_gui(colors, ImGuiCol_NavHighlight, "ImGuiCol_NavHighlight");
    color_gui(colors, ImGuiCol_NavWindowingHighlight, "ImGuiCol_NavWindowingHighlight");
    color_gui(colors, ImGuiCol_NavWindowingDimBg, "ImGuiCol_NavWindowingDimBg");
    color_gui(colors, ImGuiCol_ModalWindowDimBg, "ImGuiCol_ModalWindowDimBg");
    ImGui::End();
}

void MyGLApp::drawGui() {
    if (m_show_main_menu_bar) drawGuiMainMenuBar();
    if (m_show_sample_panel)  drawGuiSamplePanel();
    if (m_show_style_panel)   drawGuiStylePanel();
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

