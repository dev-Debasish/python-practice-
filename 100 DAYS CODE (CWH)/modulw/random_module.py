import random
#! not include the last item (10)
print(random.randrange(1,10))
#! include the last item (10)
print(random.randint(1,10))




import camelcase as cs 
c = cs.CamelCase()
txt = "debasish pal, how are you??"
print(c.hump(txt))

# print(dir(c.hump))

import platform

# print(dir(platform))

x = platform.system()
print(x)




#?   You can choose to import only parts from a module, by using the from keyword.

'''
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
'''
#!   import the module 
"""
    from mymodule import person1

print (person1["age"])
 """
 
#  FIXME:   When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

