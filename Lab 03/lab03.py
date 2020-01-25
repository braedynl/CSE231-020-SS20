# Lab03 - Example Answer (No Documentation)
# Braedyn Lettinga

VOWELS = "aeiou"
word = input("Enter a word ('quit' to quit): ").lower()

while word != "quit":

    if word[0] in VOWELS:
        print(word + "way")

    else:
        for char in word:

            if char not in VOWELS:
                word = word[1:] + word[0]
            
            else:
                break
        
        print(word + "ay")

    word = input("Enter a word ('quit' to quit): ").lower()