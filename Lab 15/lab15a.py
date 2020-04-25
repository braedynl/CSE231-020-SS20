# Lab15a - Example Answer (Undocumented)
# Braedyn Lettinga

import pandas as pd # import pandas module
import time  # used to calculate execution time
import csv  # import csv module


def read_csv_1(filename):
    ''' This function read a csv file into a list of lists (each line is an element)
    Returns: list of lists'''
    
    data = []

    reader = csv.reader(open(filename))
    next(reader)

    for line in reader:
        data.append(line)

    return data


def read_csv_2(filename):
    ''' This function read a csv file into a DataFrame
    Returns: DataFrame'''
    
    return pd.read_csv(filename)


def find_median_1(data, index):
    '''This function receives a list of lists (data) and an integer index as input 
    and calculates and prints the median of the column index'''
            
    column = []

    for i in range(len(data)):
        column.append(int(data[i][index]))

    column.sort()
    
    if len(column) % 2 == 0:
        median = (column[ len(column) // 2 ] + column[ len(column) // 2 + 1 ]) / 2
    else:
        median = column[ len(column) // 2 ]

    return median


def find_median_2(data_frame, column_name):
    '''This function receives a data frame and a string column name as input 
    and calculates and prints the median of the column name'''
    
    return data_frame[column_name].median()
    
    
def main():
    filename = "college_scorecard.csv"
    
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