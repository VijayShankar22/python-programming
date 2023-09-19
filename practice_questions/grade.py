#write a python program to print the grade of the studenet.

#if students mark is 90 or more than 90 print grade A.
#if students mark is equal to or more than 70 print B.
#if students mark is equal to or more than 50 print c.
#if students mark is equal to or more than 30 print D.
#if students mark is less than 30 print fail.











m=float(input("enter the marks obtained"))
if (m>=90):
    print("A")
if(m>=70) and (m<=90):
    print("B")
if (m>=50) and (m<=70):
    print("c")
if(m>=30) and (m<=50):
    print("D")
if (m<30):
    print("fail")
