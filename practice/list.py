# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))

# list constractor
newList= list(("abc","def","abd"))
print(newList)


'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''

# ----------------------------------------------------------------------------

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
thislist[1] = "guava"
print(thislist)

lst1 = thislist.copy()
lst1[1:3] = ["watermelon", "blue berry"]
print(lst1)
# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
lst1[1:2] = ["lotus", "rose", "lily"]  
print(lst1)
# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
lst1[1:5] = ["mango"]
print(lst1)

# --------------------------------------------------------------------------
# the remove() method removes the specified item present in the list
# if there are many occurence of that item it removes the item which is in the first occurence
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# if you remove the element at a specified index we use [pop(index no)] method
thislist.pop(1)
print(thislist)
# if you are not defined the index no inside the pop() method it removes the last item of the list by default
thislist.pop()
print(thislist)

# the del keyword also remove at the specified index
newList1 = [10, 45, "swiss", True]
del newList1[0]
print(newList1)
# The del keyword can also delete the list completely.
del newList1
# *  this will cause an error because you have succsesfully deleted "thislist".
# ? print(newList1)   
# clear() method clears the content of the list..
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# ------------------------------------------------------------------------------
#             LOOP THROUGH THE LIST
thislist = ["apple", "banana", "cherry"]
for item in thislist:
    print(item)

# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
for i in range(len(thislist)):
    print(thislist[i])

# using WHILE LOOP
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:

[print(item) for item in thislist]
# or.
l = [item for item in thislist]
print(l)

