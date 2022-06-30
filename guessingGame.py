import random

randNumber = random.randrange(0,10)


while True:

    bingoNum = int(input("Please input a number between 0 and 10: "))

    if bingoNum == randNumber:
        print("BINGO!")
        break

    if bingoNum != randNumber:
        print("********************************************************************")
