#include <Eigen/Dense>
#include <iostream>

int main(int argc, char *argv[])
{
    Eigen::MatrixXd A(2,4);
    A<< 1, 2, 3, 4,
        5, 6, 7, 8;
    Eigen::MatrixXd centered = A.colwise() - A.rowwise().mean();
    Eigen::MatrixXd cov = (centered*centered.adjoint()) / double(A.cols() - 1);

    // Eigen::MatrixXd centered = A.transpose().rowwise() - A.transpose().colwise().mean();
    // Eigen::MatrixXd cov = (centered.adjoint() * centered) / double(A.transpose().rows() - 1);


    std::cout << "Matrix A:\n"<< A << "\n";
    std::cout <<  "difference with mean (rows):\n"<< centered << "\n";
    std::cout <<  "covariance:\n"<< cov << "\n";


   return 0;
}
/*
numpy test
import numpy as np
A = np.array([[1,2,3,4],[5,6,7,8]])
np.cov(A)
*/
