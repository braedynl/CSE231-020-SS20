def double_list( in_list ):
    for i in range(len(in_list)):
        in_list[i] = 2 * in_list[i]
    # no return necessary
        
        
ex_list = [2, 5, 9]
double_list(ex_list)    # Passing by reference

print(ex_list)


ex_list = [2, 5, 9]
double_list(ex_list[:])    # Passing by value

print(ex_list)