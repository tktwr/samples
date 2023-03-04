// *sample_cpp_lib.json11*
#include <iostream>
#include <fstream>
#include <string>
#include <json11.hpp>

using namespace std;

class PrettyDump {
public:
private:
    int m_indent;
};

void f_save_json(const char *fname) {
    std::ofstream ofs(fname);

    json11::Json my_json = json11::Json::object {
        { "string", "hello world" },
        { "bool", true },
        { "int", 123 },
        { "float", 123.567 },
        { "array", json11::Json::array { 1, 2, 3 } },
    };
    std::string json_str = my_json.dump();
    ofs << json_str;
}

void f_load_json(const char *fname) {
    std::ifstream ifs(fname);
    std::string line;
    std::string text;
    while (std::getline(ifs, line)) {
        text += line;
    }

    std::string err;
    auto json = json11::Json::parse(text, err);

    std::cout << "string: " << json["string"].string_value() << std::endl;
    std::cout << "bool: " << json["bool"].bool_value() << std::endl;
    std::cout << "int: " << json["int"].int_value() << std::endl;
    std::cout << "float: " << json["float"].number_value() << std::endl;

    std::cout << "array: " << std::endl;
    for (auto &k : json["array"].array_items()) {
        std::cout << "  - " << k.dump() << std::endl;
    }
}

int main(int argc, char *argv[]) {
    f_save_json("test.json");
    f_load_json("test.json");
    return 0;
}

