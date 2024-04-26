# write a python code to print the following pattern.

'''

input: n = 7

output:

*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*

'''

n = int(input("n = "))

for rows in range(1,n+1):
    for columns in range(rows):
        print("* ", end="")

    print()

for rows in range(n-1, 0, -1):
    for columns in range(rows):
        print("* ", end="")

    print()
