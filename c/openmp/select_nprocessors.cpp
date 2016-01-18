#include <cmath>
#include <iostream>
int main(int argc, char *argv[]){
    std::cout << "Process running in " << argv[1] << " processors.\n";
    int n_processors = std::stoi(argv[1]);
    const int size = 256;
    double sinTable[size];
    for (int i = 0; i < 3600000; i++) {
#pragma omp parallel for num_threads(n_processors)
        for(int n=0; n<size; ++n)
            sinTable[n] = std::sin(2 * M_PI * n / size);
    }
}

