// *memo_sample_glm*
#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <iostream>

using namespace std;

void f_print(const std::string& s, const float v) {
    cout << s.c_str() << v << endl;
}
void f_print(const std::string& s, const glm::vec3& v) {
    cout << s.c_str() << v.x << " " << v.y << " " << v.z << endl;
}

int main(int argc, char *argv[]) {
    glm::vec3 v(1, 1, 1);
    f_print("v=", v);
    f_print("sizeof(v)=", sizeof(v));
    f_print("length(v)=", glm::length(v));
    f_print("distance(v,v)=", glm::distance(v, v));
    f_print("cross(v,v)=", glm::cross(v, v));
    f_print("normalize(v)=", glm::normalize(v));
    f_print("dot(v,v)=", glm::dot(v, v));
    f_print("degrees(f)=", glm::degrees(glm::pi<float>()));
    f_print("radians(f)=", glm::radians(180.f));

    return 0;
}

