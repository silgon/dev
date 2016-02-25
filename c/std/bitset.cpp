#include <bitset>
#include <string>
#include <iostream>
#include <climits>
// more info http://en.cppreference.com/w/cpp/utility/bitset/bitset

int main() 
{
    // empty constructor
    std::bitset<100> b1; // [0,0,...,0]
    std::bitset<100> b2;
    b2.set();
    b1[4]=true;
    b1.set(2);
    std::cout << "b1:\t" << b1 << "\n";
    std::cout << "b2:\t" << b2 << "\n";
    std::cout << "b1&b2:\t" << (b1&b2) << "\n";
    std::cout << "b2.count:\t" << b2.count() << "\n";
    b1=0;
    std::cout << "b1:\t" << b1 << "\n";
}
