# lists are mutable.
l = [1,87,56,48,95,100,45]
print(l)

# print(l.append(30))    # returns None
l.append(30)    # adds new element at the end of the list
# you have to print the list as the append method adds the element at the last of the list
print(l)  

# print(l.sort())
l.sort()        # sorting in incresing order
print(l)
# print(l.sort(reverse = True))
l.sort(reverse = True)       # sorting in decresing order
print(l)    

lst = [56,45,25,6,450,72,1]
# print(lst.reverse())
lst.reverse()          # reverse the exiting list
print(lst)

l2 = [45,11,87,56,45,89,87,45]
print(l2.index(56))       # find out the index of an element present in the list
print(l2.count(87))       # find out occurence of an element present in the list

# m = l2      # it changes the original list 
# m[0] = 5
# print(l2)    

m = l2.copy()
m[0] = 5
print(m)
print(l2)
# we can also copy a list by using list() method
lst3 = [1, 45, 8, 98]
newlist = list(lst3)
print(newlist)
# also make a copy of list using slice operator [:]
copyList = lst3[:]
print(copyList)


# insert() method add a new value to the list within a specific index, but not replaced by the old one
#  the old value on that poisition is shifted to the next index and so on...
l2.insert(4,100)
print(l2)

# append() method in list adds the new element at the last of the list. But in the case of extend() method it adds the another full list at the end of the current list & makes a new list with the new length.
books = ["Deep Work", "Atomic Habit"]
author = ["Cal Newport", "......"]
books.extend(author)
print(books)

# join / concatenation 
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# concatenation / join
a = [1, 37, 2, 8]
b = [10, 100, 45, 56]
print(a + b)

# join / concatenation
# ***
for item in b:
    a.append(item)
print(a)


