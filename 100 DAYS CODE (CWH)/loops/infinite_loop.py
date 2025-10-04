'''
write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count and average of the numbers. If the user enters anything outer than a number, detect their mistake using try and except and print an error message and skip to the next number.

    Enter a number: 4
    Enter a number: 5
    Enter a number: bad data
    Invalid Input
    Enter a number: 7
    Enter a number: done
    16  3  5.33333333333333
'''


# count = 0
# total = 0
# average = None
# while True:
#     try:
#         value = input("Enter a Number: ")
#         if value == "done":
#             break
#         #! [count] must be defined after the [total] is defined otherwise result is different
#         total += int(value)
#         count += 1
#         average = total / count
#     except:
#         print("Invalid Input")
#         # continue

# print(total, count, average)



'''
write another program that prompts for a list of numbers as above and at the end print out both the maximum amd minimum of the numbers instead of the average.
'''


count = 0
total = 0
list_of_numbers = []
while True:
    try:
        value = input("Enter a Number: ")
        if value == "done":
            break
        num = int(value)
        list_of_numbers.append(num)
        #! [count] must be defined after the [total] is defined otherwise result is different
        total += num
        count += 1
    except ValueError:
        print("Invalid Input")

if count > 0:
    min_value = min(list_of_numbers)
    max_value = max(list_of_numbers)
    print(total, count, min_value, max_value)
else:
    print("No valid numbers were entered")


