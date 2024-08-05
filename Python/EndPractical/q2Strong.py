# Write a Python program to check whether the entered number is a strong number or not.

def factorial(num):

    fact = 1
    for i in range(1,num+1):
        fact = fact*i
   
    return fact


n = int(input("Enter a number : "))
dn = n
summ = 0

while(n!=0):

    rem = n%10
    facto = factorial(rem)
    summ = summ+factorial(rem)
    n = n//10

if(summ==dn):

    print(dn," is a strong number")

else:

    print(dn," is not a strong number")

