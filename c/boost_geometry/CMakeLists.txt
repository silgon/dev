cmake_minimum_required(VERSION 2.8.11)
project(boost_graph_tests)

find_package(Boost 1.54 REQUIRED)

include_directories(${Boost_INCLUDE_DIR})

add_executable(intersection intersection.cpp)
