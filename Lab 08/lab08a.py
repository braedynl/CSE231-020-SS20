import string
from operator import itemgetter

def add_word( word_map, word ):

    # if the word is not in the dictionary
    if word not in word_map:
        word_map[ word ] = 0

    # Increment the word's value by 1
    word_map[ word ] += 1


def build_map( in_file, word_map ):

    for line in in_file:

        # Splits the line into a list
        word_list = line.split()

        for word in word_list:

            # Strips each word of punctuation and whitespace, and appends it to the dictionary
            word = word.strip().strip(string.punctuation).lower()    # ADDED: `.lower()`

            if word == "":    # ADDED: if-statement and block
                continue

            add_word( word_map, word )
        

def display_map( word_map ):

    word_list = list()

    # Iterates through the words and counts at once,
    # makes a tuple of the keys and values, and appends them
    # to a list, word_list
    for word, count in word_map.items():
        word_list.append( (word, count) )
    
    word_list.sort()    # ADDED: Sorts the list by alphabetical order of the word

    # Sorts the list by count
    freq_list = sorted( word_list, key=itemgetter(1), reverse=True )    # ADDED: `reverse=True`

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():

    try:
        in_file = open(input("Enter file name: "), "r")    # ADDED: `input("Enter file name: ")`
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:
    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()
