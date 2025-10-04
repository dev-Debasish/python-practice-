tup = (10, "Virat", True, None, 18.56)
print(tup)
# make a copy of tuple 
print(tup[:])
# print element from any Index
print(tup[2])
# sliceing
print(tup[:4])
print(tup[2:])
print(tup[2:4])
# negative indexing
print(tup[-3])
print(tup[len(tup) - 3])
print(tup[5-3])
# jump indexing
print(tup[1:4])
print(tup[1:4:2])
# check for item
animals = ("lion", "tiger", "leopard", "jaguar", "black panther")
if "leopard" in animals:
    print("Yes!")
else:
    print("No!")

# ?---------------------------------------------------------------------

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
listOfTuple = list(thistuple)
print(listOfTuple)
listOfTuple.append("orange")
print(listOfTuple)
listOfTuple.pop(2)
print(listOfTuple)
listOfTuple[1] = "blue berry"
print(listOfTuple)
newTuple = tuple(listOfTuple)
print(newTuple)

# concate two tuple
t1 = (1, 5 , 8 , 9)
t2 = (1.02, 450.7, 87.125)
t3 = t1 + t2
print(t3)

# count()
res = thistuple.count("cherry")
print(res)
# index()
idx = newTuple.index("orange")
print(idx)


# !   ✅ tuple.index(value, start, end):

tup = (0, 1, 2, 3, 3, 4, 1, 3, 2)
result = tup.index(3,4,7)    # Search for value 3 between index 4 and 7 (7 not included)
print(result)
# 3 is found at index 4 that is within the range
