'''
CSE231 - Introduction to Programming I
Lab 10b
Example Solution

Author: Braedyn Lettinga
'''

import cards

def battle(hand1_list:list, hand2_list:list):

    # We begin by taking the top card of both player's
    # hands. 
    top1 = hand1_list.pop(0)
    top2 = hand2_list.pop(0)

    # In War, the Ace is treated as the top-rank card. Because
    # the class considers Ace rank 1, we have to make an exception. 
    # This portion is dedicated to treating the Ace differently. 
    if top1.rank() == 1 and top2.rank() != 1:
        won = 1
    elif top2.rank() == 1 and top1.rank() != 1:
        won = 2

    # Otherwise, we can treat all other ranks the same way
    elif top1.rank() > top2.rank():
        won = 1
    elif top2.rank() > top1.rank():
        won = 2

    # The `won` variable is dedicated to determining who won the
    # battle. 1 represents player 1, 2 represents player 2.
    print("Battle was 1: {}, 2: {}. Player {} wins battle.".format(top1, top2, won))
    
    # Depending on who won, we add the cards to the end of the
    # winner's hand. The winning card gets appended first, then
    # the losing card.
    if won == 1:
        hand1_list.extend( [top1, top2] )
    else:
        hand2_list.extend( [top2, top1] )


def main():

    # Create the deck of cards
    deck = cards.Deck()

    # I start out by creating two lists
    # that represents both player's hands.
    hand1 = []
    hand2 = []

    # We first deal 5 cards to each player. Player 1
    # first, player 2 second.
    for _ in range(5):
        hand1.append(deck.deal())
        hand2.append(deck.deal())

    # We print-off the starting hands
    print("Starting Hands")
    print("Hand1:", hand1)
    print("Hand2:", hand2)
    print()

    # We'll be creating a loop that continually prompts the user
    # if they want to continue the game. If the user decides to
    # stop playing preemptively, the number of cards in each player's
    # hands will be compared. Whoever has the most cards wins in that case.
    while True:

        # We'll call a function called battle() to simulate the game
        battle(hand1, hand2)

        # After each battle, we print off the players' hands
        print("hand1:", hand1)
        print("hand2:", hand2)

        # If either player's hands are empty, that means the opposing player
        # wins the game.
        if len(hand1) == 0:
            print("Player 2 wins!!!")
            break
        elif len(hand2) == 0:
            print("Player 1 wins!!!")
            break

        # Here is the prompt that asks to continue with the game. As long as the user
        # responds with 'y', we continue the game. 
        prompt = input("Keep Going: (Nn) to stop:").lower()
        if prompt == "y":
            continue
        else:
            if len(hand1) > len(hand2):    # Compare the hand-card-counts in the case of discontinuation
                print("Player 1 wins!!!")
            elif len(hand2) > len(hand1):
                print("Player 2 wins!!!")
            break

if __name__ == "__main__":
    main()