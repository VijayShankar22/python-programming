user_input=input("enter a word number or phrase:")
user_input=user_input.replace(" ","").lower()
if user_input==user_input[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
