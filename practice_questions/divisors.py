n=int(input("enter a number"))
divisor=[]
for i in range(1,n+1):
    if n%i==0:
        divisor.append(i)
print("divisors of the given numbers are:",divisor)
     
