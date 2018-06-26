// *memo_array*
#include <iostream>
#include <vector>
#include <glm/glm.hpp>
#include "../util/array.h"
#include "../util/time.h"

using namespace std;

int main(int argc, char *argv[]) {
    int w, h;
    w = 3000;
    h = 2000;

    tt::Time t;
    for (int i=0; i<3; i++) {
        t.start();
        tt::Array<glm::vec3> ar;
        ar.resize(w * h);
        //ar.clear();
        t.end();
        cout << "time: ar.resize: " << t.getElapsedMSec() << " ms" << endl;
        cout << "size: ar.size: " << ar.size() << endl;
        cout << endl;

        t.start();
        std::vector<glm::vec3> vec;
        vec.resize(w * h);
        t.end();
        cout << "time: vec.resize: " << t.getElapsedMSec() << " ms" << endl;
        cout << "size: vec.size: " << vec.size() << endl;
        cout << "size: vec.capacity: " << vec.capacity() << endl;
        cout << endl;

        t.start();
        std::vector<glm::vec3> vec2;
        vec2.reserve(w * h);
        //vec2.resize(w * h);
        t.end();
        cout << "time: vec2.resize: " << t.getElapsedMSec() << " ms" << endl;
        cout << "size: vec2.size: " << vec2.size() << endl;
        cout << "size: vec2.capacity: " << vec2.capacity() << endl;
        cout << endl;
    }


    return 0;
}

