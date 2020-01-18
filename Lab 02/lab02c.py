# Lab02 - Example Answer (Documented)
# Braedyn Lettinga

in_int = int( input("Input an integer (0 terminates): ") )

# Since we need to dynamically keep track of our inputs,
# we need to initialize these variables first so we can
# add on to them later. 
odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0


# We use a while-loop here because we don't know how
# long we'll need to keep it running.

# This loop in particular is checking whether our input, 
# in_int, is not 0. While it isn't, we execute the code we
# have indented in our loop-block.
while in_int != 0:

    # We're going to check if in_int is a negative number,
    # if it is, we simply want to re-prompt and not add anything
    # to our "tracking" variables.
    if in_int < 0:
        pass

    else:
        
        # If in_int is even, we add in_int to our sum, and add 1 to our count of
        # even numbers.
        if in_int % 2 == 0:
            even_sum += in_int
            even_count += 1
        
        # If in_int isn't even (odd), we do the same but with our odd number tracking
        # variables.
        else:    
            odd_sum += in_int
            odd_count += 1

        # Since we have an if-else structure at beginning, we know that all of
        # the numbers we'll be dealing with in this block of code is going to
        # be a positive number. We don't need to have a conditional. 
        positive_int_count += 1
    
    in_int = int( input("Input an integer (0 terminates): ") )

print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
