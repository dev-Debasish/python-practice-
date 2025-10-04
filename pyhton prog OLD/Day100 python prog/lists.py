lst  =[12,15,3,"bittu",True,12,45,56,]
# how many types we print a list
print(lst[:])
print(lst)
print(lst[2])
# list indexing
print(lst[:3])
print(lst[2:])
# negative indexing
print(lst[-2])
print(lst[len(lst)-2])
print(lst[8-2])
print(lst[6])
# jump index
print(lst[0:8:2])

# list comprehension

l = [i for i in range(10) if i%2 == 0]
print(l)


###
lst2 = [45,56,89,78,23,56,54]
if 4 in lst2:
    print("yes")
else:
    print("no")
