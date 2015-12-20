project(eigen_tests)

cmake_minimum_required(VERSION 2.8.11)
find_package(Boost 1.54 COMPONENTS log REQUIRED)
find_package(Threads)
add_definitions(-DBOOST_LOG_DYN_LINK)
include_directories(${Boost_INCLUDE_DIR})

find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIR})

add_executable(covariance covariance.cpp)
add_executable(synchrony synchrony.cpp)
