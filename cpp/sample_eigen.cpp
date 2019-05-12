// *memo_cpp.eigen*
#include <iostream>
#include <Eigen/Dense>

using namespace Eigen;
using namespace std;

void f_init_matx() {
    std::cout << "=== f_init_matx()" << std::endl;

    MatrixXd m(2, 3);

    m(0, 0) = 1;
    m(0, 1) = 2;
    m(0, 2) = 3;

    m(1, 0) = 4;
    m(1, 1) = 5;
    m(1, 2) = 6;

    std::cout << "m = " << std::endl;
    std::cout << m << std::endl;
    std::cout << "rows = " << m.rows() << std::endl;
    std::cout << "cols = " << m.cols() << std::endl;
}

void f_init_mat3() {
    std::cout << "=== f_init_mat3()" << std::endl;

    Matrix3f m;

    m << 1, 2, 3,
         4, 5, 6,
         7, 8, 9;

    std::cout << "m = " << std::endl;
    std::cout << m << std::endl;
}

void f_resize_matx() {
    std::cout << "=== f_resize_matx()" << std::endl;

    MatrixXd m;
    m.resize(4, 3);
    std::cout << "m.resize(4, 3)" << std::endl;
    std::cout << "size = " << m.size() << std::endl;
    std::cout << "rows = " << m.rows() << std::endl;
    std::cout << "cols = " << m.cols() << std::endl;
}

void f_resize_vecx() {
    std::cout << "=== f_resize_vecx()" << std::endl;

    VectorXd v;
    v.resize(5);
    std::cout << "v.resize(5)" << std::endl;
    std::cout << "size = " << v.size() << std::endl;
    std::cout << "rows = " << v.rows() << std::endl;
    std::cout << "cols = " << v.cols() << std::endl;
}

void f1() {
    std::cout << "=== f1()" << std::endl;

    MatrixXd m = MatrixXd::Random(3,3);
    m = (m + MatrixXd::Constant(3,3,1.2)) * 50;
    cout << "m =" << endl << m << endl;
    VectorXd v(3);
    v << 1, 2, 3;
    cout << "m * v =" << endl << m * v << endl;
}
void f2() {
    std::cout << "=== f2()" << std::endl;

    Matrix3d m = Matrix3d::Random();
    m = (m + Matrix3d::Constant(1.2)) * 50;
    cout << "m =" << endl << m << endl;
    Vector3d v(1,2,3);
    cout << "m * v =" << endl << m * v << endl;
}

int main(int argc, char *argv[]) {
    f_init_matx();
    f_init_mat3();
    f_resize_matx();
    f_resize_vecx();
    f1();
    f2();
    return 0;
}

