from random import *

computer_num=randrange(1, 101)
score = 10
while True:
    user_num = int(input("guess the number between 1 and 100\n"))
    if user_num == computer_num:
        print("you win with score",score)
        break
    elif user_num > computer_num:
        print("Too large")
    else:
        print("Too small")
    score -= 1
