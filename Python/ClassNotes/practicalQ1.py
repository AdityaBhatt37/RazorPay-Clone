'''Q1:Write a python program to store any 10 numbers in a list. Now make a tuple haveing only even number by using filter() functions.'''

def FindEven(n1):

    if (n1%2==0):
        return True
    
    else:

        return False
    

ls = []

for i in range(1,11):
    ls.append(i)

result = tuple(filter(FindEven,ls))
print("The tuple of even numbers from 1 to 10 are : ",result)