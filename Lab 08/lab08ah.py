import string
from operator import itemgetter

def add_word( word_map, word ):

    # YOUR COMMENT
    if word not in word_map:
        word_map[ word ] = 0

    # YOUR COMMENT
    word_map[ word ] += 1


def build_map( in_file, word_map ):

    for line in in_file:

        # YOUR COMMENT
        word_list = line.split()

        for word in word_list:

            # YOUR COMMENT
            # If we want to ignore capitalization, what did we normally
            # do to circumvent that?
            word = word.strip().strip(string.punctuation)

            # We don't want to add whitespace to the dictionary,
            # so I would suggest putting something here to prevent that 🤔

            add_word( word_map, word )
        

def display_map( word_map ):

    word_list = list()

    # YOUR COMMENT
    for word, count in word_map.items():
        word_list.append( (word, count) )
    
    # If we want it sorted by both alphabetical AND the count, we
    # can do them sequentially. Sort word_list by the alphabetical order
    # of the contained word here!
    # The line below already has the sorting by count covered for us!

    # YOUR COMMENT
    # We also want to reverse the order in this function call!
    freq_list = sorted( word_list, key=itemgetter(1))

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():

    try:
        in_file = open( "document1.txt", "r" )    # Make an input() prompt here! 
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
