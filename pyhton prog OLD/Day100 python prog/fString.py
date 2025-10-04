letter = "my name is {} and I am from {}"
name ="debasish" 
country = "India" 
print(letter.format(name,country))
letter2 = "my name is {1} and I am from {0}"
print(letter2.format(country,name))  # if we alternate the value of the letter2 then we should be alternate the indexing of it..    


# the better method using string formattting is fstring
game = "cricket"
txt = f"{name} is a good boy & he is like to play {game}"
print(txt)
print(f"{2*60}")
