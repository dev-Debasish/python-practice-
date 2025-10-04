fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for item in fruits:
    if 'a' in item:
        newlist.append(item)

print(newlist)

# we can do all this things in oneline by using list comprehension
newlist1 = [item for item in fruits if 'a' in item]
print(newlist1)
# -----------------------------------------------
# newlist = [expression for item in iterable if condition == True]
'''
The return value is a new list, leaving the old list unchanged.
'''
# -----------------------------------------------
# Only accept items that are not "apple":
lst = [x for x in fruits if x != "apple"]
print(lst)

new = [x for x in fruits]
print(new)

numList = [x for x in range(10) if x < 5]
print(numList)

upperCaseItem = [x.upper() for x in fruits]
print(upperCaseItem)


# You can set the outcome to whatever you like:
# Set all values in the new list to 'hello':
[print("hello") for x in fruits]
# or.
setItem = ["hello" for x in fruits]
print(setItem)

# Return "orange" instead of "banana":
changeItem = [x if x != "banana" else "orange" for x in fruits]
print(changeItem)

# --------------------------------------------------
# Sort the list based on how close the number is to 50:
# You can also customize your own function by using the keywordArgument [key = function].

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

'''
The code provided sorts a list of numbers based on how far each number is from 50. Here's how it works step-by-step:

Explanation:

Function myfunc:
Takes a number n as input and calculates the absolute difference between n and 50.

Key Parameter in sort:
#! [The sort method is provided a key function], myfunc.
This means each element in the list is passed to myfunc, and the list is sorted based on the return value of myfunc.

Sorting Logic:
The function myfunc returns how far each number is from 50.
Numbers closer to 50 will have a smaller key value and will appear earlier in the sorted list.

Input List:
The input list is [100, 50, 65, 82, 23].

Sorting Process:
For each number in the list:
#!!
myfunc(100) = abs(100 - 50) = 50
myfunc(50) = abs(50 - 50) = 0
myfunc(65) = abs(65 - 50) = 15
myfunc(82) = abs(82 - 50) = 32
myfunc(23) = abs(23 - 50) = 27
# !!
The list is sorted based on these values: [0, 15, 27, 32, 50].

Output:
The sorted list is: [50, 65, 23, 82, 100].

'''

# ---------------------------------------------
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# Case sensitive sorting can give an unexpected result:

thislist = ["banana", "orange", "Kiwi", "Cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as [key functions] when sorting a list.

# So if you want a case-insensitive sort function, use [str.lower] as a key function:

thislist.sort(key = str.lower)
print(thislist)

# ----------------------------------------------

