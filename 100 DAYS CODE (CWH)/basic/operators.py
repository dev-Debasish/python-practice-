x = 4
y = 3
print(x + y)    # addition
print(x - y)    # substraction
print(x * y)    # multiplication
print(x / y)    # divission
print(x % y)    # modulus
print(x // y)   # floor divission    //it is the the same as divission operator but only returns the int value 
print(x ** y)   # exponential

# -----------------------------------------------------------------------------------------------

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# --------------------------------------------------------------------------------------------

x = ["apple", "banana"]
print("apple" in x)
print("orange" not in x)

# ---------------------------------------------------------------------------------------------

print(~3)

"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""
# ------------------------------------------------------------------------------------------------

print(3 << 2)

"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
# ------------------------------------------------------------------------------------------------------

print(8 >> 2)

"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

# ----------------------------------------------------------------------------------

print(r'That is Carol\'s cat.')    # raw string that prints the backslash also

# string concatenation
print("deb" + "bittu")
# print('Alice' + 42)      # not possible

# string replication
print("deb" * 3)
# print("deb" * 3.0)        # not possible
# print("deb" * "bittu")    # not possible

# -------------------------------------------------------------------------------=+
print('What is your age?')    # ask for their age
myAge = input()
# myAge = int(input())
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
print("you are" + str(myAge) + "years old")
print("you are " + str(myAge) + " years old")
# print("you are " + myAge + " years old")     # throws an error
print("you are",myAge,"years old")
# --------------------------------------------------------------------------------=+

print(len(""))  # returns 0
# space is also a character and it also has a length
print(len(" "))  # returns 1

# print(int("9.02"))
# The code print(int("9.02")) will raise a ValueError because the int() function cannot directly convert a string containing a decimal (e.g., "9.02") into an integer.
print(int(float("9.02")))  # Output: 9

'''
>>> 42 == '42'
False
>>> 42 == 42.0
True
>>> 42.0 == 0042.000
True

Python makes this distinction because strings are text, while integers and floats are both numbers.
'''

# ----------------------------------------------------------------------------------------------------------------------------

# partition method returns tuple where split method returns lists.
print("hello, world!".partition("o"))
# If the separator string you pass to partition() occurs multiple times in the string that partition() calls on, the method splits the string only on the first occurrence:

# If the separator string can’t be found, the first string returned in the tuple will be the entire string, and the other two strings will be empty:
print("hello, world!".partition("xyz"))

# -----------------------------------------------------------------------------------------------------------------------------

print("hello".rjust(10,'*'))
print("hello".ljust(10,'*'))
print("hello".center(10,'*'))

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# ------------------------------------------------------------------------------------------------------------------------
print(ord('A'))
print(chr(65))
print(ord('A') < ord('B'))
print(chr(ord('A') + 1))
# -----------------------------------------------------------------------------------------------------------------------

# The bitwise NOT operator (~) inverts the bits of its operand. In Python, integers are represented in binary using two's complement notation.
# The two's complement of a number is obtained by inverting its bits and adding 1. Therefore, the bitwise NOT operator can be expressed as: 
# !!   ~x == -x - 1
print(~20)

