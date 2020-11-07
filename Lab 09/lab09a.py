data_map = {}

'''
This is a modified version of Enbody's lab09, since his is a mess.

When you see a single-line comment that is all uppercase,
replace/write a line below that will accomplish
the described desired effect.

I encourage use of the debugger on this! The Variable Explorer
in Spyder comes in real handy alongside the debugger.

                        IMPORTANT:
When you move onto part b, DO NOT RENAME THE FILE LIKE THE PDF SAYS!
Make a copy of the part a file you're working on, and rename that copy!
Part b has you make some changes to the part a file, but Mimir wants BOTH files!

This program is meant to read in two text files, continents.txt and 
cities.txt, into a dictionary that organizes all of the data into
continents, countries, and cities. The dictionary is declared in the
global namespace above as `data_map` (Dictionaries are mutable, so
we can edit it everywhere in the program!). The program, however, is
incomplete. Can you help me out with it? 🥺

Functions main() and open_file() are completed for you. You must edit
functions build_map() and display_map(). Feel free to create the functions
from scratch if it makes more sense to you that way.

Throughout the program, treat the variable `in_file1` as continents.txt,
and treat the variable `in_file2` as cities.txt. Meaning that, when testing
the program locally, input "continents.txt" to the first prompt and
"cities.txt" for the second prompt.

`data_map` is going to be a dictionary, whose keys are strings
of the continents, and the values are other dictionaries
where the keys within those other dictionaries are
strings of countries within whatever continent, and whose values 
are lists of strings of cities that are within whatever country.

`data_map` will have a structure akin to the example here:

data_map = {
    "continent1": {
        "country1": ["city1", ...],
        ...
    },
    ...
}

# Keys are the continents
print(data_map.keys())    # Out: dict_keys(["continent1", "continent2"])

# Accessing the continent's dictionary
print(data_map["continent1"])     # Out: {"country1": ["city1", "city2"], "country2": ["city1", "city2", "city3"]}

# Accessing the cities within a continent/country
print(data_map["continent2"]["country1"])    # Out: ["city1"]

'''

def build_map( in_file1, in_file2 ):
    '''This function builds a dictionary called `data_map`
    from a given continents and cities text file.'''
    
    in_file1.readline()
    in_file2.readline()

    # ITERATE THROUGH EACH `line` IN FILE 1 (continents.txt)
        continent_list = line.strip().split()  
        
        continent = continent_list[0].strip().title()    
        country = continent_list[1].strip().title()

        if continent != "":

            # IF `continent` ISN'T IN `data_map`:
                # INSERT THE CONTINENT AS THE KEY, WITH AN EMPTY DICTIONARY VALUE
            
            # IF `country` ISN'T AN EMPTY STRING:
                # IF `country` ISN'T IN THE CONTINENT'S DICTIONARY:
                    # INSERT THE COUNTRY INTO THE CONTINENT'S INNER-DICTIONARY, WITH AN EMPTY LIST VALUE
            
    
    # ITERATE THROUGH EACH `line` IN FILE 2 (cities.txt)
        countries_list = line.strip().split()    
        
        country = countries_list[0].strip().title()   
        city = countries_list[1].strip().title()
        
        if country != "":
            for continent in data_map:
                if country in data_map[continent]:

                    # IF `city` NOT IN THE `data_map[continent][country]` LIST:
                        # APPEND `city` TO THE LIST OF CITIES

    # RETURN `data_map`


def display_map( data_map ):
    '''This function prints `data_map` with some special
    formatting to the console.'''

    # OBTAIN A LIST OF ALL THE CONTINENT NAMES AND SORT IT
    # continents_list = sorted(...)

    # ITERATE THROUGH THE `continents` IN `continents_list`
        print("{}:".format(continents))

        # OBTAIN A LIST OF ALL THE COUNTRIES ASSOCIATED WITH THE CURRENT CONTINENT AND SORT IT
        # countries_list = sorted(...)

        # ITERATE THROUGH THE `countries` IN `countries_list`
            print("{:>10s} --> ".format(countries),end = '') 

            # OBTAIN A LIST OF ALL THE `cities` ASSOCIATED WITH THE CURRENT CONTINENT/COUNTRY AND SORT IT
            # cities = sorted(...)


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
