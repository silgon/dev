import numpy as np
from cll import CL
import pyopencl as cl

class myAlgo(CL):
    def __init__(self):
        CL.__init__(self)

    def runAlgo(self):
        """
        The program implementation
        """
        #initialize client side (CPU) arrays
        N = 100
        A_VAL = .5
        B_VAL = 1
        size = N * N
        h_A = np.empty(size).astype(np.float32)
        h_B = np.empty(size).astype(np.float32)
        h_A.fill(A_VAL)
        h_B.fill(B_VAL)

        #create OpenCL buffers
        d_A = self.vectToBuffer(h_A)
        d_B = self.vectToBuffer(h_B)
        d_C = self.outBuffer(h_A.nbytes)

        np.set_printoptions(threshold='nan')
        # execute program
        mmul = self.program.mmul
        mmul.set_scalar_arg_dtypes([np.int32, None, None, None])
        mmul(self.queue, (N, N), None,
             N, d_A, d_B, d_C)
        print "First problem solved"

        h_C = np.empty_like(h_A)
        self.bufferToVect(d_C, h_C)
        print "{}".format(h_C)

        localmem = cl.LocalMemory(np.dtype(np.float32).itemsize * N)
        n_blocks = 10
        mmul2 = self.program.mmul2
        mmul2.set_scalar_arg_dtypes([np.int32, None, None, None, None])
        mmul2(self.queue, (N,), (N/n_blocks,),
              N, d_A, d_B, d_C, localmem)
        print "Second problem solved"

        h_C = np.empty_like(h_A)
        self.bufferToVect(d_C, h_C)
        print "{}".format(h_C)

        blocksize = 10
        A_block = cl.LocalMemory(np.dtype(np.float32).itemsize*blocksize**2)
        B_block = cl.LocalMemory(np.dtype(np.float32).itemsize*blocksize**2)
        mmul3 = self.program.mmul3
        mmul3.set_scalar_arg_dtypes([np.int32, None, None, None, None, None])
        mmul3(self.queue, (N, N), (blocksize, blocksize),
              N, d_A, d_B, d_C, A_block, B_block)

        print "Third problem solved"


        h_C = np.empty_like(h_A)
        self.bufferToVect(d_C, h_C)
        print "{}".format(h_C)

        # print result
        # print "a", h_A
        # print "b", h_B
        # print "c", h_C

if __name__ == "__main__":
    example = myAlgo()
    example.loadProgram("mmul.cl")
    example.runAlgo()

