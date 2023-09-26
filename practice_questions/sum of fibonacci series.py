n=int(input("enter the number"))
if(n==0 or n==1):
    print(n)
else:
    a=0
    b=1
    c=2
    fib_series=a+b
    i=2
while (i<=n):
    c=a+b
    a=b
    b=c
    fib_series += c
    i+=1
print("sum of fibonacci series:",fib_series)
