# 10. Consider a list having some values (numbers or strings). 
# Make a python function which will provide collection of unique values 
# (i.e. each value exactly one time), 
# duplicate values (which appear 2 or more time in the list), 
# and also all index numbers of duplicate values with their value. 
# e.g. [1,2,1,2,3,1,2,2], unique = [1,2,3], duplicate = [1,2], 
# index number = {1:[2, 5], 2:[3, 6, 7]}


# def uni(l):
#     unl=[]
#     dup = []
#     indx = []

#     for items in l:

#         if items in unl:
#             unl.remove(items)
#             dup.append(items)

#         else:
#             unl.append(items)
#             indx = list(enumerate(l))
#             dup.remove(items)
    
#     print("The orignal list is : ",l)
#     print("the duplicate values of list are : ",dup)
#     print("The unique values of list is : ",unl)
#     print("The indexes are of unique values are : ",indx)


# lis = ['aditya','priyanshu','Ayush','Akashn','prince']
# uni(lis)

# def uni(l):
#     unl = []
#     dup = []
#     indx = []

#     for items in l:
#         if items in unl:
#             if items not in dup:
#                 dup.append(items)
#             unl.remove(items)
#         else:
#             unl.append(items)
    
#     for item in unl:
#         indx.append(l.index(item))

#     print("The original list is: ", l)
#     print("The duplicate values of the list are: ", dup)
#     print("The unique values of the list are: ", unl)
#     print("The indexes of unique values are: ", indx)


# lis = ['aditya', 'priyanshu', 'Ayush', 'Akashn', 'prince', 'priyanshu', 'Ayush']
# uni(lis)

dic = {
 1 : 'one'

}

print(dic[1])
dic[2] = 'two'
print(dic)
dic[1].append(1)
print(dic)