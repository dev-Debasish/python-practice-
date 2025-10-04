# [is] checks the exact location of the memory ()...
# [==] checks only value...

#?   for every immutable obj. it returns same results for both [==] and [is] as, python interpreter already knows that those are the immutable so, it makes no sense to create the different location for the same value.. 

#* as the int are immutable...
a = 4
b = 4
print(a is b)
print(a == b)

#!  for every mutable obj. both the [==] and [is] different, because the value is same but the memory location is different

#? as the list are mutable
x = [4,5,1,12]
y = [4,5,1,12]
print(x is y)
print(x == y)