# Mandelbrot CPU Test

This is a simple Python implementation of the Mandelbrot algorithm used to
measure CPU performance using iterative complex number calculations.

The core of the algorithm repeatedly applies the equation:

z = z² + c

where:
* z is a complex number (starts at 0)
* c is the complex number corresponding to each point in the grid

The iteration continues until either:
*|z| > 2 (the point escapes to infinity), or
* the maximum number of iterations is reached

This behavior determines whether a point belongs to the Mandelbrot set.

FYI- It is not a professional benchmarking tool.
