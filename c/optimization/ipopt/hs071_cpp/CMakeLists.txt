cmake_minimum_required(VERSION 2.8.11)
set(CMAKE_CXX_COMPILER_ARG1 -std=c++11)

project(ipopt_example)

# set(CMAKE_POSITION_INDEPENDENT_CODE ON) # line solves -fPIC problem
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${IPOPT_CXX_FLAGS}")

SET(CMAKE_MODULE_PATH ${ipopt_example_SOURCE_DIR})

find_package(IPOPT REQUIRED)

include_directories(${IPOPT_INCLUDE_DIRS})

add_executable(hs071_main hs071_main.cpp hs071_nlp.cpp)
target_link_libraries(hs071_main ${IPOPT_LIBRARIES})
