cmake_minimum_required(VERSION 2.8.11)
set(CMAKE_CXX_COMPILER_ARG1 -std=c++11)

project(hdf5_tests)

SET(CMAKE_MODULE_PATH ${hdf5_tests_SOURCE_DIR})

find_package(HDF5 REQUIRED)
FIND_PACKAGE(Eigen3 REQUIRED)

include_directories(${EIGEN3_INCLUDE_DIR})

add_executable(test_hdf5 test_hdf5.cpp)  # added header only library
target_link_libraries(test_hdf5 ${HDF5_LIBRARIES} ${Eigen_LIBRARIES})
