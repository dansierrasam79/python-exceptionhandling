#handle TypeError

try:
    num = float(input("Enter a number: "))
    num2 = float(input("Enter a number: "))
    result = num*num2
    print("Product of two numbers: ", result)
except ValueError:
    print("One of the values is not a number")
