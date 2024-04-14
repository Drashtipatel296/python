rows = 5

for i in range(1,rows+1):
    for j in range(1,rows+1):
        if j == 1 or j == rows or i == 1 or i == rows:
          print(j,end=" ")
        else:
           print(" ",end=" ")
    print()