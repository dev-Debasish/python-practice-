str = "my name is {}, I am from {}"
name = "Debasish"
country = "India"
print(str.format(name,country))
# or.
str = "my name is {}, I am from {}".format(country, name)
print(str)
# if we alternate the value of the letter2 then we should be alternate the indexing of it..
letter = "my name is {1}, I am from {0}"
print(letter.format(country, name))

price = 87
txt = "the price is {:.2f} ruppes"
print(txt.format(price))

# !--------------------------------------------------------------------------------------------------------------------
# ?      fstring

price = 49
txt = f"the price of the item is {price} dollar"
print(txt)
newPrice = 56.325
txt = f"the price of the new item is {newPrice:.2f} dollar"
print(txt)
# we can also write like this 
print(f"the price is {59.0283:.2f}")

# V.V.I.
txt = f"the price of the item is {{price}} dollar"
print(txt)
# !--------------------------------------------------------------------------------------------------------------------
# ?    Perform Operations in F-Strings

txt3 = f"the value is {40 * 87}"
print(txt3)

price = 59
tax = 0.25
amount = f"the total tax amount {price + (price * tax)} dollar you have to pay to the government."
print(amount) 

# You can perform if...else statements inside the placeholders:
price = 48
txt = f"It is very {"Expensive" if price > 50 else "cheap"}"
print(txt)

# You can execute functions inside the placeholder:
# built-in functions
fruit = "Oranges"
txt = f"I like {fruit.upper()}"
print(txt)

# The function does not have to be a built-in Python method, you can create your own functions and use them:
def convertion(feets):
    return feets * 0.3048

heightAtFeet = 30000
heightAtMeters = f"the plane is flying at a {convertion(heightAtFeet):.2f} meter altitude"
print(heightAtMeters)

# ?      Using modifiers
price = 59000
txt = f"the price is {price:,} dollar"
print(txt)
txt = f"the price is {price:_} dollar"
print(txt)

# !--------------------------------------------------------------------------------------------------------------------
# ? Extra examples using {format()} method by index numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
myOrder = "I have a {carname}, it is a {model}"
print(myOrder.format(model = "Mustang", carname = "Ford"))

