def factor(n):
    
    SumFact = 0

    for i in range(1,n):

        if(n%i==0):
            SumFact = SumFact+i

    return SumFact


num = int(input("Enter a number : "))


if(factor(num)==num):

    print(num," is perfact number ")

else:

    print(num," is not the perfact number")

