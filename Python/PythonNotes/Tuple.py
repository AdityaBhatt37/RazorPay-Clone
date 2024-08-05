#TUPLES IN PYTHON
#->Tuples are immutable data types in python.(can not change).
#->T

a = (1,3,4,'aditya') #CREATION OF TUPLE WITH () parenthesis.
print(a)

Emptup = () #CREATION OF EMPTY TUPLE.
print(Emptup)


#SingleValueToup = (1) #WRONG WAY TO CREATE A SINGLE VALUE TUPLE.

SingleValeTup = (1,) #CORRECT WAY TO CREATE A SINGLE VALUE TUPLE.
print(SingleValeTup)


#METHODS OF TUPLE

tup = (1,2,3,4,5,5,1,2,3,4,5)

print(tup.count(5)) #Return the number of occorence of the value in a tuple.

print(tup.index(5)) #Return the first index occorence value.

#WHAT MAKES TOUPLE DIFFERENT FROM THE LIST
#That in python Touple are immutable means we cannot change their values.
#or we can say that reassignmet of values are not allowed in tuple.

print(tup[0])
#toup[0] = 33 #This will throw an error.