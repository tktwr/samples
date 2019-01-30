#include <iostream>
#include <memory>

using namespace std;

class ABase {
public:
    ABase() {
        cout << "ABase::ABase()" << endl;
    }
    virtual ~ABase() {
        cout << "ABase::~ABase()" << endl;
    }
    void hello() const {
        cout << "ABase::hello() " << this << endl;
    }
};

class A : public ABase {
public:
    A() {
        cout << "A::A()" << endl;
    }
    virtual ~A() {
        cout << "A::~A()" << endl;
    }
};

class B {
public:
    void hello() const {
        cout << "B::hello() " << this << endl;
    }
};

void f_constructor() {
    cout << "=== f_constructor()" << endl;
    A a;     // OK
    //A a(); // NG
    //A a{}; // OK
    {
        A* p = new A();
        delete p;
    }
}

void f_ptr() {
    cout << "=== f_ptr()" << endl;
    {
        ABase* p0 = new A();

        A* p = dynamic_cast<A*>(p0);
        if (p) {
            p->hello();
        }

        try {
            A& a = dynamic_cast<A&>(*p0);
            a.hello();

            const A& ca = dynamic_cast<const A&>(*p0);
            ca.hello();

            const B& cb = dynamic_cast<const B&>(*p0);
            cb.hello();
        } catch (std::bad_cast& e) {
            std::cerr << e.what() << std::endl;
        }

        delete p0;
    }
}

void f_shared_ptr() {
    cout << "=== f_shared_ptr()" << endl;
    {
        std::shared_ptr<A> p = std::make_shared<A>();
        std::shared_ptr<A> p1 = p;
    }
}

int main(int argc, char *argv[]) {
    f_constructor();
    f_ptr();
    f_shared_ptr();
    return 0;
}

