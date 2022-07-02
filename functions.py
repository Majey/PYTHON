# Using global variables locally within a function
# using global keyword

globalName = "Kevin"

def changeName():
    global globalName
    globalName = "Erick"

changeName()
print(globalName)