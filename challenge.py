"""
This program receives an uppercase string as input from the
user and converts to a secret unicode string message

It later converts the unicode message to readable character string
"""
string = str(input("Please input the string to hide: "))
secretString = ""

# Convert to secret message
for char in string:
    secretString += str(ord(char) - 23)
print(f"Secret message: {secretString}")

# Convert to normal string
normalString = ""
for i in range(0, len(secretString)-1, 2):
    charCode = secretString[i] + secretString[i+1]
    normalString += chr(int(charCode) + 23)
print(f"Original message: {normalString}")