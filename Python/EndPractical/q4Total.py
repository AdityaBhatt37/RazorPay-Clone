# . A shop will give discount of 10% if the cost of purchased quantity is more than 1000 rupees. 
# Now write a python program having a user defined function which will first calculate whether 
# a user purchased quantities more than 1000 rupees or not and then accordingly it will print the total cost for user.


def check(quantity,pricePerUnit):

    TotalPrice = quantity*pricePerUnit

    if(TotalPrice>1000):
        discount = TotalPrice * 0.1
        print("Your Total cost is : ",TotalPrice-discount)

    else:
        print("Your total cost is : ",TotalPrice)

q = int(input("Enter the number of quantity of items : "))
pu = float(input("Enter price per unit : "))
check(q,pu)