# adding one item in the set 
thisSet = {"apple", "banana", "cherry"}
thisSet .add("orange")
print(thisSet)
# adding the entire set in an another set we use the update() method
tropical = {"pinaapple", "papaya", "mango"}
thisSet.update(tropical)
print(thisSet)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# !-------------------------------------
# to remove an item from the set , we use remove() or discard() method

# * but the discard() does not raise any error 
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# ? if we want to remove an specific item from the set but the item is not present in that, the remove() method raise the error message
# thisset.remove("orange")
# print(thisset)

#!   we can also use the pop() method to remove an item, but this method will remove an random item,so you can't be sure what item it gets removed
#  the return value of the pop() method is the removed item
x = thisset.pop()
print(x) 

# the clear() method empties the content of the set
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
del thisSet
# print(thisSet)   #! it throws an error as we want to print the set that we are deleted

# The copy() method copies the set.
fruits = {"apple", "banana", "cherry"} 
x = fruits.copy()
print(x)

