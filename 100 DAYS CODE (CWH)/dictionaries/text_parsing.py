import string
import json

#!  to open the file without any error we have to go the original path to execute
fname = "100 DAYS CODE (CWH)\dictionaries\parse.txt"
try:
    fhand = open(fname)
except:
    print("file cannot be opened: ", fname)
    exit()
    
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(str.maketrans("","",string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# print(counts)     

with open("text.json", "w") as file:
    json.dump(counts, file, indent = 4)
    
