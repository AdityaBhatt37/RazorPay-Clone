# 13. Consider any empty list, now store following values by taking input from user: 
# user's name, address, last three semester 
# (make a dictionary of it, e.g. {'I': value1, 'II': value2, 'III': value3}), 
# six subject names (make a list of it), 
# and six subject marks of 4th semester mid term examination (make a tuple of it). 
# Now find the length (total number of values in it) 
# of all values entered by the user in the form of list (by using map() function) and print it.

# Step 1: Create an empty list to store all values
all_values = []

# Step 2: Take user input for the name and address
name = input("Enter your name: ")
address = input("Enter your address: ")

# Step 3: Take user input for the last three semester marks and store in a dictionary
semesters = {}
semesters['I'] = input("Enter marks for semester I: ")
semesters['II'] = input("Enter marks for semester II: ")
semesters['III'] = input("Enter marks for semester III: ")

# Step 4: Take user input for six subject names and store in a list
subjects = []
for i in range(6):
    subject = input(f"Enter name of subject {i+1}: ")
    subjects.append(subject)

# Step 5: Take user input for six subject marks and store in a tuple
marks = []
for i in range(6):
    mark = input(f"Enter marks for subject {i+1} in 4th semester mid term examination: ")
    marks.append(mark)
marks = tuple(marks)  # Convert the list to a tuple

# Adding all the values to the all_values list
all_values.append(name)
all_values.append(address)
all_values.append(semesters)
all_values.append(subjects)
all_values.append(marks)

# Function to calculate length of each value
def calculate_length(value):
    if isinstance(value, dict):
        return len(value)
    elif isinstance(value, (list, tuple)):
        return len(value)
    else:
        return len(value)  # Assuming it's a string

# Step 6: Use map() function to find the length of each value and print it
lengths = list(map(calculate_length, all_values))
print("Lengths of each entered value are:", lengths)