#define __CL_ENABLE_EXCEPTIONS

#include "CL/cl.hpp"

#include <vector>
#include <cstdio>
#include <cstdlib>
#include <string>

#include <iostream>
#include <fstream>

// pick up device type from compiler command line or from the default type
#ifndef DEVICE
#define DEVICE CL_DEVICE_TYPE_DEFAULT
#endif

//------------------------------------------------------------------------------

#define LENGTH (10)    // length of vectors a, b, and c

inline std::string loadProgram(std::string input)
{
    std::ifstream stream(input.c_str());
    if (!stream.is_open()) {
        std::cout << "Cannot open file: " << input << std::endl;
        exit(1);
    }

    return std::string(std::istreambuf_iterator<char>(stream),
                       (std::istreambuf_iterator<char>()));
}

int main(void) {
    std::vector<float> h_a(LENGTH);                // a vector 
    std::vector<float> h_b(LENGTH);                // b vector 	
    std::vector<float> h_c (LENGTH);   // c vector (result)

    cl::Buffer d_a;                       // device memory used for the input  a vector
    cl::Buffer d_b;                       // device memory used for the input  b vector
    cl::Buffer d_c;                       // device memory used for the output c vector

    // Fill vectors a and b with random float values
    int count = LENGTH;
    for(int i = 0; i < count; i++) {
        h_a[i]  = i;
        h_b[i]  = i;
    }

    try {
    	// Create a context
        cl::Context context(DEVICE);

        // Load in kernel source, creating a program object for the context

        cl::Program program(context, loadProgram("vector_add.cl"), true);

        // Get the command queue
        cl::CommandQueue queue(context);

        // Create the kernel functor
 
        cl::make_kernel<cl::Buffer, cl::Buffer, cl::Buffer> vadd(program, "vadd");

        d_a = cl::Buffer(context, h_a.begin(), h_a.end(), true);
        d_b = cl::Buffer(context, h_b.begin(), h_b.end(), true);
        d_c = cl::Buffer(context, CL_MEM_READ_WRITE, sizeof(float) * LENGTH);

        vadd(
             cl::EnqueueArgs(
                             queue,
                             cl::NDRange(count)),
             d_a,
             d_b,
             d_c);

        cl::copy(queue, d_c, h_c.begin(), h_c.end());
        std::cout << "c: ";
        for (int i = 0; i < count; i++) {
            std::cout << h_c[i] << ", ";
        }
        std::cout << "\n";
    }
    catch (cl::Error err) {
        std::cout << "Exception\n";
        std::cerr 
            << "ERROR: "
            << err.what()
            << std::endl;
    }
}
