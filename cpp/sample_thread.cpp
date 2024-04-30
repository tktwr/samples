// *memo:sample:cpp.11.thread*
#include <chrono>
#include <iostream>
#include <mutex>
#include <string>
#include <thread>

using namespace std;

void print(const std::string &str, int val) {
    static std::mutex mtx;
    std::lock_guard<std::mutex> lock(mtx);
    cout << str << ": " << val << endl;
}

int main() {
    cout << "hardware_concurrency: " << std::thread::hardware_concurrency() << endl;

    std::thread th1([]() {
        int x = 0;
        for (int i = 0; i < 15; i++) {
            print("th1", x);
            std::this_thread::sleep_for(std::chrono::seconds(1));
            x++;
        }
    });

    std::thread th2([]() {
        int y = 0;
        for (int i = 0; i < 5; i++) {
            print("    th2", y);
            std::this_thread::sleep_for(std::chrono::seconds(3));
            y++;
        }
    });

    th1.join();
    th2.join();

    return 0;
}
