# with open("100 DAYS CODE (CWH)/file2.txt","r") as f:
#     f.seek(10)
    
#     current_position = f.tell()
#     print(current_position)
    
#     data = f.read(12)
#     print(data)
    
    
# truncate() file
with open("sample.txt","w") as f:
    f.write("hello Debasish!!")
    
    f.truncate(5)

with open("sample.txt","r") as s:
    data = s.read()
    print(data)
    
    

"""

 + -----> binary format [r+, w+ a+]
 b -----> binary format [rb, wb, ab]
 t -----> text format [rt, wt, at]
 
"""


