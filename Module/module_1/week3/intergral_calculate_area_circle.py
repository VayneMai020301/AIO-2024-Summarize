import math
def fx(x):
    return math.sqrt(1 - x**2 )


def calculate_circle(fx,num_partition = 1000):
    """
        * Circle unit with r = 1, center point (0,0)
        * 
        * When delata_x we find area of circle by Sigmal (delta_x * fx (-1 + i*delta_x))
        * Return area of Circle
    
    """
    start = -1
    stop = 1 

    step  = (stop - start ) / num_partition
    area = 0
    for i in range(num_partition):

        area += step * fx(start + i*step)

    return 2 * area

area = calculate_circle(fx, 1000000)
print(f"Area of circle is: {area}")
print(f"Approximate PI is: {area}")
    

        
