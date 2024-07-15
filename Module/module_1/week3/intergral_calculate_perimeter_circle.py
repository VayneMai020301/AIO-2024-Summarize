
import math 
def calculate_perimeter(alpha = 0.01):
    """
        * Circle unit with r = 1
        * sin(alpha) = h / r (r=1) => sin(alpha) = h
        * when alpha closer to zero that mean h closer to circular arc
        * Perimeter = (360 / alpha) * sin(alpha)
    
    """
    num = 360 / alpha 

    perimeter = num * math.sin(math.radians(alpha))
    return perimeter
if __name__ == "__main__":


    print(f'Approximate Perimeter of Cirlce: {calculate_perimeter(alpha = 0.0001)}')
    print(f'Approximate PI : {calculate_perimeter(alpha = 0.01) / 2}')
