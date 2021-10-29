#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <stdlib.h>
#include "trim.h"

using namespace std;

const std::string g_help_args = R"(
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

    //-------------------------------------------------------------------------
    // command
    //-------------------------------------------------------------------------
    void cmd_help() {
        std::cout << g_cmd_help << std::endl;
    }
    void cmd_set(const std::string& name, const std::string& s) {
        m_vars[name] = s;
    }
    void cmd_print(const std::string& s) {
        std::string expanded = expand_vars(s);
        std::cout << '"' << expanded << '"' << std::endl;
    }
    void exec(const std::string& line) {
        std::istringstream istr(line);
        std::string token;

        istr >> token;

        if (token == "help") {
            cmd_help();
        } else if (token == "set") {
            std::string name;
            std::string val;
            istr >> name >> val;
            cmd_set(name, val);
        } else if (token == "print") {
            std::string l;
            std::getline(istr, l);
            trim(l);
            cmd_print(l);
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

    //-------------------------------------------------------------------------
    // args
    //-------------------------------------------------------------------------
    void help_args() {
        std::cout << g_help_args << std::endl;
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
                help_args();
                exit(0);
            }
        }
    }
    void print_args() {
        std::cout << "str1: " << m_str1 << std::endl;
        std::cout << "int1: " << m_int1 << std::endl;
        std::cout << "float1: " << m_float1 << std::endl;
    }

private:
    // expand ${...}
    std::string expand_vars(std::string line) {
        while (1) {
            auto i1 = line.find("${");
            if (i1 == std::string::npos) break;

            auto i2 = line.find("}");
            if (i2 == std::string::npos) break;

            std::string name = line.substr(i1+2, i2-i1-2);
            std::string expanded = m_vars[name];
            line.replace(i1, i2-i1+1, expanded.c_str());
        }
        return line;
    }

    std::string m_str1 = "default";
    int m_int1 = 123;
    float m_float1 = 1.23;
    std::map<std::string, std::string> m_vars;
};

int main(int argc, char *argv[]) {
    App app;
    app.parse_args(argc, argv);
    app.print_args();
    app.run();
    return 0;
}

