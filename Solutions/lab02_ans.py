'''
CSE231 - Introduction to Programming I
Lab 2
Example Solution

Author: Braedyn Lettinga
'''

# initialize some counter variables
odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0

# take an initial input
in_int = int(input('Input an integer (0 terminates): '))

# loop while user input doesn't terminate
while in_int != 0:

    # if the int input is positive...
    if in_int > 0:

        # increment the positive int count
        positive_int_count += 1

        # if exactly divisible by 2...
        if in_int % 2 == 0:
            even_sum += in_int  # add the number to even sum
            even_count += 1     # add to even count
        
        # if not exactly divisible by 2...
        elif in_int % 2 != 0:
            odd_sum += in_int  # add the number to odd sum
            odd_count += 1     # add to odd count
    
    # re-prompt for continuous inputs
    in_int = int(input('Input an integer (0 terminates): '))

# program control will then flow down
# here once the while loop ends
print()
print('sum of odds:', odd_sum)
print('sum of evens:', even_sum)
print('odd count:', odd_count)
print('even count:', even_count)
print('total positive int count:', positive_int_count)