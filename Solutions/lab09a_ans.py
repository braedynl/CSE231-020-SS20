'''
CSE231 - Introduction to Programming I
Lab 9a
Example Solution

Author: Braedyn Lettinga
'''

data_map = {}

def build_map( in_file1, in_file2 ):
    '''This function builds a dictionary called `data_map`
    from a given continents and cities text file.'''
    
    in_file1.readline()
    in_file2.readline()

    # ITERATE THROUGH EACH `line` IN FILE 1 (continents.txt)
    for line in in_file1:    # ADDED
        continent_list = line.strip().split()  
        
        continent = continent_list[0].strip().title()  
        country = continent_list[1].strip().title()

        if continent != "":

            # IF `continent` ISN'T IN `data_map`:
                # INSERT THE CONTINENT AS THE KEY, WITH AN EMPTY DICTIONARY VALUE

            # ADDED: Lines 31-32
            if continent not in data_map.keys():    
                data_map[continent] = dict()

            
            # IF `country` ISN'T AN EMPTY STRING:
                # IF `country` ISN'T IN THE CONTINENT'S DICTIONARY:
                    # INSERT THE COUNTRY INTO THE CONTINENT'S INNER-DICTIONARY, WITH AN EMPTY LIST VALUE

            # ADDED: Lines 40-42
            if country != "":
                if country not in data_map[continent].keys():
                    data_map[continent][country] = list()
            
    
    # ITERATE THROUGH EACH `line` IN FILE 2 (cities.txt)
    for line in in_file2:    # ADDED
        countries_list = line.strip().split()    
        
        country = countries_list[0].strip().title()   
        city = countries_list[1].strip().title()
        
        if country != "":
            for continent in data_map:
                if country in data_map[continent]:

                    # IF `city` NOT IN THE `data_map[continent][country]` LIST:
                        # APPEND `city` TO THE LIST OF CITIES
                    
                    # ADDED: Lines 60-61
                    if city not in data_map[continent][country]:
                        data_map[continent][country].append(city)

    # RETURN `data_map`
    return data_map    # ADDED


def display_map( data_map ):
    '''This function prints `data_map` with some special
    formatting to the console.'''

    # OBTAIN A LIST OF ALL THE CONTINENT NAMES AND SORT IT
    # continents_list = sorted(...)
    continents_list = sorted(data_map.keys())    # ADDED

    # ITERATE THROUGH THE `continents` IN `continents_list`
    for continents in continents_list:    # ADDED
        print("{}:".format(continents))

        # OBTAIN A LIST OF ALL THE COUNTRIES ASSOCIATED WITH THE CURRENT CONTINENT AND SORT IT
        # countries_list = sorted(...)
        countries_list = sorted(data_map[continents].keys())    # ADDED

        # ITERATE THROUGH THE `countries` IN `countries_list`
        for countries in countries_list:    # ADDED
            print("{:>10s} --> ".format(countries), end='') 

            # OBTAIN A LIST OF ALL THE `cities` ASSOCIATED WITH THE CURRENT CONTINENT/COUNTRY AND SORT IT
            # cities = sorted(...)
            cities = sorted(data_map[continents][countries])    # ADDED

            # I did this part below for you guys since it's irrelevant to the 
            # main takeaway of this lab problem. No work needs to be done here.
            for city in cities:
                if cities[-1] != city:    
                    print('{}, '.format(city),end = '') 
            print('{}'.format(city)) 


def open_file():
    '''Prompts console for a file name and returns a
    file pointer if successful. Returns None otherwise.'''

    try:
        filename = input("Enter file name: ")
        in_file = open( filename, "r" )

    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


def main():
    '''Opens continents.txt and cities.txt to read-in to
    a dictionary. It then prints the data in an organized 
    format to the console.'''

    in_file1 = open_file()    # Open continents.txt first,
    in_file2 = open_file()    # and cities.txt second

    if in_file1 != None and in_file2 != None:
        
        build_map( in_file1, in_file2 )
        display_map( data_map )
        in_file1.close()
        in_file2.close()

if __name__ == "__main__":
    main()