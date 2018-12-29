// *memo_cpp.11*
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <vector>
#include <array>
#include <limits>

using namespace std;

// *memo_cpp.limits*
void f_limits() {
    cout << "[limits]" << endl;

    cout << "unsigned char  max: " << int(std::numeric_limits<unsigned char>::max()) << endl;
    cout << "unsigned short max: " << std::numeric_limits<unsigned short>::max() << endl;
    cout << "unsigned int   max: " << std::numeric_limits<unsigned int>::max() << endl;
    cout << "float          max: " << std::numeric_limits<float>::max() << endl;
    cout << "double         max: " << std::numeric_limits<double>::max() << endl;
}

// *memo_cpp.initializer*
void f_initializer() {
    cout << "[initializer]" << endl;

    {
        //std::array<int, 4> ar(1, 2, 3, 4); // No such a constructor
    }

    {
        int a[]{1, 2, 3, 4};
        std::array<int, 4> ar{1, 2, 3, 4};
        std::vector<int> vec{1, 2, 3, 4};
        std::map<string, int> m{{"aaa", 10}, {"bbb", 20}, {"ccc", 30}};
    }

    {
        int a[] = {1, 2, 3, 4};
        std::array<int, 4> ar = {1, 2, 3, 4};
        std::vector<int> vec = {1, 2, 3, 4};
        std::map<string, int> m = {{"aaa", 10}, {"bbb", 20}, {"ccc", 30}};

        cout << "sizeof(a) : " << sizeof(a) << endl;
        cout << "ar.size() : " << ar.size() << endl;
        cout << "vec.size() : " << vec.size() << endl;
        cout << "m.size() : " << m.size() << endl;
    }

    {
        std::vector<int> a(4);
        cout << "a.size() : " << a.size() << endl;
        std::vector<int> b{4};
        cout << "b.size() : " << b.size() << endl;
    }
}

// *memo_cpp.auto*
void f_auto_type() {
    cout << "[auto_type]" << endl;

    std::vector<int> vec{1, 2, 3, 4, 5};

    for (std::vector<int>::const_iterator itr = vec.begin(); itr != vec.end(); ++itr) {
        cout << *itr << " ";
    }
    cout << endl;

    for (auto itr = std::begin(vec); itr != std::end(vec); ++itr) {
        cout << *itr << " ";
    }
    cout << endl;
}

// *memo_cpp.for*
void f_range_based_for_loop() {
    cout << "[range_based_for_loop]" << endl;

    std::vector<int> vec{1, 2, 3, 4, 5};

    for (int &x : vec) {
        cout << x << " ";
    }
    cout << endl;
}

// *memo_cpp.unique_ptr*
void f_unique_ptr() {
    cout << "[unique_ptr]" << endl;

    unique_ptr<int> ptr(new int(1));
    unique_ptr<int> ptr2 = std::move(ptr);

    if (ptr) {
        cout << "ptr : true" << endl;
    } else {
        cout << "ptr : false" << endl;
    }

    if (ptr2) {
        cout << "ptr2 : true" << endl;
    } else {
        cout << "ptr2 : false" << endl;
    }

    int* p = nullptr;
    p = ptr2.get();

    // explicit delete the pointer
    ptr2.reset();
}

// *memo_cpp.unique_ptr_array*
void f_unique_ptr_array() {
    cout << "[unique_ptr_array]" << endl;

    unique_ptr<int[]> ptr(new int[10]);
}

// *memo_cpp.shared_ptr*
void f_shared_ptr() {
    cout << "[shared_ptr]" << endl;

    shared_ptr<int> ptr(new int(1));
    {
        shared_ptr<int> ptr2 = ptr;
        cout << "value : " << *ptr2 << endl;
        cout << "use_count : " << ptr2.use_count() << endl;
    }
    cout << "value : " << *ptr << endl;
    cout << "use_count : " << ptr.use_count() << endl;
}

// *memo_cpp.weak_ptr*
void f_weak_ptr() {
    cout << "[weak_ptr]" << endl;
}

int main(int argc, char *argv[]) {
    f_limits();
    f_initializer();
    f_auto_type();
    f_range_based_for_loop();
    f_unique_ptr();
    f_unique_ptr_array();
    f_shared_ptr();
    f_weak_ptr();

    return 0;
}
