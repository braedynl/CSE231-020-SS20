# people = {1: {"name": "Zach", "age": "7", "sex": "Male"},
#           2: {"name": "Ann", "age": "40", "sex": "Female"}}

people = {
    1: {
        "name": "Zach", 
        "age": "7", 
        "sex": "Male"
    },
    2: {
        "name": "Ann", 
        "age": "40", 
        "sex": "Female"
    }
}

# Accessing the Dictionary
print(people[1]["name"])
print(people[1]["age"])
print(people[2]["sex"])

# Creating a new entry
people[2]["married"] = True
print(people[2])

# Deleting an entry
del people[2]["married"]
print(people[2])
    
# Iteration
for id, info in people.items():
    print("\nPerson ID:", id)
    
    for key in info:
        print(key + ":", info[key])