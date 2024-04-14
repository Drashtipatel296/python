# 18.Create a program to count the occurrence of a character in a string.

string = "Programmer"
count = 0

my_char = "m"

for i in string:
    if i == my_char:
        count += 1
print(count)