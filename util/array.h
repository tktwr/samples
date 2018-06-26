#ifndef tt_array_h
#define tt_array_h

namespace tt {

template<class T>
class Array {
public:
    typedef T data_type;

    Array() : m_data(0), m_size(0) {}
    Array(size_t size) : m_data(0), m_size(0) { resize(size); }
    virtual ~Array() { destroy(); }

    void resize(size_t size) {
        destroy();
        if (size > 0) {
            m_data = new T[size];
            m_size = size;
        }
    }

    void clear(const T& v = T()) { for (size_t i=0; i<m_size; i++) m_data[i] = v; }

    size_t size() const { return m_size; }
    size_t sizeOfDataType() const { return sizeof(data_type); }

    const T* data() const { return m_data; }
          T* data()       { return m_data; }

    const T& operator[](size_t i) const { return m_data[i]; }
          T& operator[](size_t i)       { return m_data[i]; }

private:
    void destroy() {
        if (m_data) delete [] m_data;
        m_data = 0;
        m_size = 0;
    }

    T* m_data;
    size_t m_size;
};

}  // namespace tt

#endif  // tt_array_h

