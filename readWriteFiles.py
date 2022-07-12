# ---------- READING & WRITING TEXT ----------
 
# The os module provides methods for file processing
import os
 
# We are able to store data for later use in files
 
# You can create or use an already created file with open
 
# If you use w (write) for mode then the file is
# overwritten.
# If you use a (append) you add to the end of the file
 
# Text is stored using unicode where numbers represent
# all possible characters
 
# We start the code with with which guarantees the file
# will be closed if the program crashes
with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
 
    # You can write to the file with write
    # It doesn't add a newline
    myFile.write("Some random text\nMore random text\nAnd some more")
 
 
# Open the file for reading
# You don't have to provide a mode because it is
# read by default
with open("mydata.txt", encoding="utf-8") as myFile:
 
    # We can read data in a few ways
    # 1. read() reads everything into 1 string
    # 2. readline() reads everything including the first newline
    # 3. readlines() returns a list of every line which includes
    # each newline
 
    # Use read() to get everything at once
    print(myFile.read())
 
# Find out if the file is closed
print(myFile.closed)
 
# Get the file name
print(myFile.name)
 
# Get the access mode of the file
print(myFile.mode)
 
# Rename our file
os.rename("mydata.txt", "mydata2.txt")
 
# Delete a file
# os.remove("mydata.dat")
 
# Create a directory
# os.mkdir("mydir")
 
# Change directories
# os.chdir("mydir")
 
# Display current directory
print("Current Directory :", os.getcwd())
 
# Remove a directory, but 1st move back 1 directory
# os.chdir("..")
# os.rmdir("mydir")
#  
 
# ---------- READ ONE LINE AT A TIME ----------
# You can read 1 line at a time with readline()
 
# Open the file
with open("mydata2.txt", encoding="utf-8") as myFile:
 
    lineNum = 1
 
    # We'll use a while loop that loops until the data
    # read is empty
    while True:
        line = myFile.readline()
 
        # line is empty so exit
        if not line:
            break
 
        print("Line", lineNum, " :", line, end="")
 
        lineNum += 1
 
# ---------- PROBLEM : ANALYZE THE FILE ----------
# As you cycle through each line output the number of
# words and average word length
'''
Line 1
Number of Words : 3
Avg Word Length : 4.7
Line 2
Number of Words : 3
Avg Word Length : 4.7
'''
 
with open("mydata2.txt", encoding="utf-8") as myFile:
 
    lineNum = 1
 
    while True:
        line = myFile.readline()
 
        # line is empty so exit
        if not line:
            break
 
        print("Line", lineNum)
 
        # Put the words in a list using the space as
        # the boundary between words
        wordList = line.split()
 
        # Get the number of words with len()
        print("Number of Words :", len(wordList))
 
        # Incremented for each character
        charCount = 0
 
        for word in wordList:
            for char in word:
                charCount += 1
 
        # Divide to find the answer
        avgNumChars = charCount/len(wordList)
 
        # Use format to limit to 2 decimals
        print("Avg Word Length : {:.2}".format(avgNumChars))
 
        lineNum += 1
 