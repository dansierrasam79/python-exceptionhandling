# handle Arithmetic Error
num = 25
denom = 0

try:
    result = num/denom
    print(result)
except ArithmeticError:
    print("Arithmetic error has occurred")
