# [try] block lets you to test a block of code for errors

#* [except] block handles the error

''' [else] block lets you execute code when there is no error '''

#! [finally] block lets you execute code, regardless of the result of the try-and except blocks.   the content of the [finally] block is always executed regardless the program throws any kind of errors.
#? it perfectly defines when we used it inside  the function

# The try block will generate an exception, because x is not defined:
try:
    print(x)
except Exception as e:
    print(e)
# or.
except:
    print("An error occured")

# since the try block raises an error, the except block will be executed.
# without the try block, the program will raise an error

#?    You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

try:
    print(x)
except NameError:
    print("variable x is not defined!")
except:
    print("something else went wrong!")
    

# ---------------------------------------------------------------------
# You can use the else keyword to define a block of code to be executed if no errors were raised:

# in the above prog, the else block is excuted when their is no error message are raised
# if any error occured, the else block is not executed..

try:
    print("Hello,World")
except:
    print("Somrthing went Wrong!")
else:
    print("Everything fine !")

# ----------------------------------------------------------------

# the finally block is executed regardless if the try block raised an error or. not
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("the 'try except' is finished")

# no matter if your prog. gives error it will be executed .

# if we don't use the finally keyword and print the line after the try except block .. it will also executed succesfully..

# generally, we also effectively used it in the function ......

def func1():
    try:
        print(x)
    except Exception as e:
        print(e)
    finally:
        print("executed successfully!!")

func1()

print("all done >>")

# another use of the finally clause

'''
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
'''

# ---------------------------------------------------------------

# in python you can choose to throw an exception if a condition occurs.
# to throw an exception we use the < raise > keyword..

#? Raise an error and stop the program if x is lower than 0:
# x =-1
# if x < 0:
#     raise Exception ("sorry, no numbers below 0")

#? you can define what kind of error to raise, and the text to print to the user..
#* raise a typeError if x is not an integer;;
x = "hello"
if not type(x) is int:
    print("only, integers are allowed!!!")




'''

"ZeroDivissionError" = "Raised error when the divisor is 0 "

"valueError" = "Raised Error when there is a wrong value in the specified datatype "

"typeError" = "Raise when 2 different types are combined "

"SystemExit" =	"Raised when the sys.exit() function is called"

"SystemError" = "Raised when a system error occurs"

"SyntaxError" = "Raised when a syntax error occurs"


"TabError" = "Raised when indentation consists of tabs or spaces"

"RuntimeError" = "Raised when an error occurs that do not belong to any specific exceptions"

"OverflowError" = "Raised when the result of a numeric calculation is too large"

"NameError"	 = "Raised when a variable does not exist"

"MemoryError" = "Raised when a program runs out of memory"

"KeyboardInterrupt" = "Raised when the user presses Ctrl+c, Ctrl+z or Delete"

"KeyError"	 = "Raised when a key does not exist in a dictionary"

"IndexError" = 	"Raised when an index of a sequence does not exist"

"IndentationError" = "Raised when indentation is not correct"

"ImportError" = "Raised when an imported module does not exist"

"FloatingPointError" = 	"Raised when a floating point calculation fails"

"Exception" =	"Base class for all exceptions"

"EOFError" = "Raised when the input() method hits an "end of file" condition (EOF)"

"ArithmeticError" = "Raised when an error occurs in numeric calculations"

'''
