'''
CSE231 - Introduction to Programming I
Lab 8b
Example Solution

Author: Braedyn Lettinga
'''

def add_scores(score_dict, fp):
    '''
    Adds scores from a given file pointer to a 
    dictionary of scores. 

    Parameters
    ----------
        score_dict : Score dictionary.
        fp : File pointer instance.
    
    Returns
    -------
        None
    '''

    # skip header line
    fp.readline()

    # iterate through every line of the file pointer
    for line in fp:

        # clear whitespace from the line, split
        # by whitespace into a list
        line_list = line.strip().split()

        # obtain the name and score
        name = line_list[0]
        score = int(line_list[1])

        # if the name is not already inside the dictionary...
        if name not in score_dict:
            score_dict[name] = score  # initialize him/her with this score
        
        # otherwise...
        else:
            score_dict[name] += score  # sum their current score with this new one


def print_results(score_dict):
    '''
    Prints the given score dictionary in
    sorted alphabetical order.

    Parameters
    ----------
        score_dict : Score dictionary.

    Returns
    -------
        None
    '''

    # to sort a dictionary, remember that you must take
    # the list of tuples (dict.items()), sort that, then
    # turn it BACK into a dictionary using the dict() function
    sorted_dict = dict(sorted(score_dict.items()))

    # print our header
    print('{:10s}{:<10s}'.format("Name", "Total"))

    # iterate through the sorted dictionary
    for name, score in sorted_dict.items():
        print('{:10s}{:<10d}'.format(name, score))  # print each row


def main():
    # create an empty dictionary
    score_dict = {}

    # open up our two files
    data1 = open('data1.txt', 'r')
    data2 = open('data2.txt', 'r')

    # add scores to the same dictionary with
    # both files
    add_scores(score_dict, data1)
    add_scores(score_dict, data2)

    # print the results once we've added them all
    print_results(score_dict)


if __name__ == '__main__':
    main()