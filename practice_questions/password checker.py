correct_password= str("vijay12345")
password= input("enter the password")
while password != correct_password:
    print("incorrect password. Try again.")
    password=input("enter the password:")
print("correct password")
