'''
Design a function, named open_file, that continually asks the user
for a valid file name if the file does not exist, and otherwise returns
the file pointer object if the file does exist. The function should 
take no arguments, and print the string "File does not exist. Try again."
if the file does not exist. 
'''

def open_file():
    while True:

        try:
            file_name = input("Enter a file name: ")  # ask for file name
            fp = open(file_name, mode='r')            # attempt to open it ('r', read mode)
            return fp                                 # return the file pointer (breaks loop)

        except FileNotFoundError:                     # if FileNotFoundError occurred:
            print("File does not exist. Try again.")  # print error message (loop continues)

fp = open_file()
