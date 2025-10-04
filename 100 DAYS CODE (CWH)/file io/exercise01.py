# fhand = open("file.txt")
# print(fhand)

'''
write a program to read through a file and prints the contents of the file all in upper case.
'''

fname = "exercise1.txt"
try:
    fhand = open(fname)
except:
    print(f"{fname} not found!")
    exit()

for line in fhand:
    line = line.strip()
    line = line.upper()
    print(line)