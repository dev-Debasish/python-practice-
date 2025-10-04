# f = open("project.txt", "r")
# text = f.read()
# print(text)
# f.close()

with open("project.txt", "r") as f:
    text = f.read()
    print(text)

'''
f.readlines() method returns the list of each line
'''

# f = open("file2.txt","w")
# f.write("hello I am DEBASISH!!")
# f.close()


# f = open("100 DAYS CODE (CWH)/file2.txt", "a")
# f.write("How are YOU!!")
# f.close()

#!  here we don't have to close the file 
# with open("100 DAYS CODE (CWH)/file2.txt", "a") as f:
#     f.write("all done~~")
    
    
#?   t = text  ,,, b = binary   ,,,  and so on....



# readline() method
#?  readline() mathod read the single line from a file... if you want multiple lines we should use a loop..

# f = open("100 DAYS CODE (CWH)/file2.txt","r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line, type(line))
# f.close()


#?  writeline() method writes the sequence of string to a file, it should be iterable object [list, tuple]

# f= open("100 DAYS CODE (CWH)/file2.txt","w")
# lines = ['line1\n', 'line2\n', 'line3\n']
# f.writelines(lines)
# f.close()


#?   writeline() methos doesn't add newline character between the strings in the sequence.. if we want to add new line , we use the loop separately...

# f = open("100 DAYS CODE (CWH)/file2.txt","w")
# lines = ['line1', 'line2', 'line3']

# for line in lines:
#     f.write(line + '\n')

# f.close()



# f = open("demoFile.txt", "x")
# f = open("demoFile.txt", "r")
# print(f.read(5))


#!   to delete the file you have to import the os module && you should use the os.remove() function...

# import os
# os.remove("sample.txt")

#! if the file is not exist,, then it throws an error ...to avoid this..

# import os
# if os.path.exists("new.txt"):
#     os.remove("new.txt")
# else:
#     print("the file doesn't exist!!")


#!  to delete an entire folder you should use os.rmdir() function -->

# import os
# os.rmdir("xyzfolder")


