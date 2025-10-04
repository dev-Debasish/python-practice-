print("hello world :) ")

# this is prints the line as it's own formate with the proper indentation
print('''
Numeric data: int, float, complex
int: 3, -8, 0

float: 7.349, -9.0, 0.0000001

complex: 6 + 2i

more on numeric data types in the number chapter.
''')
# --------------------------------------------------------------------------------  
# for multiline comment  """ write this inside it """ or ''' inside it '''
# we have to be used the escape sequence mostly in the program
# every print function ends with a '\n' esp sequence by default
# there would be something called sep operator by default sep operator = (space)
# --------------------------------------------------------------------------------
n ="10"   # string
a = True  #boolean type 
b = None  # none type
c = 9.09  # float
d = "abc"  # string 
print(a)
print(b)
print(c)
print(d)
print(n)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(n))

print(int(n))   # type conversion from (string) to (int) 
print(type(int(n)))  
# ----------------------------------------------------------------------------
flt1 = -8.35245     #decimal number
flt2 = 0.000001     #decimal number
flt3 = 2.6E44       #exponential number
flt4 = -6.022e23    #exponential number
print(type(flt1))
print(type(flt2))
print(type(flt3))
print(type(flt4))
# ----------------------------------------------------------------------------
# pylance knows the complex numbers imaginary part selector by 'j' or 'J' .
cmplx1 = 2 + 4j
cmplx2 = -(3 + 7j)
cmplx3 = -4.1j
cmplx4 = 6j
print(type(cmplx1))
print(type(cmplx2))
print(type(cmplx3))
print(type(cmplx4))

print(complex(4, 2))
c1 = -45.5
print(complex(c1))

num1 = 8.4
num2 = int(num1)
num3 = complex(num1)
print(num2)
print(num3)
# --------------------------------------------------------------------------
#  variable ,  
Color = "yellow"    #valid variable name
cOlor = "red"       #valid variable name
_color = "blue"     #valid variable name

# 5color = "green"    #invalid variable name
# $color = "orange"   #invalid variable name

NameOfCity = "Mumbai"       #Pascal case
nameOfCity = "Berlin"       #Camel case
name_of_city = "Moscow"     #snake case
# --------------------------------------------------------------------------
icecream = "Vanilla"    #global variable
def foods():
    vegetable = "Potato"    #local variable
    fruit = "Lichi"         #local variable
    print(vegetable + " is a local variable value.")

foods()
print(icecream + " is a global variable value.")
#  as the fruit variable in local variable so we can't declear it at outside of the block..
# print(fruit + " is a local variable value.") 
# ---------------------------------------------------------------------------

# datatype ,,

# list
l1 = [-4, 8.2, [-7, 9], ["apple", "mango"]]
print(l1);

# tuple
t1 = (("lichi", "blueberry"), ("rose", "lotus"))
print(t1)

# range
for i in range(4,14,2):
    print(i, end = ",")

# set
s1 = {4, 8.5, -7, 10}
print(s1);

# dictionary
d1 = {"name" : "Debasish", "age" : 20, "canVote" : True}
print(d1);

# bytes
str1 = "this is a string";
print(bytes(str1, 'utf-8'))
print(bytes(str1, 'utf-16'))
print(bytes(4));

# bytearray
print(bytearray(str1, 'utf-8'))
print(bytearray(str1, 'utf-16'))
print(bytearray(4));

# memoryview()
str = bytes("abc", 'utf-8')
mvStr = memoryview(str)
print(list(mvStr[0:]))

#  boolean chapter 

print("Empty string:" ,bool(""))   

#  in bool the empty {tuples, lists, dictionary, sets, string} returns {false}  
#  and every non-empty {tuples, lists, dictionary, sets, string} returns {true}  

#  in numbers the value 0 returns the false && any +ve and -ve real numbers it returns true. 

print(bool(None)) # false

#  operator,,


