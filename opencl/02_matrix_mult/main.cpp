#include "cll.hpp"

class myAlgo: public CL
{
public:
    // function to use for vector add
    cl::make_kernel<int, cl::Buffer, cl::Buffer, cl::Buffer> mmul;
    cl::make_kernel<int, cl::Buffer, cl::Buffer, cl::Buffer, cl::LocalSpaceArg> mmul2;
    cl::make_kernel<int, cl::Buffer, cl::Buffer, cl::Buffer, cl::LocalSpaceArg, cl::LocalSpaceArg> mmul3;
    myAlgo(std::string clfile):CL(clfile),
                               mmul(clprogram, "mmul"),
                               mmul2(clprogram, "mmul2"),
                               mmul3(clprogram, "mmul3"){
    }
    virtual void runAlgo();
    virtual ~myAlgo(){}
};

void myAlgo::runAlgo(){
    int N = 100;
    int size = N*N;
    // create vectors: 2 inputs and 1 output
    std::vector<float> h_A(size);
    std::vector<float> h_B(size);
    std::vector<float> h_C (size);

    // create buffers used as vectors in opencl
    cl::Buffer d_A;
    cl::Buffer d_B;
    cl::Buffer d_C;

    // set values of the vectors
    for(int i = 0; i < size; i++) {
        h_A[i]  = .5;
        h_B[i]  = 1;
    }

    // pass the value of the vectors to the buffers
    vectToBuffer(h_A, d_A);
    vectToBuffer(h_B, d_B);

    // create a buffer with the proper lenght for result
    d_C = outBuffer(size);

    // run opencl function
    mmul(cl::EnqueueArgs(queue, cl::NDRange(N, N)),
          N, d_A, d_B, d_C);

    // pass the result information into a vector
    bufferToVect(d_C, h_C);
    // printing
    std::cout << "First result:\n";
    for (int i = 0; i < size; i++) {
        std::cout << h_C[i] << ", ";
    }
    std::cout << "\n";

    // run opencl function
    int n_blocks(10);
    cl::LocalSpaceArg localmem = cl::Local(sizeof(float) * N);
    mmul2(cl::EnqueueArgs(queue, cl::NDRange(N),cl::NDRange(N/n_blocks)),
         N, d_A, d_B, d_C, localmem);

    // pass the result information into a vector
    bufferToVect(d_C, h_C);
    // printing
    std::cout << "Second result:\n";
    for (int i = 0; i < size; i++) {
        std::cout << h_C[i] << ", ";
    }
    std::cout << "\n";

    // run opencl function
    int blocksize(10);
    cl::LocalSpaceArg A_block = cl::Local(sizeof(float)*blocksize*blocksize);
    cl::LocalSpaceArg B_block = cl::Local(sizeof(float)*blocksize*blocksize);
    mmul3(cl::EnqueueArgs(queue, cl::NDRange(N, N),cl::NDRange(blocksize, blocksize)),
          N, d_A, d_B, d_C, A_block, B_block);

    // pass the result information into a vector
    bufferToVect(d_C, h_C);
    // printing
    std::cout << "Third result:\n";
    for (int i = 0; i < size; i++) {
        std::cout << h_C[i] << ", ";
    }
    std::cout << "\n";

}

int main(int argc, char *argv[])
{
    std::string clfile = "mmul.cl";
    myAlgo example(clfile);
    example.runAlgo();
    return 0;
}
