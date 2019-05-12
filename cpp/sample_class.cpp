#include <memory>
#include <iostream>

class ABase {
public:
    ABase() {
        std::cout << "ABase::ABase()" << std::endl;
    }
    virtual ~ABase() {
        std::cout << "ABase::~ABase()" << std::endl;
    }
    void hello() const {
        std::cout << "ABase::hello() " << this << std::endl;
    }
};

class A : public ABase {
public:
    A() {
        std::cout << "A::A()" << std::endl;
    }
    virtual ~A() {
        std::cout << "A::~A()" << std::endl;
    }
};

class B {
public:
    void hello() const {
        std::cout << "B::hello() " << this << std::endl;
    }
};

void f_constructor() {
    std::cout << "=== f_constructor()" << std::endl;
    A a;     // OK
    //A a(); // NG
    //A a{}; // OK
    {
        A* p = new A();
        delete p;
    }
}

void f_ptr() {
    std::cout << "=== f_ptr()" << std::endl;
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
    std::cout << "=== f_shared_ptr()" << std::endl;
    {
        std::shared_ptr<int> p = std::make_shared<int>(100);
    }
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

