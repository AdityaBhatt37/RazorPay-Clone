#1)replace() method

str1 = "Graphic era deemed to be university"

res = str1.replace("deemed to be","hill") #replace method does not change the actual string
print(str1)
print(res)


#2)index() method

#->Using the index() method we can get the index number of the charcter, string(first letter).
#->if the string is repeating then the index number we will get of that string which will occour first.

#print(str1.index("era"))


#3)find() mehtod 

#->using the find() method we can also get the index number of the charcter, string(first letter).
#->if the string is repeating then the index number we will get of that string which will occour first.

print("The string is present in the index number of : ",str1.find("era"))



#DIFFERENCE BETWEEN THE INDEX() and FIND() METHODS

#INDEX() -> This mehtod will give ERROR if we pass a wrong string or char as an argument to the method.
            #and program will terminate.
            
#FIND() -> This method will return (-1) if we pass a wring string or charas an argument to the method.

#EXAMPLE

print("passing the wrong string to find using the find() method output is : ",str1.find("eraa")) 
#searching an wrong sub string of str1. #OUTPUT -> -1

# print("passing the wrong string to find using the index() method output is :",str1.index("eraa")) 
#this will give the error ot the program and program will program. And program will get terminated.


#4)count() method

#->using the count() method we can find the occurrence of character substring or string and space also.

print("The number of spaces present in the string is : ",str1.count(" "))


#5)strip() method

#->This method is used to excusses the unnecessory spaces from the begining and the end of the string.
#->Default value of strip() method is single space (spacebar space).
#->We remove the value from starting and ending not from the middle.

#EXAMPLE -:
str2  = "***** This is the starting string this is ending string *****"
print("value of str2 before using strip() method is : ",str2)
print("Value of str2 after using strip() method is : ",str2.strip("*"))

# strip() method has two sub  methods -:
# 1)lstrip() -> this method will remove the left startring part of the string.
# 2)rstrip() -> this method will remove the right ending part of the string.

print("Value of the str2 after using the lstrip() method is : ",str2.lstrip("*"))
print("Value of the str2 after using the rstrip() method is : ",str2.rstrip("*"))


#6)swapcase() method
# ->This method is used to convert upper case into lower and lower case into upper case of a string.
# ->swapcase() method has also two sub method they are upper() and lower().

str3 = "THIS IS UPPER CASE this is lower case"

print("The result of swapcase() method is : ",str3.swapcase())
print("The result of upper() method is : ",str3.upper())
print("The resuldt of lower() mehtod is : ",str3.lower())


#7)title() method
# ->This method is used to capitalize first Alphabet of each words in a string.
# ->If all words are capital it will make them all small.

print("The value of str3 after using the title() method is : ",str3.title())

#8)capitalize() method 
# ->This method is used to capitalize first Alphabet of first words of a string.
# ->If ather word are capital it will make them all small.

print("The value of str3 after using the capitalize() method is : ",str3.capitalize())


#9)split() method
#->This function seperate the substring of a string on the basis of argument passed on split() method.
#->Bydeafult value of split() method is single string.
#->it return type is list.

str4 = "My name is. Aditya"
print("The result of using split() method is : ",str4.split())
print("The result of using split() method after passing an argument is : ",str4.split("."))


#10)join() method
#->This methods return string in which the elements of sequence (i.e list) have been joind by a sperator.
#->it also works on split() method.

l1 = ['I','am','doing','my','Work']
print(type(l1))

res1 = " ".join(l1)

print("The result before using join() miethod is : ",l1)
print("The result after  using join() method is : ",res1)

