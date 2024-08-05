# 14. Create a function (for filter() function) which will check an alphabet whether it is a vowel or not.
# Now consider any string input by a user and by using filter()
# function print the count of total number of vowels and list of vowels present in the given string. 


def vowel(str):

    return str.lower() in 'aeiou'


st = input("Enter a string : ")

rl = list(filter(vowel,st))


count = len(rl)

print(f"The list of vowel present in the string is : {rl}")
print("The number of vowels are : ",count)