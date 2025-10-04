# yield keyword is used to create a generator function. A type of function that is memory efficient and can be used like an iterator object.

#?  <class 'generator'>

# The yield keyword in Python is similar to a return statement used for returning values in Python which returns a generator object to the one who calls the function which contains yield, instead of simply returning a value. [The main difference between them is], the return statement terminates the execution of the function. Whereas, the yield statement only pauses the execution of the function. Another difference is return statements are never executed. whereas, yield statements are executed when the function resumes its execution.

# ------------------------------------------------------------

def fun_generator():
    yield "hello, world!"
    yield "yield keyword"
    
obj = fun_generator()

# print(obj)

print(type(obj))

'''
# print(next(obj))
# print(next(obj))
'''
#!    or.  
# for i in fun_generator():
#     print(i)
#!    or.
for i in obj:
    print(i)
    
    
# -------------------------------------------------------------

    
#!  use yield 

def even_gen(limit):
    for i in range(2, limit + 1, 2):
        yield i
        
for num in even_gen(10):
    print(num)
    
# ------------------------------------------------------------

#!   Demonstrating yield working with a list.

# generator to print even numbers
def print_even(test_list):
    for i in test_list:
        if i % 2 == 0:
            yield i

# initializing list
test_list = [1, 4, 5, 6, 7]

# printing initial list
print("The original list is : " + str(test_list))

# printing even numbers
print("The even numbers in list are : ", end=" ")
for j in print_even(test_list):
    print(j, end=",")

print()

# -------------------------------------------------------------

#**  thus, yield is a iterator tool so, we have to iterate the value inside the function using loop

# -------------------------------------------------------------

#!    writing a two liner string 

test_string = " There are many geeks around you, \
              geeks are known for teaching other geeks"
            

# ---------------------------------------------------------    

#!  Use of yield Keyword as Boolean

def print_even(test_string):
    for i in test_string:
        if i == "geeks":
            yield i

test_string = """
                There are many geeks around you, 
              geeks are known for teaching other geeks
                """
                
count = 0
print("the number of geeks in the string is: ", end = '')

test_string = test_string.split()

for j in print_even(test_string):
    count = count + 1
    
print(count)

# ==========================================================

