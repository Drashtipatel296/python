# 36.Write a program to calculate the average of elements in an array using functions.
 
def Average(lst): 
    return sum(lst) / len(lst) 

lst = [15, 9, 55, 41, 35, 20, 62, 49] 
average = Average(lst) 
 
print("Average of the list : ", round(average, 2)) 
