#palindrome number checker

num = int(input("enter the digit: "))
sum=0
cp=num
while num != 0 :
    r = num % 10
    sum = sum*10 + r
    num = num // 10
print("Reverse of",cp, "is",sum)
if cp == sum:
    print("Palindrome number")
else:
    print("Not a palindrome number")
