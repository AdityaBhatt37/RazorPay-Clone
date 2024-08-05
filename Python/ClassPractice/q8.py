
ol = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 8, 4]

ul = []

for items in ol:

    if items not in ul:

        ul.append(items)
    
print(ol)
print(ul)

