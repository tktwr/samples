// *memo_cpp.class*
#include <memory>
#include <vector>
#include <iostream>

class ABase {
public:
    ABase(int val = 0) {
        m_val = val;
        std::cout << "ABase::ABase()" << std::endl;
    }
    virtual ~ABase() {
        std::cout << "ABase::~ABase()" << std::endl;
    }
    void hello() const {
        std::cout << "ABase::hello() " << this << std::endl;
    }
    int m_val = 0;
};

class A : public ABase {
public:
    A(int val = 0) : ABase(val) {
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

void f_emplace_back() {
    std::cout << "=== f_emplace_back()" << std::endl;
    std::vector<A> vec;
    vec.reserve(5);
    std::cout << "=== push_back()" << std::endl;
    vec.push_back(1);
    std::cout << "=== emplace_back()" << std::endl;
    vec.emplace_back(2);
    std::cout << "===" << std::endl;
}

int main(int argc, char *argv[]) {
    f_constructor();
    f_ptr();
    f_shared_ptr();
    f_emplace_back();
    return 0;
}

