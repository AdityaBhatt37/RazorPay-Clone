# 5. Suppose a company decided to give bonus of 5% to their employee if his/her year of service in the company is more than 5 years. 
# Now write a python program having a user defined function which will print the net bonus amount. 
# Ask user to input the salary and the year of service.


def bonus(salary,service):

    if(service>5):
        salary = salary+(salary*0.05)
        print("Your net salary is : ",salary)

    else:
        print("Your newt salary is : ",salary)


sal = float(input("Enter your salary : "))
ser = float(input("Enter your service in years : "))

bonus(sal,ser)


