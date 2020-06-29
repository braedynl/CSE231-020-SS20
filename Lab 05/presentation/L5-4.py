def is_float(in_str:str):
    '''
    Checks if an input string can be
    converted to a float. Returns bool.
    '''

    try:
        float(in_str)
        return True 
    
    except ValueError:
        return False 

# print( is_float( "0.030" ) )
# print( is_float("0.e33i01j1") )


def get_file(file_name:str, mode:str):
    '''
    Obtains a file object given a file_name string.
    Returns file object, else returns None if the
    file doesn't exist.
    '''

    try:
        in_file = open(file_name, mode)
        return in_file
    
    except FileNotFoundError:
        print("File: '{}' does not exist".format(file_name))
        return None

in_file = get_file("input.txt", "r")
# for line in in_file:
#     print(line.strip())

in_file = get_file("thisfiledoesntexist.txt", "r")
# print(in_file)