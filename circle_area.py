import math

def fx(x) -> float :

    """
        ## This is circle equation 

    """
    return math.sqrt(1 - x**2)

def run(n_sample):
    area = 0
    start = -1 
    stop = 1
    step =   2 / n_sample
    for i in range(n_sample):
        area+= step * fx(-1 + i *step)


    return 2* area


if __name__ == "__main__":
    print(f"Area of Circle is: {run(20000)}")

