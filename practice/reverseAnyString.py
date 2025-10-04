txt = "bittu pal"
print(txt[::-1])

def reverseString(x):
    return x[-1::-1]
#!  or..
    # return x[::-1]

txt = reverseString("why your's mood is off today!!")

print(txt)







#! reverse technique

#? full reverse
#     x[::-1]     or..   x[-1::-1]

#? reverse without the last character..
#? means start from the 2nd last character
#   x[-2::-1]

#?  reverse withour the last 2 character
#?  means start from the 3rd last character
#    x[-3::-1]
