'''
CSE231 - Introduction to Programming I
Lab 7
Example Solution

Author: Braedyn Lettinga
'''

import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']


def read_file(fp):
    reader = csv.reader(fp)
    
    for i in range(4):  # Skips the first 4 rows of the CSV
        next(reader, None)

    L = []

    # Grabs every row if it isn't empty, and creates a list
    # comprised of all rows as lists (a list of lists)
    for row in reader:  # remember that every row with the CSV reader will already be a list
        if row[0] != "":
            L.append(row)

    return L


def get_totals(L):

    # US pop is the 0th row, 1st item
    us_pop = int(L[0][1].replace(",", ""))

    total_pop = 0

    # [1:] to skip the US row
    for row in L[1:]:
        # strip the row of commas and '<' symbols if any, add to sum
        total_pop += int(row[1].replace('<', '').replace(',', ''))

    return us_pop, total_pop


def get_largest_states(L):

    # US percent is the 0th row, 2nd item
    us_percent = float(L[0][2].replace('%', ''))

    largest_states = []

    # [1:] to skip the US row
    for row in L[1:]:
        
        # extract necessary info from the row
        state_name = row[0]
        state_percent = float(row[2].replace('%', ''))

        # if the state percent is greater than the US percent
        if state_percent > us_percent:
            largest_states.append(state_name)  # append the state name

    return largest_states


def get_industry_counts(L):
    # This creates a list of lists, where each inner-list contains
    # a string of the industry at index 0, and an associated count
    # for that industry at index 1, alike:
    # [ [{industry name}, {count}], [{industry name}, {count}], ... ]
    industry_counts = []

    for industry in INDUSTRIES:
        industry_counts.append( [industry, 0] )

    # [1:] to skip the US row
    for row in L[1:]:
        industry = row[9]  # obtain the industry for the row we're on

        # We search through the industry_counts list to find the count
        # associated with whatever industry we have for this particular row.
        for counter_list in industry_counts:
            if counter_list[0] == industry:  # once we find it,
                counter_list[1] += 1         # we add one to the count

    # we want to sort the industry_counts list by their frequency,
    # (remember that they're at index 1 of each sub-list), so we
    # supply the value '1' to the itemgetter() function. we also
    # reverse it to make it sort in descending order (largest to smallest) 
    industry_counts.sort(key=itemgetter(1), reverse=True)

    return industry_counts


def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    
    us_pop, total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))


if __name__ == "__main__":
    main()