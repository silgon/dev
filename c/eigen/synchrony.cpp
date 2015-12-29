#include <Eigen/Dense>
#include <iostream>

double prodlog(double var){
    if(var<10e-4)
        return 0;
    return var*std::log(var);
}
int main(int argc, char *argv[])
{
    Eigen::MatrixXd A(2,4);
    A<< 1, 2, 3, 4,
        5, 6, 7, 8;
    Eigen::MatrixXd centered = A.colwise() - A.rowwise().mean();
    Eigen::MatrixXd cov = (centered*centered.adjoint()) / double(A.cols() - 1);

    Eigen::VectorXcd eig =cov.eigenvalues();
    Eigen::MatrixXd lambda_spectrum = eig.real()/cov.trace();
    double SI;
    SI= 1+(lambda_spectrum.unaryExpr(std::ptr_fun(prodlog))).sum()/std::log(lambda_spectrum.rows());

    std::cout << "Matrix A:\n"<< A << "\n";
    std::cout << "difference with mean (rows):\n"<< centered << "\n";
    std::cout << "covariance:\n"<< cov << "\n";
    std::cout << "SI: " << SI << "\n";

    return 0;
}
/*
# numpy test
import numpy as np
A = np.array([[1,2,3,4],[5,6,7,8]])
covar= np.cov(A)
trace_covar = np.trace(covar)
eigval, eigvec = np.linalg.eig(covar)
lambda_spectrum = eigval/trace_covar
lambda_spectrum_zeros = np.array([lmbd for lmbd in lambda_spectrum
                            if lmbd>10e-4])
SI = 1 + sum(lambda_spectrum_zeros*np.log(lambda_spectrum_zeros))/np.log(len(lambda_spectrum))
*/
