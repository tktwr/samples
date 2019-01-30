#include <iostream>
#include <sstream>
#include <string>

using namespace std;

std::string g_help_text = R"(COMMANDS:
  help
  quit
)";

class App {
public:
    App() {}
    ~App() {}

    void cmd_help() {
        std::cout << g_help_text << std::endl;
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
};

int main(int argc, char *argv[]) {
    App app;
    app.run();
    return 0;
}

