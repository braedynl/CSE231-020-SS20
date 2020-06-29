import copy

L1 = ["a", "b", "c"]
L2 = [1, L1, 2]

L1[1] = "🅱"    # Yes, Python supports emojis

print("L1:", L1)
print("L2:", L2)

L3 = L2

print("L3:", L3)

# This is where it gets weird. The [:] syntax
# takes a regular copy, not a DEEP copy. Since
# L2 is storing a REFERENCE to L1, L4 gets
# a separate L2 list value, but maintains a
# reference to L1 as its 2nd item in the list
L4 = L2[:]

print("L4:", L4)

L1.append("d")

print()
print("L1:", L1)
print("L2:", L2)
print("L3:", L3)
print("L4:", L4)

print("L3 is L2:", L3 is L2)
print("L4 is L2:", L4 is L2)

L5 = copy.deepcopy(L2)

print("L5:", L5)

L1.append("e")
L2.append(3)

# L5 doesn't care about changes to L1/2,
# it has it's own copy all to itself
print("L5:", L5)