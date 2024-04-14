# Write a program to check if a string is a palindrome.

x = str(input("Enter the string : "))

if(x==x[::-1]):
    print("This string is palindrome.")
else:
    print("This string is not palindrome.")

