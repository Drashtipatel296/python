# Create a program to find the largest element in an array.

arr = [10,8,5,12,20,30,1,40,15]
max = arr[0]

for i in range(len(arr)):
    if(arr[i] > max):
        max = arr[i]
print(max)

