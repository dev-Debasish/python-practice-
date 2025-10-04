def alternateSort(arr):
    a = []
    arr.sort()
    # for index, value in enumerate(arr):
    #     if index % 2 == 0:
    #         a.append(value)
    # return a
    for i in range(0, len(arr), 2):
        a.append(arr[i])
    return a

arr = [3, 5, 1, 5, 9, 10, 2, 6]
# size = int(input())
# arr = list(map(int,input.split()))
result = alternateSort(arr)
print(result)




# def unaffectedChar(dataStream):
#     rev = dataStream[::-1]
#     # return rev
#     count = 0
#     for char_d in dataStream:
#         for char_r in rev:
#             if(char_r == char_d):
#                 count += 1
#     return count

# dataStream = str(input())
# result = unaffectedChar(dataStream)
# print(result)




#! The reduce function in Python is used to apply a rolling computation to a sequence of values, reducing them to a single output. It is part of the functools module.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

new = reduce(lambda x,y : x + y, numbers)
print(new)