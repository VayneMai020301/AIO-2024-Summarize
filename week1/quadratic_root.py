

def run(a = 9, n =100) :
    """
    
    """
    x =  float(a) / 2 
    for _ in range(n):
        x = (x + a /x ) /2 

    return x

if __name__ == "__main__" :

    print(run(81,1000))