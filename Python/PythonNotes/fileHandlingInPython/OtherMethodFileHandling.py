#1->readline() method in python for filehandling

obr = open("method.txt","r")

cont = obr.readline()#This will read only one line 
# print(cont)


ob = open("method.txt")
while True:

    content = ob.readline()
    if not content:
        break

    print(content)


#2->writelines() method in python for filehandling

obr = open("method.txt","w")
lis = ["this is line third \n","This is line four \n","This is line five \n"]

obr.writelines(lis)
obr.close()
