# program for ph calculation of an element ----->
phString = "PH SCALE";
print(phString.center(30,"*"));
ph = int(input("Enter the value of PH [e.g:0 to 14]:"));
match ph:
    case 7:
      print("the element is neither acidic nor alkaline it is neutral(WATER)");
    case ph if ph>=0 and ph<7:
      print("the element is acidic");
    case ph if ph>=8 and ph<=14:
      print("the element is alkaline");
    case _:
      # print(ph.index("Error Occur"));
      print("Invalid Input!")


# str6 = "he's bittu.he is a good boy"
# print(str6.index("nice"))


# GRADE CALCULATION
# gradeString = "GRADE CALCULATION";
# print(gradeString.center(40,"."));
# score = int(input("Enter your score:"));
# match score:
#     case score if score >= 90:
#         print("your grade is: AA ");
#     case score if score >= 80:
#         print("your grade is: A ");
#     case score if score >= 70:
#         print("your grade is: B ");
#     case score if score >= 60:
#         print("your grade is: C ");
#     case _:
#         print("your grade is: D ");