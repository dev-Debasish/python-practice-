i = 1
while i < 5:
    i += 1
    print(i)
# --------------------------------------------------------------------------------
i = 1
while i < 5:
    print(i)
    i += 1

# --------------------------------------------------------------------------------
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1

i = 0
while i < 5:
    print(i)
    if i == 3:
        break    
    i += 1
    #* we can use the increment logic after the break statement  
    #! but you are not doing the same for the continue statement
print("\n")
# --------------------------------------------------------------------------------

num = 1
while num < 10:
    if num == 5:
        num += 2     #?  to avoid infinite loop we should increment it before continue statement
        continue
    print(num)
    num += 2

#  while loop with else 
k = 0
while k < 3:
    print(k)
    k += 1
else:
    print("ALL DONE !!")

# -------------------------------------------------------------------------------- 
#!   if condition: states the print function to execute only once if the condition is true
print("------------------------------")
spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1
print("------------------------------")
# --------------------------------------------------------------------------------
#!  it is prints the content as long as the condition is true 
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
# --------------------------------------------------------------------------------
name = ""
while name != "debasish":
    print("Please Enter your Name: ")
    name = input()
print("Thank You")

# or

'''
# while True:
#     print("please enter your name: ")
#     name = input()
#     if name.lower() == "deb":
#         break
# print("Thank you")

'''

# --------------------------------------------------------------------------------


