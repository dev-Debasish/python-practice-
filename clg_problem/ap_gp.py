def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def findSeries(num):
    sum = 0
    for i in range(num):
        sum =sum + factorial(i+1)
    return sum

n = int(input("Enter the value of n: "))

value = findSeries(n)
print(value)

