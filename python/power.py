# 31.Create a program to calculate the power of a number using functions.

base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))