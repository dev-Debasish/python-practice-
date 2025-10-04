'''
write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary ? 
'''
d = {}
with open("100 DAYS CODE (CWH)\dictionaries\words.txt", "r") as file:
    line = file.read()
    print(line)
    #!  split() method in string that splits the line in a list of words
    text = line.split()
    print(text)
    for word in text:
        d[word] =d.get(word, 0)

print(d)

print("book" in d.keys())
print("oopo" in d.keys())

# d = {}
# fname= "words.txt"
# try:
#     fhand = open(fname)
# except Exception as e:
#     print(e)

# for line in fhand:
#     words = line.split()
#     for word in words:
#         d[word] = d.get(word, 0)
        
# print(d)


