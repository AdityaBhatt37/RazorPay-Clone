from functools import reduce
def proIT(a,b):
    return a+b #this produce will act as first argument for proII()

v1=[1,2,3,4,5] # each value of v1 will act as second argument for proIt()
rv=reduce(proIT,v1) # rv is an integer value
rv1=reduce(proIT,v1,1) # we can place any required value instead of 10
print("Final sum is ",rv) 
print("Final sum is ",rv1)