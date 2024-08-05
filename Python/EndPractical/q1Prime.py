for n in range(2,101):

    flag = 0
    q = n//2

    for i in range(2,q+1):
        
        if(n%i==0):

            flag = 1
            break

    if(flag!=0):
        print(n," is not a prime number")
    else:
        print(n," is a prime number")


