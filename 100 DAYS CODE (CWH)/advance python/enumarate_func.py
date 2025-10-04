x = ("apple", "Orange", "kiwi")
y = enumerate(x)
print(list(y))
# the enumerate function returns a tuple with it's index value and its value itself..

index = 0
for item in x:
    print(item)
    if index == 1:
        print("winter specific!")
    index += 1
# if we want to print the index no of the items wehave to define the flag (index = 0) first and increment the index no. by 1 to access the iterable object..


# another is we have to use the enumerate() function for doing the same things of the above..

for index, item in enumerate(x):
    print(item)
    if index == 1:
        print("winter specific!!")

# in the above program we don't have to increment the index no. by 1 ,as the enumerate() function doing the same things by default and returns the unpacked tuple of index and the item together..


nums = [10, 15, 41, 78, 154, 65, 458, 321, 123]
for index, item in enumerate(nums, start = 1):
    print(index, item)


# in the above program we specify that the index no. is start from [1] to till the end of the list...



    