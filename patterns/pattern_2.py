# write a python program to print the following pattern.

'''
input: n = 5

output:

1
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

'''

n = int(input("n = "))

for rows in range(1,n+1):
    for columns in range(rows):
        print(rows, end=" ")
    print()

