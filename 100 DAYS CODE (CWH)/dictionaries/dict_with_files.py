import json

fname = input("Enter the filename: ")
try:
    fhand = open(fname)
except Exception as e:
    print(e)
    exit()
    
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        # if word not in counts:
        #     counts[word] = 1
        # else:
        #     counts[word] += 1
        #!!!  or....
        counts[word] = counts.get(word, 0) + 1

# print(counts)

# data = json.dumps(counts, indent = 4)

with open("data.json", "w") as file:
    json.dump(counts, file, indent = 4)
    


# import string    
#!    string.punctuation      !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~    
