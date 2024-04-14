# find maximum number

x = input("Enter the value of x : ")
y = input("Enter the value of y : ")
z = input("Enter the value of z : ")

if(x>=y) and (x>=z):
    large = x
elif(y>=x) and (y>=z):
    large = y
else:
    large = z

print("Maximum num is : ",large)     
