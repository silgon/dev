/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * Copyright by The HDF Group.						     *
 * Copyright by the Board of Trustees of the University of Illinois.	     *
 * All rights reserved.							     *
 *	                                                                     *
 * This file is part of HDF5.  The full HDF5 copyright notice, including     *
 * terms governing use, modification, and redistribution, is contained in    *
 * the files COPYING and Copyright.html.  COPYING can be found at the root   *
 * of the source code distribution tree; Copyright.html can be found at the  *
 * root level of an installed copy of the electronic HDF5 document set and   *
 * is linked from the top-level documents page.  It can also be found at     *
 * http://hdfgroup.org/HDF5/doc/Copyright.html.  If you do not have	     *
 * access to either file, you may request a copy from help@hdfgroup.org.     *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

/*
 *  This example illustrates how to create a dataset that is a 4 x 6
 *  array. It is used in the HDF5 Tutorial.
 *
 *  Compile with: g++ -o test_hdf5 test_hdf5.cpp -lhdf5_cpp -lhdf5
 */

#include <iostream>
#include <string>
#include <H5Cpp.h>
#include <vector>
#include <Eigen/Eigen>

typedef Eigen::Matrix<double, Eigen::Dynamic,
                      Eigen::Dynamic, Eigen::RowMajor> MatrixXdR;

const H5std_string	FILE_NAME("h5tutr_dset.h5");
const H5std_string	DATASET_NAME("dset2");

int main (void)
{
    unsigned int seed = 3;
    std::srand(seed);
    // Try block to detect exceptions raised by any of the calls inside it
    try {
        // Turn off the auto-printing when failure occurs so that we can
        // handle the errors appropriately
        H5::Exception::dontPrint();

        // Create a new file using the default property lists.
        H5::H5File file(FILE_NAME, H5F_ACC_TRUNC);
        // H5::H5File file(FILE_NAME, H5F_ACC_RDWR);

        int rank = 2; // dataset dimensions
        hsize_t dims[2];
        hsize_t * dims_ptr;
        dims_ptr = dims;

        dims[0] = 10;
        dims[1] = 2;

        // generate random data
        double *dataptr;
        MatrixXdR A(dims[0], dims[1]);
        A = Eigen::MatrixXd::Random(A.rows(), A.cols());
        std::cout << A << "\n";
        dataptr = A.data();
        H5::DataSpace *dataspace = new H5::DataSpace(rank, dims);

        // Create the dataset
        H5::DataSet *dataset = new H5::DataSet(file.createDataSet(DATASET_NAME,
                                      H5::PredType::NATIVE_DOUBLE, *dataspace));
        dataset->write(dataptr, H5::PredType::NATIVE_DOUBLE);

        file.close();
        delete dataspace;
        delete dataset;
        dataptr = NULL;

        file.openFile(FILE_NAME, H5F_ACC_RDONLY);
        dataset = new H5::DataSet(file.openDataSet(DATASET_NAME));
        dataspace = new H5::DataSpace(dataset->getSpace());
        std::cout << "old rank: "<<rank << "\t old dims: "
                  << dims[0] << ","<<dims[1] << "\n";
        rank = dataspace->getSimpleExtentNdims();
        rank = dataspace->getSimpleExtentDims(dims_ptr);
        std::cout << "new rank: "<<rank << "\t new dims: "
                  << dims[0] << ","<<dims[1] << "\n";
        file.close();
        delete dataspace;
        delete dataset;
        dataptr = NULL;

    }  // end of try block
    // catch failure caused by the H5File operations
    catch(H5::FileIException error) {
        error.printError();
        return -1;
    }

    // catch failure caused by the DataSet operations
    catch(H5::DataSetIException error) {
        error.printError();
        return -1;
    }

    // catch failure caused by the DataSpace operations
    catch(H5::DataSpaceIException error) {
        error.printError();
        return -1;
    }

    return 0;  // successfully terminated
}
