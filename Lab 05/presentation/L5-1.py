
fp = open("Lab 05/presentation/input.txt", 'r')

for line in fp:
    print(line)

# When we run this, you'll notice that we get empty lines
# for every line print. This is because the .txt file
# uses the '\n' character to denote to itself that there's a new line.
# Python comes with a `.strip()` str method to get rid of these.

fp.seek(0)

for line in fp:
    line = line.strip()
    print(line)

fp.close()