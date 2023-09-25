n = int(input("Enter the number: "))

if n == 0 or n == 1:
    print("yes")
else:
    a = 0
    b = 1
    list = [a, b]
    i = 2
    while i <= n:
        c = a + b
        a = b
        b = c
        list.append(c)
        i = i + 1

    if n in list:
        print("yes")
    else:
        print("no")
