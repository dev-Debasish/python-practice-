def count_up_to(n):
    for i in range(1, n+1):
        # return i
        yield i
        
'''
How Generators Work ??
------>>>> 
A generator function returns a generator object when called. You can iterate over it (e.g., with a for loop) or fetch values one-by-one with next().
''' 

counter = count_up_to(3)
print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter))     #! raise stopIteration...

for num in count_up_to(3):
    # but it knows where to stop...
    print(num)             
    
    
print(count_up_to(3))