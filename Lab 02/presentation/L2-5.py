
for letter in "Python":
    if letter == 'h':
        break   # We preemptively break from the loop when we hit 'h'
    print("Current Letter:", letter)

print()

for letter in "Python":
    if letter == 'h':   # 'h' is skipped by continuing the loop instantly
        continue 
    print("Current Letter:", letter)