# Lab14 - Example Answer (Undocumented)
# Braedyn Lettinga

import pylab 
import csv 

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

    DATA[state] = percent


fig, ax = pylab.subplots( figsize=(10, 7) )

ax.bar( list(DATA.keys()), list(DATA.values()) )

ax.set_xticklabels( list(DATA.keys()), rotation=90 )

ax.set_xlabel("State")
ax.set_ylabel("Ratio")
ax.set_title("Ratio of Sales Tax to All State Taxes by State")

pylab.show()