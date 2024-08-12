# handle Keyboard Interrupt error
try:
    user_input = int(input("Enter a number: "))
    print(user_input)
except KeyboardInterrupt:
    print("User input cancelled")
