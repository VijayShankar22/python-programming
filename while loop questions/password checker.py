import time

password = "vijay12345"
attempts = 5

while True:
    user_password = input("\nEnter the password: ")
    if user_password == password:
        print("Login successful")
        break
    else:
        print("Wrong password, try again")
        attempts -= 1
        if attempts <= 0:
            print("Failed to login")
            count = 10
            while count != 0:
                print(count, end=' ')
                time.sleep(1)
                count -= 1
            attempts = 5
