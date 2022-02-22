// *memo_cpp.stl*
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <stdexcept>

using namespace std;

template<class T>
void f_print(const std::string& text, const T& container) {
    std::cout << text;
    for (auto&& x : container) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
}

// *memo_cpp.stl.vector*
void f_vector_init() {
    std::vector<int> vec = {0, 1, 2, 3, 4, 5};
    f_print("vec = ", vec);
}

void f_vector_add() {
    std::vector<int> vec;
    vec.reserve(10);
    vec.push_back(0);
    vec.emplace_back(1);
    f_print("vec = ", vec);
}

void f_vector_cat() {
    std::vector<int> v0 = {0, 1};
    std::vector<int> v1 = {2, 3};
    v0.insert(v0.end(), v1.begin(), v1.end());
    v0.insert(v0.end(), {4, 5});

    f_print("v0 = ", v0);
}

void f_vector_sample() {
    std::vector<int> vec = {0, 1, 2, 3, 4, 5};
    std::vector<int> vec0;
    std::vector<int> vec1;

    for (auto&& itr = vec.begin(); itr != vec.end(); ++itr) {
        if ((*itr % 2) == 0) {
            vec0.push_back(*itr);
        } else {
            vec1.push_back(*itr);
        }
    }

    std::vector<int> vec_out;
    vec_out.insert(vec_out.end(), vec0.begin(), vec0.end());
    vec_out.insert(vec_out.end(), vec1.begin(), vec1.end());

    f_print("vec = ", vec);
    f_print("vec0 = ", vec0);
    f_print("vec1 = ", vec1);
    f_print("vec_out = ", vec_out);
}

// *memo_cpp.stl.list*
void f_list_init() {
    std::list<int> l = {0, 1, 2, 3, 4, 5};
    f_print("l = ", l);
}

// *memo_cpp.stl.map*
void f_map() {
    std::map<std::string, int> m = {
        {"aaa", 10},
        {"bbb", 11},
        {"ccc", 12},
    };
    std::cout << m["aaa"] << std::endl;
    std::cout << m["bbb"] << std::endl;
    std::cout << m["ccc"] << std::endl;

    try {
        std::cout << m.at("ddd") << std::endl;
    } catch(std::out_of_range&) {
        std::cout << "exception std::out_of_range" << std::endl;
    }
}

int main(int argc, char *argv[]) {
    //f_vector_init();
    //f_vector_add();
    //f_vector_cat();
    //f_vector_sample();
    //f_list_init();
    f_map();
    return 0;
}

