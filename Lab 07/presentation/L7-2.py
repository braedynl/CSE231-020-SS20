import copy

# Shallow copy behavior

colors1 = ["red", "blue"]
colors2 = colors1
colors2[1] = "green"

print("colors1:", colors1)
print("colors2:", colors2)


# Deep copy behavior (functions like how you normally use assignment for immutables)

colors1 = ["red", "blue"]
colors2 = copy.deepcopy(colors1)

colors2[1] = "green"

print("\ncolors1:", colors1)
print("colors2:", colors2)