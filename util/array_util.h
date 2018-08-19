#ifndef array_util_h
#define array_util_h

#include <array>
#include <iostream>

template<typename T>
inline std::istream& operator>>(std::istream& is, std::array<T, 2>& ar) {
	return is >> ar[0] >> ar[1];
}

template<typename T>
inline std::ostream& operator<<(std::ostream& os, const std::array<T, 2>& ar) {
	return os << ar[0] << " " << ar[1];
}

template<typename T>
inline std::istream& operator>>(std::istream& is, std::array<T, 3>& ar) {
	return is >> ar[0] >> ar[1] >> ar[2];
}

template<typename T>
inline std::ostream& operator<<(std::ostream& os, const std::array<T, 3>& ar) {
	return os << ar[0] << " " << ar[1] << " " << ar[2];
}

template<typename T>
inline std::istream& operator>>(std::istream& is, std::array<T, 4>& ar) {
	return is >> ar[0] >> ar[1] >> ar[2] >> ar[3];
}

template<typename T>
inline std::ostream& operator<<(std::ostream& os, const std::array<T, 4>& ar) {
	return os << ar[0] << " " << ar[1] << " " << ar[2] << " " << ar[3];
}

#endif  // array_util_h

