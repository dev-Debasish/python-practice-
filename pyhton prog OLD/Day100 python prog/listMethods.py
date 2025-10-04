l = [56,45,25,6,450,72,1]
print(l[:])
l.append(12)  # add a new element in the  list
print(l)

l.sort()   # sort the list
print(l)
l.sort(reverse=True)     # sort the list in reverse
print(l)

l1 = [12,45,85,65,89]
l1.reverse()    # reverse the full list
print(l1)

l2 = [45,11,87,56,45,89,87,45]
print(l2.index(87))  # find out the index of an element present in the list

print(l2.count(45))    # find out occurence of an element present in the list

m = l2.copy()    # copies the l2 list to m 

n = m.insert(3,58)  # to insert the element in the list as your own wish, first type the index no then type the element do you want to insert...                  
print(m)    # here enter the root list to print the value of it

colors = ["violet","blue","indigo"]
rainbow = ["green","yellow","orange","red"]
colors.extend(rainbow)    # this is used to print the entire list with the value of the other list that point at the last of the list
print(colors)

## CONCATENATE  the lists into a single list..
b = ["bittu","debasish"]
a = ["abhi","...."]
print(b+a)