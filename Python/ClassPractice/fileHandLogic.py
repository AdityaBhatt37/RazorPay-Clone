nl = int(input("Enter how much lines you want to enter in file: "))
f = open("fileHandLogic.txt","w")


for i in range(1,nl+1):
    ln = input("Enter a line : ")
    f.writelines(nl)

f.close()

ob = open("fileHandLogic.txt","r")

while True:

    re = ob.readline()
    print(f"{re},\n")

    if not re:

        break
ob.close()