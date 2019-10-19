// *memo_cpp.glm*
#include <glm/glm.hpp>
#include <glm/vec3.hpp> // glm::vec3
#include <glm/vec4.hpp> // glm::vec4
#include <glm/mat4x4.hpp> // glm::mat4
#include <glm/gtc/constants.hpp>
#include <glm/gtc/matrix_transform.hpp> // glm::translate, glm::rotate, glm::scale, glm::perspective
#include <glm/gtx/string_cast.hpp> // glm::to_string
#include <iostream>
#include <tt/ext/glm/glm_util.h>

using namespace std;

void f_print(const std::string& s, const float v) {
    cout << s.c_str() << v << endl;
}

void f_print(const std::string& s, const glm::vec3& v) {
    cout << s.c_str() << v.x << " " << v.y << " " << v.z << endl;
}

void f_print(const std::string& s, const glm::mat4& m) {
    cout << s.c_str() << glm::to_string(m) << endl;
}

void f_constructor() {
    std::cout << "=== f_constructor() ===" << std::endl;

    glm::vec3 v(1.0f);
    glm::mat4 m(1.0f);

    f_print("v = ", v);
    f_print("m = ", m);
    f_print_mat4_col("m = ", m);
}

void f_operator() {
    std::cout << "=== f_operator() ===" << std::endl;

    glm::vec3 v(1, 2, 3);
    glm::mat4 m(1.0f);
    float f = 4;

    f_print("v = ", v);
    f_print("m = ", m);
    f_print("f = ", f);

    f_print("v + v = ", v + v);
    f_print("v - v = ", v - v);
    f_print("v * v = ", v * v); // component-wise
    f_print("v / v = ", v / v); // component-wise
    f_print("v * f = ", v * f);
    f_print("f * v = ", f * v);
}

void f_func() {
    std::cout << "=== f_func() ===" << std::endl;

    glm::vec3 v(1, 2, 3);
    glm::mat4 m(1.0f);
    float f = 4;

    f_print("v = ", v);
    f_print("m = ", m);
    f_print("f = ", f);

    f_print("sizeof(v) = ", sizeof(v));
    f_print("length(v) = ", glm::length(v));
    f_print("distance(v,v) = ", glm::distance(v, v));
    f_print("normalize(v) = ", glm::normalize(v));
    f_print("dot(v,v) = ", glm::dot(v, v));
    f_print("cross(v,v) = ", glm::cross(v, v));
    f_print("degrees(f) = ", glm::degrees(glm::pi<float>()));
    f_print("radians(f) = ", glm::radians(180.f));
}

void f_transform() {
    std::cout << "=== f_transform() ===" << std::endl;

    glm::mat4 T = glm::translate(glm::mat4(1.0f), glm::vec3(1.0f, 1.0f, 1.0f));
    glm::mat4 R = glm::rotate(glm::mat4(1.0f), glm::radians(90.0f), glm::vec3(1.0f, 0.0f, 0.0f));
    glm::mat4 S = glm::scale(glm::mat4(1.0f), glm::vec3(0.5f));
    glm::mat4 M = T * R * S;

    f_print_mat4_col("M = ", M);
    f_print_mat4_col("T = ", T);
    f_print_mat4_col("R = ", R);
    f_print_mat4_col("S = ", S);
}

glm::mat4 camera(float z, const glm::vec2& rot) {
    glm::mat4 proj = glm::perspective(glm::radians(45.0f), 4.0f / 3.0f, 0.1f, 100.f);
    glm::mat4 view = glm::translate(glm::mat4(1.0f), glm::vec3(0.0f, 0.0f, -z));
    view = glm::rotate(view, rot.y, glm::vec3(-1.0f, 0.0f, 0.0f));
    view = glm::rotate(view, rot.x, glm::vec3(0.0f, 1.0f, 0.0f));
    glm::mat4 model = glm::scale(glm::mat4(1.0f), glm::vec3(0.5f));
    return proj * view * model;
}

int main(int argc, char *argv[]) {
    f_constructor();
    f_operator();
    f_func();
    f_transform();

    return 0;
}

