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

#ifndef CL_SOURCE_DIR
#define CL_SOURCE_DIR ""
#endif

class CL
{
public:
    cl::Context context;
    cl::Program program;
    cl::CommandQueue queue;

    CL(std::string clfile): context(DEVICE), queue(context),
          program(context, readFile(clfile), true){}
    virtual ~CL(){}
    template <class T>
    void vectToBuffer(T & in, cl::Buffer & out){
        out = cl::Buffer(context, in.begin(), in.end(), true);
    }
    virtual void runAlgo(){
        std::cout << "Not Implemented function runAlgo" << "\n";
        std::exit(0);
    }

private:

    inline std::string readFile(std::string input)
    {
        std::string filepath;
        // if created with make file
        if(CL_SOURCE_DIR == "")
            filepath = input;
        // if created with CMakeLists.txt file
        else
            filepath = static_cast<std::string>(CL_SOURCE_DIR) +"/" + input;

        std::ifstream stream(filepath.c_str());
        if (!stream.is_open()) {
            std::cout << "Cannot open file: " << filepath << std::endl;
            exit(1);
        }
        return std::string(std::istreambuf_iterator<char>(stream),
                           (std::istreambuf_iterator<char>()));
    }

};
