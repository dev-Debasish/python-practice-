s1 = {10, 12, 14, 16}
s2 = {15, 10, 25}
s1 = s1.union(s2)
print(s1)
print(type(s1))

st1 = {"bittu",10,False,"deb","bittu",15,True}
print(st1)

for item in st1:
    print(item)

if "bittu" in st1:
    print("YES!")
else:
    print("NO!")

# creating an empty set
s = set()
print(s)
print(type(s))

# todo:  Sets are unordered, so you cannot be sure in which order the items will appear.

#! ---------------------------------------------------------------------
# The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# the values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", False, 0, 2}
print(thisset)
# get the length of a set
print(len(thisset))
# we can also introduced a set just like this using set() constractor
thisSet = set(("bittu", 1 , False, 0, 13.5))
print(thisSet)
print(type(thisSet))
# this set() constractor can also used to initialize the empty set

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)     #? v.v.i

# another way to print all the items present in the set
for x in {'apple', 'banana', 'cherry'}:
  print(x)

#!  --------------------------------------------

# the isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False
x = {"apple", "orange", "kiwi", "avogardo"}
y = {"core", "google", "microsoft", "nvidia", "meta"}
z = x.isdisjoint(y)
print(z)

# it returns false as "apple" present in the both sets
fruits = {"apple", "banana", "cherry"}
company = {"google", "microsoft", "apple"}
new = fruits.isdisjoint(company)
print(new)

#! --------------------------------------------

#? 'x' is subset of 'y' means that all items in 'x' are present in 'y', then it returns true else false..
x = {'a', 'b', 'c'}
y = {'f', 'g', 'h', 'a', 'b', 'c'}
# check that 'x' is subset of 'y' or not.
z = x.issubset(y)
print(z)

#* as short we use this  [<=] operator
z = x <= y
print(z)

#? if not all items in the set 'x' are present in set 'y', then it returns False.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
# z = x <= y
z = x.issubset(y)
print(z)

#!  issuperset() is the opposite of the previous issubset() method
x = {'a', 'b', 'c'}
y = {'f', 'g', 'h', 'a', 'b', 'c'}
# check that 'y' is superset of 'x' or not
z = y.issuperset(x)
print(z)

#* as short we use this  [>=] operator
z = y >= x
print(z)

#? if not all items in the set 'x' are present in set 'y', then it returns False.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
# z = x >= y
z = y.issuperset(x)
print(z)

