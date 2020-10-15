''' Write SOURCE HEADER here '''

import csv
import matplotlib.pyplot as plt

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def open_file():
    ''' Docstring '''
    pass

def read_file(fp):
    ''' Docstring '''
    pass

def get_reactor_location(location_string):
    ''' Docstring '''
    pass

def reactors_per_region(master_list):
    ''' Docstring '''
    pass

def top_react_by_mwt(master_list):
    ''' Docstring '''
    pass

def bot_react_by_mwt(master_list):
    ''' Docstring '''
    pass

def reactors_in_state (master_list, state):
    ''' Docstring '''
    pass
    
def years_active (master_list):
    ''' Docstring '''
    pass

def plot_years_active(years_active_list):
    '''
    DO NOT CHANGE
    Given list of ints, plot histogram showing age of reactors in US
    '''
    plt.grid(which = 'both')
    plt.hist(years_active_list, bins=22, edgecolor='black')
    plt.title('Active years per Nuclear Reactor')
    plt.xlabel('Years active')
    plt.ylabel('Number of reactors')
    plt.show()

def display_options():
    '''
    DO NOT CHANGE
    Display menu of options for program
    '''
    OPTIONS = 'Menu\n\
1: # Reactors in each region\n\
2: Top energy producing reactors\n\
3: Bottom energy producing reactors\n\
4: List reactors in specific state\n\
5: Plot histogram for how long reactors have been active'       
    print(OPTIONS)

def main():
    ''' Docstring '''
    pass

if __name__ == '__main__':
    main()
