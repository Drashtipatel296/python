# swap two numbers

x = int (input('Enter the value of x : '))
y = int (input("Enter the value of y : "))

x = x + y
y = x - y
x = x - y

print("After swapping :-")

print('Enter the value of x : ',x)
print("Enter the value of y : ",y)