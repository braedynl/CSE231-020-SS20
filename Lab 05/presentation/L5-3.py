
in_file = open("filethatdoesntexist.txt", "r")

# if we try running this, we get a "FileNotFoundError".
# We can "catch" the error with a try-except

try:
    in_file = open("filethatdoesntexist.txt", "r")

except FileNotFoundError:    # You can also write `except:` to catch ANY error (can be hard to debug, though)
    print("File doesn't exist")