# Solitaire: Scorpion


#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)

MENU = '''     
Input options:
    D: Deal to the Tableau (one card to first three columns).
    M c r d: Move card from Tableau (column,row) to end of column d.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def initialize():
	'''Docstring'''
	pass

def display(stock, tableau, foundation):
    '''Display the stock and foundation at the top.
       Display the tableau below.'''
       
    print("\n{:<8s}{:s}".format( "stock", "foundation"))
    if stock.is_empty():
        print("{}{}".format( " ", " "),end='') # fill space where stock would be so foundation gets printed in the right place
    else:
        print("{}{}".format( " X", "X"),end='')  # print as if face-down
    for f in foundation:
        if f:
            print(f[0],end=' ')  # print first card in stack(list) on foundation
        else:
            print("{}{}".format( " ", " "),end='') # fill space where card would be so foundation gets printed in the right place
            
    print()
    print("\ntableau")
    print("   ",end=' ')
    for i in range(1,8):
        print("{:>2d} ".format(i),end=' ')
    print()
    # determine the number of rows in the longest column        
    max_col = max([len(i) for i in tableau])
    for row in range(max_col):
        print("{:>2d}".format(row+1),end=' ')
        for col in range(7):
            # check that a card exists before trying to print it
            if row < len(tableau[col]):
                print(tableau[col][row],end=' ')
            else:
                print("   ",end=' ')
        print()  # carriage return at the end of each row
    print()  # carriage return after printing the whole tableau
    
def deal_from_stock(stock,tableau):
	'''Docstring'''
	pass
        
def validate_move(tableau,src_col,src_row,dst_col):
	'''Docstring'''
	pass
    
def move(tableau,src_col,src_row,dst_col):
	'''Docstring'''
	pass

def check_sequence(column_lst):
	'''Docstring'''
	pass
    
def move_to_foundation(tableau,foundation):
  	'''Docstring'''
	pass
                    
def check_for_win(foundation):
	'''Docstring'''
	pass

def get_option():
    '''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    D: Deal to the Tableau (one card to first three columns).
    M c r d: Move card from Tableau column,row to end of column d.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
    '''
    option = input( "\nInput an option (DMRHQ): " )
    option_list = option.strip().split()
    
    opt_char = option_list[0].upper()
    
    if opt_char in 'DRHQ' and len(option_list) == 1:  # correct format
        return [opt_char]

    if opt_char == 'M' and len(option_list) == 4 and option_list[1].isdigit() \
        and option_list[2].isdigit() and option_list[3].isdigit():
        return ['M',int(option_list[1]),int(option_list[2]),int(option_list[3])]

    print("Error in option:", option)
    return None   # none of the above
 
def main():
	'''Docstring'''

    print("\nWelcome to Scorpion Solitaire.\n")
    stock, tableau, foundation = initialize()
    display(stock, tableau, foundation)
    print(MENU)
    option_lst = get_option()
    while option_lst and option_lst[0] != 'Q':
        # YOUR CODE HERE
#            else: # move failed
#                print("Error in move:",option,",",option_lst[1],",",option_lst[2],",",option_lst[3])
        option_lst = get_option()
    
    print("Thank you for playing.")

if __name__ == '__main__':
    main()
