#A SHOPKEEPER WILL GIVE YOU A DISCOUNT OF 10% IF THE PURCHASE QUANTITY IS MORE THAN 1000RS.
#ASK USER TO THE ENTER THE NUMBER OF UNIT HE WANTS TO PURCHASE.SUPPOSE THE COST OF PER UNIT IS 100.
#PRINT THE DISCOUNT HE WILL GET.







u=int(input("enter the unit to purchase"))

if (u*100>=1000):
    print("you got a discount of:", u*100/10)
else:
    print("you did not got any discount")

