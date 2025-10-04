'''
write a while loop that starts at the last character in the string and works its way backwards to the first character in the string. printing each letter on the separate line, except backwards.
'''
# fruit = "banana"
# start_index = len(fruit) - 1
# while start_index >= 0:
#     print(fruit[start_index])
#     start_index -= 1






'''
count a occurance of a letter in a word using function
'''
def count(strParam, letter):
    count = 0
    for char in strParam:
        if char == letter:
            count += 1
    return count
        
strParam = "banana"
letter = 'a'
count = count(strParam, letter)
print(count)




'''
use the count method 
'''
print("banana".count("a"))



