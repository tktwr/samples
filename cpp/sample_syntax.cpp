// *memo_sample_syntax*
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

void func() {
}

int main(int argc, char *argv[]) {
    int i;

    // if
    cout << "[if]" << endl;
    i = 0;
    if (i == 0) {
        cout << i << endl;
    } else if (i == 1) {
        cout << i << endl;
    } else {
        cout << i << endl;
    }
    cout << endl;

    // for
    cout << "[for]" << endl;
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
    cout << endl;

    // switch
    cout << "[switch]" << endl;
    i = 0;
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
    cout << endl;

    // while
    cout << "[while]" << endl;
    i = 5;
    while (--i) {
        cout << i << " ";
    }
    cout << endl;

    cout << "[enum]" << endl;
    for (i = SampleEnum::Type0; i < SampleEnum::NumTypes; i++) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
