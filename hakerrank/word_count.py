n = int(input())
#! shows how to take the input values into a empty dictionary
word_count = {}
for _ in range(n):
    word = input()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1



print(len(word_count))

print(" ".join(str(count) for count in word_count.values()))