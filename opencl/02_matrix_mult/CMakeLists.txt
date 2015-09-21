CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
project(02_matrix_mult)

message("lib path: $ENV{LD_LIBRARY_PATH}")
message("opencl_libraries: ${OPENCL_LIBRARIES}")

# definition needed by the cpp file to get the global path of the opencl file
ADD_DEFINITIONS(-DCL_SOURCE_DIR="${02_matrix_mult_SOURCE_DIR}")

FIND_LIBRARY(OPENCL_LIBRARIES OpenCL ENV LD_LIBRARY_PATH)
SET(EXEC 02_matrix_mult)
ADD_EXECUTABLE(${EXEC} main.cpp)

TARGET_LINK_LIBRARIES (${EXEC}
   ${OPENCL_LIBRARIES}
)