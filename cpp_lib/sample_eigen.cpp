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

namespace tt {

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

}

//==================================================

void f_memory_order() {
    std::cout << "=== f_memory_order() ===" << std::endl;

    {
        Translation3f T = Translation3f(1.0f, 2.0f, 3.0f);
        Affine3f affine = Affine3f(T);
        Matrix4f M = affine.matrix();
        tt::f_print_mat4_col("T = ", M);
    }

    Matrix3f m;
    // row order input
    m << 1, 2, 3, 4, 5, 6, 7, 8, 9;
    Matrix3f mt;
    mt = m.transpose();
    tt::f_print_mat3_col("m = ", m);
    tt::f_print_mat3_col("mt = ", mt);

    Matrix3f m2;
    // row order input
    m2 << 1, 2, 3, 4, 5, 6, 7, 8, 9;
    Matrix3f m2t;
    m2t = m2.transpose();
    tt::f_print_mat3_col("m2 = ", m2);
    tt::f_print_mat3_col("m2t = ", m2t);

    Matrix3f M;
    M = mt * m2t;
    tt::f_print_mat3_col("M = ", M);

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
    tt::f_print_mat("Vector2f v;", v);

    v = Vector2f(1.0f, 2.0f);
    tt::f_print_mat("v = Vector2f(1.0f, 2.0f);", v);

    v = {3.0f, 4.0f};
    tt::f_print_mat("v = {3.0f, 4.0f};", v);

    // default values are unknown
    Matrix2f m;
    tt::f_print_mat("Matrix2f m;", m);

    // set matrix as row major
    m << 1.0f, 2.0f, 3.0f, 4.0f;
    tt::f_print_mat("m << 1.0f, 2.0f, 3.0f, 4.0f;", m);
}

void f_vec3() {
    std::cout << "=== f_vec3() ===" << std::endl;

    Vector3f v;
    v = Vector3f::Identity();
    tt::f_print_mat("v = Vector3f::Identity();", v);

    // (0, 0, 0)
    v = Vector3f::Zero();
    tt::f_print_mat("v = Vector3f::Zero();", v);

    // (1, 1, 1)
    v = Vector3f::Ones();
    tt::f_print_mat("v = Vector3f::Ones();", v);

    // (1, 0, 0)
    v = Vector3f::UnitX();
    tt::f_print_mat("v = Vector3f::UnitX();", v);

    // (0, 1, 0)
    v = Vector3f::UnitY();
    tt::f_print_mat("v = Vector3f::UnitY();", v);

    // (0, 0, 1)
    v = Vector3f::UnitZ();
    tt::f_print_mat("v = Vector3f::UnitZ();", v);
}

void f_mat3() {
    std::cout << "=== f_mat3() ===" << std::endl;

    // column major storage
    Matrix3f m;

    // set matrix as row major
    m << 1, 2, 3,
         4, 5, 6,
         7, 8, 9;

    tt::f_print_mat("m = ", m);
    tt::f_print_mat3_col("m = ", m);

    Vector3f v = {1, 2, 3};
    Vector3f V;
    V = m * v;
    tt::f_print_mat("m * v = ", V);

    // invalid product
    //V = v * m;
    //tt::f_print_mat("v * m = ", V);
}

constexpr float PI = static_cast<float>(EIGEN_PI);
using Vec3 = Eigen::Vector3f;
using Quat = Eigen::Quaternionf;

float DegToRad(float deg) {
    return PI * deg / 180.f;
}

float RadToDeg(float rad) {
    return 180.f * rad / PI;
}

// convert quaternion to Euler angle (radian)
Vec3 Quat2Euler(const Quat& q) {
    return q.toRotationMatrix().eulerAngles(0, 1, 2);
}

// convert Euler angle (radian) to quaternion
Quat Euler2Quat(const Vec3& v) {
    return Eigen::AngleAxisf(v[0], Vec3::UnitX()) *
           Eigen::AngleAxisf(v[1], Vec3::UnitY()) *
           Eigen::AngleAxisf(v[2], Vec3::UnitZ());
}

