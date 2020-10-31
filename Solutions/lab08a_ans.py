'''
CSE231 - Introduction to Programming I
Lab 8a
Example Solution

Author: Braedyn Lettinga
'''

import string 
from operator import itemgetter


def add_word(word_map, word):

    # if the word is not already a key inside
    # word_map...
    if word not in word_map:
        word_map[word] = 0  # set the word with value 0
    
    # increment the word's value by 1
    word_map[word] += 1


def build_map(in_file, word_map):

    # iterate through every line of the file
    for line in in_file:

        # splits the line into a list (delimited by whitespace)
        word_list = line.split()

        for word in word_list:

            # strips each word of punctuation and extraneous
            # whitespace
            word = word.strip().strip(string.punctuation).lower()  # ADDED: .lower()

            # ADDED
            # if the word is an empty string, continue
            # to next iteration
            if word == '':
                continue

            add_word(word_map, word)


def display_map(word_map):

    # create an empty list
    word_list = list()

    # appends tuple pairs of each key-value pair
    # (word-count pair in our case) to word_list
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # ^ the algorithm above is equivalent to:
    # word_list = list(word_map.items())
    
    # ADDED
    # to sort by alphabetical AND frequency, with
    # frequency taking the most precedence, we first
    # sort by alphabetical...
    word_list.sort()

    # then we sort by frequency (index 1 of each tuple,
    # so itemgetter(1) is necessary here)
    freq_list = sorted(word_list, key=itemgetter(1), reverse=True)  # ADDED: reverse=True

    print("\n{:15s}{:5s}".format('Word', 'Count'))
    print('-' * 20)
    for item in freq_list:
        print('{:15s}{:>5d}'.format(item[0], item[1]))


def open_file():
    try:
        file_name = input("Enter file name: ")  # ADDED
        in_file = open(file_name, 'r')
    except IOError:
        print('\n*** unable to open file ***\n')
        in_file = None
    
    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:
    build_map(in_file, word_map)
    display_map(word_map)
    in_file.close()