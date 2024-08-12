# handle index error
init_list = [0,1,2,3,4,5,6,7,8,9,10]

try:
    idx = int(input("Enter an index: "))
    print(init_list[idx])
except IndexError:
    print("Incorrect index. Out of range.")
          
