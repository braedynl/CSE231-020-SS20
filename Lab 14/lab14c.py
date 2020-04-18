# Lab14 - Example Answer (Documented)
# Braedyn Lettinga

import pylab 
import csv 

# I'll be storing all of the CSV
# file things I need here
DATA = {}

fp = open("STC_2014_STC005.csv")

reader = csv.reader(fp)
next(reader)
next(reader)

for row_list in reader:

    state = row_list[2]

    total_taxes = int(row_list[3])
    sales_gross = int(row_list[5])

    percent = (sales_gross / total_taxes) * 100

    # Since all of the states only appear once inside
    # the CSV file, we won't need to check if the key
    # is already present. We'll just make one on-the-spot
    # and set its associated value to be the percentage
    DATA[state] = percent

# If we're doing this the object-oriented way,
# we can create a figure and axes object and
# plot what we need that way
fig, ax = pylab.subplots( figsize=(10, 7) )

# The stuff we want on the x-axis is the state names,
# while the bar heights that correspond to them will be
# the percentages
ax.bar( list(DATA.keys()), list(DATA.values()) )

# We'll set the xticks to be the state names, but since
# there are so many of them, we'll have to rotate them 90
# degrees for all of them to fit nicely
ax.set_xticklabels( list(DATA.keys()), rotation=90 )

# xlabel, ylabel and title
ax.set_xlabel("State")
ax.set_ylabel("Ratio")
ax.set_title("Ratio of Sales Tax to All State Taxes by State")

# And lastly, if we want to see what we've made,
# we can call .show()
pylab.show()


# An equivalent way of achieving the same effect would be
# the non-object-oriented way below. All of the functions
# act the same way, but have slightly different names.
# You now call through `pylab` instead of an axes object.

# Alternatively, since the pylab module is just matplotlib
# combined with numpy (but we're only using matplotlib),
# you could run:

# import matplotlib.pyplot as plt

# and replace all instance where you have `pylab` with `plt`
# and it would be equivalent.

'''
pylab.figure(figsize=(10, 7))

pylab.bar(list(DATA.keys()), list(DATA.values()))

pylab.xticks(list(DATA.keys()), rotation=90)

pylab.xlabel("State")
pylab.ylabel("Ratio")
pylab.title("Ratio of Sales Tax to All State Taxes by State")

pylab.show()
'''