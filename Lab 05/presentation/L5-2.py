
# When using write-mode, a new file will be created
# if one of the same name isn't found. If one IS found,
# it is overwritten. Be careful!
out_file = open("Lab 05/presentation/output.txt", 'w')

out_file.write("Hello, world\n")    # You can use the .write() method to.. write

# You'll manually have to add '\n' to your strings if you use .write(), however.
# print() adds newlines by default

print("Hello, world.. but with print()", file=out_file)    # use the `file` parameter

out_file.close()