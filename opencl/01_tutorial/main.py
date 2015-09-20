import numpy as np
from cll import CL

class myAlgo(CL):
    def __init__(self):
        CL.__init__(self)

    def runAlgo(self):
        """
        The program implementation
        """
        #initialize client side (CPU) arrays
        a = np.array(range(10), dtype=np.float32)
        b = np.array(range(10), dtype=np.float32)

        #create OpenCL buffers
        a_buf = self.vectToBuffer(a)
        b_buf = self.vectToBuffer(b)
        dest_buf = self.outBuffer(b.nbytes)
        # execute program
        self.program.vadd(self.queue, a.shape, None,
                          a_buf, b_buf, dest_buf)
        c = np.empty_like(a)
        self.bufferToVect(dest_buf, c)

        # print result
        print "a", a
        print "b", b
        print "c", c

if __name__ == "__main__":
    example = myAlgo()
    example.loadProgram("vector_add.cl")
    example.runAlgo()

