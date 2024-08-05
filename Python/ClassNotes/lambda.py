# lambda function is also known as anonymous function because it can take any no. of argument but it can have only expression 

def AddNum(x,y):
    return x+y

lm1=lambda x,y,z:(x*y*z)/100

x,y,z=1000,10,2
rv1 = lm1(x,y,z)
print("Sum is ",rv1)