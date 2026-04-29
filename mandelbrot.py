import time

def mandelbrot(c, max_iteration):
    z = 0

    for i in range(max_iteration):
        z = z * z + c

        if abs(z)>2:
            return i
        
    return max_iteration

def run(width, height, max_iteration):
    start_time = time.time()

    for x in range(width):
        for y in range(height):
            c= complex(
                (x -width/2) * 4/width, 
                (y -height/2) * 4/width 
            )
            mandelbrot(c, max_iteration)

        end_time = time.time()

        print(f"Execution time: {end_time - start_time:.2f} seconds")

run(width = 800, height = 800, max_iteration = 100)