# 12. Write a lambda function to calculate simple interest. 
# Ask user to enter the principal amount, and time period. Assume rate of interest is 6.25%.

#SI = P*R*T /100

SI = lambda P,R,T: (P*R*T)/100

P = float(input("Enter principal amount : "))
R = 6.25
T = float(input("Enter time amount : "))

result = SI(P,R,T)

print(result)