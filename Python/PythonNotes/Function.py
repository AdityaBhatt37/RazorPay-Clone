#FUNCTION  IN PYTHON 
#->Functions are block of code which is used to perform some specific task
#->user define function in python are created using the 'def' keyword

# IN PYHON THEIR ARE TWO TYPES OF FUNCTION -:
# 1)USER DEFINE FUNCTION   2)BUILT IN FUNCTION


def greater(a,b):

    if(a>b):
        print(f"a = {a} is greater then b = {b}")

    else:

        print(f"b = {b} is greater then a = {a}")
    
val1 = 3
val2 = 9

greater(val1,val2)


#BELOW IS A WAY OF CREATING A EMPTY BODY FUNCTION IN PYTHON:

def empty(a,b):
    pass  #we have to use pass keyword to create an empty function in python.
          #we can create the body of the function later in our program.

