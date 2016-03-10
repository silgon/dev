cmake_minimum_required(VERSION 2.8.11)
set(CMAKE_CXX_COMPILER_ARG1 -std=c++11)

project(lbfgs_example)

# set(CMAKE_POSITION_INDEPENDENT_CODE ON) # line solves -fPIC problem
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -llbfgs")

add_executable(liblbfgs_example liblbfgs_example.cpp)
# target_link_libraries(liblbfgs_example "-llbfgs")
target_link_libraries(liblbfgs_example "-llbfgs")