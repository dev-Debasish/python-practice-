import math

def power(num, expo):
    value = math.pow(num,expo)
    return value

def findPowerSeries(num):
    sum =0
    for i in range(num):
        sum = sum + ((i+1)/power(i+1, i+1))
    return sum

n = int(input("Enter the value of n: "))

result = findPowerSeries(n)
print(result)
    

# print(math.pow(4,2))