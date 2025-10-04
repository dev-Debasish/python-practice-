tup = (42,56,87,58,"deb",False)

print(type(tup))
print(len(tup))

print(tup)
print(tup[:])
print(tup[3])
# indexing
print(tup[:3])
print(tup[3:])
# negative indexing
print(tup[-4])
print(tup[len(tup)-4])
print(tup[6-4])
print(tup[2])
# jump index
print(tup[1:5:2])
#  check for item
country = ("India","Dubai","Switzerland","Singapore","Japan")
if "India" in country:
    print("yes")
else:
    print("no")
