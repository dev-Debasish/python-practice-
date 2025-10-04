def triRecursion(k):
    '''
    Explanation:
Function triRecursion:

It is a recursive function, meaning it calls itself with a smaller input (k - 1).
Base case:
If k <= 0, the function returns 0 and stops further recursion.
Recursive case:
If k > 0, the function calculates result as k + triRecursion(k - 1).
Recursive Flow:

Each recursive call reduces the value of k by 1 until k reaches 0.
The function then begins to "unwind" the recursion, adding the values back up.
Print Statement:

The print(result) statement inside the function prints the intermediate results at each step as the recursion "unwinds."
Execution for triRecursion(6):

Recursive calls (winding phase):

triRecursion(6) calls triRecursion(5)
triRecursion(5) calls triRecursion(4)
triRecursion(4) calls triRecursion(3)
triRecursion(3) calls triRecursion(2)
triRecursion(2) calls triRecursion(1)
triRecursion(1) calls triRecursion(0)
triRecursion(0) returns 0.

Returning results (unwinding phase):

triRecursion(1) returns 1 + 0 = 1
triRecursion(2) returns 2 + 1 = 3
triRecursion(3) returns 3 + 3 = 6
triRecursion(4) returns 4 + 6 = 10
triRecursion(5) returns 5 + 10 = 15
triRecursion(6) returns 6 + 15 = 21
    '''
    if k > 0:
        result =  k + triRecursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion result = ")
triRecursion(6)


#  print(triRecursion.__doc__)


#!  this is the zen of python
# import this


#! print factorial
def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return (num * factorial(num - 1))
    
print("factorial = ",factorial(6))


#! implement fibonacci sequence
def fibonacciSequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacciSequence(n - 1) + fibonacciSequence(n - 2))

print("Enter the last index number that you want to print the fibonacci sequence: ")
num = int(input()) 
i = 0;
while i < num:
    print(fibonacciSequence(i),end = ",")
    i = i + 1


print("\n")

