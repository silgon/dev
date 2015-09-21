#include "cll.hpp"

class myAlgo: public CL
{
public:
    cl::make_kernel<cl::Buffer, cl::Buffer, cl::Buffer> func_vadd;
    myAlgo(std::string clfile):CL(clfile),
                               func_vadd(clprogram, "vadd"){
    }
    virtual void runAlgo();
    virtual ~myAlgo(){}
};

void myAlgo::runAlgo(){
    int length = 10;
    std::vector<float> v_a(length);
    std::vector<float> v_b(length);
    std::vector<float> v_c (length);

    cl::Buffer d_a;
    cl::Buffer d_b;
    cl::Buffer d_c;

    for(int i = 0; i < length; i++) {
        v_a[i]  = i;
        v_b[i]  = i;
    }
    vectToBuffer(v_a, d_a);
    vectToBuffer(v_b, d_b);
    d_c = outBuffer(length);
    func_vadd(cl::EnqueueArgs(queue,cl::NDRange(length)),
         d_a, d_b, d_c);

    bufferToVect(d_c, v_c);
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
