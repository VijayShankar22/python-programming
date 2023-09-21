n=int(input("enter a number"))
sum=0
i=1
while i<=n:
    if i%2==0:
        sum += i
    i +=1
print("sum of all even numbers upto",n,"is:",sum)