// convert quaternion to Euler angle (degree)
Vec3 Quat2EulerInDeg(const Quat& q) {
    Vec3 v = q.toRotationMatrix().eulerAngles(0, 1, 2);
    return Vec3(RadToDeg(v[0]), RadToDeg(v[1]), RadToDeg(v[2]));
}

// convert Euler angle (degree) to quaternion
Quat Euler2QuatInDeg(const Vec3& _v) {
    Vec3 v = Vec3(DegToRad(_v[0]), DegToRad(_v[1]), DegToRad(_v[2]));
    return Eigen::AngleAxisf(v[0], Vec3::UnitX()) *
           Eigen::AngleAxisf(v[1], Vec3::UnitY()) *
           Eigen::AngleAxisf(v[2], Vec3::UnitZ());
}

void f_quat() {
}

void f_affine() {
    std::cout << "=== f_affine() ===" << std::endl;

    {
        Translation3f T = Translation3f(1.0f, 2.0f, 3.0f);
        Affine3f affine = Affine3f(T);
        Matrix4f M = affine.matrix();
        tt::f_print_mat4_col("T = ", M);
    }

    {
        Quaternionf R = Quaternionf(AngleAxisf(tt::ToRadian(90.0), Vector3f::UnitX()));
        Affine3f affine = Affine3f(R);
        Matrix4f M = affine.matrix();
        tt::f_print_mat4_col("R = ", M);
    }

    {
        DiagonalMatrix<float, 3> S = Scaling(1.0f, 2.0f, 3.0f);
        Affine3f affine = Affine3f(S);
        Matrix4f M = affine.matrix();
        tt::f_print_mat4_col("S = ", M);
    }
}

void f_conv() {
    std::cout << "=== f_conv() ===" << std::endl;

    Translation3f T = Translation3f(1000.0f, 1000.0f, 0.0f);
    Quaternionf R = Quaternionf(AngleAxisf(tt::ToRadian(90.0), Vector3f::UnitX()));
    DiagonalMatrix<float, 3> S = Scaling(1.0f, 1.0f, 1.0f);

    Affine3f M;
    M = T * R * S;

    Matrix4f m = M.matrix();
    tt::f_print_mat4_col("m = ", m);

    Vector4f v = {1, 0, 0, 1};
    Vector4f v2 = m * v;
    tt::f_print_vec4("v2 = ", v2);
}

void f_transform() {
    std::cout << "=== f_transform() ===" << std::endl;

    Translation3f T = Translation3f(1.0f, 2.0f, 3.0f);
    Quaternionf R = Quaternionf(AngleAxisf(tt::ToRadian(90.0), Vector3f::UnitX()));
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

    tt::f_print_mat("v = ", v);
    tt::f_print_val("size = ", v.size());
    tt::f_print_val("rows = ", v.rows());
    tt::f_print_val("cols = ", v.cols());
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

    tt::f_print_mat("m = ", m);
    tt::f_print_val("size = ", m.size());
    tt::f_print_val("rows = ", m.rows());
    tt::f_print_val("cols = ", m.cols());

    m.resize(4, 3);
    std::cout << "m.resize(4, 3)" << std::endl;

    tt::f_print_mat("m = ", m);
    tt::f_print_val("size = ", m.size());
    tt::f_print_val("rows = ", m.rows());
    tt::f_print_val("cols = ", m.cols());
}

void f_decompose(const Matrix4f& M, Vector3f& trans, Vector3f& scale, Quaternionf& quat) {
    auto&& affine = Affine3f(M);
    Matrix3f S;
    Matrix3f R;
    affine.computeScalingRotation(&S, &R);
    trans[0] = M(12);
    trans[1] = M(13);
    trans[2] = M(14);
    scale = S.diagonal();
    quat = Quaternionf(R);
}

void f_color() {
    Vector3f color_srgb = {0.8, 0.8, 0.8};
    Vector3f color_linear = color_srgb.array().pow(2.2);
}

int main(int argc, char *argv[]) {
    //f_memory_order();
    //f_constructor();
    //f_vec3();
    f_mat3();
    //f_affine();
    //f_conv();
    //f_transform();
    //f_vecx();
    //f_matx();
    //f_decompose();
    //f_color();
    return 0;
}

