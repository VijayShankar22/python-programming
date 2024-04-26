# write a python program to print the following pattern.

'''
input: n = 5

output:

1
1 2
1 2 3 
1 2 3 4
1 2 3 4 5 

'''

n = int(input("n = "))

for rows in range(1,n+1):
    for columns in range(1,rows+1):
        print(columns, end=" ")
    print()