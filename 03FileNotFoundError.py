# handle FileNotFoundError
filename = "marks2.txt"
try:
    file = open(filename, 'r')
    text = file.read()
    print(text)
    file.close()
except FileNotFoundError:
    print("No such file exists")
