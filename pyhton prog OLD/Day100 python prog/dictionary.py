info ={
    'name':'debasish','age':20 , "eligibility":True
}

print(info);

print("........")

print(info['name']);
print(info.get('name'))

print("........")

print(info.keys())
print("--->")
for key in info:
    print(f"the key {key} is {info[key]}")
print("<..or..>")
for key in info.keys():
    print(f"the key {key} is {info[key]}")

print("........")

print(info.values())
print("--->")
for value in info.values():
    print(f"the value is {value}")

print("........")

print(info.items())
print("--->")
for key, value in info.items():
    print(f"the key {key} is {value}")

