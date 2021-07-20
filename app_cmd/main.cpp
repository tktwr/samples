#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>

using namespace std;

const std::string g_cmdline_help = R"(
NAME:
    app_cmd

SYNOPSIS:
    app_cmd [options]

OPTIONS:
    --help ... print help

EXAMPLES:
    app_cmd --help
)";

const std::string g_cmd_help = R"(
COMMANDS:
  help
  quit
)";

class App {
public:
    App() {}
    ~App() {}

    void cmdline_help() {
        std::cout << g_cmdline_help << std::endl;
    }
    void cmd_help() {
        std::cout << g_cmd_help << std::endl;
    }
    void parse_args(int argc, char *argv[]) {
        for (int i = 1; i < argc; ++i) {
            std::string key = argv[i];
            if (key == "--str1") {
                m_str1 = argv[++i];
            } else if (key == "--int1") {
                m_int1 = atoi(argv[++i]);
            } else if (key == "--float1") {
                m_float1 = atof(argv[++i]);
            } else if (key == "--help") {
                cmdline_help();
                exit(0);
            }
        }
    }
    void print() {
        std::cout << "str1: " << m_str1 << std::endl;
        std::cout << "int1: " << m_int1 << std::endl;
        std::cout << "float1: " << m_float1 << std::endl;
    }
    void exec(const std::string& line) {
        std::istringstream istr(line);
        std::string token;

        istr >> token;

        if (token == "help") {
            cmd_help();
        }
    }
    void run() {
        std::string line;
        while (1) {
            std::cout << "> " << std::flush;
            if (!std::getline(std::cin, line)) return;
            if (line == "quit") return;
            if (line == "") continue;
            if (line[0] == '#') continue;
            exec(line);
        }
    }

private:
    std::string m_str1;
    int m_int1;
    float m_float1;
};

int main(int argc, char *argv[]) {
    App app;
    app.parse_args(argc, argv);
    app.print();
    app.run();
    return 0;
}

