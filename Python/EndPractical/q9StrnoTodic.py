# 9. Write a python program to create a function which will count the occurrence 
# (in the form of dictionary) of each character in a string. e.g. 
# "aabaac", here count of a=4, b=1, c=1 in the form of dictionary

str = input("Enter a string : ")

dic = {}
    
for char in str:
    
    if char in dic:

        dic[char] += 1
    else:
        dic[char] = 1


print(dic)


#NOTE ->Since dic['x'] = 9 : This will add a new key as x in dictionary with value 9.
