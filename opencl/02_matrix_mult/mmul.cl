__kernel void mmul(
    const int N,
    __global float* A,
    __global float* B,
    __global float* C)
{
    int k;
    int i = get_global_id(0);
    int j = get_global_id(1);
    float tmp;
    if ((i < N) && (j < N))
    {
        tmp = 0.0f;
        for (k = 0; k < N; k++)
            tmp += A[i*N+k] * B[k*N+j];
        C[i*N+j] = tmp;
    }
}

// with private and local row
__kernel void mmul2(
    const int N,
    __global float* A,
    __global float* B,
    __global float* C,
    __local float* Bwrk)
{
    int k, j;
    int i    = get_global_id(0);
    int iloc = get_local_id(0);
    int nloc = get_local_size(0);
    float Awrk[1024];
    float tmp;
    if (i < N) {
        for (k = 0; k < N; k++)
            Awrk[k] = A[i*N+k];

        for (j = 0; j < N; j++) {
            barrier(CLK_LOCAL_MEM_FENCE);
            for (k = iloc; k < N; k += nloc)
                Bwrk[k] = B[k*N+j];
            barrier(CLK_LOCAL_MEM_FENCE);
            tmp = 0.0f;
            for (k = 0; k < N; k++)
                tmp += Awrk[k] * Bwrk[k];
            C[i*N+j] = tmp;
            barrier(CLK_LOCAL_MEM_FENCE);
        }
    }
}

// everything running in local
#define blksz 10
__kernel void mmul3(
                const unsigned int             N,
                __global const float* restrict A,
                __global const float* restrict B,
                __global       float* restrict C,
                __local        float* restrict Awrk,
                __local        float* restrict Bwrk)
{
    int kloc, Kblk;
    float Ctmp=0.0f;

    //  This work-item will compute element C(i,j)
    const int i = get_global_id(0);
    const int j = get_global_id(1);

    // Element C(i,j) is in block C(Iblk,Jblk)
    const int Iblk = get_group_id(0);
    const int Jblk = get_group_id(1);

    // C(i,j) is element C(iloc, jloc) of block C(Iblk, Jblk)
    const int iloc = get_local_id(0);
    const int jloc = get_local_id(1);

    // The number of blocks are the same in each dimension
    const int Num_BLK = N/blksz;

    // Setup the upper-left-corner (base address) for the A and
    // B blocks plus the increments to advance base addresses as
    // we loop over blocks
          int Abase = Iblk*N*blksz;    
    const int Ainc  = blksz;

          int Bbase = Jblk*blksz;
    const int Binc  = blksz*N;


    // C(Iblk,Jblk) = (sum over Kblk) A(Iblk,Kblk)*B(Kblk,Jblk)
    for (Kblk = 0;  Kblk<Num_BLK;  Kblk++)
    {
       // Load A(Iblk,Kblk) and B(Kblk,Jblk) into local memory.
       // Each work-item loads a single element of the two blocks
       // which are shared with the entire work-group.

       Awrk[jloc*blksz+iloc] = A[Abase+jloc*N+iloc];
       Bwrk[jloc*blksz+iloc] = B[Bbase+jloc*N+iloc];

       barrier(CLK_LOCAL_MEM_FENCE);

       // Compute dot products over local blocks to find
       // the contribution to C(i,j) from this block
       #pragma unroll
       for (kloc=0; kloc<blksz; kloc++)
          Ctmp += Awrk[jloc*blksz+kloc] * Bwrk[kloc*blksz+iloc];

       barrier(CLK_LOCAL_MEM_FENCE);
       Abase += Ainc;
       Bbase += Binc;
    }
 
    // update global C matrix 
    C[j*N+i] = Ctmp;
}
