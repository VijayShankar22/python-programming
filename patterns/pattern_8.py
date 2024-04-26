# write a python program to print the following pattern.

'''

input: n = 10

output:

         *
        * *
       *   *
      *     *
     *       *
    *         *
   *           *
  *             *
 *               *
*******************

'''



n = int(input("n = "))


for rows in range(1, n):
    print(" " * (n - rows), end="")       
    if rows == 1:
        print("*", end="")
    else:
        print("*" + " " * (2 * rows - 3) + "*", end="")
    print(" " * (n - rows))             

print("*" * (2 * n - 1))
