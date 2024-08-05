def uni(t):
    l = []

    for items in t:

        if items not in l:
            l.append(items)
        
        else:
            l.remove(items)
    
    return l
        


t1 = (1,2,3,4,5,2,3)
t2 = (1,2,3,4,5,5,5,4)
t3 = (1,2,3,4,5,3,3,1)
t4 = (1,2,3,4,5,1,1)
t5 = (1,2,3,4,5,1,2,3,4,5)

lis = [t1,t2,t3,t4,t5]
result = list(map(uni,lis))

print(lis)
print(result)