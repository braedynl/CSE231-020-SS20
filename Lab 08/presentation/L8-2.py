D = {
    "this": 1,
    "is": 2,
    "an": 3,
    "example": 4
}

print(D.items())    # Notice how these are all lists! (Or at least a list-type)
print(D.keys())
print(D.values())

for key in D:    # Will normally iterate through by key
    print(key)
    
for key in D.keys():    # Explicitly by key
    print(key)

for value in D.values():    # By value
    print(value)
    
for key, value in D.items():    # By both
    print(key, value)