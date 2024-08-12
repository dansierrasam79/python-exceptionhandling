# handle Value Error
try:
    user_input = int(input("Enter an integer: "))
    print(user_input)
except ValueError:
    print("Value entered is not an integer")
