#1->update() METHOD -> This method simply update or extend the dictionary

Rating1={111:5, 113:7, 115:4, 117:9}
print("The value of Dictionary before update Rating1 : ",Rating1)

Rating2={112:7, 114:9, 116:3}
print("The vaue of Dictionary before update Rating2 : ",Rating2)

Rating1.update(Rating2) #syntax Rating1 is updated by the values of Rating2 

print("The Value of Dictionary Rating1 after update mehtod is : ",Rating1,"\n\n")


#2->clear() METHOD -> This method is used to clear the all the dictionary

Rating2.clear()
print(f"The values in Rating2 dictionary after using clear method is : {Rating2}\n\n")

#Way to create an empty dictionary
empt = {}
print(empt)


#3->pop() -> This method is used to delete the particular key value pair
            #we have to pass the key of a dictionary as an arugument inside it.

print(f"The key and values of Dictionary Rating1 before use of 'pop' method is : {Rating1}")
Rating1.pop(112)
print(f"The key and values of Dictionary Rating1 After use of 'pop' method is : {Rating1}\n\n")

#4->popitem() -> This method delete the last key value pair from the dictionary
print(f"The key and values of Dictionary Rating1 before use of 'pop' method is : {Rating1}")
Rating1.popitem()
print(f"The key and values of Dictionary Rating1 After use of 'pop' method is : {Rating1}\n\n")

#4->'del' keyword is used to delete entire or a key value pair values form the dictionary.

# del Rating1
# print(Rating1) #output will be Rating1 is undefined because the 'del' keyword has delete the entir dictionary.

del Rating1[111] #this will delete the '111' key and its corresponding value.
