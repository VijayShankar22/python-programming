# write a python code to print the multiplication table of a given number when the number is entered by the user.

n = int(input("Enter a number: "))
i = 1
print()
print(f"Multiplication table of {n}") 
print()
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1
