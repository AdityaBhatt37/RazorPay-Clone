#Consider a tuple having values integer, decimal and string. 
#Write a python program to delete all decimal values and add 3 charcter values in it.


original_tuple = (10, 3.14, 'hello', 4.5, 'world')


modified_list = list(original_tuple)


for item in original_tuple:

    if type(item) == float:
        modified_list.remove(item) 

    elif type(item) == str and len(item) <= 3:
        modified_list.append(item)  


modified_tuple = tuple(modified_list)


print("Modified Tuple:", modified_tuple)
