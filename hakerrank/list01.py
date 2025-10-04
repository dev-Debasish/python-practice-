'''
input = 
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print
output = 
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]
'''



n = int(input("Enter: "))
l1 = []
str = input()
for _ in range(n):
    parts = str.split()
    command = parts[0]
    
    if command == "insert":
        l1.insert(int(parts[1]), int(parts[2]))
    elif command == "print":
        print(l1)
    elif command == "remove":
        l1.remove(int(parts[1]))
    elif command == "append":
        l1.append(int(parts[1]))
    elif command == "sort":
        l1.sort()
    elif command == "pop":
        l1.pop()
    elif command == "reverse":
        l1.reverse()