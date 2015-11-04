cmake_minimum_required(VERSION 2.8.3)
project (test001)
SET(CMAKE_MODULE_PATH ${test001_SOURCE_DIR})

# FIND_PACKAGE(Qt REQUIRED)
find_package(MathGL)
include_directories(
    ${MathGL_INCLUDE_DIRS}
)
add_executable(test001 test001.cpp)
target_link_libraries(test001 ${MathGL_LIBRARIES})