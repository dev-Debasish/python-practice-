'''
def func():
    print("loading...")
    print("loading...")
    print("loading...")
    print("loading...")
    print("loading...")
    # return 7
    return 40

#! here the problem is that atfirst inside the function it is just calling the function then returning the value afterthat the if condition is check this
#?   but when the condition is true it is called the function twice as we call the function twice [first at to check the statement and second at the inside the if statement]
# if(func() > 10):
#     func()
# else:
#     print("not loading...")


#!   we can just solve this redundancy by using walrus operator
#?   walrus operator is used to assign a value to a variable as part of an expression
#?   it is also called assignment expression
#?   it is used to avoid redundancy
if((a := func()) > 10):
    print(a)
else:
    print("not loading...")
    
    
'''
    
while (data := input("Enter the data: ")):
    print(data)
    if data == "q":
        break
    