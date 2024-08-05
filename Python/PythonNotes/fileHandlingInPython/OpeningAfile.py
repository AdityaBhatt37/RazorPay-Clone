#FILE HANDLING IN PYTHON
#Python provides us features to perform operation and manipulate a file

#OPENING A FILE
# Before we can perform any operations on a file, we must first open it. 
# Python provides the open() function to open a file. 
# It takes two arguments: the name of the file and 
# the mode in which the file should be opened. 
# The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.


# MODES IN FILE
# There are various modes in which we can open files.

# read (r): This mode opens the file for reading only and gives an error if the file does not exist. 
#           This is the default mode if no mode is passed as a parameter.

# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

# create (x): This mode creates a file and gives an error if the file already exists.

# text (t): Apart from these modes we also need to specify how the file must be handled. 
#           t mode is used to handle text files. t refers to the text mode. 
#           There is no difference between r and rt or w and wt since text mode is the default. 
#           The default mode is 'r' (open for reading text, synonym of 'rt' ).

# binary (b): used to handle binary files (images, pdfs, etc).


#READING A FILE IN PYTHON
f = open("myfile.txt","r") #'r' mode is by default in python

readd = f.read()

print(readd)


#WRITE A FILE IN PYTHON
#->If a file is not created and we open a file in 'W' or "a" mode then the file is created automatically.
#->write mode delete the previous all content of the file and then print the new one.
#->On the other hand "a" append mode does not delete the content it add the new one from the last.

wr = open("myfile.txt","w")

wr.write("Hello Python file handling is here")

wr.close() #This is how we close the file in python


ap = open("myfile.txt","a")

ap.write("1,2,3,4,5.....infinite")

ap.close()#file closing is so necessary in pyton other wise if the file is empty then the content will
          #not written in the text file.


#IF WE DONT WANT TO USE THE close() to close file always we can use "WITH" keyword

with open("myfile.txt","a") as ob:
    ob.write(" ALL IS WELL") #using with keyword it automatically close() the file.






