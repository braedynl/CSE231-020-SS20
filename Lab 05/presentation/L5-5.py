
in_file = open("input.txt", "r")

for line in in_file:
    print(line.strip())

# print(line)
in_file.seek(0)    # Resets the reader back to the first line

for line in in_file:
    print(line.strip())
