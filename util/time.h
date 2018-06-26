#ifndef tt_time_h
#define tt_time_h

#include <chrono>

namespace tt {

class Time {
public:
    Time() {}

    void start() { m_start = std::chrono::system_clock::now(); }
    void end() { m_end = std::chrono::system_clock::now(); }

    float getElapsedMSec() const {
        return std::chrono::duration_cast<std::chrono::milliseconds>(m_end-m_start).count();
    }

private:
    std::chrono::system_clock::time_point m_start, m_end;
};

}  // namespace tt

#endif  // tt_time_h

