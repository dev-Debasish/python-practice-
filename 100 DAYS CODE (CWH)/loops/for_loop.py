# in string
name = "debasish pal"
for ch in name:
    print(ch, end = ",")
print("\n")

# --------------------------------------------------------------------------------------------------------

#  in list
fruits = ["mango", "licchi", "guava"]
for fruit in fruits:
    print(fruit)
    for character in fruit:
        print(character)

# -------------------------------------------------------------------------------------------------------

flowers = ["lotus", "Rose", "lily", "sunflower"]
for flower in flowers:
    print(flower)
    if flower == "lily":
        break
print("complete :>\n")

# --------------------------------------------------------------------------------------------------------

flowers = ["lotus", "Rose", "lily", "sunflower"]
for flower in flowers:
    if flower == "lily":
        break
    print(flower)
print("done :>\n")

# ----------------------------------------------------------------------------------------------------------

items = ["bat", "ball", "wicket", "player"]
for item in items:
    if item == "wicket":
        continue
    print(item)
print("Well Done :>\n")

# ------------------------------------------------------------------------------------------------------------
# we should print the element after the continue as it prints the full element set |

items = ["bat", "ball", "wicket", "player"]
for item in items:
    print(item)
    if item == "ball":
        continue
print("Well Done :>\n")
# --------------------------------------------------------------------------------------------------------------
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for i in range(6):
    print(i)
else:
    print("Finally finished !")

#---------------------------------------------------------------------------------------------------------------

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# for i in range(3):
#     for j in range(3):
#         print(adj[i],fruits[j])

for i in range(7):
    pass

