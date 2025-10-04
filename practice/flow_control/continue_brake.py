while True:
    print("Who are you?")
    name = input()
    if name != "debasish":
        continue
    print("hello, Debasish. What is the password: ")
    password = input()
    if password == "king":
        break
    else:
        print("Wrong password")
print("Access Granted!")
    
# Conditions will consider some values in other data types equivalent to True and False. When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True. 



'''
import sys
while True:
    print("Type exit to EXIT,")
    response = input()
    if response == "exit":
        sys.exit()
    print("You typed "+ response + ".")
    
'''