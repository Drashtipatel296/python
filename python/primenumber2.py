# Create a program to print all prime numbers between two given numbers.

num1 = int(input("Enter the value of num1 : "))
num2 = int(input("Enter the value of num2 : "))

print ("The Prime Numbers in the range are : ")

for i in range(num1, num2+1):
    if i > 1:
        for j in range(2, i):
            if(i%j) == 0:
               break
            else:
              print(i)
