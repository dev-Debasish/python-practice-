def infinite_numbers():
    n = 1
    while True:
        yield n
        n += 1
        
numbers = infinite_numbers()
# the yield statement only pauses the execution of the function.
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

for i in infinite_numbers():
    print(i)
    if i >= 5:
        break