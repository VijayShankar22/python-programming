print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

value = int(input("Enter a number from 1, 2, 3, 4 for operations: "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if value == 1:
    print("Sum of", num1, "and", num2, "is", num1 + num2)
elif value == 2:
    print("Difference of", num1, "and", num2, "is", num1 - num2)
elif value == 3:
    print("Product of", num1, "and", num2, "is", num1 * num2)
elif value == 4:
    if num2 != 0:
        print("Division of", num1, "and", num2, "is", num1 / num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Enter a valid value from 1, 2, 3, 4.")
