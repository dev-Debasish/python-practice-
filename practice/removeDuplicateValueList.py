myList = ["a","b","a","c","c"]
mylist = list(dict.fromkeys(myList))
print(mylist)


# using function 

def removeListDuplicateItem(x):
    return list(dict.fromkeys(x))

newList = ["a","b","a","c","c"]
newList = removeListDuplicateItem(newList)
print(newList)