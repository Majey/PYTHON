from decimal import Decimal as D

"""
Use decimal for accurate answers on arithmetic
operations on floating point values
""" 
sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.03")
 
print("Sum = ", sum) 
print(f"{0.1 + 0.1 + 0.1 - 0.3}")