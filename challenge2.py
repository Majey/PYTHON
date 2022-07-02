# ACRONYM GENERATOR

string = input("Please enter a sentense string: ")
string = string.upper()
print(f"Uppercased string: {string}")

listOfWords = string.split()
acronym = ""

for word in listOfWords:
    acronym += word[0]

print(f"String acronym: {acronym}")
