# Armstrong number


num= int(input("enter the digit"))
cp = num
pw = 0
while num != 0:
    pw += 1
    num = num // 10
s = 0
num = cp
while num != 0:
    r = num%10
    s = s+r ** pw
    num = num // 10
if s == cp:
    print(cp,"is Armstrong number")
else:
    print(cp, "is not Armstrong")
