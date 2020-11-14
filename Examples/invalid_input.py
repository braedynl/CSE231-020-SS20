'''
PROBLEM
-------

Create a short program that asks the user for
an integer value above 0. If the user's input
does not meet these conditions, print the message
"Invalid input. Try again.", and re-prompt until
the input is valid. 
'''

# initial prompt
user_input = input("Input a number above 0: ")

# loop while user input is invalid
while (not user_input.isdigit()) or (float(user_input) <= 0):

    # error message
    print("Invalid input. Try again.")

    # prompt again
    user_input = input("Input a number above 0: ")

print("Valid input!")