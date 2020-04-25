# Lab15b - Example Answer (Undocumented)
# Braedyn Lettinga

import pandas as pd

def read_csv_2(filename):
    ''' This function read a csv file into a DataFrame
    Returns: DataFrame'''

    return pd.read_csv(filename)     

def find_median_2(data_frame, column_name):
    '''This function receives a data frame and a string column name as input 
    and returns the median of the column name
    Returns: float'''
    
    return data_frame[column_name].median()
    
    
def find_highest_mpg(data_frame, country):
    '''This function receives a DataFrame and country as input and returns 
    the model of the country cars (str) with the highest mpg and the highest mpg.
    Returns: str, float'''
    
    country_df = data_frame[ data_frame["origin"] == country ]

    max_mpg = country_df["mpg"].max()

    max_mpg_car_df = country_df[ country_df["mpg"] == max_mpg ]

    max_mpg_cars = max_mpg_car_df["name"].to_list()

    return max_mpg_cars[0], max_mpg
    
    
def main():
    filename = "mpg.csv"
    data_frame = read_csv_2(filename)    # replace with the appropriate function call

    print("First 5 rows of columns mpg and horsepower:")
    print(data_frame[ ["mpg", "horsepower"] ].head())    # replace with the correct statement
    print()

    print("Last 5 rows of columns mpg, horsepower, model_year, and name:")
    print(data_frame[ ["mpg", "horsepower", "model_year", "name"] ].tail())    # replace with the correct statement
    print()
    
    acc_median = find_median_2(data_frame, "acceleration")    # replace with the appropriate function call
    print("Mean 0-60 mph acceleration time (in sec): {:.1f}\n".format(acc_median))
    
    car_name, country_max = find_highest_mpg(data_frame, "usa")    # replace with the appropriate function call
    print("Highest MPG US car:")
    print(car_name, "-", country_max, "mpg")
       
    
if __name__ == '__main__':
    main()





