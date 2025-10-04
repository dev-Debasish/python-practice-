x = pow(4.8,3)
# it returns by-default the integer value
print(f"{x:.2f}")

a = min(4,5,10)
b = max(4,5,10)
print(a)
print(b)
# The abs() function returns the absolute (positive) value of the specified number:
c = abs(-458.24)
print(c)

import math

print(dir(math))
# python has built-in pow function and also has a pow() function that is with-in the math module
y = math.pow(4.8,3)
# it returns by-default float value 
print(y)

z = math.sqrt(576)
print(z)
# The [math.ceil()] method rounds a number upwards to its nearest integer, and the [math.floor()] method rounds a number downwards to its nearest integer, and returns the result:
m = math.ceil(1.15)  # 2
n = math.floor(1.95)   # 1
print(m)
print(n)

d = math.pi
print(d)
print(f"The power function of the given function is {d**3}")