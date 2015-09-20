import pyopencl as cl
import numpy as np  # just in case but not used yet

class CL(object):
    """
    This class have all the configuration of to load and run
    an openCL program
    """
    def __init__(self):
        self.ctx = cl.create_some_context()
        self.queue = cl.CommandQueue(self.ctx)
        self.mf = cl.mem_flags

    def loadProgram(self, filename):
        """
        The file with the opencl program is loaded
        """
        # read in the OpenCL source file as a string
        f = open(filename, 'r')
        fstr = "".join(f.readlines())
        # create the program
        self.program = cl.Program(self.ctx, fstr).build()

    def vectToBuffer(self, vector):
        """ Converts numpy array to opencl array"""
        return cl.Buffer(self.ctx, self.mf.READ_ONLY | self.mf.COPY_HOST_PTR, hostbuf=vector)

    def bufferToVect(self, buff, vect):
        """ Converts opencl array to numpy array"""
        cl.enqueue_read_buffer(self.queue, buff, vect).wait()
        
    def outBuffer(self, nbytes):
        """creates output for opencl """
        return cl.Buffer(self.ctx, self.mf.WRITE_ONLY, nbytes)
    
    def runAlgo(self):
        """
        The program implementation
        """
        raise NotImplementedError
