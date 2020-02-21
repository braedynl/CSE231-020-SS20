import csv 
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    # reader = csv.reader(fp)

    # using `csv.reader()` makes going through .csv files
    # exactly like .txt files with `open()`

    # You can skip unnecessary lines with `next(reader)`

    # iterate through each line with
    # `for line in reader:`
    # Lines will ALREADY BE BROKEN UP INTO LISTS

    # Create a big list to hold all your smaller lists
    
    # One way to ensure you don't get empty lines in your big list
    # is to check the state column for its contents, `line[0]`
    pass

def get_totals(L):
    # Initialize a total population number

    # for row in L:    # `row` is now a list

        # row[1] is the population column

        # if row[0] == "U.S.":
            # Store population as int, make sure to get rid of the comma separators

        # else:
            # Add to total population from earlier
            # .strip("<").replace(",","") works well here
            # make sure to convert!
    
    # return us_pop, total_pop
    pass 

def get_largest_states(L):
    # US percent is 3.3, just hard-code that, it's unnecessary to template it in my opinion

    # I would begin iterating through from `L[1:]` onwards to skip the US entry

    # row[2].strip("%"), what type is row[2]?

    # Append row[0] (the state) to a big list
    pass

def get_industry_counts(L): 
    # The template for the return looks like:
    # [ [{industry name}, {count}], [{industry name, count}], ... ]
    
    # My Lists, Tuples and Sorting notebook talks more about list comprehension
    # and sort functions if you need a refresher.
    # (In this repository, Extra/ folder)

    # You can quickly create a list like this with list comprehension,
    # and using the list of industries already given to us at the beginning
    # `[ [industry, 0] for industry in INDUSTRIES ]`

    # for row in L[1:]:

        # industry at row[9]

        # find the industry in your list of lists from earlier,
        # and +=1 to the count initialized alongside it

    # You can use itemgetter() or lambda functions. I know
    # lambdas may be difficult for right now so here's one you can use:
    # .sort( key=lambda li: li[1], reverse=True )
    pass

def main():
    # Already finished for you
    pass 

if __name__ == "__main__":
    main()
