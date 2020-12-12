#
#PURPOSE    : To Play arround with Sets, Understand its Functionalities.
#DATE       : 12-DEC-2020
#AUTHOR     : prakashvel.periyannan@gmail.com
#REFERENCE  :https://www.w3schools.com/python/python_sets.asp


# FEATURES OF SET 
# Set items are unordered, unchangeable, and do not allow duplicate values.

fruits = {"apple","banana","pears"}
print("DEBUG:fruits"+str(fruits)) #Type Conversion is Need as we are combining the STR and SET

#Answer DEBUG:fruits{'pears', 'banana', 'apple'}


#DUPLICATE
fruits = {"apple","banana","pears","apple"}
print("DEBUG:fruits"+str(fruits)) #Type Conversion is Need as we are combining the 

#DEBUG:fruits{'banana', 'pears', 'apple'}
#ANSWER Even if you add it does not show when u print them.

#DIFFERENT Data Type 
basket={2,"apple",2.5, True}
print ("My Basket Contains: "+str(basket))
#ANSWER If you keep 1 and True , Only 1 will be printed and True will not be.

#TYPE of SET
print (type(basket))
#ANSWER <class 'set'>

fruits = set(("apple","pears","oranges"))
print(fruits)
print(type(fruits))

# ANSWER 
# {'oranges', 'pears', 'apple'}
# <class 'set'>

#Iterating the values in set use For €loop
for items in fruits:
    print(items)
#ANSWER: Order is not Gaurnteed during the Printing Time.
# pears
# apple
# oranges

#Check if the Value is present in the SET or Not is important.
print ("apple" in fruits)
#ANSWER: True

#Add an item to a set
fruits.add("Kiwi")
print(fruits)
#ANSWER
#ORIGINAL SET {'oranges', 'pears', 'apple'}
#AFTER ADDING {'oranges', 'Kiwi', 'pears', 'apple'}

#Adding the set to another set using update keyword.
waterey_fruits = {"Water Mellon", "Musk Mellon" ,"coconut"}
fruits.update(waterey_fruits)
print(fruits)
#ANSWER : {'apple', 'pears', 'oranges', 'coconut', 'Water Mellon', 'Musk Mellon', 'Kiwi'}


#Adding the List to the set.
fruits_list = ["sapota","butterfruit","cherry"]
fruits.update(fruits_list)
print(fruits)
#ANSWER : {'oranges', 'pears', 'sapota', 'coconut', 'apple', 'Musk Mellon', 'cherry', 'Water Mellon', 'butterfruit', 'Kiwi'}

# Note: If the item to remove does not exist, remove() will raise an error.[Key Error]
fruits.remove("apple")
print (fruits)
#ANSWER
# {'Kiwi', 'Musk Mellon', 'butterfruit', 'pears', 'oranges', 'coconut', 'sapota', 'cherry', 'Water Mellon'}

# Note: If the item to remove does not exist, discard() will NOT raise an error.
fruits.discard("apple")
print (fruits)
#ANSWER
# {'Kiwi', 'Musk Mellon', 'butterfruit', 'pears', 'oranges', 'coconut', 'sapota', 'cherry', 'Water Mellon'}


#Removing the Last Item from the 
# You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

# The return value of the pop() method is the removed item.
removedvalue = fruits.pop()
print ("removedvalue:"+removedvalue)
print (fruits)

# ANSWER
# removedvalue:sapota
# {'coconut', 'Kiwi', 'oranges', 'butterfruit', 'cherry', 'Musk Mellon', 'Water Mellon', 'pears'}

#Clear Empties the Set
fruits.clear()
print (fruits)

# ANSWER
# set()

del fruits
#print (fruits)

# ANSWER
# Will Raise Error Fuits is not defined
