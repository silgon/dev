cmake_minimum_required(VERSION 2.8.11)
project(boost_graph_tests)

find_package(Boost 1.54 COMPONENTS graph REQUIRED)

include_directories(${Boost_INCLUDE_DIR})

add_executable(directed_graph_simple directed_graph_simple.cpp)
link_libraries(directed_graph_simple ${Boost_GRAPH_LIBRARY})
