# 19.Write a program to find the intersection of two arrays.

def intersection_list(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3

list1 = [40,90,12,8,14,60,45,72,80,33]
list2 = [50,40,5,45,33,30,90,100,95,62]

print(intersection_list(list1, list2))