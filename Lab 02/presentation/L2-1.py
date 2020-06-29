
# Boolean Operations and Conditionals

print( 3.5 >= 1.0 )
print()

grade = 3.5

# The print statement only runs if the conditional
# evaluates True. Note the colon at the end, and the
# indentation of the print statement.
if grade >= 1.0:
    print("You passed!")

grade = 0.5

if grade >= 1.0:    # The line evaluates to False, so we skip this print statement
    print("You passed!")


grade = 0.5

if grade >= 1.0:
    print("You passed!")
else:
    print("You failed!")    # Adding an else condition can give us the feedback we want


grade = 3.5

if grade >= 3.0:
    print("Excellent")
elif grade >= 2.0:      # Further categorization with elif
    print("Good")
else:
    print("Oof")


grade = 4.0

if not grade == 3.0:
    print("You did not get a 3.0")

print(not True == False)