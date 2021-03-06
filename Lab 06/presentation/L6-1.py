# Source: ourworldindata.org
# Retrieved: 8/3/2020

# *.txt files w/ lists

def open_file():
    while True:
        try:
            return open(input('Enter file name: '), 'r')
        except FileNotFoundError:
            print('File not found, try again.')

def print_data(data):
    # (only extracting certain countries for sake of brevity)

    header = "{:<16s}{:<16s}{:<16s}{:<16s}{:<16s}{:<16s}".format('Date', 'World', 'Canada', 'South Korea', 'United States', 'US%')
    body = "{:<16}{:<16}{:<16}{:<16}{:<16}{:<16.2%}"

    us_percents = []    # we'll create a list to store the column of US percents

    print(header)
    for line_list in data:      # iterate through the list of lists
        print(body.format(line_list[0], line_list[1], line_list[2], line_list[6], line_list[7], line_list[8]))

        us_percents.append(line_list[8])    # continually add with each row value

    print('\nMax US%: {:.2%}'.format(max(us_percents)))     # extract the max with the max() function


def parse_data(fp):
    fp.readline()                           # skips header line
    
    data = []                               # we'll store all of our interpreted data here

    for line_str in fp:                     # reads through each line of the file
        line_str = line_str.strip()         # you should ALWAYS .strip() *.txt file lines


        # You'll typically be interested in particular columns and rows. It's always
        # a good idea to inspect the data file(s) beforehand to get a reference on where 
        # your important indices are.

        # By inspection of the file, we can deduce that the date will be index 0, world
        # at index 1, Canada at index 2, etc.

        # for this example, we'll examine the percent of world cases that are from the US.

        line_list = line_str.split()        # we .split() the string into a list of strings

        world_cases = int(line_list[1])     # extract the world cases,
        us_cases = int(line_list[-1])       # and the US cases -- ensuring they're of proper type

        try:
            us_percent = us_cases / world_cases
        except ZeroDivisionError:           # error catch in case world_cases is 0
            us_percent = 0.0                # defaults to 0 if true

        line_list.append(us_percent)        # we'll add the data we discovered to the existing list

        data.append(line_list)              # and model the entire file by making a list-of-lists

    return data

def main():
    fp = open_file()
    data = parse_data(fp)
    print_data(data)

    # (always import at the top of your program, I just put it down here for ease of demonstration)
    from plot_data import plot_data; plot_data(data)
    

if __name__ == "__main__":
    main()