# Lab10a - Example Answer (Documented)
# Braedyn Lettinga

##
## Demonstrate some of the operations of the Deck and Card classes
##

import cards

# Seed the random number generator to a specific value so every execution
# of the program uses the same sequence of random numbers (for testing).

import random
random.seed( 100 )

# Create a deck of cards

my_deck = cards.Deck()


# Shuffle the deck, then display it in 13 columns

my_deck.shuffle()
print( "===== shuffled deck =====" )
my_deck.display()


# Deal five cards to each player (alternating)

print( "Dealt five cards to each player (alternating)" )
print()

player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append( my_deck.deal() )
    player2_list.append( my_deck.deal() )

# Display each player's cards and the cards still in the deck

print( "===== player #1 =====" )
print()
print( player1_list )
print()
print( "===== player #2 =====" )
print()
print( player2_list )
print()
print( "===== remaining cards in deck =====" )
my_deck.display()


# First card dealt to Player #1

player1_card = player1_list.pop( 0 )

print( "First card dealt to player #1:", player1_card )
print("Player #1 hand:", player1_list) # ADDED


# First card dealt to Player #2

player2_card = player2_list.pop( 0 )

print( "First card dealt to player #2:", player2_card )
print("Player #2 hand:", player2_list) # ADDED


# Compare the ranks of the two cards

print()
if player1_card.rank() == player2_card.rank():
    print( "Tie:", player1_card, "and", player2_card, "of equal rank" )
elif player1_card.rank() > player2_card.rank():
    print( "Player #1 wins:", player1_card, "of higher rank than", player2_card )
else:
    print( "Player #2 wins:", player2_card, "of higher rank than", player1_card )

#########################################################
# ADDED: Everything below this line

# Remember that .pop(0) removes the first item in a list, and
# returns whatever was popped. We do that for both player 1 and 2
player1_card = player1_list.pop(0)
print( "\nSecond card dealt to player #1:", player1_card )
print("Player #1 hand:", player1_list) 

player2_card = player2_list.pop(0)
print( "\nSecond card dealt to player #2:", player2_card )
print("Player #2 hand:", player2_list) 

# If we want the last item in each of the player's hands, we
# can just use .pop() with no arguments.
player1_last_card = player1_list.pop()
player2_last_card = player2_list.pop()

print()
print("Last card in hand of player #1:", format(player1_last_card))
print("Last card in hand of player #2:", format(player2_last_card))

# We can then compare the ranks of the drawn cards in the same way
# Dr. Enbody had above.
print()
if player1_last_card.rank() == player2_last_card.rank():
    print(player2_last_card, "and", player2_last_card, "of equal rank" )
elif player1_last_card.rank() > player2_last_card.rank():
    print(player1_last_card, "of higher rank than", player2_last_card )
else:
    print(player2_last_card, "of higher rank than", player1_last_card )