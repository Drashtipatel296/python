# Create a program to find the factorial of a number using recursion.

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)


num = int(input("Enter the value of num : "))
print("Factorial is : ",factorial(num))
