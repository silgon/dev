cmake_minimum_required(VERSION 2.8.11)
# set(CMAKE_CXX_COMPILER_ARG1 -std=c++11)

project(firstqt)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)

find_package(Qt5Widgets)
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${Qt5Widgets_EXECUTABLE_COMPILE_FLAGS} -std=c++11 -Wall")
# set(CMAKE_POSITION_INDEPENDENT_CODE ON) # line solves -fPIC problem
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)


add_executable(main main.cpp my_form.h)  # added header only library
target_link_libraries(main Qt5::Widgets)

# header only but another option
# add_library(my_form my_form.h widget.h)
# target_link_libraries(my_form Qt5::Widgets)
# add_executable(main main.cpp) 
# target_link_libraries(main Qt5::Widgets my_form)

