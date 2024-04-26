# write a python program to print the following pattern.

'''
input: n = 8

output:

       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************

'''

n = int(input("n = "))

for rows in range(1,n+1):
    for columns in range(n-rows):
        print(" ", end="")
        
    for stars in range(2*rows-1):
        print("*",end="")
        
    print()
