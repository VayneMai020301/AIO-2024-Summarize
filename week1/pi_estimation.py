
def run(method = None , n =None) :
    assert method in ["1","2"], print(f"Please retry pi estimation calculation method")
    assert str(n).isnumeric() , print(f"Please retry n, n must be unsigned integer value")
    print("-"*50)
    if method == "1":
        print(f"PI Estimation is: Gregory-Leibniz Series - with n = {n}")
        result = 0 

        for i in range(1,n+1):
            result += (-1)**(i+1) / (2*i -1)

        return 4 * result

    elif  method == "2":
        result  = 0

        print(f"PI Estimation is: Nilakantha Series - with n = {n}")

        for i in range(0,n+1):
            result += (-1)**(i) / ((2*i+2)*(2*i+3)*(2*i+4))

        return 3 + 4*result


    return 0

if __name__ == "__main__" :

    print(run("1",200000))
    print(run("2",200000))
