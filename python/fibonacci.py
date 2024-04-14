# generate the fibonacci series.

num = int(input("Enter the value of n : "))

n1 = 0
count = 0
n2 = 1

if num == 1:  
    print ("The Fibonacci sequence of the numbers up to", num, ": ")  
    print(n1)  
else:
    print ("The fibonacci sequence of the numbers is:")
while count < num:
    print(n1)

    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1


