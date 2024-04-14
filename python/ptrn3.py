alpha = 65

for i in range(1,6):
    alpha =65
    for j in range(1,6):
        if(i == 1 or i == 5 or j == 1 or j == 5):
            print(chr(alpha),'',end='')
        else:
            print('  ',end='')
        alpha += 1

    print()