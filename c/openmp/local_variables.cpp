#include <iostream>
#include <cmath>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

#ifdef _OPENMP
    omp_lock_t omp_lock;
#endif
int main(int argc, char *argv[]){
    std::cout << "Process running in " << argv[1] << " processors.\n";
    unsigned int n_processors = std::stoi(argv[1]);
#ifdef _OPENMP
    // initialize lock
    omp_init_lock(&omp_lock);
#endif
    const unsigned int iters = 10000, n_accu=5000;  // iterations and accumulator
    double accu[n_accu];
    // std::vector<double> accu(n_accu);
#pragma omp parallel num_threads(n_processors)
    {
        size_t i, j;
        double sum;
#pragma omp for
        for (i = 0; i < n_accu; i++){
            sum = 0;
            for (j = 0; j < iters; j++) {
                sum += std::sin(2 * M_PI * j / iters);
            }
#ifdef _OPENMP
            // set lock
            omp_set_lock(&omp_lock);
#endif
            // global variables assignment
            accu[i] = sum;
#ifdef _OPENMP
            // unset lock
            omp_unset_lock(&omp_lock);
#endif
        }
    }

#ifdef _OPENMP
    // destroy lock
    omp_destroy_lock(&omp_lock);
#endif
    return 0;
}
