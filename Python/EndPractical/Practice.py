#FILE HANDLING IN PYTHON

fo = open("myf.txt","w")

str = input("Enter any string to enter in the file : ")

fo.write(str)

fo.close()

fo = open("myf.txt","r")

data = fo.read()
print(data)

fo.close()