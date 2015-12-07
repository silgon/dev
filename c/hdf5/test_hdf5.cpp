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

const H5std_string	FILE_NAME("h5tutr_dset.h5");
const H5std_string	DATASET_NAME("dset");
const int	 NX = 4;                     // dataset dimensions
const int	 NY = 6;
const int	 RANK = 2;

int main (void)
{
    // Try block to detect exceptions raised by any of the calls inside it
    try
        {
            // Turn off the auto-printing when failure occurs so that we can
            // handle the errors appropriately
            H5::Exception::dontPrint();

            // Create a new file using the default property lists. 
            H5::H5File file(FILE_NAME, H5F_ACC_TRUNC);

            // Create the data space for the dataset.
            hsize_t dims[2];               // dataset dimensions
            dims[0] = NX;
            dims[1] = NY;
            H5::DataSpace dataspace(RANK, dims);

            // Create the dataset.      
            H5::DataSet dataset = file.createDataSet(DATASET_NAME,
                                                     H5::PredType::STD_I32BE,
                                                     dataspace);

        }  // end of try block

    // catch failure caused by the H5File operations
    catch(H5::FileIException error)
        {
            error.printError();
            return -1;
        }

    // catch failure caused by the DataSet operations
    catch(H5::DataSetIException error)
        {
            error.printError();
            return -1;
        }

    // catch failure caused by the DataSpace operations
    catch(H5::DataSpaceIException error)
        {
            error.printError();
            return -1;
        }

    return 0;  // successfully terminated
}