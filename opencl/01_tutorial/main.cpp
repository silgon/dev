#include "cll.hpp"

class myAlgo: public CL
{
public:
    myAlgo(std::string clfile):CL(clfile){
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

    int count = length;
    for(int i = 0; i < count; i++) {
        v_a[i]  = i;
        v_b[i]  = i;
    }

    cl::make_kernel<cl::Buffer, cl::Buffer, cl::Buffer> vadd(program, "vadd");

    d_a = cl::Buffer(context, v_a.begin(), v_a.end(), true);
    d_b = cl::Buffer(context, v_b.begin(), v_b.end(), true);
    d_c = cl::Buffer(context, CL_MEM_READ_WRITE, sizeof(float) * length);

    vadd(cl::EnqueueArgs(queue,cl::NDRange(count)),
         d_a, d_b, d_c);

    cl::copy(queue, d_c, v_c.begin(), v_c.end());
    std::cout << "c: ";
    for (int i = 0; i < count; i++) {
        std::cout << v_c[i] << ", ";
    }
    std::cout << "\n";

}

int main(int argc, char *argv[])
{
    std::string clfile = "vector_add.cl";
    myAlgo example(clfile);
    // example.loadProgram("vector_add.cl");
    example.runAlgo();
    
    return 0;
}
