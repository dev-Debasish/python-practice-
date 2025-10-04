# if ladder 
a = 30
b = 200
if (a > b):
    print("a is grater than b")

# if-else ladder
if(a > b):
    print('a')
    print("yes!")
else:
    print('b')
    print("no")
print("done~")   # outside the if-else ladder, it prints always for every execution

# if-elif-else ladder
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# nested-if ladder
x =41
if x > 10:
   print("it is above 10")
   if x > 20:
    print("It is also above 20!")
   else:
    print("but not above 20")
      
# shorthand if
if a > b: print("a > b")

# shorthand if-else
print('a') if a > b else print('b')

# One line if else statement, with 3 conditions:
a = 330
b = 330
print('A') if a > b else print("=") if a == b else print('B')

# logical and
a = 200
b = 33
c = 500
if a > b and a > c:
   print("both conditions are true!")
# logical or
if a > b or a > c:
   print("atleast one condition is true!")

# logical not
a = 33
b = 200
if not a > b:
   print("a is not grater than b :>")

# --------------------------------------------------------------------------------

#    if  cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
   pass
# having an empty if statement like this, would raise an error without the pass statement

# --------------------------------------------------------------------------------
# name = "debasish"
name = input("Enter your name: ")
# password = "emperor"
password = input("Enter the password: ")
if name == "debasish":
   print("hello, Debasish")
   if password == "emperor":
      print("Access Granted")
   else:
      print("Wrong Password, Access Denied!!")

# --------------------------------------------------------------------------------