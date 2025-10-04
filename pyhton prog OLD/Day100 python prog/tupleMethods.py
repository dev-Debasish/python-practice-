##  Manipulating Tuples
# ------->Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

###---> after changing the tuple in to the list we can perform the list operation on that and then convert to tuple. 

fruits = ("licchi","mango","guava","waterMalon")
print(fruits)
temp = list(fruits) 
print(temp)
temp.append("dragonFruit")    # add item
print(temp)
temp.pop(2)                   # remove item
print(temp)
temp[1] = "apple"             # change item
print(temp)
fruits = tuple(temp)   #* after the changes, we can change the veriable name of the tuple or. use this pervious veriable name 
print(fruits)


### ---> we can also concatinate two or more tuple into a one tuple as it is create a new tuple..
flower = ("lotus","lili","...")
print(flower)
myFavourite = fruits + flower
print(myFavourite)


# -----> we can use some built-in methode in the tuple that are--->
# --> count()
res =fruits.count("licchi")   # --> it tells that how many time the element present in the tuple
print(res)
# ---> index()
# ! if the element is not present in the tuple the index() method throws an error
res2 = fruits.index("waterMalon")   # --> it tells the index of the item
print(res2)
# ---> we can also change the occurence of the tuple by indexing...

tup = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res3 = tup.index(3,4,8)     # --->(element,start,end)
print('First occurrence of 3 is', res3)

