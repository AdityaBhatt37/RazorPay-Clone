# 8. Write a python program to create a function which will find out all unique values present in string. 
# (i.e. all characters appeared in the string)

str = input("Enter a String : ")

ostr = []
unstr = []
for word in str:
    
    if(word in ostr and word in unstr):
        ostr.append(word)
        unstr.remove(word)
    
    else:
        unstr.append(word)
    
    lis = [1,2,3,4,5,6]
    print("The value of a is : ",bool)

    b = 3.14
    print("The value of b is : ",b)

    dic = {

        "name" : "Aditya",
        "rollNO" : 3,
        "section" : 'f2'
    }
    print(dic)

print("The orignal string is : ", str)
print("The filtered string is : ", ' '.join(unstr))