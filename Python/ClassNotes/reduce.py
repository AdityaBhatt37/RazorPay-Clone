from functools import reduce

def func(a,b):
    return a+b

ls = [1,2,3,4,5]

result = reduce(func,ls)

print("The sum is : ",result)