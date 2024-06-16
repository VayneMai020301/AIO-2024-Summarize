

def derivate(fx, x, delta = 0.000001):
    '''
        This fucntin calculate derivate of curve at the point X = x 
        #Ouput
            Return derivate of point
    '''
    return float((fx(x+delta) - fx(x) ) /delta)

def minimum(fx,x, iteration = 1000):
    '''
        Using new-ton method to calcualte glocal minimum of f(x)
        #Ouput
            Return minimum/maximum of function
    
    '''
    for _ in range(iteration):
        x = x - fx(x)/(derivate(fx, x))

    return x

def quadratic(x):
    '''
        Defination quadratic function f(x) = 2*x*x + x /2 + 5
    '''
    return 2*x*x + x / 2 + 5


def exe(fx, left, right, iteration ,epsilon = 0.000001):

    if abs(left - right) <= epsilon:
        return (left + right) / 2

    mid = (left + right) /2 
    print(f'ITERARTION: {iteration:2} | Left point: {left:20} | Right point: {right:20} | Middle point: {mid:20} | epsilon: {epsilon:10}')
    mid_left  = mid - epsilon
    mid_right = mid + epsilon 
    
    iteration+=1
    if fx(mid_left) == fx(mid_right):
        return mid
    
    elif fx(mid_left) < fx(mid_right):
        new_right = mid
        exe(fx, left, new_right,iteration,epsilon)

    elif fx(mid_left) > fx(mid_right):
        new_left = mid
        exe(fx, new_left, right,iteration,epsilon)

LEFT_POINT  =  -80
RIGHT_POINT =  50
EPSILON = 0.000000000001
ITERARTION = 1


if __name__ == "__main__":
    f_x = quadratic
    min_x = minimum(f_x,10000,100000)
    print(f'Minimum of function at x={min_x} with y={f_x(min_x)}')
    exe(f_x, LEFT_POINT,RIGHT_POINT, ITERARTION,EPSILON)