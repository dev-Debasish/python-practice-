# sigle line docString
def add(a, b):
    """Return the sum of two numbers"""
    return a + b

print("Sum: ",add(4, 5))
# print the docString
print(add.__doc__)



#! multi line docString
def multiply(a, b):
   """     # this is also print as space
   Multiply two numbers and return the result.

   Parameters:
   a (int or float): The first number.
   b (int or float): The second number.

   Returns:
   int or float: The result of multiplying a and b.
   """
   return a * b
result = multiply(5, 3)
print("Product:", result)
# print the docString
print(multiply.__doc__)



'''
#! # docString for Modules
import os

"""
This module provides Utility functions for file handling operations.

Functions:
- 'read_file(filepath)': Reads and returns the contents of the file.
- 'write_file(filepath, content)': Writes content to the specified file.

Classes:
- 'FileNotFoundError': Raised when a file is not found.

Example usage:

   >>> import file_utils
   >>> content = file_utils.read_file("example.txt")
   >>> print(content)
   'Hello, world!'
   >>> file_utils.write_file("output.txt", "This is a test.")
"""
print("This is os module")
print(os.__doc__)
help(os)

'''

class Calculator:
   """
   A simple calculator class to perform basic arithmetic operations.

   Methods:
   - add(a, b): Return the sum of two numbers.
   - multiply(a, b): Return the product of two numbers.
   """

   def add(self, a, b):
      """Return the sum of two numbers."""
      return a + b

   def multiply(self, a, b):
      """
      Multiply two numbers and return the result.

      Parameters:
      a (int or float): The first number.
      b (int or float): The second number.

      Returns:
      int or float: The result of multiplying a and b.
      """
      return a * b
	  
cal = Calculator()
print(cal.add(87, 98))
print(cal.multiply(87, 98))
print(cal.__doc__)
print(cal.add.__doc__)
print(cal.multiply.__doc__)

help(Calculator.add)