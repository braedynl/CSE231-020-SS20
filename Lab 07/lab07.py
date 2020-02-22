# Lab07 Example Answer (Undocumented)
# Braedyn Lettinga

import csv

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    reader = csv.reader(fp)
    
    for _ in range(4):  
        next(reader)

    L = []
    for row in reader:
        if row[0] != "":
            L.append(row)

    return L


def get_totals(L):
    us_pop = int(L[0][1].replace(",", ""))

    populations = []
    for row in L[1:]:
        populations.append( int(row[1].strip("<").replace(",","")) )

    total_pop = sum(populations) 

    return us_pop, total_pop


def get_largest_states(L):

    us_percent = float(L[0][2].strip("%"))

    largest_states = []
    for row in L[1:]:
        if float(row[2].strip("%")) > us_percent:
            largest_states.append(row[0])

    return largest_states


def get_industry_counts(L):
    industry_counts = [ [industry, 0] for industry in INDUSTRIES ]

    for row in L[1:]:
        industry = row[9]

        for counter_list in industry_counts:
            if counter_list[0] == industry:
                counter_list[1] += 1

    industry_counts.sort(key=lambda counter_list: counter_list[1], reverse=True)

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