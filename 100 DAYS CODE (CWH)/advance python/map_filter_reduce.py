# MAP
myList = [12, 45, 18, 29, 20, 6]
# map() func. only returns the map obj...so, you have to change it to your desirable iterators
newList = list(map(lambda x: x*x, myList))
print(newList)




# FILTER()
def myfunc(x):
    return x > 15

newNewList = list(filter(myfunc, myList))
print(newNewList)




# REDUCE()

#*  the reduce() function applies the function to the first 2 elements in the iterable and applies the function to the result and the next element,and so on...the reduce() func. returns the final result. 

#?   in this function you don't have to convert it the any iterable as it returns the result (single value) directly.

from functools import reduce

theList = reduce(lambda x, y : x+y, myList)
print(theList)



