// *memo_cpp.eigen*
#define _USE_MATH_DEFINES
#include <cmath>

#include <iostream>
#include <Eigen/Core>
#include <Eigen/Geometry>
#include <Eigen/Dense>

using namespace Eigen;
using namespace std;

template<class T>
void f_print_s(const std::string& s, const T& val) {
    std::cout << s << val << std::endl;
}

template<class T>
void f_print_m(const std::string& s, const T& val) {
    std::cout << s << std::endl;
    std::cout << val << std::endl;
}

void f_constructor() {
    std::cout << "=== f_constructor() ===" << std::endl;

    // default values are unknown
    Vector2f v;
    f_print_m("Vector2f() = ", v);

    v = Vector2f(1.0f, 2.0f);
    f_print_m("v = ", v);

    // default values are unknown
    Matrix2f m;
    f_print_m("Matrix2f() = ", m);

    m << 1.0f, 2.0f, 3.0f, 4.0f;
    f_print_m("m = ", m);
}

void f_vec3() {
    std::cout << "=== f_vec3() ===" << std::endl;

    Vector3f v;
    v = Vector3f::Identity();
    f_print_m("Identity() = ", v);

    // (0, 0, 0)
    v = Vector3f::Zero();
    f_print_m("Zero() = ", v);

    // (1, 1, 1)
    v = Vector3f::Ones();
    f_print_m("Ones() = ", v);

    // (1, 0, 0)
    v = Vector3f::UnitX();
    f_print_m("UnitX() = ", v);

    // (0, 1, 0)
    v = Vector3f::UnitY();
    f_print_m("UnitY() = ", v);

    // (0, 0, 1)
    v = Vector3f::UnitZ();
    f_print_m("UnitZ() = ", v);
}

void f_mat3() {
    std::cout << "=== f_mat3() ===" << std::endl;

    Matrix3f m;

    m << 1, 2, 3,
         4, 5, 6,
         7, 8, 9;

    f_print_m("m = ", m);
}

void f_transform() {
    std::cout << "=== f_transform() ===" << std::endl;

    Translation<float, 3> T = Translation<float, 3>(1.0f, 2.0f, 3.0f);
    Quaternionf R = Quaternionf(AngleAxisf(0.5f * M_PI, Vector3f::UnitY()));
    DiagonalMatrix<float, 3> S = Scaling(1.0f, 2.0f, 3.0f);

    Affine3f M;
    M = T * R * S;

    Vector3f p0(1.0f, -1.0f, 0.5f);
    Vector3f p1 = M * p0;

    Vector3f v1(1.0f, 0.0f, -1.0f);
    Vector3f v2;

    v2 = T * v1;
    v2 = R * v1;
    v2 = S * v1;
    v2 = T * R * S * v1;

    Matrix4f m = M.matrix();
}

void f_vecx() {
    std::cout << "=== f_vecx() ===" << std::endl;

    VectorXd v;

    v.resize(5);
    std::cout << "v.resize(5)" << std::endl;

    f_print_m("v = ", v);
    f_print_s("size = ", v.size());
    f_print_s("rows = ", v.rows());
    f_print_s("cols = ", v.cols());
}

void f_matx() {
    std::cout << "=== f_matx() ===" << std::endl;

    MatrixXd m(2, 3);

    m(0, 0) = 1;
    m(0, 1) = 2;
    m(0, 2) = 3;

    m(1, 0) = 4;
    m(1, 1) = 5;
    m(1, 2) = 6;

    f_print_m("m = ", m);
    f_print_s("size = ", m.size());
    f_print_s("rows = ", m.rows());
    f_print_s("cols = ", m.cols());

    m.resize(4, 3);
    std::cout << "m.resize(4, 3)" << std::endl;

    f_print_m("m = ", m);
    f_print_s("size = ", m.size());
    f_print_s("rows = ", m.rows());
    f_print_s("cols = ", m.cols());
}

int main(int argc, char *argv[]) {
    f_constructor();
    f_vec3();
    f_mat3();
    f_transform();
    f_vecx();
    f_matx();
    return 0;
}

