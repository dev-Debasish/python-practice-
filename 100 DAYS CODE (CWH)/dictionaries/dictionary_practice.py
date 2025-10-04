dic = {"name" : "bittu", "age" : 21, "birthPlace" : "kusumda"}
print(dic)
# print the empty dictionary
d1 = {}
print(d1)
print(type(d1))
# print the length of the dictionary
print(len(dic))
# as the dictionary is ordered and indexed so, we can access the items of the dictionary by the key
print(dic["birthPlace"])
print(dic["name"])
print(dic["age"])

#  if you want specifecly the keys of the dic
print(dic.keys())
# print the all the keys of the dic 
for key in dic:
    print(f"the key {key} is  {dic[key]}")
# or
for key in dic.keys():
    print(f"the key {key} is {dic[key]}")

# print only the values of the dictionary
print(dic.values())

for values in dic.values():
    print(f"the value is {values}")

# print both the keys and the values of the dictionary
print(dic.items())

for key, value in dic.items():
    print(f"the value of the key {key} is {value}")
    

#! -----------------------------------------------------
# dictionary doesn't contain the duplicate values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

# It is also possible to use the dic() constructor to make a dictionary.
thisdict = dict(name = "debasish", age = 21, country = "India")
print(thisdict)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
# before the change
print(x)
car["color"] = "deepBlack"
# after the change
print(x)

# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
# before the change
print(x)
car["year"] = 1972
# after the change
print(x)

# Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
# before the change
print(x)
car["color"] = "black"
# after the change
print(x)

# ? all this are same in the items() method


# To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "brand" in thisdict:
  print("Yes! 'brand' is one of the keys in the thisdict dictionary")

# ------------------------------------------

#! we can use this for [adding items]

# You can change the value of a specific item by referring to its key name:
thisdict["year"] = 2021
print(thisdict)

# we will do the same thing by using the update() method
thisdict.update({"year" : 2020})
print(thisdict)

# the pop() method removes the item with the specified key name:
thisdict.pop("brand")
print(thisdict)

# The popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)

# del keyword removes the item with the specified key name 
del thisdict["model"]
print(thisdict)
# del keyword also delete the dictionary completely
del thisdict
# print(thisdict)     #! that throws error while after deleting the dictionary there is no meaning to print it 

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# ----------------------------------------------

#!  LOOP THROUGH A DICTIONARY
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Print all key names in the dictionary, one by one:
for key in thisdict:
  print(key)
#? or
  # You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)

# Print all values in the dictionary, one by one:
for value in thisdict:
  print(thisdict[value])
#? or.
# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

# ----------------------------------------------------

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
dict1 = {1 : "abhi", 2 : "deb" }
dict2 = {"you" : "me", "me" :"you"}
dict1 = dict2
print(dict1)
dict1[2] = "bittu"
print(dict2) 

# sometimes we don't need to change the original one, beside this we make a copy of it ..
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict().
mydict = dict(thisdict)
print(mydict)

# --------------------------------------------------------------------------

#!  NESTED DICTIONARY
# type 1
myfamily = {
   "child1" : {
      "name" : "Debasish",
      "age" : "21",
      "birth" : 2003
   },
   "child2" : {
      "name" : "santu", "age" : 21, "birth" : 2003
   },
   "child3" : {
      "name" : "suvajit",
      "age" : 28,
      "birth" : 1996
   }
}
print(myfamily)

# type 2
child1 = {
  "name" : "Debasish",
  "age" : 21,
  "birth" : 2003
}
child2 = {
  "name" : "santu",
  "age" : 21,
  "birth" : 2003
}
child3 = {
  "name" : "suvajit", "age" : 28, "birth" : 1996
}

myfamily = {
   "child1" : child1, "child2" : child2, "child3" : child3
}
print(myfamily)

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
print(myfamily["child1"]["name"])
print(myfamily["child2"]["age"])
print(myfamily["child3"]["birth"])

print("--------------------------------------")

# You can loop through a dictionary by using the items() method like this:
for child, status in myfamily.items():
   print(child)
   
  #  for value in status:
  #     print(value , ":" , status[value])
  
   for key, value in status.items():
     print(f"{key} : {value}")

print("--------------------------------------------------")
# ----------------------------------------------------------

# the fromkeys() method returns a dictionary with the specified keys and the specified values
#? it is the method of creating dictionary from the tuple 
x= ('key1', 'key2', "key3")
y = (5, 6, 7)
newdict = dict.fromkeys(x, y)
print(newdict)
y = 0
newdict = dict.fromkeys(x, y)
print(newdict)

#* keys	Required. An iterable specifying the keys of the new dictionary
#? value	Optional. The value for all keys. Default value is None
#! dict.fromkeys(keys, value)

# Default value is None
x = ('key1', 'key2', 'key3')
dic = dict.fromkeys(x)
print(dic)

# --------------------------------------------------------------

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# dictionary.setdefault(keyname, value)
x = car.setdefault("model", "AMG")
print(x)
'''
Explanation:
The setdefault() method of a dictionary returns the value of the specified key if it exists. If the key does not exist, it inserts the key with the specified value and returns that value.
In this case, the key "model" already exists in the car dictionary with the value "Mustang".
Therefore, setdefault("model", "AMG") simply prints "Mustang" without making any changes in the dictionary.
'''
y = car.setdefault("color" , "black")
print(y)

#FIXME:  Default value None
# as the key name age is not defined so, it returns None as the default value..
z = car.setdefault("age")
print(z)


