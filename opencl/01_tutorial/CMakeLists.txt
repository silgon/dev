CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
project(01_tutorial)

message("lib path: $ENV{LD_LIBRARY_PATH}")
message("opencl_libraries: ${OPENCL_LIBRARIES}")

# definition needed by the cpp file to get the global path of the opencl file
ADD_DEFINITIONS(-DCL_SOURCE_DIR="${01_tutorial_SOURCE_DIR}")

FIND_LIBRARY(OPENCL_LIBRARIES OpenCL ENV LD_LIBRARY_PATH)
SET(EXEC 01_tutorial)
ADD_EXECUTABLE(${EXEC} main.cpp)

TARGET_LINK_LIBRARIES (${EXEC}
   ${OPENCL_LIBRARIES}
)