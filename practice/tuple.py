# create a tuple with 1 item
thisTuple = ("bittu")
# this is not the tuple this is the type string enclosed with a parenthesis
print(type(thisTuple))   
# to create the tuple with 1 item we have to define like this --->
tup = ("bittu",)
print(type(tup))

# *  we can also make a tuple by using the tuple() constractor
mytuple = tuple(("apple", "banana", "cherry"))
print(mytuple)

del mytuple
# print(mytuple)     #? this will raise an error because the tuple no longer exists

# ----------------------------------------------

#!          UNPACK TUPLES
fruits = ("apple", "banana", "cherry")
# here the number of veriables are equal to the number of elements in the tuple
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)


#?          Using Asterisk(*)
#*  If the number of variables is less than the number of values, you can add an (*) to the variable name and the values will be assigned to the variable as a {list}:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# here the number variables is not equal to the number of elements present in the tuple.. that's why we use the (*) symbol to print the remaining elements present in the tuple 
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

flowers = tuple(("lily", "rose", "lotus", "rosegold", "merigold"))
(*green, blue, red) = flowers
print(green)
print(blue)
print(red)

# ----------------------------------------------

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
# Multiply the fruits tuple by 2:
myTuple = fruits * 3
print(myTuple)

# ----------------------------------------------

thistuple = ("apple", "banana", "cherry")
for item in thistuple:
    print(item)

#!         Loop Through the Index Numbers
#* You can also loop through the tuple items by referring to their index number.
#? Use the [range()] and [len()] functions to create a suitable iterable.

for i in range(len(thistuple)):
    print(thistuple[i])

# !      using while loop
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1