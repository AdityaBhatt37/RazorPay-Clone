#Q8:WAPP to remove duplicate values from a list.


li=[1,2,3,3,2,1,4,5,5,7,8,9,10,11]

li2 = []

for items in li:

    if items not in li2:
        li2.append(items)

    else:
        li2.remove(items)


print(li2)
    