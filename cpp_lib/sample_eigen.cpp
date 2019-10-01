// *memo_cpp.eigen*
#define _USE_MATH_DEFINES
#include <cmath>

#include <iostream>
#include <Eigen/Core>
#include <Eigen/Geometry>
#include <Eigen/Dense>

using namespace Eigen;
using namespace std;

double ToRadian(double degree) {
    return degree * M_PI / 180.0;
}

double ToDegree(double radian) {
    return radian * 180.0 / M_PI;
}

void f_print(const std::string& s) {
    std::cout << s << std::endl;
}

template<class T>
void f_print_val(const std::string& s, const T& val) {
    std::cout << s << val << std::endl;
}

template<class T>
void f_print_mat(const std::string& s, const T& val) {
    std::cout << s << std::endl;
    std::cout << val << std::endl;
}

void f_print_mat3_row(const std::string& s, const Matrix3f& _m) {
    std::cout << s << std::endl;
    const float* m = _m.data();
    printf("%f %f %f\n", m[0], m[1], m[2]);
    printf("%f %f %f\n", m[3], m[4], m[5]);
    printf("%f %f %f\n", m[6], m[7], m[8]);
}

void f_print_mat3_col(const std::string& s, const Matrix3f& _m) {
    std::cout << s << std::endl;
    const float* m = _m.data();
    printf("%f %f %f\n", m[0], m[3], m[6]);
    printf("%f %f %f\n", m[1], m[4], m[7]);
    printf("%f %f %f\n", m[2], m[5], m[8]);
}

void f_print_mat4_row(const std::string& s, const Matrix4f& _m) {
    std::cout << s << std::endl;
    const float* m = _m.data();
    printf("%f %f %f %f\n", m[0],  m[1],  m[2],  m[3]);
    printf("%f %f %f %f\n", m[4],  m[5],  m[6],  m[7]);
    printf("%f %f %f %f\n", m[8],  m[9],  m[10], m[11]);
    printf("%f %f %f %f\n", m[12], m[13], m[14], m[15]);
}

void f_print_mat4_col(const std::string& s, const Matrix4f& _m) {
    std::cout << s << std::endl;
    const float* m = _m.data();
    printf("%f %f %f %f\n", m[0], m[4], m[8],  m[12]);
    printf("%f %f %f %f\n", m[1], m[5], m[9],  m[13]);
    printf("%f %f %f %f\n", m[2], m[6], m[10], m[14]);
    printf("%f %f %f %f\n", m[3], m[7], m[11], m[15]);
}

//==================================================

void f_constructor() {
    std::cout << "=== f_constructor() ===" << std::endl;

    // default values are unknown
    Vector2f v;
    f_print_mat("Vector2f() = ", v);

    v = Vector2f(1.0f, 2.0f);
    f_print_mat("v = Vector2f(1.0f, 2.0f)", v);

    v = {3.0f, 4.0f};
    f_print_mat("v = {3.0f, 4.0f}", v);

    // default values are unknown
    Matrix2f m;
    f_print_mat("Matrix2f() = ", m);

    // set matrix as row major
    m << 1.0f, 2.0f, 3.0f, 4.0f;
    f_print_mat("m = ", m);
}

void f_vec3() {
    std::cout << "=== f_vec3() ===" << std::endl;

    Vector3f v;
    v = Vector3f::Identity();
    f_print_mat("Vector3f::Identity() = ", v);

    // (0, 0, 0)
    v = Vector3f::Zero();
    f_print_mat("Vector3f::Zero() = ", v);

    // (1, 1, 1)
    v = Vector3f::Ones();
    f_print_mat("Vector3f::Ones() = ", v);

    // (1, 0, 0)
    v = Vector3f::UnitX();
    f_print_mat("Vector3f::UnitX() = ", v);

    // (0, 1, 0)
    v = Vector3f::UnitY();
    f_print_mat("Vector3f::UnitY() = ", v);

    // (0, 0, 1)
    v = Vector3f::UnitZ();
    f_print_mat("Vector3f::UnitZ() = ", v);
}

void f_mat3() {
    std::cout << "=== f_mat3() ===" << std::endl;

    // column major storage
    Matrix3f m;

    // set matrix as row major
    m << 1, 2, 3,
         4, 5, 6,
         7, 8, 9;

    f_print_mat("m = ", m);
    f_print_mat3_col("m = ", m);
}

void f_affine() {
    std::cout << "=== f_affine() ===" << std::endl;

    {
        Translation3f T = Translation3f(1.0f, 2.0f, 3.0f);
        Affine3f affine = Affine3f(T);
        Matrix4f M = affine.matrix();
        f_print_mat4_col("T = ", M);
    }

    {
        Quaternionf R = Quaternionf(AngleAxisf(ToRadian(30.0), Vector3f::UnitX()));
        Affine3f affine = Affine3f(R);
        Matrix4f M = affine.matrix();
        f_print_mat4_col("R = ", M);
    }

    {
        DiagonalMatrix<float, 3> S = Scaling(1.0f, 2.0f, 3.0f);
        Affine3f affine = Affine3f(S);
        Matrix4f M = affine.matrix();
        f_print_mat4_col("S = ", M);
    }

    {
        Matrix3f m;
        m << 1, 2, 3, 4, 5, 6, 7, 8, 9;
        f_print_mat3_col("m = ", m);

        Matrix3f m2;
        m2 << 11, 12, 13, 14, 15, 16, 17, 18, 19;
        f_print_mat3_col("m2 = ", m2);

        Matrix3f M;
        M = m * m2;
        f_print_mat3_col("m * m2 = ", M);

        M = m2 * m;
        f_print_mat3_col("m2 * m = ", M);

        Vector3f v = {1, 2, 3};
        Vector3f V;
        V = m * v;
        f_print_mat("m * v = ", V);

        // invalid product
        //V = v * m;
        //f_print_mat("v * m = ", V);
    }
}

void f_transform() {
    std::cout << "=== f_transform() ===" << std::endl;

    Translation3f T = Translation3f(1.0f, 2.0f, 3.0f);
    Quaternionf R = Quaternionf(AngleAxisf(ToRadian(30.0), Vector3f::UnitX()));
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

    f_print_mat("v = ", v);
    f_print_val("size = ", v.size());
    f_print_val("rows = ", v.rows());
    f_print_val("cols = ", v.cols());
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

    f_print_mat("m = ", m);
    f_print_val("size = ", m.size());
    f_print_val("rows = ", m.rows());
    f_print_val("cols = ", m.cols());

    m.resize(4, 3);
    std::cout << "m.resize(4, 3)" << std::endl;

    f_print_mat("m = ", m);
    f_print_val("size = ", m.size());
    f_print_val("rows = ", m.rows());
    f_print_val("cols = ", m.cols());
}

int main(int argc, char *argv[]) {
    f_constructor();
    f_vec3();
    f_mat3();
    f_affine();
    f_transform();
    f_vecx();
    f_matx();
    return 0;
}

