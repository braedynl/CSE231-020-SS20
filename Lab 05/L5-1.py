
in_file = open("input.txt", 'r')

for line in in_file:
    print(line)

in_file.close()

# When we run this, you'll notice that we get newlines
# for every line print. This is because the .txt file
# uses the \n to denote to itself that there's a newline.
# Python comes with a `.strip()` method to get rid of these.

# in_file = open("input.txt", 'r')

# for line in in_file:
#     line = line.strip()
#     print(line)

# in_file.close()