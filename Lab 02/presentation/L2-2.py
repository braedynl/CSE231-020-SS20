
# We get an initial answer
answer = input("Please say 'Hi': ")

# If the answer is not 'Hi', keep running
while answer != "Hi":

    print("You don't want to say Hi?")
    
    # Here, we keep redefining 'answer' with the input
    # until we get our desired message, 'Hi'
    answer = input("Let's try again... say 'Hi': ")

# This line will only run if the while-loop doesn't
print("Thanks for saying Hi!")