n=int(input("enter the number of entries to calculate their product and average:"))
sum1=0
prod=1
for i in range(0,n,1):
    x=int(input("enter the number:"))
    sum1=sum1+x
    prod=prod*x
print("average of the given numbers is:", sum1/n)
print("product of the given numbers is:",prod)
