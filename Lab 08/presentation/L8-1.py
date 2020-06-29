# Note that we have to check if the key exists already.
# If we try adding 1 to the value of letter_frequency[char]
# without checking if it exists, we would get KeyError

letter_frequency = {}

example_string = "mirror"

for char in example_string:
    if char in letter_frequency:
        letter_frequency[char] += 1
    else:
        letter_frequency[char] = 1
    
print(letter_frequency)