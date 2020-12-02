"""
    SOURCE HEADER GOES HERE!
"""
import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1) #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================
    
def read_file_moves(fp):  
    '''
        WRITE DOCSTRING HERE!!!
    '''
    pass


def read_file_pokemon(fp):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    pass

def choose_pokemon(choice,pokemon_list):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    pass

def add_moves(pokemon,moves_list):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    pass

def turn (player_num, player_pokemon, opponent_pokemon):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    pass

def main():
        
    usr_inp = input("Would you like to have a pokemon battle?").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q:").lower()
        
    if usr_inp != 'y':
        print("Well that's a shame, goodbye")
        return
    
    else:
        pass
    
if __name__ == "__main__":
    main()
