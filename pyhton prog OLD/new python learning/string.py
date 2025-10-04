# strings are primarily write in 3 ways----->
name1 = 'bittu'
name2 = "bittu"
name3 = '''bittu'''

# strings are immutable....

# str1 = "Welcome to the Console !!!"
# print(str1.endswith("to", 5, 10))


str6 = "he's bittu.he is a good boy"
# if it is false it throws -1..
print(str6.find("is"))
print(str6.find("am"))
# the <find> and <index> method are same where the substring is present in the main string and throws the index no. of the substring location .... but the difference is that if the substring is not present in the main string then the <find> method throws -1 as a result. but for the <index> method it throws exception , as a result.....
print(str6.index("good"))


# check this out ------>
# C:\Users\asus\Desktop\pyhton prog\Day100 python prog\stringMethode.py