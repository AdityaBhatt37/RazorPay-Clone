# 11. Create a function which will print only those values which appear only one time in a given tuple,
# i.e. values having unique appearance. 
# Now consider any 5 tuple having any 5 values 
# and use the later function with map() function to 
# find out all values having unique appearance for all 5 tuples.

def uni(t):
    lis = []

    for items in t:

        if items in lis:
            lis.remove(items)
        else:
            lis.append(items)
        
    return tuple(lis)

t1 = (1, 2, 2, 3, 4)
t2 = (5, 5, 6, 7, 8)
t3 = (9, 10, 11, 11, 12)
t4 = (13, 14, 15, 15, 16)
t5 = (17, 18, 19, 19, 20)

tup = [t1,t2,t3,t4,t5]

result = tuple(map(uni,tup))
print("The orignal tuples values : ",tup)
print("The uniqe items in all the tuples are : ",result)

