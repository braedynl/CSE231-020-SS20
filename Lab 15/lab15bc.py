# Lab15b - Example Answer (Documented)
# Braedyn Lettinga

import pandas as pd

def read_csv_2(filename):
    ''' This function read a csv file into a DataFrame
    Returns: DataFrame'''

    # Same function as in lab15a
    return pd.read_csv(filename)     

def find_median_2(data_frame, column_name):
    '''This function receives a data frame and a string column name as input 
    and returns the median of the column name
    Returns: float'''
    
    # Same function as in lab15a
    return data_frame[column_name].median()
    
    
def find_highest_mpg(data_frame, country):
    '''This function receives a DataFrame and country as input and returns 
    the model of the country cars (str) with the highest mpg and the highest mpg.
    Returns: str, float'''
    
    # the main challenge of this function is to find the 
    # car's name associated with the highest mpg. You could
    # employ a lot of different tactics here, but I'll be
    # doing it the "pandas way".

    # This function takes in a `country` parameter to find the
    # highest mpg car within that specific country. So the first
    # thing I wanted to do was filter out all of the countries that
    # WEREN'T the country we're looking for. The column of interest
    # for this is the column named "origin", which you can
    # see by opening up the mpg.csv file, or by printing the df.

    # It might be helpful to think of this upcoming line as saying:
    # "Access the df, where in column 'origin', the row contains 'country'"

    # This gives us back a new data frame comprised of all rows that
    # contained the `country` in it's "origin" column
    country_df = data_frame[ data_frame["origin"] == country ]

    # We'll then use that df for our other operations. We're going to
    # create a Series() from country_df["mpg"], (essentially a big list of 
    # everything in the 'mpg' column), and simply call .max() to find the maximum mpg.
    max_mpg = country_df["mpg"].max()

    # We now know what the maximum mpg is, but we don't know what car/truck
    # has it. So we'll filter the df again, (using the country_df this time),
    # to where only cars with that maximum mpg are allowed. You'll want to be
    # careful here, and not use the original `data_frame`, since that df isn't
    # filtered for the `country` we're looking for.

    # "Access country_df, where in column 'mpg', the row contains 'max_mpg'"
    max_mpg_car_df = country_df[ country_df["mpg"] == max_mpg ]

    # There is a possibility that more than one car/truck has that maximum
    # mpg value, but this function only returns ONE car name and mpg value. 
    # I don't think Dr. Enbody ever specified what to do if there's more
    # than one, so I'm just going to take the first row's car name. 

    # We'll create a Series() of the car names, max_mpg_car_df["name"], and
    # then I'm going to use the .to_list() method function, which will
    # take all of the values and put them in a default Python list type. 
    # (Not a method function you'll need to know for the final exam)  
    max_mpg_cars = max_mpg_car_df["name"].to_list()

    # I can then just take the 0th index of that list for the first car/truck.
    return max_mpg_cars[0], max_mpg
    
    
def main():

    # We lastly need to fill in the statements Dr. Enbody left for us

    filename = "mpg.csv"
    data_frame = read_csv_2(filename)    # replace with the appropriate function call

    # Remember that we can compose entirely new DataFrame() instances as
    # subsets from others by doing df[ ["COLUMN_NAME", "COLUMN_NAME", ...] ]

    # DataFrame() objects have a .head() and .tail() method to display only the 
    # first 5/last 5 rows

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





