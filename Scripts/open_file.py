'''
PROBLEM
-------

Design a function, named open_file, that continually asks the user
for a valid file name if the file does not exist, and otherwise returns
the opened file pointer instance if the file does exist. The function should 
take no arguments, and print the string "File does not exist. Try again."
if the file does not exist. 
'''

def open_file():
    while True:
        try:
            # ask for file name (str)
            file_name = input("Enter a file name: ")
            
            # attempt to open it ('r' = read mode)
            fp = open(file_name, mode='r')
            
            # return the file pointer (breaks loop)
            return fp  
        
        # if FileNotFoundError occurred:
        except FileNotFoundError: 
            
            # print error message (loop continues)
            print("File does not exist. Try again.")


fp = open_file()  # example call
