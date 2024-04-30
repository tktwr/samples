// *memo:sample:cpp.11*
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <vector>
#include <array>
#include <limits>
#include <chrono>
#include <ctime>
#include <iomanip>  // put_time

using namespace std;

void f_title(const std::string& title) {
    cout << "=== [" << title << "] ===" << endl;
}

//-------------------------------------------------------------------------

// *memo:sample:cpp.11.constexpr*
constexpr int f_val() { return 10; }

void f_constexpr() {
    f_title("constexpr");

    constexpr int a = 1;
    constexpr int b = f_val();
    std::cout << "a: " << a << std::endl;
    std::cout << "b: " << b << std::endl;
}

// *memo:sample:cpp.11.datetime*
void f_datetime() {
    f_title("datetime");

    auto now = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(now);
    std::cout << "ctime(): " << std::ctime(&end_time) << std::endl;

    std::time_t t = std::time(nullptr);
    std::tm* lt = std::localtime(&t);
    std::cout << std::put_time(lt, "%Y%m%d-%H%M%S") << std::endl;
}

// *memo:sample:cpp.11.limits*
void f_limits() {
    f_title("limits");

    cout << "unsigned char  max: " << int(std::numeric_limits<unsigned char>::max()) << endl;
    cout << "unsigned short max: " << std::numeric_limits<unsigned short>::max() << endl;
    cout << "unsigned int   max: " << std::numeric_limits<unsigned int>::max() << endl;
    cout << "float          max: " << std::numeric_limits<float>::max() << endl;
    cout << "double         max: " << std::numeric_limits<double>::max() << endl;
}

// *memo:sample:cpp.11.initializer*
void f_initializer() {
    f_title("initializer");

    {
        //std::array<int, 4> ar(1, 2, 3, 4); // No such a constructor
    }

    {
        int i {1};
        int a[]{1, 2, 3, 4};
        struct S { int a, b; };
        S s {1, 2};
        std::array<int, 4> ar{1, 2, 3, 4};
        std::vector<int> vec{1, 2, 3, 4};
        std::map<string, int> m{{"aaa", 10}, {"bbb", 20}, {"ccc", 30}};
        std::pair<int, float> p {1, 2.3};
    }

    {
        int i = {1};
        int a[] = {1, 2, 3, 4};
        struct S { int a, b; };
        S s = {1, 2};
        std::array<int, 4> ar = {1, 2, 3, 4};
        std::vector<int> vec = {1, 2, 3, 4};
        std::map<string, int> m = {{"aaa", 10}, {"bbb", 20}, {"ccc", 30}};
        std::pair<int, float> p = {1, 2.3};

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

// *memo:sample:cpp.11.auto*
void f_auto_type() {
    f_title("auto_type");

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

// *memo:sample:cpp.11.universal_reference*
void f_universal_reference() {
    f_title("universal_reference");

    int i = 1;
    auto&& a = i; // int&  a;と等価 (左辺値参照型)
    auto&& b = 1; // int&& b;と等価 (右辺値参照型)

    std::vector<int> vec{1, 2, 3, 4, 5};
    for (auto&& x : vec) {}
}

// *memo:sample:cpp.11.range_for*
void f_range_for() {
    f_title("range_for");

    std::vector<int> vec{1, 2, 3, 4, 5};

    for (auto x : vec) { x = 1; }
    for (auto& x : vec) { x = 1; }
    for (const auto& x : vec) {}
    for (auto&& x : vec) { x = 1; }
}

// *memo:sample:cpp.11.unique_ptr*
void f_unique_ptr() {
    f_title("unique_ptr");

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

// *memo:sample:cpp.11.unique_ptr_array*
void f_unique_ptr_array() {
    f_title("unique_ptr_array");

    unique_ptr<int[]> ptr(new int[10]);
}

// *memo:sample:cpp.11.shared_ptr*
void f_shared_ptr() {
    f_title("shared_ptr");

    shared_ptr<int> ptr(new int(1));
    {
        shared_ptr<int> ptr2 = ptr;
        cout << "value : " << *ptr2 << endl;
        cout << "use_count : " << ptr2.use_count() << endl;
    }
    cout << "value : " << *ptr << endl;
    cout << "use_count : " << ptr.use_count() << endl;
}

// *memo:sample:cpp.11.weak_ptr*
void f_weak_ptr() {
    f_title("weak_ptr");
}

// *memo:sample:cpp.11.lambda*
void f_lambda() {
    f_title("lambda");

    auto plus = [](int a, int b) { return a + b; };
    int result = plus(2, 3); // result == 5
}

int main(int argc, char *argv[]) {
    f_constexpr();
    f_datetime();
    f_limits();
    f_initializer();
    f_auto_type();
    f_universal_reference();
    f_range_for();
    f_unique_ptr();
    f_unique_ptr_array();
    f_shared_ptr();
    f_weak_ptr();
    f_lambda();

    return 0;
}
