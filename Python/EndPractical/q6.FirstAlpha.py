# 6. Write a python program to create a function which will print the first alphabet of each word of a string entered by a user. e.g. 
# "Graphic Era Hill University" as "G.E.H.U".


str = input("Enter a string : ")

l = str.split()

for val in l:
    print(val[0].upper()+".",end="")