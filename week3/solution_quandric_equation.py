
def fx(x):
    return x**2 - 9

def derivate_fx(x):
    return 2*x 

def solution(fx,dx ,iteration = 1000):

    x0 = 1
    for _ in range(iteration):
        x_next = (x0 * dx(x0)  + fx(x0) ) / dx(x0)
        x0 = x_next
    result = []
    result.append(x0)

    x0 = 1
    for _ in range(iteration):
        x_next = (x0 * dx(x0)  - fx(x0) ) / + dx(x0)
        x0 = x_next
    result.append(x0)
    return result

print(f'Solution of quandric equation is: {solution(fx, derivate_fx )}')
