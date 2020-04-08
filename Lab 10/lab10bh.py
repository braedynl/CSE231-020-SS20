
import cards

# LAB PROCEDURE
# https://www.cse.msu.edu/~cse231/Online/Labs/Lab10/

# Create the deck of cards
the_deck = cards.Deck()

# DO NOT SHUFFLE THE DECK, IT MESSES WITH MIMIR TESTING
# the_deck.shuffle()

# I would start out by creating a list for
# the hands of both players in the global namespace here.

# You can approach this in many different ways. In general,
# here's what needs to be accounted for:
'''
Deal to hand1 first, hand2 second. 5 cards go to each
in alternating order. Example:

for i in range(5):
    hand1.append(the_deck.deal())
    hand2.append(the_deck.deal())

The cards that battle are the two top cards,
AKA the 0th index of your two lists.

These two cards get removed from the front, (.pop(0) is useful)
and then you compare the ranks of the two you just drew

The rank of aces is the highest in this game, but the class considers
aces the lowest (rank 1). You'll have to make the program account
for this. 

When a player wins, the two cards that battled get put to the back
of the winning player's hand. The order is dependent on who won.
If player 1 won, player 1's winning card gets appended first, and
then player 2's card, and vice versa. Pseudocode example:

if player1_win == True and player2_win == False:
    hand1_list.extend( [top1, top2] )
elif player2_win == True and player1_win == False:
    hand2_list.extend( [top2, top1] )
    
Once somebody's hand is empty, the opposing player wins.

If the user declines to keep going to the prompt, the player
with the most cards wins.

Look at the lab documentation and Mimir tests for
how the output is formatted.
'''
