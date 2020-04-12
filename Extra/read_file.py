# Example read_file() from Proj08
# Braedyn Lettinga
# (Uploaded 4/12/2020)

import csv
from operator import itemgetter

def read_file(fp):
    D1 = {}
    D2 = {}
    D3 = {}
    
    reader = csv.reader(fp)
    next(reader)
    
    for line in reader:
       
        name = line[0].lower().strip()
        platform = line[1].lower().strip()
        genre = line[3].lower().strip()
        publisher = line[4].lower().strip()

        # The year column may sometimes have "N/A" as its
        # value, so we can try-except-continue in that case.
        try:
            year = int(line[2])
        except:
            continue

        na_sales = float(line[5]) 
        europe_sales = float(line[6]) 
        japan_sales = float(line[7]) 
        other_sales = float(line[8])
        
        na_sales = na_sales * 10**6
        europe_sales = europe_sales * 10**6
        japan_sales = japan_sales * 10**6
        other_sales = other_sales * 10**6
        
        global_sales = na_sales + europe_sales + japan_sales + other_sales

        '''
        Remember that our goal is to create three dictionaries that look like this:

        D1 = { name:[(name, platform, year, genre, publisher, global_sales), …], …}

        D2 = { genre: [(genre, year, na_sales, eur_sales, jpn_sales, other_sales, global_sales), …], …}

        D3 = { publisher: [(publisher, name, year, na_sales, eur_sales, jpn_sales, other_sales, global_sales), …], …}
        
        You'll notice that the lists may contain more tuples of info, and there'll be multiples
        of name, genre and publisher keys. 

        If we want to add to an existing value, then we need to check if it's present in the dictionary already.
        In order for it to be present in the dictionary, we need to initialize it first.
        '''

        if name not in D1.keys():    # Check if the name exists in D1...
            D1[name] = [(name, platform, year, genre, publisher, global_sales)]    # If it isn't, we'll initialize it with a list containing the first tuple of info
        else:
            D1[name].append((name, platform, year, genre, publisher, global_sales))    # Otherwise, we'll append to the list with more tuples

            # These lists need to be sorted by the global_sales in descending order. If you
            # were to try and go about this outside of the for-loop, it would be extremely difficult
            # (and inefficient). So we'll sort every time we add a new tuple
            D1[name].sort(key=itemgetter(5), reverse=True)
        
        # The same exact process happens for D2 and D3, just that the tuples contain different information
        # and the keys are different
        if genre not in D2.keys():
            D2[genre] = [(genre, year, na_sales, europe_sales, japan_sales, other_sales, global_sales)]
        else:
            D2[genre].append((genre, year, na_sales, europe_sales, japan_sales, other_sales, global_sales))
            D2[genre].sort(key=itemgetter(6), reverse=True)

            # ^^^
            # Since D2 has more items in its tuples, we need to specify itemgetter(6), since the global_sales
            # are at index 6 instead of 5 now. 
            
            
        if publisher not in D3.keys():
            D3[publisher] = [(publisher, name, year, na_sales,europe_sales, japan_sales, other_sales, global_sales)]
        else:
            D3[publisher].append((publisher, name, year, na_sales, europe_sales, japan_sales, other_sales, global_sales))
            D3[publisher].sort(key=itemgetter(7), reverse=True)
    

    # We lastly need to sort the dictionaries in alphabetical order
    # of their keys. We can accomplish this using .items(), (which will
    # break the dictionary into a list of tuples, remember), sort the
    # list of tuples, and then convert that back into a dictionary
    # using the dict() constructor 

    D1 = dict(sorted(D1.items()))
    D2 = dict(sorted(D2.items()))
    D3 = dict(sorted(D3.items()))
    
    return D1, D2, D3