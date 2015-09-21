#include "cll.hpp"

class myAlgo: public CL
{
public:
    // function to use for vector add
    cl::make_kernel<cl::Buffer, cl::Buffer, cl::Buffer> func_vadd;
    myAlgo(std::string clfile):CL(clfile),
                               func_vadd(clprogram, "vadd"){
    }
    virtual void runAlgo();
    virtual ~myAlgo(){}
};

void myAlgo::runAlgo(){
    int length = 10;
    // create vectors: 2 inputs and 1 output
    std::vector<float> v_a(length);
    std::vector<float> v_b(length);
    std::vector<float> v_c (length);

    // create buffers used as vectors in opencl
    cl::Buffer d_a;
    cl::Buffer d_b;
    cl::Buffer d_c;

    // set values of the vectors
    for(int i = 0; i < length; i++) {
        v_a[i]  = i;
        v_b[i]  = i;
    }

    // pass the value of the vectors to the buffers
    vectToBuffer(v_a, d_a);
    vectToBuffer(v_b, d_b);

    // create a buffer with the proper lenght for result
    d_c = outBuffer(length);

    // run opencl function
    func_vadd(cl::EnqueueArgs(queue,cl::NDRange(length)),
         d_a, d_b, d_c);

    // pass the result information into a vector
    bufferToVect(d_c, v_c);

    // printing
    std::cout << "c: ";
    for (int i = 0; i < length; i++) {
        std::cout << v_c[i] << ", ";
    }
    std::cout << "\n";

}

int main(int argc, char *argv[])
{
    std::string clfile = "vector_add.cl";
    myAlgo example(clfile);
    example.runAlgo();
    return 0;
}
