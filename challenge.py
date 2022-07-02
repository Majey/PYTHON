# Returning multiple values

x, y = input("Please enter two numbers for arithmetic operations: ").split()
x = int(x)
y= int(y)

def findSum(x, y):
    return (f"{x} + {y} = {x+y}"), (f"{x} * {y} = {x*y}")

add, multiply = findSum(x, y)
print(add)
print(multiply)
