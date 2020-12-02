"""
    SOURCE HEADER GOES HERE!
"""

from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ Initialize attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
            
        '''
            WRITE DOCSTRING HERE!!!
        '''        
        pass

    def __repr__(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
    
    def get_name(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
    
    def get_element(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
    
    def get_power(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
    
    def get_accuracy(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
    
    def get_attack_type(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass

    def __repr__(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass


    def get_name(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
    
    def get_element1(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
    
    def get_element2(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
    
    def get_hp(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
    
    def get_patt(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass

    def get_pdef(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass

    def get_satt(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass

    def get_sdef(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
    
    def get_moves(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass

    def get_number_moves(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass

    def choose(self,index):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass

        
    def show_move_elements(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass


    def show_move_power(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass

    def show_move_accuracy(self):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
        
        
    def add_move(self, move):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
            
        
    def attack(self, move, opponent):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass
            
        
    def subtract_hp(self,damage):
        '''
            WRITE DOCSTRING HERE!!!
        '''
        pass   
    

        