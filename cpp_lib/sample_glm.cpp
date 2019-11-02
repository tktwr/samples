// *memo_cpp_lib.glm*
#include <iostream>
#include <glm/glm.hpp>
#include <glm/vec3.hpp> // glm::vec3
#include <glm/vec4.hpp> // glm::vec4
#include <glm/mat4x4.hpp> // glm::mat4
#include <glm/gtc/constants.hpp>
#include <glm/gtc/matrix_transform.hpp> // glm::translate, glm::rotate, glm::scale, glm::perspective
#include <glm/gtx/string_cast.hpp> // glm::to_string
#include <tt/ext/glm/glm_util.h>

using namespace std;

void f_print(const std::string& s, const float v) {
    std::cout << s << v << std::endl;
}

void f_print(const std::string& s, const glm::vec3& v) {
    std::cout << s << v.x << " " << v.y << " " << v.z << std::endl;
}

void f_print(const std::string& s, const glm::mat4& m) {
    std::cout << s << glm::to_string(m) << std::endl;
}

//==================================================

void f_memory_order() {
    std::cout << "=== f_memory_order() ===" << std::endl;

    glm::mat4 T = glm::translate(glm::mat4(1.0f), glm::vec3(1.0f, 2.0f, 3.0f));
    f_print_mat4_col("T = ", T);

    // colum order input
    glm::mat3 m = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    glm::mat3 mt = glm::transpose(m);
    f_print_mat3_col("m = ", m);
    f_print_mat3_col("mt = ", mt);

    // colum order input
    glm::mat3 m2 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    glm::mat3 m2t = glm::transpose(m2);
    f_print_mat3_col("m2 = ", m2);
    f_print_mat3_col("m2t = ", m2t);

    glm::mat3 M;
    M = m * m2;
    f_print_mat3_col("M = ", M);

    // M[col][row]
    printf("M = \n");
    printf("%f %f %f\n", M[0][0], M[1][0], M[2][0]);
    printf("%f %f %f\n", M[0][1], M[1][1], M[2][1]);
    printf("%f %f %f\n", M[0][2], M[1][2], M[2][2]);

    // column order memory
    float* p = &(M[0][0]);
    printf("M = \n");
    printf("%f %f %f\n", p[0], p[3], p[6]);
    printf("%f %f %f\n", p[1], p[4], p[7]);
    printf("%f %f %f\n", p[2], p[5], p[8]);
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

void f_affine() {
    std::cout << "=== f_affine() ===" << std::endl;

    {
        glm::mat4 T = glm::translate(glm::mat4(1.0f), glm::vec3(1.0f, 2.0f, 3.0f));
        f_print_mat4_col("T = ", T);
    }

    {
        glm::mat4 R = glm::rotate(glm::mat4(1.0f), glm::radians(30.0f), glm::vec3(1.0f, 0.0f, 0.0f));
        f_print_mat4_col("R = ", R);
    }

    {
        glm::mat4 S = glm::scale(glm::mat4(1.0f), glm::vec3(1.0f, 2.0f, 3.0f));
        f_print_mat4_col("S = ", S);
    }

    {
        glm::mat3 m = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        f_print_mat3_col("m = ", m);

        glm::mat3 m2 = {11, 12, 13, 14, 15, 16, 17, 18, 19};
        f_print_mat3_col("m2 = ", m2);

        glm::mat3 M;
        M = m * m2;
        f_print_mat3_col("m * m2 = ", M);

        M = m2 * m;
        f_print_mat3_col("m2 * m = ", M);

        glm::vec3 v = {1, 2, 3};
        glm::vec3 V;
        V = m * v;
        f_print("m * v = ", V);

        // invalid product
        //V = v * m;
        //f_print_mat("v * m = ", V);
    }
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
    f_memory_order();
    //f_constructor();
    //f_operator();
    //f_func();
    //f_affine();
    //f_transform();

    return 0;
}
