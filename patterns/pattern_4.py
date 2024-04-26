# write a python progran to print the following pattern.

'''
input: n = 8

output: 

*
* *
* * *
* * * * 
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *

'''

n = int(input("n = "))

for rows in range(1,n+1):
    for columns in range(rows):
        print("*",end=" ")
    print()