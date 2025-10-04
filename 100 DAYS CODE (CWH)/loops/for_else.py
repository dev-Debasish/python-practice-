#  we can use else right after the loop when the loop is successfully executed then the else block is executed
# if we use only [break] statement inside the loop then the else block is not executed.
for i in range(5):
    print(i)
else:
    print("in the else block")

for st in []:
    print(st)
else:
    print("not print st as the empty string is used")

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("not printed as break statement is used")

