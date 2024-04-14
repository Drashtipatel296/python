alpha = 65

for i in range(1, 6):
    for j in range(5 - i):
        print("  ", end="")
        
    for k in range(1, 2*i):
        if(k==1 or i==5 or k==2*i-1):
            print(chr(alpha),'', end="")
        else:
            print("  ", end="")
        alpha += 1
    alpha = 65
    print()