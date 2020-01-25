# Lab03 - Example Answer (Documented)
# Braedyn Lettinga

VOWELS = "aeiou"    # Creating a string that holds all of our vowel characters for later use

# We can lowercase the word to make it easier to check in our while-loop 
word = input("Enter a word ('quit' to quit): ").lower()    

while word != "quit":

    # If the first character in the word (word[0]) is a vowel,
    # all we need to do is add "way" to the end
    if word[0] in VOWELS:
        print(word + "way")

    # In the case of consonant letters at the beginning, we
    # need to take ALL consonant letters and move them to the
    # back until we find a vowel
    else:

        for char in word:    # Iterate through all of the characters in word

            if char not in VOWELS:    # If the character is consonant, move it to the back
                word = word[1:] + word[0]
        
            else:    # If the character is a vowel, we know we're finished, so we break the loop
                break
        
        # We complete the word by adding "ay" to the end
        print(word + "ay")

    word = input("Enter a word ('quit' to quit): ").lower()