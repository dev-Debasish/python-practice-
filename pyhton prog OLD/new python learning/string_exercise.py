# ex-1
name = input()
print(f"Good Morning {name}")

# ex-2
letter = '''
        Dear <|name|>,
        You are selected
        <|date|>
        '''
print(letter.replace("<|name|>","Debasish").replace("<|date|>","29th April,2003"))

# ex-3
str = "my name  is Debasish pal"
print(str.find("  "))
str1 = "my age is 21"
print(str1.find("  "))

# ex-4
print(str.replace("  "," "))

# ex-5
letter1 = "Dear Bittu,\n\t this python course is nice.\n Thanks!"
print(letter1)