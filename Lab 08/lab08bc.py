# Lab08b - Example Answer (Documented)
# Braedyn Lettinga

DATA1 = open("data1.txt") 
DATA2 = open("data2.txt")

SCORES = dict()

def add_scores( score_dict:dict, fp ):
    '''Adds scores to a dictionary of names. If a name
    is already within the dictionary, the scores are combined.'''

    fp.readline()

    for line in fp:
        line_list = line.strip().split()    # Breaks line into a list

        if line_list[0] not in score_dict:    # If the name isn't in the dictionary
            score_dict[line_list[0]] = int(line_list[1])    # ..set their score to be whatever is in the line
        else:
            score_dict[line_list[0]] += int(line_list[1])    # ..otherwise, add to their currently existing score
        

def print_results(score_dict:dict):
    '''Prints a dictionary of names and score totals.'''
    
    sorted_dict = sorted(score_dict.items())    # sorts dictionary by the first item (0th index)

    print("{:10s}{:<10s}".format("Name", "Total"))
    for name, score in sorted_dict:
        print("{:10s}{:<10d}".format(name, score))


def main():
    add_scores(SCORES, DATA1)
    add_scores(SCORES, DATA2)
    print_results(SCORES)

if __name__ == "__main__":
    main()