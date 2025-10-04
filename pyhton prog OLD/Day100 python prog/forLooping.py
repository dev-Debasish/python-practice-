##              FOR LOOP 

# for STRING -->
name = "Debasish"
for character in name:
  print(character, end=", ")
print("\n")
#for LIST --->
flowers = ["lily", "rose", "lotus"]
for flower in flowers:
  print(flower)
  for character in flower:
    print(character)
print("\n")
# using range() function for printing numbers
for numbers in range(10):
  print(numbers)  # prints 0 to 9
print("\n")
for numbers in range(10):
  print(numbers + 1)  # prints 1 to 10
print("\n")
for num1 in range(1, 15):
  print(num1)  #prints 1 to 14
print("\n")
for num1 in range(1, 15):
  print(num1 + 1)  # prints 2 to 15

# using 3 parameters for range() function --->
for k in range(10, 54, 8):
  print(k)
# it prints the values from 10 to 54 with 8 gap each that is ------->10,18,26,34,42,50.

  ###               WHILE LOOP

# simple while loop program
x = int(input("initialize x:"))
while (x <= 5):
  print(x)
  x = x + 1
print("loop exit")

#while loop with else statement
x = 1
while (x <= 5):
  print(x)
  x = x + 1
else:
  print("it is out of the loop")


###     DO-WHILE LOOP

# do-while loop is unfimillier in python programming
## do-while is a loop in which a set of instructions will execute at least once..to emulate a do-while loop in Python is to use an infinite while loop with a break statement 

  while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
      break
  # i = 0                        # Here true used for infinite looping 
  # while True:
  #   print(i)          
  #   i = i+1;
  #   if(i %15 == 0):
  #     break
  
