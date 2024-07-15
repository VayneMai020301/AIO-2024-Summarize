"""
    * Geobra - Graphic Simuilation
    * Suppose we have f(x) = 3x^2 + 3x - 6
    * Let contribute f'(x) flowing derivate one-side and derivate center 
    * Find the glocal minimum after 100 ITERATION and Obsvervation the difference derivative one-side and derivative center
"""

def fx(x):
    return 3*x**2 + 3*x - 6

def derivative_one_side(fx, x, epsilon = 4):
    return (fx(x+epsilon) - fx(x)) / epsilon

def derivative_center(fx, x, epsilon = 4):
    return (fx(x+epsilon /2 ) - fx(x - epsilon /2 )) / epsilon

ITERATION = 5

learning_rate = 0.1
if __name__ == "__main__":
    x0 = 200
    for i in range(ITERATION):
        x0 = x0 - learning_rate * derivative_one_side(fx,x0)
        print(f"ITERATION {i}: {x0}")

    print('_'*100)
    x0 = 200
    for i in range(ITERATION):
        x0 = x0 - learning_rate * derivative_center(fx,x0)
        print(f"ITERATION {i}: {x0}")

