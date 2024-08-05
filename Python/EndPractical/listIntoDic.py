#Question -> write a program in python to take 10 names of employ's and print them in a list.
#Question -> Wrtie a program in python to take 10  rating of employ's and print them in a list.
#Now for the above 2 question print the 10 names and rating of employ's in a dictionary such that they are links
#ex-> names: [a,b ,c,d..]
#     rating: [1,2,3...]




data=input("enter names of employee : ")   
lis=data.split(" ")
# print(lis)

data2=input("enter rating : ")
rating=data2.split(" ")
# print(rating)

dic1={}

for i in range(0,len(lis)):

    dic2 = {

        lis[i]:rating[i]
    }

    dic1.update(dic2)

print(dic1)
