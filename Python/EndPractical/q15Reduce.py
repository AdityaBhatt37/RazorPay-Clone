# 15. Write a python program to ask user to enter any 10 numbers. Now find the sum of all these values by using reduce() function.

from functools import reduce

def summ(a,b):

    return a+b


l = []


for i in range(1,11):
    
    num = int(input(f"Enter {i} number : "))
    l.append(num)


res = reduce(summ,l)

print(f"The sum of 10 numbers are : {res}")


