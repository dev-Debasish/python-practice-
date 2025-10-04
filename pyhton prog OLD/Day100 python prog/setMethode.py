c1 = {2,3,4,5,2}
c2 = {8,9,10,2,4}

# union()&update()------>

c3 = c1.union(c2)
print(c3)
# c1.update(c2)
# print(c1)

# Intersection()& intersection_update()------->

c4 = c1.intersection(c2)
print(c4)
# c1.intersection_update(c2)
# print(c1)

# Symmectric_difference() & symmectric_difference_update()---->

c5 = c1.symmetric_difference(c2)
print(c5)
# c1.symmetric_difference_update(c2)
# print(c1)

# difference()& difference_update()------->

c6 = c1.difference(c2)
print(c6)
# c1.difference_update(c2)
# print(c1)


# isdisjoint()---->
print(c1.isdisjoint(c2))
# it returns <*false*> if any one element in the c2 set is <*present*> in the c1 set

c7 = {2,3,10,11,14}
c8 = {10,11,12}
c9 = {16,17}
c10 = {2,3,10}
## issuperset()----->
print(c7.issuperset(c8))
print(c7.issuperset(c9))
print(c7.issuperset(c10))
## issubset()--->
print(c8.issubset(c7))
print(c9.issubset(c7))
print(c10.issubset(c7))
     

## add(), remove()/discard() , update(), pop(), del , clear() ---->

num1 = {4,6,5}
no = 7
num1.add(7)
print(num1)
num1.add(no)
print(num1) 

num2 = {8,9,10}
num1.update(num2)
print(num1)

num1.remove(4)
print(num1)
# in this the unauthorized value throws error
# num1.remove(12)
# print(num1)

num1.discard(4)
print(num1)
num1.discard(11)  # it does not throws error instead of using an unauthorized value
print(num1)

item = num1.pop()
print(item)
print(num1)

del num2

num1.clear()
print(num1)
