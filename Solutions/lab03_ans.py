'''
CSE231 - Introduction to Programming I
Lab 3
Example Solution

Author: Braedyn Lettinga
'''

# string that holds all of the vowels
VOWELS = 'aeiou'

# initial prompt
word = input("Enter a word ('quit' to quit): ").lower()

# loop while user input does not quit
while word != 'quit':

    # if the first character is a vowel...
    if word[0] in VOWELS:
        print(word + 'way')  # concatenate 'way'

    # otherwise...
    else:

        # for every character in the word,
        for char in word:

            # if the character is not a vowel...
            if char not in VOWELS:
                word = word[1:] + word[0]  # move to the back
            
            # otherwise...
            else:
                break  # stop iterating
        
        # append 'ay' to the end
        print(word + 'ay')
    
    # re-prompt for continuous user input
    word = input("Enter a word ('quit' to quit): ").lower()

