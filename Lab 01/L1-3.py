
# Basic Mathematical Operators

pi = 3.14
e = 2.72

addition = pi + e
subtraction = pi - e 
multiplication = pi * e
division = pi / e

print("pi + e:", addition)
print("pi - e:", subtraction)
print("pi * e:", multiplication)
print("pi / e", division)
print()

# Modulus and Floor Division

int_5 = 5
int_2 = 2

print( "5 % 2:", int_5 % int_2 )    # 2 goes into 5 twice, with one left over (remainder)
print( "5 // 2:", int_5 // int_2 )    # 2 goes into 5 twice completely, any remainder is cutoff
print()

# Power

print( "2^3:", 2 ** 3 )    # 2 raised to the third power
print( "2^(1/2):", 2 ** (1/2) )    # 2 raised to the 1/2, or sqrt(2)

# Compound Assignment Operations

int_5 = 5

int_5 += 5    # We add 5 to int_5, and then re-assign int_5 to be that sum

print()
print(int_5)

int_5 = 5

int_5 = int_5 + 5    # This is an equivalent way of accomplishing that effect

print(int_5)

# This syntax notation can be applied to all of the operators shown.
# Append an '=' symbol to any of them and it works in just the same way.
