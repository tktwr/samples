// *memo_sample_c++*
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <vector>

using namespace std;

void initializer() {
    cout << "initializer()" << endl;

    {
        int a[]{1, 2, 3, 4};
        std::vector<int> vec{1, 2, 3, 4};
        std::map<string, int> m{{"aaa", 10}, {"bbb", 20}, {"ccc", 30}};
        cout << "sizeof(a) : " << sizeof(a) << endl;
    }

    {
        int a[] = {1, 2, 3, 4};
        std::vector<int> vec = {1, 2, 3, 4};
        std::map<string, int> m = {{"aaa", 10}, {"bbb", 20}, {"ccc", 30}};
        cout << "sizeof(a) : " << sizeof(a) << endl;
    }

    {
        std::vector<int> a(4);
        cout << a.size() << endl;
        std::vector<int> b{4};
        cout << b.size() << endl;
    }
}

void auto_type() {
    cout << "auto_type()" << endl;

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

void range_based_for_loop() {
    cout << "range_based_for_loop()" << endl;

    std::vector<int> vec{1, 2, 3, 4, 5};

    for (int &x : vec) {
        cout << x << " ";
    }
    cout << endl;
}

void pointer() {
    cout << "pointer()" << endl;

    int *p = nullptr;

    {
        cout << "unique_ptr" << endl;
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

        int *p = ptr2.get();

        // explicit delete the pointer
        ptr2.reset();
    }

    {
        unique_ptr<int[]> ptr(new int[10]);
    }

    {
        cout << "shared_ptr" << endl;
        shared_ptr<int> ptr(new int(1));
        {
            shared_ptr<int> ptr2 = ptr;
            cout << "value : " << *ptr2 << endl;
            cout << "use_count : " << ptr2.use_count() << endl;
        }
        cout << "value : " << *ptr << endl;
        cout << "use_count : " << ptr.use_count() << endl;
    }

    /*
    {
        weak_ptr<int> ptr(new int(1));
    }
    */
}

int main(int argc, char *argv[]) {
    initializer();
    auto_type();
    range_based_for_loop();
    pointer();

    return 0;
}
