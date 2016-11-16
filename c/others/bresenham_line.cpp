#include <stdio.h>
#include <iostream>
#include <cstdlib>
 
////////////////////////////////////////////////////////////////////////////////
void Bresenham(int x1, int y1, int const x2, int const y2){
    int delta_x(x2 - x1);
    // if x1 == x2, then it does not matter what we set here
    signed char const ix((delta_x > 0) - (delta_x < 0));
    delta_x = std::abs(delta_x) << 1;
 
    int delta_y(y2 - y1);
    // if y1 == y2, then it does not matter what we set here
    signed char const iy((delta_y > 0) - (delta_y < 0));
    delta_y = std::abs(delta_y) << 1;
 
    std::cout<<x1<<","<<y1<<std::endl;;
 
    if (delta_x >= delta_y)
    {
        // error may go below zero
        int error(delta_y - (delta_x >> 1));
 
        while (x1 != x2)
        {
            if ((error >= 0) && (error || (ix > 0)))
            {
                error -= delta_x;
                y1 += iy;
            }
            // else do nothing
 
            error += delta_y;
            x1 += ix;
 
            std::cout<<x1<<","<<y1<<std::endl;;
        }
    }
    else
    {
        // error may go below zero
        int error(delta_x - (delta_y >> 1));
 
        while (y1 != y2)
        {
            if ((error >= 0) && (error || (iy > 0)))
            {
                error -= delta_y;
                x1 += ix;
            }
            // else do nothing
 
            error += delta_x;
            y1 += iy;
 
            std::cout<<x1<<","<<y1<<std::endl;;
        }
    }
}

int main(int argc, char *argv[])
{
    int start_x = 0, start_y = 0;
    int end_x =10, end_y = 6;
    Bresenham(start_x, start_y, end_x, end_y);
    return 0;
}
