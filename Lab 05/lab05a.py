# Lab05 (a) - Example Answer (No Comments)
# Braedyn Lettinga

in_file = open("data.txt", "r")
print(in_file.readline().strip() + "  BMI")

avg_height = 0
avg_weight = 0
avg_bmi = 0

max_height = 0
max_weight = 0
max_bmi = 0

min_height = 10**6
min_weight = 10**6
min_bmi = 10**6

i = 0
for line in in_file:
    line = line.strip()

    height = float(line[12:16])
    weight = float(line[24:29])

    bmi = weight / ((height)**2)

    avg_height += height
    avg_weight += weight
    avg_bmi += bmi

    if height > max_height:
        max_height = height
    if height < min_height:
        min_height = height
    
    if weight > max_weight:
        max_weight = weight
    if weight < min_weight:
        min_weight = weight

    if bmi > max_bmi:
        max_bmi = bmi
    if bmi < min_bmi:
        min_bmi = bmi
    
    i += 1

    print("{}{:>12.2f}".format(line, bmi))

print("\nAverage{:>9.2f}{:>13.2f}{:>12.2f}".format(avg_height/i, avg_weight/i, avg_bmi/i))
print("Max{:>13}{:>13.2f}{:>12.2f}".format(max_height, max_weight, max_bmi))
print("Min{:>13}{:>13.2f}{:>12.2f}".format(min_height, min_weight,min_bmi))