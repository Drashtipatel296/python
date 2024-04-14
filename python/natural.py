# Create a program to find the sum of natural numbers using a while loop.

num = int(input("Enter any number : "))

if num < 0:
    print("Enter a Positive number.")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
print("Sum is all Natural numbers : ",sum)