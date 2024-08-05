# example of map 

def addnum(x,y):
    return x+y

l1=[1,2,3,4,5]
l2=[5,4,3,2,1]

m1=map(addnum,l1,l2)
fr=list(m1)
print("The sum is ",fr)