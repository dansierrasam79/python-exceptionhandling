# handle Attribute error
init_list = [1,2,3,4,5,6]

try:
    len_val = len(init_list)
    #len_val = init_list.length
    print(len_val)
except AttributeError:
    print("No such attribute available for", init_list)
