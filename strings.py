string = "This is a string"

print(string[0])
print(string[-1])
print(len(string))

# slice strings
print(string[:4]) 
print(string[4:10])
print(string[-4])
print(string[-4:])

print("Hello " * 5)

# convert integer to string
print(type(str(4)))

for char in string:
    print(char)

# cycle throough strings in pairs
for i in range(0, len(string)-1, 2):
    print(string[i] + string[i+1])