# handle zero division error

num = 25
den = 0

try:
    result = num/den
    print("Division: ", result)
except ZeroDivisionError:
    print("Division by zero is not allowed")
