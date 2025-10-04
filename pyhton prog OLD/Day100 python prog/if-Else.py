                ## condition for determining leapyear
                        # year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


 # 2,4---> not weird
 #above 20 all even no is ---> not weird
 #all odd numbes are --> weird
 #6,8,10,12,14,16,18,20 ----> weird
    
# n = int(input("Enter the number:"));
# range1 = n>=2 and n<=5;
# range2 = n>=6 and n<=20;
# if(n%2 == 0):
#     if(n > 20 ):
#         print("not weird");
#     elif(range1):
#         print("Not Weird");
#     elif(range2):
#         print("Weird");
# else:
#     print("Weird");
    

def check_weirdness(n):
    if n % 2 != 0:
        print("Weird")
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        else:
            print("Not Weird")

# Test cases
n = 3
check_weirdness(n)  # Output: Weird

n = 4
check_weirdness(n)  # Output: Not Weird

n = 8
check_weirdness(n)  # Output: Weird

n = 22
check_weirdness(n)  # Output: Not Weird


                     