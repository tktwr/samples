#include <functional>
#include <iostream>
#include <vector>

using namespace std;

class Image {
public:
    Image(int w, int h) {
        m_w = w;
        m_h = h;
        m_data.resize(m_w * m_h);
    }
    int w() const { return m_w; }
    int h() const { return m_h; }
    int getValue(int x, int y) const { return m_data[y * m_w + x]; }
    void setValue(int x, int y, int val) { m_data[y * m_w + x] = val; }

private:
    int m_w, m_h;
    std::vector<int> m_data;
};

void f_image_foreach(Image &image, const std::function<void(Image &, int, int)> &func) {
    for (int y = 0; y < image.h(); y++) {
        for (int x = 0; x < image.w(); x++) {
            func(image, x, y);
        }
    }
}

void f_image_print(Image &image) {
    f_image_foreach(image, [](Image &image, int x, int y) {
        cout << image.getValue(x, y) << " ";
        if (x == image.w() - 1)
            cout << endl;
    });
    cout << flush;
}

int main(int argc, char *argv[]) {
    Image image(10, 5);

    f_image_foreach(image, [](Image &image, int x, int y) {
        image.setValue(x, y, x);
    });
    f_image_print(image);
    cout << endl;

    f_image_foreach(image, [](Image &image, int x, int y) {
        int val = image.getValue(x, y);
        val++;
        image.setValue(x, y, val);
    });
    f_image_print(image);
    cout << endl;

    return 0;
}
