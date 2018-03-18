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
    }

    {
        int a[] = {1, 2, 3, 4};
        std::vector<int> vec = {1, 2, 3, 4};
        std::map<string, int> m = {{"aaa", 10}, {"bbb", 20}, {"ccc", 30}};
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
    int *p = nullptr;

    {
        unique_ptr<int> ptr(new int(1));
        unique_ptr<int> ptr2 = std::move(ptr);

        cout << "ptr" << endl;
        if (ptr) {
            cout << "true" << endl;
        } else {
            cout << "false" << endl;
        }

        cout << "ptr2" << endl;
        if (ptr2) {
            cout << "true" << endl;
        } else {
            cout << "false" << endl;
        }

        int *p = ptr2.get();

        // explicit delete the pointer
        ptr2.reset();
    }

    /*
    {
        shared_ptr<int> ptr(new int(1));
    }

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
