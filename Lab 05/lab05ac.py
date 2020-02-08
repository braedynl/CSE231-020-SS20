# Lab05 (a) - Example Answer (Documented)
# Braedyn Lettinga

in_file = open("data.txt", "r")

# One thing that I forgot to mention that using .readline()
# will return the line that was just read as a string. So you
# can use normal string operations on them.
print(in_file.readline().strip() + "  BMI")

# Averages
avg_height = 0
avg_weight = 0
avg_bmi = 0

# Maximums
max_height = 0
max_weight = 0
max_bmi = 0

# Minimums
min_height = 10**6
min_weight = 10**6
min_bmi = 10**6

# We're going to use a "tracker" variable, `i`,
# to count the number of people in the file
i = 0
for line in in_file:
    line = line.strip()

    height = float(line[12:16])
    weight = float(line[24:29])

    bmi = weight / ((height)**2)

    # For each person, we're going to add to our
    # average variables and divide by the number
    # of people at the end
    avg_height += height
    avg_weight += weight
    avg_bmi += bmi

    # One way of checking for a max or min is by
    # comparing each with the currently set max/min.

    if height > max_height:    # If this individual's height is greater than the current, that's the new max
        max_height = height
    if height < min_height:    # If this individual's height is less than the current, that's the new min
        min_height = height

    # Same goes for the weight and BMI
    if weight > max_weight:
        max_weight = weight
    if weight < min_weight:
        min_weight = weight

    if bmi > max_bmi:
        max_bmi = bmi
    if bmi < min_bmi:
        min_bmi = bmi
    
    i += 1    # Increment the amount of people

    print("{}{:>12.2f}".format(line, bmi))    # Prints the line + the new column of BMI

# Prints all of the averages, maxes and mins in a separate section
# but in the same format. We divide the averages by the amount of people
# we counted in `i`. 
print("\nAverage{:>9.2f}{:>13.2f}{:>12.2f}".format(avg_height/i, avg_weight/i, avg_bmi/i))
print("Max{:>13}{:>13.2f}{:>12.2f}".format(max_height, max_weight, max_bmi))
print("Min{:>13}{:>13.2f}{:>12.2f}".format(min_height, min_weight,min_bmi))