# Lab15a - Example Answer (Documented)
# Braedyn Lettinga

import pandas as pd # import pandas module
import time  # used to calculate execution time
import csv  # import csv module


def read_csv_1(filename):
    ''' This function read a csv file into a list of lists (each line is an element)
    Returns: list of lists'''
    
    data = []    # One big list that will simulate the entire table

    reader = csv.reader(open(filename))
    next(reader)

    for line in reader:
        data.append(line)    # We append each smaller list to that table

    return data


def read_csv_2(filename):
    ''' This function read a csv file into a DataFrame
    Returns: DataFrame'''
    
    # .read_csv() will go through the entire CSV file and
    # give you back a data frame for it. Very quick and easy!

    return pd.read_csv(filename)


def find_median_1(data, index):
    '''This function receives a list of lists (data) and an integer index as input 
    and calculates and prints the median of the column index'''
    
    # In order to find the median traditionally, we'll have to do
    # some pretty weird stuff

    column = []

    # Since we're trying to extract a column, (and each index of the
    # ghetto data frame we made is a list of lists), we have to iterate
    # through each row in the outer-list and extract each value at the
    # specified index. These are all strings at the moment, so we'll
    # additionally have to make them into ints. 
    for i in range(len(data)):
        column.append(int(data[i][index]))

    column.sort()    # We then sort that column list
    
    # If the column has an even amount of values, that means there are
    # two values in the "middle" of the dataset. We'll take the middle "lower-bound"
    # index of the set, (the length of the column divided by 2, floored),
    # and then the middle lower-bound incremented by 1 to get the "upper-bound".
    # We finally take those two values and evaluate the average. 
    if len(column) % 2 == 0:
        median = (column[ len(column) // 2 ] + column[ len(column) // 2 + 1 ]) / 2

    # Otherwise, if there's an odd number of values inside the dataset, that means
    # there's an explicit middle value. So it's as simple as floor-dividing the length of
    # the dataset by 2, and extracting the value at that index.
    else:
        median = column[ len(column) // 2 ]

    return median


def find_median_2(data_frame, column_name):
    '''This function receives a data frame and a string column name as input 
    and calculates and prints the median of the column name'''
    
    # In pandas, all we'll need to do is extract a column, (by name for
    # this function), and take the median by calling .median(). 
    # data_frame[column_name] is a Series() object, remember, so the
    # .median() function is a METHOD FUNCTION of a Series() object.

    return data_frame[column_name].median()
    
    
def main():
    filename = "college_scorecard.csv"

    # In main(), we just replace some parts of Enbody's code to
    # include our function calls. 

    # The thing he wanted to demonstrate is the speed of pandas
    # compared to our traditional methods. The pandas library,
    # and a lot of other scientific Python libraries, are built
    # in C++ to make them faster.
    
    start_time = time.time()
    data_1 = read_csv_1(filename)    # REPLACE: read csv file using csv module
    time1 = time.time()
    print("read_csv_1: {:.4f}".format((time1 - start_time)*1000))
    
    start_time = time.time()
    data_2 = read_csv_2(filename)    # REPLACE: read csv file using pandas module
    time2 = time.time()
    print("read_csv_2: {:.4f}".format((time2 - start_time)*1000))
    
    index = 1
    column = 'OPEID'    # replace with the method to retrieve the column name 
    
    start_time = time.time()
    median_1 = find_median_1(data_1, index)    # REPLACE: find the median using lists
    time3 = time.time()
    print("find_median_1 time: {:.4f}".format((time3 - start_time)*1000))
    print("Median: ", median_1)
    
    start_time = time.time()
    median_2 = find_median_2(data_2, column)    # REPLACE: find the median using pandas
    time4 = time.time()
    print("find_median_2: {:.4f}".format((time4 - start_time)*1000))
    print("Median: ", median_2)
    
    
if __name__ == '__main__':
    main()