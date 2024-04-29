# write a python code to convert decimal number to octal.


number = int(input("Enter a number: "))
orignal_num = number
octal = []
while number > 0:
    remainder = number % 8
    octal.append(remainder)
    number = number // 8

octal.reverse()
result = ''.join(map(str, octal))
print("Decimal to octal conversion.\n")
print(f"({orignal_num})\u2081\u2080 = ({result})\u2088")
