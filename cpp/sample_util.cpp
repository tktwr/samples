#include <iostream>
#include <map>
#include <vector>
#include <initializer_list>

using namespace std;

enum EnumType {
    EN_NONE = 0,
    EN_APPLE,
    EN_ORANGE,
    EN_BANANA,
    EN_SIZE
};

template<class K, class V>
class BiMap {
public:
    using value_type = std::pair<const K, V>;

    BiMap() {}
    BiMap(std::initializer_list<value_type> init_list)
    : m_k2v(init_list.begin(), init_list.end()) {
        for (auto&& x : init_list) {
            m_v2k[x.second] = x.first;
        }
    }

    void setValue(const K& key, const V& val) {
        m_k2v[key] = val;
        m_v2k[val] = key;
    }
    void setKey(const V& val, const K& key) {
        m_v2k[val] = key;
        m_k2v[key] = val;
    }

    V getValue(const K& key) {
        return m_k2v[key];
    }
    K getKey(const V& val) {
        return m_v2k[val];
    }

private:
    std::map<K, V> m_k2v;
    std::map<V, K> m_v2k;
};

int main(int argc, char *argv[]) {
#if 0
    BiMap<EnumType, std::string> idname;
    idname.setValue(EN_NONE, "None");
    idname.setValue(EN_APPLE, "Apple");
    idname.setValue(EN_ORANGE, "Orange");
    idname.setValue(EN_BANANA, "Banana");
#else
    // use initializer_list
    BiMap<EnumType, std::string> idname = {
        {EN_NONE, "None"},
        {EN_APPLE, "Apple"},
        {EN_ORANGE, "Orange"},
        {EN_BANANA, "Banana"},
    };
#endif

    for (int i = 0; i < EN_SIZE; ++i) {
        std::cout << i << " " << idname.getValue(EnumType(i)) << std::endl;
    }

    std::vector<std::string> names = {
        "Banana",
        "Orange",
        "Apple",
    };
    for (auto&& name : names) {
        std::cout << name << " " << idname.getKey(name) << std::endl;
    }

    return 0;
}

