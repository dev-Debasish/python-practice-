import math

def power(num, expo):
    value  = math.pow(num, expo)
    return value

def series(num, exponent):
    sum = 1
    for i in range(exponent):
        sum = sum + power(num, i+1)
    return sum
num = int(input("Enter the number: "))
exponent = int(input("Enter the exponent: "))

result = series(num, exponent)
print(result)


