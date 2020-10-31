'''
CSE231 - Introduction to Programming I
Lab 5
Example Solution

Author: Braedyn Lettinga
'''

fp = open("data.txt", "r")

# .readline() returns the line that it "read", we
# can simply take it and add the "BMI" title to the end
print(fp.readline().strip() + "  BMI")

# averages
avg_height = 0
avg_weight = 0
avg_bmi = 0

# maximums
max_height = 0
max_weight = 0
max_bmi = 0

# minimums
min_height = 10**6
min_weight = 10**6
min_bmi = 10**6

# we're going to use a tracker variable, 'n',
# to count the number of people in the file
n = 0

for line in fp:
    line = line.strip()

    # extract the necessary info, converting types appropriately
    height = float(line[12:16])
    weight = float(line[24:29])

    bmi = weight / ((height)**2)

    # for each person, we're going to add to our
    # average variables and divide by the number
    # of people at the end
    avg_height += height
    avg_weight += weight
    avg_bmi += bmi

    # one way of checking for a max or min is by
    # comparing each with the currently set max/min.

    if height > max_height:    # if this individual's height is greater than the current, that's the new max
        max_height = height
    if height < min_height:    # if this individual's height is less than the current, that's the new min
        min_height = height

    # same goes for the weight and BMI
    if weight > max_weight:
        max_weight = weight
    if weight < min_weight:
        min_weight = weight

    if bmi > max_bmi:
        max_bmi = bmi
    if bmi < min_bmi:
        min_bmi = bmi
    
    n += 1    # increment the amount of people

    print("{}{:>12.2f}".format(line, bmi))    # prints the line + the BMI column data concatenated

# prints all of the averages, maxes and mins in a separate section,
# but in the same format. We divide the averages by the amount of people
# we counted in 'n'. 
print("\nAverage{:>9.2f}{:>13.2f}{:>12.2f}".format(avg_height / n, avg_weight / n, avg_bmi / n))
print("Max{:>13}{:>13.2f}{:>12.2f}".format(max_height, max_weight, max_bmi))
print("Min{:>13}{:>13.2f}{:>12.2f}".format(min_height, min_weight,min_bmi))