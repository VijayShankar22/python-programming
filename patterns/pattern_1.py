# write a python program to print the following pattern.

'''
input: n = 5

output:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 

'''

n = int(input("n = "))
number = 1

for rows in range(1,n+1):
    for columns in range(rows):
        print(number, end=" ")
        number += 1
    print()