/*
  run the following commands after compilation

      time ./select_nprocessors 1
      time ./select_nprocessors 2
      time ./select_nprocessors 4
      time ./select_nprocessors 8

  you'll see the difference in time between the performance
 */
#include <cmath>
#include <iostream>
#include <vector>
int main(int argc, char *argv[]){
    std::cout << "Process running in " << argv[1] << " processors.\n";
    int n_processors = std::stoi(argv[1]);
    const size_t size = 256;
    double sinTable[size]; // faster with pointer than vector
    // std::vector<double> sinTable(size);
#pragma omp parallel for num_threads(n_processors)
    for(size_t i=0; i<100000; ++i){
        for(size_t n=0; n<size; ++n){
            sinTable[n] = std::sin(2 * M_PI * n / size);
        }
    }
}

