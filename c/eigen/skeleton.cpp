#include <Eigen/Dense>
#include <iostream>

int main(int argc, char *argv[])
{
    Eigen::MatrixXd A(2,4);
    A<< 1, 2, 3, 4,
        5, 6, 7, 8;
    std::cout << A << "\n";
    return 0;
}

