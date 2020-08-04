
user_input = input("Type 'yes': ")
user_score = int(input("Input a score greater than/equal to 50: "))

if user_input == 'yes' and user_score >= 50:
    print("Thank you!")

elif user_input == 'yes' and user_score < 50:
    print("Your score was below 50")

elif user_input != 'yes' and user_score >= 50:
    print("Your input wasn't 'yes'")

else:
    print("Both your input and score were invalid :(")