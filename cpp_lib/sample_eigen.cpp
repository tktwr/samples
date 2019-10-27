// *memo_cpp_lib.eigen*
#define _USE_MATH_DEFINES
#include <cmath>

#include <iostream>
#include <Eigen/Core>
#include <Eigen/Geometry>
#include <Eigen/Dense>
#include <tt/ext/eigen/eigen_util.h>

using namespace Eigen;
using namespace std;

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

//==================================================

void f_memory_order() {
    std::cout << "=== f_memory_order() ===" << std::endl;

    {
        Translation3f T = Translation3f(1.0f, 2.0f, 3.0f);
        Affine3f affine = Affine3f(T);
        Matrix4f M = affine.matrix();
        f_print_mat4_col("T = ", M);
    }

    Matrix3f m;
    // row order input
    m << 1, 2, 3, 4, 5, 6, 7, 8, 9;
    Matrix3f mt;
    mt = m.transpose();
    f_print_mat3_col("m = ", m);
    f_print_mat3_col("mt = ", mt);

    Matrix3f m2;
    // row order input
    m2 << 1, 2, 3, 4, 5, 6, 7, 8, 9;
    Matrix3f m2t;
    m2t = m2.transpose();
    f_print_mat3_col("m2 = ", m2);
    f_print_mat3_col("m2t = ", m2t);

    Matrix3f M;
    M = mt * m2t;
    f_print_mat3_col("M = ", M);

    // M(row, col)
    printf("M = \n");
    printf("%f %f %f\n", M(0, 0), M(0, 1), M(0, 2));
    printf("%f %f %f\n", M(1, 0), M(1, 1), M(1, 2));
    printf("%f %f %f\n", M(2, 0), M(2, 1), M(2, 2));

    // column order memory
    float* p = M.data();
    printf("M = \n");
    printf("%f %f %f\n", p[0], p[3], p[6]);
    printf("%f %f %f\n", p[1], p[4], p[7]);
    printf("%f %f %f\n", p[2], p[5], p[8]);
}

void f_constructor() {
    std::cout << "=== f_constructor() ===" << std::endl;

    // default values are unknown
    Vector2f v;
    f_print_mat("Vector2f v;", v);

    v = Vector2f(1.0f, 2.0f);
    f_print_mat("v = Vector2f(1.0f, 2.0f);", v);

    v = {3.0f, 4.0f};
    f_print_mat("v = {3.0f, 4.0f};", v);

    // default values are unknown
    Matrix2f m;
    f_print_mat("Matrix2f m;", m);

    // set matrix as row major
    m << 1.0f, 2.0f, 3.0f, 4.0f;
    f_print_mat("m << 1.0f, 2.0f, 3.0f, 4.0f;", m);
}

void f_vec3() {
    std::cout << "=== f_vec3() ===" << std::endl;

    Vector3f v;
    v = Vector3f::Identity();
    f_print_mat("v = Vector3f::Identity();", v);

    // (0, 0, 0)
    v = Vector3f::Zero();
    f_print_mat("v = Vector3f::Zero();", v);

    // (1, 1, 1)
    v = Vector3f::Ones();
    f_print_mat("v = Vector3f::Ones();", v);

    // (1, 0, 0)
    v = Vector3f::UnitX();
    f_print_mat("v = Vector3f::UnitX();", v);

    // (0, 1, 0)
    v = Vector3f::UnitY();
    f_print_mat("v = Vector3f::UnitY();", v);

    // (0, 0, 1)
    v = Vector3f::UnitZ();
    f_print_mat("v = Vector3f::UnitZ();", v);
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

    Vector3f v = {1, 2, 3};
    Vector3f V;
    V = m * v;
    f_print_mat("m * v = ", V);

    // invalid product
    //V = v * m;
    //f_print_mat("v * m = ", V);
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
        Quaternionf R = Quaternionf(AngleAxisf(ToRadian(90.0), Vector3f::UnitX()));
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
}

void f_conv() {
    std::cout << "=== f_conv() ===" << std::endl;

    Translation3f T = Translation3f(1000.0f, 1000.0f, 0.0f);
    Quaternionf R = Quaternionf(AngleAxisf(ToRadian(90.0), Vector3f::UnitX()));
    DiagonalMatrix<float, 3> S = Scaling(1.0f, 1.0f, 1.0f);

    Affine3f M;
    M = T * R * S;

    Matrix4f m = M.matrix();
    f_print_mat4_col("m = ", m);

    Vector4f v = {1, 0, 0, 1};
    Vector4f v2 = m * v;
    f_print_vec4("v2 = ", v2);
}

void f_transform() {
    std::cout << "=== f_transform() ===" << std::endl;

    Translation3f T = Translation3f(1.0f, 2.0f, 3.0f);
    Quaternionf R = Quaternionf(AngleAxisf(ToRadian(90.0), Vector3f::UnitX()));
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
    //f_memory_order();
    //f_constructor();
    //f_vec3();
    //f_mat3();
    //f_affine();
    f_conv();
    //f_transform();
    //f_vecx();
    //f_matx();
    return 0;
}

