# Question: take a number n as input and print it in reverse order.


number = int(input("Enter a number: "))
for i in range(number, 0, -1):
    number -= 1
    print(number)
