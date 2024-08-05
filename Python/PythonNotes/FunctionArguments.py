#FUNCTION ARGUMENT AND RETURN STATEMENT IN PYTHON.

# There are four types of arguments that we can provide in a function:

# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments


#1->DEFAULT ARGUMENTS

def func(a=2,b=3):

    print("The average of two number using 'DEFALUT ARGUMENTS' are : ",(a+b)/2,"\n\n")

func()#Not neccessary to pass the values of the arguments.




#2->KEYWORD ARGUMENTS

def funck(x,y=9):
   print("The average of two number using 'KEYWORD ARGUMENTS' are : ",(x+y)/2,"\n\n")


funck(y=9,x=5)#Using the Keyword Arguments we dont have to mentain the order
              #of paasing values to the arguments interpreter recognise the 
              #the arguments by their name which we provides.



#3->REQUIRED ARGUMENTS

def funcR(p,q):
    print("The average of two number using 'REQUIRED ARGUMENTS' are : ",(p+q)/2,"\n\n")

funcR(3,4)#now here we have to pass the values to the arguments are compelsory.


#4->VARIABLE LENGTH ARGUMENTS

'''
Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function.
This can be done using variable-length arguments.

There are two ways to achieve this:

Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. 
The function accesses the arguments by processing them in the form of tuple.
'''

def funcV(*numbers):

    sum = 0
    for i in numbers:
        sum = sum+i

    # print("The average numbers using 'VARIABLE LENTH ARGUMENTS' are : ",sum/len(numbers),"\n\n")

    return sum/len(numbers)

c = funcV(2,3,4,5,8,100)#This function will take these value as a tuple in its arguments.

print("The average numbers using 'VARIABLE LENTH ARGUMENTS' are : ",c)


