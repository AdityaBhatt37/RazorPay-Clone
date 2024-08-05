# 7. Write a python program to create a function which will print the first alphabet of each word except last word 
# and along with the alphabets of last word completely. e.g "Graphic Era Hill University" as "G.E.H.University".


str = input("Enter a string : ")

l = str.split()
res = []

for val in l[:-1]:
     res.append(val[0].upper())


res.append(l[-1].capitalize())

result = '.'.join(res)

print(result)


