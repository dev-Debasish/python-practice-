#    BREAK STATEMENT ---->
# it exit the loop

#  using for loop
fruits = ["licchi","mango","apple","guava"];
for i in fruits:
    print(i);
    if (i == "apple"):
        break;

for i in range(7):
    if(i == 5):
        break;
    print("5 X",i,"=",5*i);
print("Break the loop");

#  using while loop
x = 3;
while x <= 10:
    print(x);
    if x >= 7:
     break;
    x = x+1;
print("\n")

# CONTINUE STATEMENT---->
# it skip the iteration

# using for loop
for i in range(7,19,2):  # (initial, stop[n-1], step)
   if (i == 13):
      continue;      # here continue statement skips 13
   print(i);

# using while loop
num = 0;
while num< 10:
   num = num+1;
   if num % 2 == 0:    # it skips the number which is devided by zero
      continue;
   print (num);

