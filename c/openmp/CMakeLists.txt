cmake_minimum_required(VERSION 2.8.11)
set(CMAKE_CXX_COMPILER_ARG1 -std=c++11)

project(openmp_tests)

FIND_PACKAGE(OpenMP REQUIRED)

set(USEOMP ON)
if (OPENMP_FOUND AND ${USEOMP})
  set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
  set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()
include_directories(${OpenMP_INCLUDE_DIR})


add_executable(select_nprocessors select_nprocessors.cpp)
add_executable(local_variables local_variables.cpp)

