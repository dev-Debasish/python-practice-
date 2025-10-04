#----------------------------------------------------------------------
# String Introduction

name = "bittu"
print("hello" + name) # it is also the kind of print the value of a variable
print("hello",name)

print("I am Debasish Pal~!!")
print("how are \"you\"")
print('how are "you"')

a = ''' hello I am debasish pal
        I am the Trillionear (# NO.1)
        now, I am learning DATA SCIENCE
'''
print(a)
# or.....
b = """hello I am debasish pal
        I am not doing well 
        now, I am learning Python
"""
print(b)

arrayOfString = "hello,"
#  by default the print function is end with '\n'
print(arrayOfString[0])
print(arrayOfString[1])
print(arrayOfString[2])
print(arrayOfString[3])
print(arrayOfString[4])
print(arrayOfString[5])
# print(arrayOfString[6])  # can't access as the string length is 5

# using for loop
for character in arrayOfString:
    print(character)

#  find length of the string
print(len(arrayOfString))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword "in", that returns in boolean
txt = "The best things about life is independency!"
print("independency" in txt)   # it returns the boolean as result

# Use it in an if statement:
if "independency" in txt:
    print("YES")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not "in" & returns in boolean
print("expensive" not in txt)   # it returns the boolean as result

# Use it in an if statement:
if "expensive" not in txt:
    print("NO")

#------------------------------------------------------------------------
# String Slicing

slicedString = "Hello, World!"
print(len(slicedString))
print(slicedString[2:5])
# slice from the start
print(slicedString[:5])
# slice to the end
print(slicedString[2:])
# negative slicing
print(slicedString[-5:-2])
# print(slicedString[len(slicedString)-5:len(slicedString)-2])
print(slicedString[8:11])

#---------------------------------------------------------------------------
# modify strings
# strings are immutable we can't modify the strings but we can change it and returns it in a new variable
# string methods are doing the same things 
a = " Hello, World! "
print(a.upper()) # returns the string in uppercase letter
print(a.lower()) # returns the string in lowercase letter
print(a.strip())   # remove the whiteSpace from the beginning as well as the ending
str3 = " !!bittu pal !!"
#!  here the str3 is startswith the <space> so it is not strip the string 
print(str3.lstrip("!"))
print(str3.rstrip("!"))
# this leftStrip and rightStrip method are used to remove the exact thing that is inside the parenthesis but not remove the whitespace
a = "Hello, World!"
print(a.replace("World", "bittu"))   # replace a string with another string
print(a.split(","))  # The split() method splits the string into substrings if it finds instances of the separator, and return as a list

#--------------------------------------------------------------------------
# string concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#----------------------------------------------------------------------
# string methods
txt = "hello, and welcOMe to my world."
print(txt.capitalize())
# The casefold() method returns a string where all the characters are lower case.
print(txt.casefold())
# This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.

centeritem = "go to hell!!"
print(centeritem.center(40)) #assigned the string in a center
print(centeritem.center(40, "."))
print(len(centeritem))
cit2 = centeritem.center(40)
print(len(cit2))
str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))

# txt = "I love apples, apple are my favorite fruit"
# print(txt.center(50))
# print(txt.center(50,"*"))


# w3 school string method check out....-->

txt = "I love apples, apple are my favorite fruit"
print(txt.count("apple"))
# string.count(value, start, end)
print(txt.count("apple",10,24))
# returns the no. of occurences of apple in 'txt'


# -----------------------------------------------
# string.encode(encoding=encoding, errors=errors)
txt = "My name is Ståle"
print(txt.encode())
# 'backslashreplace'	- uses a backslash instead of the character that could not be encoded
# 'ignore'	- ignores the characters that cannot be encoded
# 'namereplace'	- replaces the character with a text explaining the character
# 'strict'	- Default, raises an error on failure
# 'replace'	- replaces the character with a questionmark
# 'xmlcharrefreplace'	- replaces the character with an xml character
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))


txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2)) # add 2 space in \t places
print(txt.expandtabs(4))
print(txt.expandtabs(10))

txt1 = "My name is {fname}, I'm {age}"
print(txt1.format(fname = "bittu", age = "21"))
txt2 = "My name is {0}, I'm {1}"
print(txt2.format("deb",21))
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt3)


a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())




