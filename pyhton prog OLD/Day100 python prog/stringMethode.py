# num1 = int(input())
# num2 = int(input())
num1 = input()
num2 = input()
print(int(num1) + int(num2))

str1 = "aBcDEFghIj"
print(str1.upper())
print(str1.lower())

str2 = " bittu pal "
str3 = "!!bittu pal !!"
print(str2.strip())
print(str3.lstrip("!"))
print(str3.rstrip("!"))

str4 = "bittu pal"
print(str4.replace("bittu", "abhi"))
print(len(str4))
print("\n")
for character in str4:
  print(character)
print(type(str4))

name = "bittu abhi"
print(name.split(" ")) #split the value and assigned it in a list..

code = "hello wORld"
print(code.capitalize()) # reconstruct the string

centeritem = "go to hell!!"
print(centeritem.center(40)) #assigned the string in a center
print(centeritem.center(40, "."))
print(len(centeritem))
cit2 = centeritem.center(40)
print(len(cit2))
print("\n\n")
str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))

countingno = "abhtibittu"
print(countingno.count("t")) # count the total no of character in the string and also count the substring ...
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

str5 = "my name is debasish pal.I am a student of midnapore college,lives in midnapore. !! "
# This string endswith space not ! --->
print(str5.endswith("!"))
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
# -----------------------------------------
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 5, 10))
# -----------------------------------------
txt = "Hello, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)
# -----------------------------------------

str6 = "he's bittu.he is a good boy"
# if it is false it throws -1..
print(str6.find("a"))
#the methode <index> throws an exception if and only if the substring is not found in the current string.--->
       # print(str6.index("nice"))

#The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
# it is not count any space
str7 = "welcome bittu.How can I help you?"
print(str7.isalnum())

# it is actually same as the <isalnum> but it doesn't contain the no's (0,9)..
str8 = "iambittu"
print(str8.isalpha())
# it is not count any space

# this methode checks all the character present in the string is lowercase or not if not then it throws false
str9 = "bittu pal"
print(str9.islower())

# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
str10 = "happy birthday to you\n"
#if there is any escape sequence or any puntuation left in the string then it is false
print(str10.isprintable())

# The isspace() method returns True only and only if the string contains white spaces, else returns False.
str11 = "        "  #using Spacebar
print(str11.isspace())
str12 = "        "  #using Tab
print(str12.isspace())

# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str13 = "Beyond the Limit"
print(str13.istitle())

# checks the each character of the string is upper case or not
str14 = 'WORLD HEALTH ORGANIZATION'
print(str14.isupper())

# The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
str15 = "Python is a Interpreted Language"
print(str15.startswith("Python"))

# this methode swap all the character as per its case either lowercase or uppercase
print(str15.swapcase())

# The title() method capitalizes each letter of the word within the string.
str16 = "hello bittu.how are you!"
print(str16.title())



