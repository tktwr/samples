#include <iostream>
#include <glm/glm.hpp>
#include <Eigen/Core>
#include <tt/ext/glm/glm_util.h>
#include <tt/ext/eigen/eigen_util.h>

using namespace std;

void f_mat() {
    glm::vec3 v = {1, 2, 3};
    tt::f_print_vec3("glm::vec3 = ", v);

    glm::mat3 m = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    tt::f_print_mat3_row("glm::mat3 = ", m);

    Eigen::Vector3f v1 = {1, 2, 3};
    tt::f_print_vec3("Eigen::Vector3f = ", v1);

    Eigen::Matrix3f m1;
    m1 << 1, 2, 3, 4, 5, 6, 7, 8, 9;
    tt::f_print_mat3_row("Eigen::Matrix3f = ", m1);
}

int main(int argc, char *argv[]) {
    f_mat();
    return 0;
}

