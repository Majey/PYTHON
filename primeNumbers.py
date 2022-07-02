# Printing out prime numbers

limit = int(input("Please enter your range for prime numbers: "))

def isPrime(limit):
    for i in range(2, limit):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            print(f"{i},", end="")

isPrime(limit)