print("this the first file!")

def display(name):
    return name


#! using this IDEOM  it is only print in this file it is not imported in the another file..., even if you use [import] 

#? by this we just only access the function but not the part that is inside of the function itself...


# if __name__ == "__main__":
#     name = input("Enter your name: ")
#     print(display(name))   
#     print(__name__)

name = input("Enter your name: ")
print(display(name))
print(__name__)

# name = input("Enter your name: ")
# print(display(name))   

#! this is always executed....just by only importing the module 
print("rest of the code !!")