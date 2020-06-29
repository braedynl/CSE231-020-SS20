my_str = "Hello!"

# Iterating through the indices in my_str
for i in range( len(my_str) ):
    print(my_str[i])

# Iterating through the characters in my_str
for char in my_str:
    print(char)
    
# Iterating through BOTH in my_str
for i, char in enumerate(my_str):
    print(char)
    print(my_str[i])