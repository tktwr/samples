// *memo_cpp.cereal*
#include <cereal/cereal.hpp>
#include <cereal/archives/json.hpp>
#include <cereal/types/vector.hpp>
#include <fstream>
#include <string>

class Config {
public:
    template <class Archive>
    void serialize(Archive& ar) {
        ar(
            cereal::make_nvp("fname0", m_fname0),
            cereal::make_nvp("fname1", m_fname1),
            cereal::make_nvp("int0", m_int0),
            cereal::make_nvp("int1", m_int1),
            cereal::make_nvp("float0", m_float0),
            cereal::make_nvp("float1", m_float1),
            cereal::make_nvp("vec", m_vec)
        );
    }

    std::string m_fname0;
    std::string m_fname1;
    int m_int0;
    int m_int1;
    float m_float0;
    float m_float1;
    std::vector<int> m_vec;
};

void f_load(const std::string& fname, Config& cfg) {
    std::ifstream is(fname);
    cereal::JSONInputArchive ar(is);
    ar(cereal::make_nvp("config", cfg));
}

void f_save(const std::string& fname, const Config& cfg) {
    std::ofstream os(fname);
    cereal::JSONOutputArchive ar(os);
    ar(cereal::make_nvp("config", cfg));
}

int main() {
    {
        Config cfg;
        cfg.m_fname0 = "file0.txt";
        cfg.m_fname1 = "file1.txt";
        cfg.m_int0 = 0;
        cfg.m_int1 = 1;
        cfg.m_float0 = 0.5;
        cfg.m_float1 = 1.0;
        cfg.m_vec = {1, 2, 3, 4, 5};

        f_save("test0.json", cfg);
    }

    {
        Config cfg;

        f_load("test0.json", cfg);

        cfg.m_int0 += 1;
        cfg.m_int1 += 1;
        cfg.m_float0 += 1;
        cfg.m_float1 += 1;
        int sz = cfg.m_vec.size();
        for (int i=0; i<sz; i++) {
            cfg.m_vec[i] += 1;
        }

        f_save("test1.json", cfg);
    }

    return 0;
}

