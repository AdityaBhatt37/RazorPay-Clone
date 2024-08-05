
#DICTIONARY IN PYTHON
#->Dictionary in python is a collection of key value pair.
#->Means collection of a key and value stored corresponding to it.

#Syntax
'''
Name_Of_Dictionary = {

      "key" : "value",
      
      "key2" : "values"
}
'''


Dic = {

    "My Dic" : "So fast",
    "fast" : "Quick way to do something",
    "positive numbers " : [1,2,3,4,5,'...']
}

print("The values stored in Dic Dictionary is : ",Dic) #Accesing full dictionary

print("The value stored in key 'My Dic' is : ",Dic["My Dic"]) #Accessing the single value of a dictionary

#print("Trying to ecess a key value which is not available in our dictionary : ",Dic["number"]) #This will throw an error and program will terminate

#So, if you dont want an error so we can use a "get()" method.

print("Trying to ecess a key value which is not available in our dictionary : ",Dic.get("number")) #This print 'none' if key does not present
                                                                                                   #And program will not terminate
                                                                                  
print("Accesing the all keys of dictionary not their values : ",Dic.keys(),"\n")

#BELOW IS THE USE OF LOOP ON 'keys()' method to get the values stored in all keys.
print("#BELOW IS THE USE OF LOOP ON 'keys()' method to get the values stored in all keys.")
for i in Dic.keys():

    print(Dic[i]) #simple way
    
    

for k in Dic.keys():

    print(f"The value correspoinding to key '{k}' is : '{Dic[k]}' ")



# In Python, f-strings are a type of string literal that allows you to embed expressions inside of them. 
#This makes it easier to format strings and add dynamic content to them.
# To use an f-string, you simply need to prefix the string with the letter f. 
#You can then embed expressions inside of the string using curly braces ({}). 
#Python will evaluate the expressions at runtime and insert the results into the string.
# For example, the following code would print the string "Hello, John!" to the console:
# Python


# name = "John"
# print(f"Hello, {name}!")


Dicn ={

 1:"one",
 2:"two",
 3:"three"

}

print(Dicn.items()) #itmes() method will print the dictionary keys along with its vlaue which are packed as an tuple.

Dic2 = {

    "my" : "mine",
    "Hello" : "World",

    "Dic2Child " :  {

        "CPU" : "Centeral Processing Unit",
        'PC' : "A Register inside CPU(Program Counter)"

    }

}



