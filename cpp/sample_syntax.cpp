// *memo_cpp.syntax*
#include <iostream>

using namespace std;

class SampleClass {
public:
    SampleClass() {}
    ~SampleClass() {}

private:
    int i;
    float f;
};

enum SampleEnum {
    Type0 = 0,
    Type1,
    Type2,
    Type3,
    Type4,
    NumTypes
};

void f_if() {
    cout << "[if]" << endl;

    int i = 0;
    if (i == 0) {
        cout << i << endl;
    } else if (i == 1) {
        cout << i << endl;
    } else {
        cout << i << endl;
    }
}

void f_for() {
    cout << "[for]" << endl;

    int i;
    for (i = 0; i < 5; i++) {
        cout << i << " ";
    }
    cout << endl;

    cout << "[for xy]" << endl;
    int nx = 5;
    int ny = 3;
    int x, y;
    for (y = 0; y < ny; y++) {
        for (x = 0; x < nx; x++) {
            cout << "(" << x << ", " << y << ") ";
        }
        cout << endl;
    }
}

void f_switch() {
    cout << "[switch]" << endl;

    int i = 0;
    switch (i) {
    case 0:
        cout << i << endl;
        break;
    case 1:
        cout << i << endl;
        break;
    default:
        break;
    }
}

void f_while() {
    cout << "[while]" << endl;

    int i = 5;
    while (--i) {
        cout << i << " ";
    }
    cout << endl;
}

void f_enum() {
    cout << "[enum]" << endl;

    int i;
    for (i = SampleEnum::Type0; i < SampleEnum::NumTypes; i++) {
        cout << i << " ";
    }
    cout << endl;
}

int main(int argc, char *argv[]) {
    f_if();
    f_for();
    f_switch();
    f_while();
    f_enum();

    return 0;
}
