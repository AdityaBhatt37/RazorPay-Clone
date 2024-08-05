# example of the filter with even number 

def even(x):
    if(x%2==0):
        return True
    else:
        return False
    
l1=[1,2,3,4,5,6]
m1=filter(even,l1)
print(m1)
fr=list(m1)
print("The list of the even is ",fr)