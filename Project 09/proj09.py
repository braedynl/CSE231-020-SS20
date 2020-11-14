import csv
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt

def open_file(year_str):
    ''' Docstring '''
    pass   # replace with your code

def build_dictionary(fp):
    ''' Docstring '''
    pass   # replace with your code

def combine_dictionaries(year, subD, superD):
    ''' Docstring '''
    superD[year] = subD
    return superD

def search_by_country(country, superD, print_boolean):
    ''' Docstring '''
    pass   # replace with your code

def top_10_ranks_across_years(superD, year1, year2):
    ''' Docstring '''
    pass   # replace with your code
    
def print_ranks(superD, list1, list2, year1, year2):
    ''' Docstring '''
    pass   # replace with your code

def prepare_plot(country1, country2, superD):
    ''' Docstring '''
    pass   # replace with your code

def bar_plot(country1, country2, countrylist1, countrylist2):
    ''' Bar plot comparing two countries.'''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    N = 4
    ind = np.arange(N)
    width = 0.25

    rects1 = ax.bar(ind, countrylist1, width,
                    color='black',
                    error_kw=dict(elinewidth=2, ecolor='blue'))

    rects2 = ax.bar(ind + width, countrylist2, width,
                    color='red',
                    error_kw=dict(elinewidth=2, ecolor='red'))

    ax.set_xlim(-width, len(ind) + width)
    ax.set_ylabel('Quantity')
    ax.set_title('Comparison between the two countries')
    xTickMarks = ['Happiness Sc.', 'Family', 'Health', 'Freedom']
    ax.set_xticks(ind + width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=0, fontsize=10)

    ax.legend((rects1[0], rects2[0]), (country1, country2))
    plt.show()

def main():
    ''' Docstring '''

    BANNER = '''
                    __ooooooooo__
                 oOOOOOOOOOOOOOOOOOOOOOo
             oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
          oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
        oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
      oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
     oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo
    oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo
    oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo
    oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
    oOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo
    oOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo
    *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*
    *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
     *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
      *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*
        *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*
          *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*      
             *OOOOOOOOo           oOOOOOOOO*      
                 *OOOOOOOOOOOOOOOOOOOOO*    
                      ""ooooooooo""
    '''

    MENU = '''
    1. Search by country
    2. Top 10 countries
    3. Compare countries
    x. Exit 
    :'''
    print(BANNER)

    superD = {}

    # YOUR CODE TO READ THE FILES AND BUILD SUPER DICTIONARY
    
    user_choice = input(MENU)
    
    while user_choice.lower() != 'x':
        
        # YOUR CODE TO RESPOND TO USER CHOICES
        pass   # replace with your code
#        else:
#            print("[ - ] Incorrect input. Try again.")
        user_choice = input(MENU)

if __name__ == '__main__':
    main()
    
