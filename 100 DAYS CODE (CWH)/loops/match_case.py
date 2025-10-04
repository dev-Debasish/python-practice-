# x = int(input("Enter the value of x: "))
# match x:
#     case 1:
#         print("x is one 1")
#     case 4:
#         print("X is four 4")
#     case _:
#         print(x)

def weekday(n):
    match n:
        case 1: return "Sunday"
        case 2: return "Monday"
        case 3: return "Tuesday"
        case 4: return "Wednesday"
        case 5: return "Thursday"
        case 6: return "Friday"
        case 7: return "Saturday"
        case _: return "Invalid Input"

print(weekday(1))
print(weekday(2))
print(weekday(3))
print(weekday(4))
print(weekday(5))
print(weekday(6))
print(weekday(7))
print(weekday(16))


# The code below shows how to combine cases in match statement. It defines a function named access() and has one string argument, representing the name of the user
def access(user):
    match user:
        case "admin" | "manager": return "Full Access"
        case "guest": return "Limited Access"
        case _: return "No Access"

print(access("Bittu"))
print(access("admin"))
print(access("guest"))
print(access("manager"))


# Normally Python matches an expression against literal cases. However, it allows you to include if statement in the case clause for conditional computation of match variable.
def intr(details):
    match details:
        case [amt, time] if amt < 10000:
            return amt * 10 * time / 100
        case [amt, time] if amt >= 10000:
            return amt * 15 * time / 100
        
print("interest = ",intr([5000, 5]))
print("interest = ",intr([15000, 3]))

# Since Python can match the expression against any literal, you can use a list as a case value. Moreover, for variable number of items in the list, they can be parsed to a sequence with "*" operator.
def greeting(details):
    match details:
        case [time, name]:
            return f'good {time} {name}!'
        case [time, *names]:      #(*names captures remaining list elements)
            msg = ' '              #That adds a extra space in starting of '&'
            for name in names:
                msg += f'good {time} {name}!\n'
            return msg

print(greeting(["Morning", "Debasish"]))
print(greeting(["Afternoon", "Bittu"]))
# '&'
print(greeting(["Evening", "Kaberi","Shankar","Abhi"]))