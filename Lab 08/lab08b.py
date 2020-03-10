# Lab08b - Example Answer (Undocumented)
# Braedyn Lettinga

DATA1 = open("data1.txt") 
DATA2 = open("data2.txt")

SCORES = dict()

def add_scores( score_dict:dict, fp ):
    fp.readline()

    for line in fp:
        line_list = line.strip().split()    

        if line_list[0] not in score_dict:   
            score_dict[line_list[0]] = int(line_list[1]) 
        else:
            score_dict[line_list[0]] += int(line_list[1])   
        

def print_results(score_dict:dict):
    sorted_dict = sorted(score_dict.items())   

    print("{:10s}{:<10s}".format("Name", "Total"))
    for name, score in sorted_dict:
        print("{:10s}{:<10d}".format(name, score))


def main():
    add_scores(SCORES, DATA1)
    add_scores(SCORES, DATA2)
    print_results(SCORES)

if __name__ == "__main__":
    main()