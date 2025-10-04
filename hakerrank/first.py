n = int(input("Enter the value of n: "))
arr = []
for _ in range(n):
    arr.append(int(input()))
print(arr)
# print(type(arr))
arr.sort(reverse = True)
print(arr)

arr = list(dict.fromkeys(arr))
print(arr)

