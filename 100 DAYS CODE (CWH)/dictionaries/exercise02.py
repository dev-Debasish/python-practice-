'''
write a python program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary(Order doesn't matter).
'''


# filename = input("Enter the filename: ")   #  mbox.txt
# counts = {}
# try:
#     with open(filename, "r") as file:
#         while True:
#             line = file.readline()
#             if not line:
#                 break
#             line = line.strip()
#             # print(type(line))
#             if line.startswith("From "):
#                 text = line.split()
#                 counts[text[2]] = counts.get(text[2], 0) + 1
# except Exception as e:
#     print(e)
    
# print(counts)




#!!    fixed  [pythonic version]



filename = input("Enter the filename: ")   #  mbox.txt
counts = {}
try:
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            # print(type(line))
            if line.startswith("From "):
                text = line.split()
                counts[text[2]] = counts.get(text[2], 0) + 1
except Exception as e:
    print(e)
    
print(counts)
