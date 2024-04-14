# 20.Create a program to remove duplicates from an array.

list = [12,11,8,3,12,10,15,14,3,10]
print("The initialized list is : ",list)

empty_list = []

for i in list:
    if i not in empty_list:
        empty_list.append(i)

print("The resultant list after removing duplicates is : ",empty_list)        