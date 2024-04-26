# write a python program to print the following pattern.

'''
input: n = 5

output:

*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 *

'''

n = int(input("n = "))


for rows in range(1, n+1):
    for columns in range(1, rows+1):
        print("* ", end="")
    print(" " * (4 * (n-rows)), end="")
    for columns in range(1, rows+1):
        print("* ", end="")
    print()


for rows in range(n-1, 0, -1):
    for columns in range(1, rows+1):
        print("* ", end="")
    print(" " * (4 * (n-rows)), end="")
    for columns in range(1, rows+1):
        print("* ", end="")
    print()




#2

'''

input: n = 7

output:

*            *
**          **
***        ***
****      ****
*****    *****
******  ******
**************
******  ******
*****    *****
****      ****
***        ***
**          **
*            *

'''

n = int(input("n = "))


for rows in range(1, n+1):
    for columns in range(1, rows+1):
        print("*", end="")
    print(" " * (2 * (n-rows)), end="")
    for columns in range(1, rows+1):
        print("*", end="")
    print()


for rows in range(n-1, 0, -1):
    for columns in range(1, rows+1):
        print("*", end="")
    print(" " * (2 * (n-rows)), end="")
    for columns in range(1, rows+1):
        print("*", end="")
    print()
