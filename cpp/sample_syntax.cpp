// *memo:sample:cpp.syntax*
#include <iostream>

using namespace std;

// ----------------------------------------------------
// *memo:sample:cpp.syntax.if*
void f_if() {
    cout << "[if]" << endl;

    int i = 0;
    if (i == 0) {
        cout << "i == 0" << endl;
    } else if (i == 1) {
        cout << "i == 1" << endl;
    } else {
        cout << "else" << endl;
    }
}

// ----------------------------------------------------
// *memo:sample:cpp.syntax.for*
void f_for_i() {
    cout << "[for]" << endl;

    int i;
    for (i = 0; i < 5; i++) {
        cout << i << " ";
    }
    cout << endl;
}

// ----------------------------------------------------
// *memo:sample:cpp.syntax.for_xy*
void f_for_xy() {
    cout << "[for xy]" << endl;

    int nx = 4;
    int ny = 3;
    int x, y;
    for (y = 0; y < ny; y++) {
        for (x = 0; x < nx; x++) {
            cout << "(" << x << ", " << y << ") ";
        }
        cout << endl;
    }
}

// ----------------------------------------------------
// *memo:sample:cpp.syntax.switch*
void f_switch() {
    cout << "[switch]" << endl;

    int i = 0;
    switch (i) {
    case 0:
        cout << "i == 0" << endl;
        break;
    case 1:
        cout << "i == 1" << endl;
        break;
    default:
        break;
    }
}

// ----------------------------------------------------
// *memo:sample:cpp.syntax.while*
void f_while() {
    cout << "[while]" << endl;

    int i = 5;
    while (--i) {
        cout << i << " ";
    }
    cout << endl;
}

// ----------------------------------------------------
// *memo:sample:cpp.syntax.enum*
void f_enum() {
    cout << "[enum]" << endl;

    enum SampleEnum {
        Type0 = 0,
        Type1,
        Type2,
        Type3,
        Type4,
        NumTypes
    };

    int i;
    for (i = SampleEnum::Type0; i < SampleEnum::NumTypes; i++) {
        cout << i << " ";
    }
    cout << endl;
}

// ----------------------------------------------------
// *memo:sample:cpp.syntax.class*
void f_class() {
    cout << "[class]" << endl;

    class SampleClass {
    public:
        SampleClass() {
            cout << "constructor called" << endl;
        }
        ~SampleClass() {
            cout << "destructor called" << endl;
        }

    private:
        int i;
        float f;
    };

    SampleClass c;
}

// ----------------------------------------------------
int main(int argc, char *argv[]) {
    f_if();
    f_for_i();
    f_for_xy();
    f_switch();
    f_while();
    f_enum();
    f_class();

    return 0;
}
