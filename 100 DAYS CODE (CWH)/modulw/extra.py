# import sys
# print(sys.version)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x+y+z)

# x = 5
# y = "John"
# print(x,y)

import random
print(random.randrange(1,10))


# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
print(bool("bittu"))
print(bool(10))
# all of them are returns false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
print(isinstance(2,int))
print(isinstance(1j,complex))






